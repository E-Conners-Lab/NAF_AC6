# Accessibility review — 2026-11-04

The owner requested a gentler introduction. The welcome now has one primary beginner action,
four short SVG teaching steps, an interactive ECN example, and a guided first sorter edit.
Briefings lead with plain language; technical detail is expandable. A separate Demo button allows
presentations without navigating or unlocking the advanced campaign.

## Automated and keyboard evidence

`research/browser/accessibility.json` records axe-core WCAG 2 A/AA and 2.1 AA scans with zero
reported violations in ten states: welcome, introduction, briefing, schematic floor, sorter
inspector, Demo, prediction form, twin meter, Spillway thresholds and Priority Merger forms.
`accessibility-before.json` preserves the original contrast findings. Supporting text was darkened,
key labels enlarged, and presentation captions/headings placed on dark opaque-backed panels.

`keyboard-3d.json` and `keyboard-schematic.json` record all twelve complete campaigns using keyboard
inputs, trace seeking, view parity and persistence. `polish.json` records keyboard navigation of
all introduction steps, ECN toggling, ten Demo beats, view switching and return without awards.
`demo-rehearsal.json` records the complete automatic 85-second presentation from fresh progress,
entered and exited through presenter keys.

## Visual and interaction review

- Visible focus, native dialog focus containment, labeled controls, semantic buttons, field labels,
  status announcements and skip navigation. Closing a dialog restores its opener when still
  present, or returns to the grid after a view rebuild. No positive tabindex order is used.
- Keyboard grid editing and all machine forms use the same state as pointer editing. Arrow-key
  select behavior is explicit across native popup implementations. The parts cabinet, inspector,
  output connections, undo, run controls and crate search are keyboard reachable.
- Twelve distinct patterns accompany class colors, including a separate chevron for historical
  Low Priority. A text/SVG legend identifies them. Dark crates use light pattern ink. DSCP and ECN
  lights differ in size and spacing; on/off states also have binary text in lid readouts.
- Meter outcomes have color names in traces and predictions; grade states have PASS/REVIEW text
  and symbols. Charts have class labels, percent labels, and textual totals alongside color.
- Reduced-motion emulation was used during accessibility scans. Decorative spray and oscillation
  are suppressed; Demo uses immediate camera cuts. The pure camera test verifies reduced-motion
  poses. Manual camera control and discrete simulation state remain available.
- At 1920×1080, the welcome fits on screen and the Demo keeps presenter controls, caption and
  live summary visible. The sidebar scrolls for detailed source notes. Decorative images have
  empty alt text and all teaching content is real DOM/SVG text.

Axe marks some canvas/SVG/image-background contrast cases as requiring manual review rather than
reporting a pass. Screenshots were visually inspected, and foreground text uses explicit dark/light
panels. This report does not claim a comprehensive assistive-technology certification; full campaign
keyboard play and the listed browser/visual checks are the evidence provided.
