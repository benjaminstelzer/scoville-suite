{{ package: standalone }}This Skill works on its own. Other Scoville Skills are optional and handle
only their own concerns when available and applicable.
{{ /package }}{{ package: suite }}This package requires every Skill included in this suite to be installed and
enabled. Partial installation is not supported. Skills keep their own task
scope and invocation rules; Workflow still requires an explicit request.
{{ /package }}