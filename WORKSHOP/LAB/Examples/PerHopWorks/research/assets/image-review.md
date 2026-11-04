# Image production and review — 2026-11-04

Ten individual images were generated through ChatGPT's built-in `image_gen`, without an API key.
The tool does not expose a model identifier; the manifest records that limitation. The title was
inspected first, then supplied as the style reference for every subsequent image. Every prompt
includes “no text, no letters, no numbers” and excludes glyph-like markings.

Visual inspection accepted the title, three act cards, hall backdrop, three briefing plates, icon,
and loading illustration: no text, digits, logos or glyph-like markings observed. Structural beams,
conveyor rails, crate seams and data-light sockets are ordinary depicted geometry. Decorative art
does not teach bit counts; exact six-plus-two lights and all teaching diagrams are generated from
data in SVG/Three.js.

The owner's “all models all things approved” message authorizes continuation. These later images
are assistant-reviewed under that authorization; the manifest does not claim the owner personally
reviewed images that did not yet exist when they sent that message.

The WebPs total 995,678 bytes. Largest file: 159,352 bytes; largest dimension: 1672 pixels.
Each image has an individual prompt, original output path, SHA-256, dimensions and byte count in
`assets/manifest.json`. `tests/assets.test.js` checks actual WebP headers, dimensions and hashes.
