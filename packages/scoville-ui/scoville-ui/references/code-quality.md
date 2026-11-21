# Code quality

Authors and reviewers apply these criteria; the complete criteria in Code
count as read. For a review, also use the review section
below.

## Criteria

### What the code has to be

The result is code a person can follow and another agent can extend: the
simplest design that meets the request, with the least code and plain
control flow. Change what the complete result needs and nothing else. What
the request does not change stays as it is: behavior, guarantees and user
state.

The affected path is the operation the request changes, from where the
application enters it to where its result is used, including the callers and
helpers it runs through that you do not edit. A defect on that path that the
requested result depends on is part of this change, also in code you did not
write: fix it at its owner. Other defects are unrelated cleanup: report them.

The rules are checks you make by reading the code on the affected path. A
rule whose subject does not occur there needs no action.

1. **Work that grows.** Judge total work by how often the caller runs the code
   and how much work each call performs, including work inside the functions
   it calls. Before you add or accept a loop, a lookup, a
   query or a call to a helper, read upward to where the application runs
   it more than once (the batch call, the outer loop, the handler that runs
   per row, per event, per request, per poll or per timer tick) and
   downward into every helper and library call you use, including code you
   do not edit. Ask what each one walks, searches, loads, copies, rebuilds
   or writes per call. These are the forms it takes:
   - A search in a list, a walk over another collection, a copy of a
     growing structure or a recursion that revisits shared parts, done once
     per item: quadratic when both sides grow with the data.
   - A query, request, file read or parse per item. Remove it already at
     modest numbers.
   - A structure for the whole page, site or collection (an index, an
     inspection, a set of active entries) rebuilt per item or per call. A
     helper that caches its result only inside one scope rebuilds it for
     every caller outside that scope.
   - The same unchanged input parsed, validated or resolved again in a
     later step of one operation, where the earlier result could be passed
     on.
   - Work on every request, poll, tick or event that only needs doing when
     its input changed: a lock, a write, a cache flush, a recomputation over
     all entries.
   - Work for parts nobody sees or uses yet, done up front for all of them.
   - A stored list or cache that only grows.

   Do such work once: build a set, map or index before the loop that lives
   as long as the operation (rule 2 forbids only a stored second copy), fetch in
   one batch, group once, pass the earlier result on, or do it when the
   input changes or the part is first needed. Use the language's built-in
   function or a plain map before you write an algorithm of your own; a fix
   for repeated work that brings its own parser or matcher has overshot. So
   has one that changes what the user sees or adds state to keep in step:
   no paging, no cache with its own invalidation and no change-tracking
   flag where doing the work once per action is enough.
   Where an existing helper is what repeats, change it at its owner instead
   of building around it. Keep results, order, freshness and the failure of
   a single item as they were. Work in memory over a handful of items by
   contract needs none of this. Decide by reading the source; measure only
   when the request or a project rule asks for it.
2. **Nothing without a need.** Protection, options and bookkeeping that
   nobody asked for are defects, not diligence: each is code to read, test
   and keep in step, and it hides what the code does. A need is the
   request, an input that can reach this code now, another rule of this
   list, or what the plan and the existing code show is coming; how much
   structure such a need justifies is decided by rule 4. That something
   could go wrong is not a need. Without a need:
   - no option, parameter or setting that no existing or planned use needs;
   - no stored flag, marker, counter, intermediate status or second copy of
     data to optimise or coordinate what the existing flow already handles;
   - no guard, lock, retry, check, repeated validation or recovery path
     against a failure an existing guarantee excludes, against an actor who
     already has full rights, of a value this code just built or checked,
     or for a use nobody described: a second actor writing at the same
     moment, a second open window, another process on the same data. Such a
     use is a question for the user, named in the report: not a mechanism
     to build and not a defect to report;
   - no code without a caller in the product: a helper nothing calls, a
     method kept only for tests, a branch for an error nothing produces, an
     interface method implemented empty.

   Input from a person, another system or a public interface can hold any
   value its format allows and is checked once, where it enters. A write, a
   request or a file read can fail in the described use: such a failure
   reaches the user or the caller where it occurs. A catch that swallows it
   or a default value that hides it is a defect too. A
   plan step or acceptance criterion that prescribes such a mechanism
   without naming the case or failure it serves is not a need: trace it to
   a requirement of the user or a failure of the described use, and where you
   find none, say so before you build it. A different style, a shorter
   possible version or a missing hypothetical extension is no defect.
