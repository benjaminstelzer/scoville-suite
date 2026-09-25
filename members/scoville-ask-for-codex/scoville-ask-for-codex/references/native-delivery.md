# Native answer delivery

Send this consultation's answer only to the verified `return_to_thread_id`
through `send_message_to_thread`. The dispatch authorizes this result message
only. Include your exact task ID, `consultation_reference`, scope, answer and
material evidence limits. Copy the supplied scope value exactly; do not paraphrase it or add a follow-up suffix. Keep the answer within 6000 characters unless more
detail was requested. If essential content does not fit, explicitly mark it
incomplete and request continuation; do not silently truncate.

After confirmed delivery, your own final response contains only a delivery
receipt and asks whether the user wants this adviser task archived. Do not
repeat the answer or archive automatically. Only an explicit yes in this task
authorizes self-archival; verify the exact task ID and `archived:true`. A
follow-up keeps this conversation and delivery destination, with a new reference.
Failed delivery is reported here as failed, without an automatic retry.
