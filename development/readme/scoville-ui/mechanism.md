## How it works

- Identify the existing design system, implementation owner and approved product decisions.
- Load the local WordPress adapter only for supported plugin-owned `wp-admin`
  pages. Editor surfaces and metaboxes keep their host owner. Other frameworks
  use the general route.
- Read the relevant component and styling code before changing the interface.
- Implement affected states and responsive behavior through supported framework components.
- Check the completed batch in the actual rendered interface, including relevant input and focus behavior.
- Use one common validation process with the selected platform's additional checks.
- Return blocked product decisions to their owner. Without an approved visual
  direction, choose a limited direction within the existing framework conventions.
