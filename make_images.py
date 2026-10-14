import cairosvg, random
random.seed(7)
W, H = 1600, 900

# ---------- shared geometry (same coords in both images) ----------
# Figure centred, head at top. Everything in 1600x900 space.
cx = 800

def textured_bg():
    # feature-rich backdrop so the tracker has plenty of corners
    out = []
    # faint grid
    for x in range(0, W, 50):
        out.append(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="#2d3a4a" stroke-width="1"/>')
    for y in range(0, H, 50):
        out.append(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#2d3a4a" stroke-width="1"/>')
    # scattered "medical chart" glyphs and dots
    glyphs = ["+", "x", "o", "◇", "△", "▢", "ʘ", "Ж", "λ", "Ψ", "#", "%", "@", "§"]
    for _ in range(260):
        x, y = random.randint(20, W-20), random.randint(20, H-20)
        if 480 < x < 1120 and 40 < y < 880:   # keep off the figure
            continue
        g = random.choice(glyphs); s = random.randint(14, 40)
        c = random.choice(["#4fd1c5", "#f6ad55", "#fc8181", "#90cdf4", "#f6e05e", "#b794f4"])
        out.append(f'<text x="{x}" y="{y}" font-size="{s}" fill="{c}" opacity="0.85" font-family="monospace">{g}</text>')
    # corner labels
    out.append('<text x="30" y="60" font-size="40" fill="#e2e8f0" font-family="monospace" font-weight="bold">PATIENT 0427</text>')
    out.append('<text x="30" y="100" font-size="24" fill="#a0aec0" font-family="monospace">WARD B · BED 12 · ADULT MALE</text>')
    out.append('<text x="1170" y="60" font-size="40" fill="#e2e8f0" font-family="monospace" font-weight="bold">SCAN ME →</text>')
    out.append('<text x="1170" y="100" font-size="24" fill="#a0aec0" font-family="monospace">point your phone at the screen</text>')
    out.append('<text x="30" y="860" font-size="24" fill="#a0aec0" font-family="monospace">ECG ▁▂▃▅▂▇▂▁▂▃▁▂▇▃▂▁▂▃▅▂▇▂▁</text>')
    out.append('<text x="1130" y="860" font-size="24" fill="#a0aec0" font-family="monospace">BP 118/76  SpO2 98%  HR 64</text>')
    return "\n".join(out)

def person():
    p = []
    # shadow
    p.append(f'<ellipse cx="{cx}" cy="880" rx="260" ry="18" fill="#000" opacity="0.4"/>')
    # legs (trousers, pinstripe)
    p.append('<defs><pattern id="stripe" width="18" height="18" patternUnits="userSpaceOnUse" patternTransform="rotate(90)"><rect width="18" height="18" fill="#2b4c7e"/><rect width="4" height="18" fill="#6c8cc0"/></pattern>'
             '<pattern id="check" width="36" height="36" patternUnits="userSpaceOnUse"><rect width="36" height="36" fill="#c0392b"/><rect width="18" height="18" fill="#e74c3c"/><rect x="18" y="18" width="18" height="18" fill="#e74c3c"/></pattern></defs>')
    p.append(f'<path d="M{cx-110},520 L{cx-130},860 L{cx-40},860 L{cx-20},540 Z" fill="url(#stripe)" stroke="#111" stroke-width="4"/>')
    p.append(f'<path d="M{cx+110},520 L{cx+130},860 L{cx+40},860 L{cx+20},540 Z" fill="url(#stripe)" stroke="#111" stroke-width="4"/>')
    # shoes
    p.append(f'<path d="M{cx-150},860 L{cx-30},860 L{cx-30},885 L{cx-160},885 Z" fill="#222" stroke="#000" stroke-width="3"/>')
    p.append(f'<path d="M{cx+150},860 L{cx+30},860 L{cx+30},885 L{cx+160},885 Z" fill="#222" stroke="#000" stroke-width="3"/>')
    # torso (check shirt)
    p.append(f'<path d="M{cx-150},250 L{cx+150},250 L{cx+140},540 L{cx-140},540 Z" fill="url(#check)" stroke="#111" stroke-width="4"/>')
    # buttons
    for y in range(290, 530, 40):
        p.append(f'<circle cx="{cx}" cy="{y}" r="7" fill="#f7e9b7" stroke="#111" stroke-width="2"/>')
    # arms
    p.append(f'<path d="M{cx-150},260 L{cx-250},560 L{cx-200},575 L{cx-110},330 Z" fill="url(#check)" stroke="#111" stroke-width="4"/>')
    p.append(f'<path d="M{cx+150},260 L{cx+250},560 L{cx+200},575 L{cx+110},330 Z" fill="url(#check)" stroke="#111" stroke-width="4"/>')
    # hands
    p.append(f'<circle cx="{cx-230}" cy="590" r="32" fill="#f1c27d" stroke="#111" stroke-width="4"/>')
    p.append(f'<circle cx="{cx+230}" cy="590" r="32" fill="#f1c27d" stroke="#111" stroke-width="4"/>')
    # neck & head
    p.append(f'<rect x="{cx-40}" y="200" width="80" height="60" fill="#f1c27d" stroke="#111" stroke-width="4"/>')
    p.append(f'<ellipse cx="{cx}" cy="140" rx="95" ry="110" fill="#f1c27d" stroke="#111" stroke-width="4"/>')
    # hair
    p.append(f'<path d="M{cx-95},110 Q{cx-80},20 {cx},25 Q{cx+80},20 {cx+95},110 Q{cx+60},70 {cx},80 Q{cx-60},70 {cx-95},110 Z" fill="#3b2a1a" stroke="#111" stroke-width="4"/>')
    # face
    p.append(f'<circle cx="{cx-35}" cy="135" r="10" fill="#111"/><circle cx="{cx+35}" cy="135" r="10" fill="#111"/>')
    p.append(f'<path d="M{cx-30},185 Q{cx},215 {cx+30},185" stroke="#111" stroke-width="5" fill="none"/>')
    p.append(f'<path d="M{cx},145 L{cx-8},170 L{cx+8},170" stroke="#111" stroke-width="4" fill="none"/>')
    # name badge
    p.append(f'<rect x="{cx+40}" y="300" width="90" height="40" fill="#fff" stroke="#111" stroke-width="3"/>')
    p.append(f'<text x="{cx+85}" y="328" font-size="22" text-anchor="middle" fill="#111" font-family="monospace" font-weight="bold">BOB</text>')
    return "\n".join(p)

def skeleton():
    s = []
    bone = 'fill="#e8f4ff" stroke="#9ad0ff" stroke-width="3" opacity="0.95"'
    lbl = 'font-family="monospace" font-size="18" fill="#7fe3ff"'
    def label(x, y, t): s.append(f'<text x="{x}" y="{y}" {lbl} text-anchor="middle">{t}</text>')
    # skull
    s.append(f'<ellipse cx="{cx}" cy="130" rx="85" ry="95" {bone}/>')
    s.append(f'<ellipse cx="{cx-32}" cy="120" rx="18" ry="22" fill="#0a1a2a"/><ellipse cx="{cx+32}" cy="120" rx="18" ry="22" fill="#0a1a2a"/>')
    s.append(f'<path d="M{cx},150 L{cx-9},178 L{cx+9},178 Z" fill="#0a1a2a"/>')
    # teeth
    s.append(f'<rect x="{cx-45}" y="195" width="90" height="28" rx="6" {bone}/>')
    for x in range(cx-40, cx+40, 12):
        s.append(f'<line x1="{x}" y1="195" x2="{x}" y2="223" stroke="#0a1a2a" stroke-width="2"/>')
    label(cx+150, 110, "SKULL")
    # spine
    for i, y in enumerate(range(240, 540, 22)):
        s.append(f'<rect x="{cx-16}" y="{y}" width="32" height="16" rx="5" {bone}/>')
    label(cx+70, 420, "SPINE")
    # ribs
    for i, y in enumerate(range(275, 430, 24)):
        r = 120 - i*6
        s.append(f'<path d="M{cx-14},{y} Q{cx-r},{y+5} {cx-r+10},{y+30}" fill="none" stroke="#e8f4ff" stroke-width="7" opacity="0.95"/>')
        s.append(f'<path d="M{cx+14},{y} Q{cx+r},{y+5} {cx+r-10},{y+30}" fill="none" stroke="#e8f4ff" stroke-width="7" opacity="0.95"/>')
    label(cx-150, 265, "RIBS")
    # clavicle / shoulders
    s.append(f'<path d="M{cx-20},255 L{cx-140},265" stroke="#e8f4ff" stroke-width="9" stroke-linecap="round"/>')
    s.append(f'<path d="M{cx+20},255 L{cx+140},265" stroke="#e8f4ff" stroke-width="9" stroke-linecap="round"/>')
    # pelvis
    s.append(f'<path d="M{cx-110},540 Q{cx-120},470 {cx-40},530 L{cx+40},530 Q{cx+120},470 {cx+110},540 Q{cx+60},600 {cx},585 Q{cx-60},600 {cx-110},540 Z" {bone}/>')
    label(cx+160, 560, "PELVIS")
    # arms: humerus, radius/ulna
    def limb(x1,y1,x2,y2,w=12):
        s.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#e8f4ff" stroke-width="{w}" stroke-linecap="round"/>')
        s.append(f'<circle cx="{x1}" cy="{y1}" r="{w}" {bone}/><circle cx="{x2}" cy="{y2}" r="{w}" {bone}/>')
    limb(cx-140, 265, cx-195, 420); limb(cx-195, 420, cx-230, 580, 9); limb(cx-200, 430, cx-238, 585, 6)
    limb(cx+140, 265, cx+195, 420); limb(cx+195, 420, cx+230, 580, 9); limb(cx+200, 430, cx+238, 585, 6)
    label(cx-260, 340, "HUMERUS"); label(cx+280, 500, "RADIUS")
    # hands
    for hx in (cx-230, cx+230):
        for k in range(-2, 3):
            s.append(f'<line x1="{hx}" y1="590" x2="{hx+k*14}" y2="{625}" stroke="#e8f4ff" stroke-width="5" stroke-linecap="round"/>')
    # legs: femur, tibia/fibula
    limb(cx-70, 560, cx-85, 720, 14); limb(cx-85, 720, cx-95, 860, 11); limb(cx-70, 725, cx-78, 858, 6)
    limb(cx+70, 560, cx+85, 720, 14); limb(cx+85, 720, cx+95, 860, 11); limb(cx+70, 725, cx+78, 858, 6)
    label(cx-180, 650, "FEMUR"); label(cx+190, 800, "TIBIA")
    # feet
    s.append(f'<path d="M{cx-95},860 L{cx-150},878" stroke="#e8f4ff" stroke-width="8" stroke-linecap="round"/>')
    s.append(f'<path d="M{cx+95},860 L{cx+150},878" stroke="#e8f4ff" stroke-width="8" stroke-linecap="round"/>')
    # a "fracture" highlight on left tibia for fun
    s.append(f'<circle cx="{cx-90}" cy="790" r="34" fill="none" stroke="#ff5a5a" stroke-width="4" stroke-dasharray="8 6"/>')
    s.append(f'<text x="{cx-90}" y="845" font-family="monospace" font-size="16" fill="#ff8a8a" text-anchor="middle">FRACTURE</text>')
    return "\n".join(s)

target_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<rect width="{W}" height="{H}" fill="#1a2330"/>
{textured_bg()}
{person()}
</svg>'''

xray_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs><radialGradient id="g" cx="50%" cy="45%" r="65%"><stop offset="0" stop-color="#0d2a44" stop-opacity="0.92"/><stop offset="1" stop-color="#03101c" stop-opacity="0.97"/></radialGradient></defs>
<rect width="{W}" height="{H}" fill="url(#g)"/>
<text x="30" y="60" font-size="40" fill="#7fe3ff" font-family="monospace" font-weight="bold">X-RAY · PATIENT 0427</text>
<text x="30" y="100" font-size="24" fill="#5bb8d6" font-family="monospace">kV 70 · mAs 8 · AP VIEW</text>
{skeleton()}
</svg>'''

cairosvg.svg2png(bytestring=target_svg.encode(), write_to="target.png", output_width=W, output_height=H)
cairosvg.svg2png(bytestring=xray_svg.encode(), write_to="xray.png", output_width=W, output_height=H)
print("done")
