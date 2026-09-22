/* Execution-memory transport. Evaluate this expression; inject host store/load. */
(function dispatchTransport(store, load) {
  "use strict";
  const require = (ok, reason) => { if (!ok) throw new Error(reason); };
  const clone = value => JSON.parse(JSON.stringify(value));
  const parse = result => {
    require(result.exit_code === 0 && typeof result.output === "string",
      "helper incomplete or failed; no dispatch");
    return JSON.parse(result.output); // Truncated JSON is never a payload.
  };
  function sha256(text) {
    const bytes = Array.from(unescape(encodeURIComponent(text)), c => c.charCodeAt(0));
    const bitLength = bytes.length * 8;
    bytes.push(128);
    while (bytes.length % 64 !== 56) bytes.push(0);
    for (let n = 7; n >= 0; n--) bytes.push(Math.floor(bitLength / 2 ** (n * 8)) & 255);
    const primes = [];
    for (let n = 2; primes.length < 64; n++)
      if (!primes.some(p => n % p === 0)) primes.push(n);
    let h = primes.slice(0, 8).map(p => (Math.sqrt(p) % 1 * 2 ** 32) | 0);
    const k = primes.map(p => (Math.cbrt(p) % 1 * 2 ** 32) | 0);
    const rotr = (x, n) => (x >>> n) | (x << (32 - n));
    for (let off = 0; off < bytes.length; off += 64) {
      const w = [];
      for (let i = 0; i < 16; i++)
        w[i] = (bytes[off + i * 4] << 24) | (bytes[off + i * 4 + 1] << 16) |
          (bytes[off + i * 4 + 2] << 8) | bytes[off + i * 4 + 3];
      for (let i = 16; i < 64; i++) {
        const x = w[i - 15], y = w[i - 2];
        w[i] = (w[i - 16] + (rotr(x, 7) ^ rotr(x, 18) ^ (x >>> 3)) +
          w[i - 7] + (rotr(y, 17) ^ rotr(y, 19) ^ (y >>> 10))) | 0;
      }
      let [a,b,c,d,e,f,g,j] = h;
      for (let i = 0; i < 64; i++) {
        const t = (j + (rotr(e,6) ^ rotr(e,11) ^ rotr(e,25)) +
          ((e & f) ^ (~e & g)) + k[i] + w[i]) | 0;
        const u = ((rotr(a,2) ^ rotr(a,13) ^ rotr(a,22)) +
          ((a & b) ^ (a & c) ^ (b & c))) | 0;
        [a,b,c,d,e,f,g,j] = [(t+u)|0,a,b,c,(d+t)|0,e,f,g];
      }
      h = h.map((v,i) => (v + [a,b,c,d,e,f,g,j][i]) | 0);
    }
    return h.map(v => (v >>> 0).toString(16).padStart(8, "0")).join("");
  }
  function valid(e) {
    require(e && e.receipt && typeof e.prompt === "string", "missing payload");
    const r = e.receipt;
    require(["executor", "reviewer", "repair"].includes(r.role) &&
      e.prompt.startsWith("scoville_role=" + r.role + "\n"), "role mismatch");
    require(/^[a-f0-9]{64}$/.test(e.binding) &&
      sha256(e.prompt) === r.sha256 &&
      Array.from(e.prompt).length === r.characters &&
      unescape(encodeURIComponent(e.prompt)).length === r.bytes, "payload integrity failure");
  }
  function receipt(state) { return {...state.envelope.receipt, delivery_state: state.state}; }
  return {
    async prepare(key, build) {
      require(!load(key), "dispatch already retained; do not regenerate");
      store(key, {state:"building"});
      const envelope = parse(await build());
      valid(envelope);
      const state = {state:"not_sent", envelope};
      store(key, state);
      return receipt(state);
    },
    inspect(key) {
      const state = load(key);
      require(state && state.envelope, "payload unavailable; reconcile retained delivery evidence");
      valid(state.envelope);
      return receipt(state);
    },
    async send(key, check, sender) {
      let state = load(key);
      require(state && state.state === "not_sent", "missing or attempted dispatch; reconcile, never replay");
      valid(state.envelope);
      // Reserve before awaiting: concurrent calls cannot both pass this gate.
      state.state = "checking"; store(key, state);
      let verified;
      try {
        verified = await check(clone(state.envelope));
        require(verified.binding === state.envelope.binding, "inputs changed; do not send stale payload");
        const args = verified.arguments, r = state.envelope.receipt, g = verified.guard;
        require(args && args.prompt === state.envelope.prompt, "lifecycle changed payload");
        require(g && g.ok === true && g.workflow_id === state.envelope.guard.workflow_id &&
          g.generation === state.envelope.guard.generation &&
          g.revision === state.envelope.guard.revision, "stale or failed guard");
        if (r.role === "reviewer") {
          require(g.state === "coordinator_active" && g.writer === null &&
            args.target?.type === "project" &&
            "project:" + args.target.projectId === r.target, "review creation target or guard mismatch");
        } else {
          require(args.threadId === r.target && g.state === "writer_active" &&
            g.writer?.task_id === r.target && g.writer?.role === r.role &&
            g.writer?.unit === state.envelope.guard.unit &&
            g.writer?.dispatch_key === state.envelope.guard.dispatch_key, "writer binding mismatch");
        }
      } catch (error) {
        state.state = "not_sent"; store(key, state); throw error;
      }
      // Store before the external call. Any exception or ambiguous reply stays unknown.
      state.state = "send_unknown"; store(key, state);
      const reply = await sender(verified.arguments);
      state = load(key);
      state.reply = reply; store(key, state);
      return {...receipt(state), reply_retained:true};
    },
    takeReply(key) {
      const state = load(key);
      require(state && Object.hasOwn(state, "reply"), "no host reply; reconcile exact task");
      return clone(state.reply);
    }
  };
})
