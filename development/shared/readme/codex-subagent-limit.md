Native agents consume the host's available capacity. Close finished agents only
when the host exposes a documented operation. Interruption alone proves neither
termination nor a freed slot, so preserve progress if capacity blocks more work.