3. **One implementation.** Before writing logic, search for what already
   does it: in the project by what it does and by the domain terms, also in
   sibling packages, and in the language's standard library and the
   platform. Call it when it fits and extend it where it lives when it
   almost fits. Solve a kind of problem the way the project already solves
   it; a second pattern for the same job is a second implementation. When a change replaces a path, an interface, a
   configuration or a data form, switch everything that uses it and remove
   the old one in the same change, with the helpers, parameters and tests
   only it needed. Do not keep the old form alive on your own: no fallback,
   adapter, alias, second code path, migration, version switch or check
   whether your own code exists, unless the request or a project rule asks
   for it. While a product has not been released, a break in compatibility
   is usually wanted, and such code is dead weight. Compatibility is the user's decision:
   where something outside this codebase may still depend on the old form
   (other software, or data that real users have already stored) and the
   request and the project rules leave that open, say what breaks
   and for whom, and ask before you write compatibility code.
4. **Structure that follows the uses.** Each module has one responsibility
   and a small public interface, and the code gets as much structure as its
   uses need. Judge this yourself. A shared helper, class, component or
   interface is wanted where several places do the same thing now, or the
   plan or the code shows they will: it removes hand-written repetition and
   keeps one module's details out of shared code. Build it for those uses,
   with the options they need, and name the uses in your report. For a
   single use write the direct code: a layer, a base class or a general
   function with settings nobody sets is as wrong as the same code written
   by hand in five places. Code you add, move or extend belongs in the
   module that owns the data or rule it works on:
   - Shared or core code knows no single module's keys, texts or special
     cases; a new module must not require editing it.
   - Business rules stay out of handlers, templates and the files that only
     register or wire things together.
   - Use another module through its interface and extend that interface at
     its owner when it lacks what you need. Do not reach into its private
     names, its storage or its internal structures, and do not register a
     stub of an unrelated interface or probe for methods to get at a
     capability.
   - One source of truth: a fact (a default value, a limit, a status, a
     list of codes, a message) and mutable state are defined in one place,
     and every other place reads them from there, also across layers and
     languages: server and client, code and configuration. A value written
     out again in a second file is a defect, because a change then needs
     both.
   - A file, class or function keeps its one responsibility as it grows.
     When your addition would give it a second one, or it already has
     several, put the addition in a unit of its own and say what else
     belongs there: boundaries erode one reasonable addition at a time.
   - Leave global state of the platform and state of other components
     alone: change your own.

   Where one concern makes you change many modules, the boundary is in the
   wrong place: say so instead of spreading the concern further.
5. **Check, then load again.** When code checks or selects something and
   loads it again before use in the same operation, the loaded value can
   differ from the checked one. Check the value that is used, or carry the
   checked value through. Only a guarantee that excludes a change between
   the reads, such as one transaction with a consistent snapshot, makes
   that unnecessary. Who may write between two separate operations is a
   matter of the described use: rule 2.
6. **State and effects across a change.** When a change replaces a call,
   turns a full pass into partial updates or rebuilds something a user sees
   or another component reads, read the old path for what it did besides
   returning its result: state it set (selection, focus, position, entered
   text), events and hooks it fired, caches and records it wrote. The new
   path does the same at every step where it is visible or used, also on
   failure, unless the request removes it. That the state "cannot change"
   is no reason to drop the line that set it.

## Reviewing a change

A reviewer checks the change against the rules its author had to follow:
the whole Skill it reviews with, and in it every rule of "What the code has
to be" in their order. It writes down the defects each one shows; a rule
you do not check is a rule nobody checked. Start with rule 1, because the
author of a loop usually sees it as linear.

A finding names the file and line, the rule it breaks and, where one exists,
the function or structure to use instead. Report each defect on its own. A
defect is a breach of one of the rules. A read-only reviewer changes nothing.
