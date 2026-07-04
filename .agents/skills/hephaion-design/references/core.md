# Shared Design Engineering Rules

Use these rules for design work across product packages. Product-specific design systems may refine them.

## Principles

- Make the real object of the interface visible.
- Use native controls before custom controls.
- Use semantic tokens before raw values.
- Do not rely on color alone for state.
- Avoid layout shift on hover, focus, active, or selected states.
- Keep text readable at narrow widths.
- Define empty, loading, error, disabled, selected, and success states.
- Keep motion purposeful and respect reduced-motion preferences.

## Accessibility

- Controls need accessible names.
- Inputs need labels.
- Keyboard navigation must work for dialogs, menus, tabs, lists, and command palettes.
- Focus states must be visible.
- Meaningful images need useful alt text; decorative images use empty alt text.
- Use true tables for truly tabular content.

## Layering

Universal design rules live here. Product packages own:

- color values and token names
- product vocabulary
- component-specific rules
- screenshots and visual references
- product copy and tone
- runtime UI constraints
