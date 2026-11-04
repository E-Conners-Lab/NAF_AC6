# Quickstart and acceptance scenarios

This example is a local browser game. See README.md for the beginner walkthrough and presenter keys.

From the workshop repository root, run:

```sh
python3 WORKSHOP/LAB/Examples/PerHopWorks/start.py
```

It serves only this example at `http://localhost:8000`, opens the browser and stops with Ctrl+C.
The direct fallback, from this example directory, is `python3 -m http.server 8000`.
Node is for developer tests only: `node --test tests/` from the example directory.

Acceptance: start from a fresh save; finish L1–L5 using keyboard only; make a deliberate incorrect
sort/mark and inspect the diagnostic; switch to 3D mid-run and compare the result; finish L6–L12;
open Demo from fresh progress and traverse all beats with Left/Right, Space, S and Escape. Confirm
that Demo awarded no campaign progress. Repeat with no external network and WebGL2 unavailable.
Measure performance at 1920×1080 with 400 in-flight crates and record hardware/browser/version,
frame timing, draw calls, model payload and texture dimensions.

Never use file://. Missing teaching data must fail visibly; absence of WebGL2 alone must use SVG.
