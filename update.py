import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.write = f.read()

# 1. Replacements for Lumora -> Shivteam
html = html.replace("Lumora", "Shivteam")
html = html.replace("LUMORA", "SHIVTEAM")
html = html.replace("lumora", "shivteam")

# 2. Hero Image Replacement
html = html.replace('src="https://api.getlayers.ai/storage/v1/object/public/public/assets/shivteam-e8b711fc68/hero/after.jpg"', 'src="shivteg.jpeg"')

# 3. Add Team section
team_section = """
  <!-- Team Section -->
  <section id="team" style="background:#fff;">
    <div class="shell" style="padding-block:5rem; display:grid; grid-template-columns:1fr; gap:3rem; align-items:center;">
      <div style="display:flex; justify-content:center;">
        <img src="shivteg.jpeg" style="width:100%; max-width:400px; border-radius:2rem; object-fit:cover; box-shadow:0 25px 50px -12px rgba(0,0,0,0.25);" alt="Shivteg Singh" />
      </div>
      <div style="display:flex; flex-direction:column; align-items:flex-start;">
        <h2 style="font-size:clamp(2.25rem, 5vw, 3rem); font-weight:600; letter-spacing:-0.02em;">CEO Shivteg Singh</h2>
        <p style="margin-top:1rem; font-size:1.125rem; color:rgba(17,17,17,.7);">Finding more people to join.</p>
        <button class="pill-btn dark with-arrow" style="margin-top:2rem;" onclick="openRequestModal()">
          <span class="hover-scale pill-btn-inner">
            To join contact me
            <span class="pill-badge arrow-right">
              <svg viewBox="0 0 24 24" style="width:1rem; height:1rem; stroke:currentColor; stroke-width:2; stroke-linecap:round; fill:none;"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
            </span>
          </span>
        </button>
      </div>
    </div>
  </section>
  <style>
  @media (min-width:768px) {
    #team .shell { grid-template-columns:1fr 1fr; }
  }
  </style>
"""

# Insert Team section before the About section (or after Hero)
if '<section id="about"' in html:
    html = html.replace('<section id="about"', team_section + '\n  <section id="about"')

# 4. Add Team link to Header and Mobile Nav
nav_link_desktop = '<li><button class="hover-lift" onclick="smoothScrollTo(\'team\')">Team</button></li>'
if '<li><button class="hover-lift" onclick="smoothScrollTo(\'about\')">Studio</button></li>' in html:
    html = html.replace(
        '<li><button class="hover-lift" onclick="smoothScrollTo(\'about\')">Studio</button></li>',
        nav_link_desktop + '\n      <li><button class="hover-lift" onclick="smoothScrollTo(\'about\')">Studio</button></li>'
    )

nav_link_mobile = '<li class="nav-item" style="transition-delay:190ms;"><button class="nav-btn" onclick="navTo(\'team\')"><span class="nav-idx">Team</span><span class="nav-lbl">Team</span></button></li>'
if '<li class="nav-item" style="transition-delay:215ms;"><button class="nav-btn" onclick="navTo(\'about\')">' in html:
    html = html.replace(
        '<li class="nav-item" style="transition-delay:215ms;"><button class="nav-btn" onclick="navTo(\'about\')">',
        nav_link_mobile + '\n      <li class="nav-item" style="transition-delay:215ms;"><button class="nav-btn" onclick="navTo(\'about\')">'
    )

# 5. Modify Request Modal
new_modal_content = """
    <!-- Custom Contact View -->
    <div id="modal-form-view" style="text-align:center; padding-block:3rem; display:flex; flex-direction:column; align-items:center; gap:1.5rem;">
      <h2 style="font-size:clamp(1.5rem, 3.5vw, 2rem); font-weight:600; letter-spacing:-0.01em;">Drop email to me on</h2>
      <a href="mailto:official@shivteg.com" class="hover-scale" style="display:inline-block; font-size:clamp(1.25rem, 3vw, 1.5rem); font-weight:600; color:#b15f2c; background:rgba(177,95,44,0.1); padding:0.75rem 1.5rem; border-radius:1rem;">official@shivteg.com</a>
    </div>
"""
# We'll use regex to replace the entire <div id="modal-form-view">...</div> block
import re
html = re.sub(r'<div id="modal-form-view">.*?</div>\s*<!-- Success View -->', new_modal_content + '\n    <!-- Success View -->', html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
