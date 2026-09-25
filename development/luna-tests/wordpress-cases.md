# WordPress suite cases

Use only the built package. Cases 01-03 apply the complete Skill. Cases 04-05
are discovery-only and receive WordPress and UI frontmatter only.

## wp-01
A plugin owns a single-site Classic PHP settings page on WordPress 7.0. The user asks for a source-only spacing audit, with no code changes. The supplied source uses native .wrap, .form-table and p.submit, unchanged Core CSS and no tokens. A reviewer calls the native margins defective because they differ from a proposed 16px fallback scale and wants React plus custom --wpds-* values. No browser is available. State the mode, scope, ownership, whether the recommendation is justified, the next useful action and what cannot be concluded.

## wp-02
Fix a plugin-owned workflow page on WordPress 7.1, not other screens. Core owns the shell and page Notices. The plugin mount uses stable @wordpress/components, with no experimental opt-in. A newly composed generic Flex column leaves space for a hidden conditional field. A Save failure loses keyboard focus and offers no recovery. A portal renders outside the plugin mount. Existing specialized controls retain their default spacing. Explain the bounded correction and validation sequence, spacing ownership, component choice and portal checks. Do not claim execution.

## wp-03
Implement i18n readiness and accessible validation in an explicit plugin-owned Network Admin settings page, Classic PHP plus a registered Core Components JS subtree, supporting WordPress 7.0 and 7.1. Only English and German are planned. Source fixtures: a PHP label concatenates a count into text, a JS error uses a different text domain, the registered script has no wp_set_script_translations call, and invalid input has no error association. No translation delivery was requested. The user also proposes Core 7.1 theme tokens for a missing layout relationship. State ownership, necessary corrections, version/fallback checks and the evidence needed. Clarify whether catalogs, RTL proof, a React rewrite or a full-suite audit are required.

## wp-04
There are two independent requests: A implements responsive states and keyboard navigation in a React/Mantine customer dashboard outside WordPress. B defines three visual concepts before selecting one for a future plugin admin page, with no implementation requested. Select the relevant supplied Skill for each, say whether the WordPress specialist applies, and explain the scope boundary briefly. Do not execute either request.

## wp-05
A plugin author asks to reuse the WordPress plugin-page shell and spacing matrix in a Block Editor SlotFill, a post metabox and a public theme landing page. No plugin-owned admin page is requested. Determine whether the WordPress specialist should activate, identify the owning surface for each request and state what cannot be prescribed under this specialist. Do not force a supplied Skill to own an unsupported surface.
