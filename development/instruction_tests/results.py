"""Classify runner failures without hiding observed model behavior as transport."""
BEHAVIOR_FAILURES = {
    'unmanifested_request', 'ambiguous_relative_request', 'duplicate_request',
    'unexpected_action_or_empty_response',
    'forbidden_model_action', 'turn_limit_without_final_answer',
}
TRANSPORT_FAILURES = {
    'turn_timeout', 'nonzero_exit', 'stderr_not_empty', 'event_parse_error',
    'event_is_not_object', 'unexpected_event_order', 'incomplete_turn',
    'process_tree_close_failure',
}


def failure_class(reason):
    if reason is None:
        return None
    if not isinstance(reason, str):
        raise ValueError('protocol_failure must be a string diagnostic or null')
    if reason in BEHAVIOR_FAILURES:
        return 'behavior'
    if reason in TRANSPORT_FAILURES or reason.startswith(('process_start_failure:', 'stdin_write_failure:', 'stdin_or_process_io_failure:')):
        return 'transport'
    # Identity, changed package bytes and unknown defects invalidate the harness
    # evidence. They are neither observed bad model behavior nor a pass.
    return 'harness'
