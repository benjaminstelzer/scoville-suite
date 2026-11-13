# Fallback composition only

Read this file only after you have shown that a new plugin-owned relationship
gets no spacing from the available Core markup, classes and component APIs.

- No value here is a Classic compliance target.
- Do not add a value to existing native margins or padding.
- Do not use the scale to judge an existing native paragraph, Notice, table
  or control.
- Treat a list with its filters and pagination as one composed region before
  you decide where a section ends.

## Skill-Norm choices for an owner gap

| Relationship | Gap | WPDS gap if provided | Core Components `Flex` gap |
| --- | ---: | --- | ---: |
| Control to help, status, or error text | 4px | `xs` | `1` |
| Heading to its own introductory body text | 8px | `sm` | `2` |
| Tightly related controls, or icon and label | 8px | `sm` | `2` |
| Elements in one field group | 12px | `md` | `3` |
| Related setting groups | 16px | `lg` | `4` |
| Independent sections | 24px | `xl` | `6` |
| Major page regions | 32px | `2xl` | `8` |
| Exceptional strong separation | 40px | `3xl` | `10` |
