# Browser interface contract

One HTML entry. Main owns run state; both renderers consume identical immutable snapshots and grades.
Views: title, campaign/act selection, briefing, work order/editor, playback, dashboard/debrief and Demo.
Initial state explains how to begin. Loading shows the pending resource. Failure provides retry or
safe schematic fallback. Missing teaching data prevents starting that level and names the file.

## Keyboard

Tab/Shift+Tab traverse controls in visible order. A focusable grid uses arrows for tile movement;
Enter selects/places the selected palette tool; R rotates; Delete/Backspace removes unlocked parts;
Ctrl/Cmd+Z undoes. Configuration is a labeled form; bit toggles are real buttons with pressed state.
Palette tools and port connections have keyboard actions and accessible names. Escape closes panels
and returns focus to their opener. Shortcuts never intercept typing in forms. Run, pause, speed and
one-tick Step are ordinary buttons. A help panel lists the bindings. Error lists link focus to culprits.

Demo is always available per user confirmation and never changes campaign progress. Presenter keys:
Right/Left = next/previous beat, Space = pause, S = schematic toggle, Escape = exit. These keys work
only in Demo outside editable controls. Returning to a beat seeks reproducibly to its defined tick.
Reduced motion uses stable cuts instead of camera swoops; interpolation cannot change simulation time.

## Saves and progress

A versioned key `perhopworks:v1` contains schemaVersion, contentVersion, per-level drafts, passed
level IDs and settings. Validate on load. Unknown/corrupt saves offer a deliberate reset without
crashing. Storage denial leaves the current session playable with a persistence notice. Progress
requires every applicable check, including both parts of L6–L8, and the prerequisite chain. Demo
and reference fixtures cannot call the campaign-completion path. Changing factory/config/predictions
invalidates the existing grade. Replay and view switching preserve selection and tick.

## Art and accessibility

Decorative images carry no teaching facts. Text and bit values are rendered from data. Class color
is paired with a pattern; meter colors with shapes/text. Focus and selected/failed machines remain
visible in both views. Text contrast is at least 4.5:1 (large text 3:1), UI indicators 3:1.
Global delivery requires recorded keyboard-only traversal and render parity for all twelve levels.
