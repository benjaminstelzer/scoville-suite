# Scoville UI Anti-AI-Slop

A good desktop screenshot does not tell you whether someone can use the page.
The main action may disappear on mobile, keyboard focus may be missing, or an
error may leave the user with no way forward.

Scoville UI helps implement and audit interfaces through the framework and
design system the product already uses. It covers components, interaction
states, responsive behavior and accessibility, then asks for evidence from the
actual rendered interface.

The agent must connect implementation choices to the existing components and
check the affected states and layouts, rather than treating a successful build
as visual proof. Browser checks and corrections take additional time and tokens.
Without access to the rendered interface, that part of the result stays unverified.

UI implements approved product decisions or develops a bounded direction for a new interface. Backend-only work and
wording alone do not activate it.
