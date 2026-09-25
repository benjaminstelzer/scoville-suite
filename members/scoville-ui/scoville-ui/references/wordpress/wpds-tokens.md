# WPDS token values

Read only for a region that actually consumes WPDS tokens. Availability does
not establish native use by a Classic component. Preserve each token reference
and distinguish its supplied value from the property's rendered effect.
Sources and runtime pins are in [sources.md](sources.md).

## WPDS token facts at Gutenberg `wp/7.0`

The density matrix below describes the pinned 7.0 bundled package. The default
gap and padding values also match the inspected 7.1 Core stylesheet. Do not
infer availability of alternate densities or provider props from this matrix.

The 7.1 Core stylesheet ships one density. `@wordpress/theme` 1.0.0 exposes no
public density switch. Compact and comfortable values below remain historical
7.0 bundled-package facts, not available 7.1 modes.

### Gap

| Token | compact | default | comfortable |
| --- | ---: | ---: | ---: |
| `xs` | 4px | 4px | 8px |
| `sm` | 4px | 8px | 12px |
| `md` | 8px | 12px | 16px |
| `lg` | 12px | 16px | 20px |
| `xl` | 20px | 24px | 32px |
| `2xl` | 24px | 32px | 40px |
| `3xl` | 32px | 40px | 48px |

### Padding

| Token | compact | default | comfortable |
| --- | ---: | ---: | ---: |
| `xs` | 4px | 4px | 8px |
| `sm` | 4px | 8px | 12px |
| `md` | 8px | 12px | 16px |
| `lg` | 12px | 16px | 20px |
| `xl` | 16px | 20px | 24px |
| `2xl` | 20px | 24px | 32px |
| `3xl` | 24px | 32px | 40px |

Gap and padding names are not interchangeable. Density is an independent mode,
not a mobile breakpoint.
