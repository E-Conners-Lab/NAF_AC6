# Per-Hop Works asset style guide

Established before the first smoke asset; refine production silhouettes in Loop 3.
Low-poly, flat-shaded original factory shapes; neutral charcoal floor, warm ivory machinery,
roughness approximately 0.6. No text, letters, numbers, icons resembling glyphs, logos or watermarks
in models or raster images. All teaching diagrams, labels and bit states are generated from data.

Use the Okabe–Ito palette with a separate stable pattern for every service class: orange #E69F00,
sky blue #56B4E9, green #009E73, yellow #F0E442, blue #0072B2, vermilion #D55E00 and purple #CC79A7,
plus neutral variants. Pattern identity, not hue alone, distinguishes classes; palette ordering never
implies service priority. Meter states also use text and circle/diamond/triangle indicators in code.

Silhouettes: sorter split chute, paint booth arch/nozzle, single tank column, cascade stepped pair,
twin tank side-by-side pair, recycler low hopper, merger converging gates, dock broad doorway.
Crates use three distinct sizes with eight socket empties; code creates six equal DSCP lights and
two smaller ECN lights separated by a gap. Emission is reserved for data lights, token water and
active machine states. Decorative structure never suggests a false signal.

Models follow plan triangle/node budgets, +Y up export, meters, floor-centered origin and applied
transforms. Images are decorative, WebP <=2048px long edge and <=400KB. Record actual generator,
prompt/script, date, license and real human review; never infer approval or an unexposed model name.

Production geometry uses one vertex-colored PBR mesh for the stationary body and separate named
meshes only for animated parts. This keeps silhouettes rich without multiplying draw calls.
Machine footprints fit one meter; taller tanks are visible from the demonstration camera. Belts
sit at 0.12 m and crates travel just above their surface. Hall architecture is open at the front and
top so it never conceals the datapath. No downloaded model, texture, HDRI or third-party art is used.

Pattern mapping is held in `data/profiles.json` and drawn by code: cross, dots, bars, diagonal,
checker, waves, horizontal, rings, vertical, diamond, chevron and plain. Metered token water uses sky blue;
active states may emit softly. All housing is matte ivory, graphite, muted teal or warm orange.

Owner continuing authorization (2026-11-04) covers subsequent image production; each image records
assistant visual inspection honestly. Source images are generated through ChatGPT built-in image_gen
with title art as style reference. No unexposed model identifier is claimed. Exact bit counts, class
patterns and all teaching text are produced in code, not inferred from decorative raster art.
