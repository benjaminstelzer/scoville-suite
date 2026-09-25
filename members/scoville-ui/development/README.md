# Scoville UI development

The canonical runtime sources are in `../scoville-ui/`. `suite.json` owns the
single UI distribution and its README fragments. WordPress rules live in
`references/wordpress/` and are selected only for admin surfaces.

Historical UI and WordPress member records remain in their original member
directories. PLAN-0006 owns the current merge and practical evaluation. Package
checks live in `development/tests/test_build_suite.py` at the suite root.
