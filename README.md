# Phone X-ray prototype

Two static pages + two images. No build step.

| file | role |
|---|---|
| `display.html` | TV / laptop. Fullscreens `target.png`. Click or press `f`. |
| `scanner.html` | Phone. Camera + MindAR image tracking. Pins `xray.png` over the tracked `target.png`. |
| `target.png` | What the TV shows. Feature-rich on purpose (grid, glyphs, patterned clothes) so the tracker has corners to lock onto. |
| `xray.png` | The overlay. Same 1600x900 coordinate space as `target.png`, so bones land on the body. |
| `make_images.py` | Regenerates both PNGs (`pip install cairosvg`). Edit and re-run to change the figure. |

## Run it

Camera access needs HTTPS (or `localhost`). Quickest:

```bash
cd xray
npx -y http-server -p 8080 .          # serves the folder
npx -y cloudflared tunnel --url http://localhost:8080   # free public https URL, no account
```

Open `https://<tunnel>/display.html` on the TV, `https://<tunnel>/scanner.html` on the phone.
Any static host works the same (Azure Static Web Apps, GitHub Pages, etc.).

## First run

`scanner.html` looks for a precompiled `targets.mind`. If it isn't there it compiles one from
`target.png` in the browser (10–40 s on a phone, once, then cached in IndexedDB). Tap **Save .mind**
after that and drop the file in this folder as `targets.mind` so nobody waits again.
If you change `target.png`, bump `TARGET_VERSION` in `scanner.html` and delete `targets.mind`.

## How it works

MindAR compiles `target.png` into feature descriptors, matches them against camera frames, and
gives three.js a pose for the target. The overlay is a plane of width 1 unit (the target width)
in that anchored group, so it inherits position, rotation and scale every frame. Far away → the
plane covers the whole TV; close up → only the bit of the plane in view is drawn, i.e. you zoom
into one bone for free.

## Next steps (not done yet)

- Animation: keep `target.png` static (the tracker needs a stable image) and animate the *overlay*
  — swap `mat.map` per frame, use a video texture, or add more meshes to `anchor.group`.
- Layers: skin → muscle → bone on a slider instead of just opacity.
- Game ideas: hotspots in overlay coordinates + raycast from screen centre to detect "aiming" at a bone.
- Multiple targets: `compileImageTargets([img1, img2, ...])` and `addAnchor(n)`.
