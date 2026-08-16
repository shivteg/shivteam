import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Loader
html = html.replace('Bold ideas, shipped with quiet precision.', 'Turning imaginative ideas into clean, interactive, and functional code.')

# Hero text replacements in JS
html = html.replace(
    "wrapLines('hero-h1', ['Bold ideas,', 'shipped with', 'quiet precision.'], 120);",
    "wrapLines('hero-h1', ['Creative Frontend', 'Developer & Web', 'Game Creator.'], 120);"
)
html = html.replace(
    "const carouselItems = [\n  {caption:\"Conversion design\", title:\"Crafted to convert.\"},\n  {caption:\"Engineering\", title:\"Built to scale.\"},\n  {caption:\"Brand systems\", title:\"Designed to last.\"}\n];",
    "const carouselItems = [\n  {caption:\"Creative Coding\", title:\"Canvas & SVG Animations.\"},\n  {caption:\"Game Development\", title:\"Retro Arcade Logic.\"},\n  {caption:\"Frontend Interfaces\", title:\"Responsive UI/UX Design.\"}\n];"
)
html = html.replace(
    'wrapWords(\'about-statement\', "We partner with ambitious teams to ship digital products, brand systems, and the strategy that holds them together.", 35);',
    'wrapWords(\'about-statement\', "I am a passionate student and self-taught developer dedicated to building interactive web applications, retro arcade games, and creative digital experiences.", 35);'
)

# Hero visual text
html = html.replace('Independent Studio', 'Creative Developer')
html = html.replace('200+ brands shipped', '7+ Web Apps Deployed')
html = html.replace('Working since 2014', 'Self-Taught Developer')
html = html.replace('Remote-first, worldwide', 'Building Digital Experiences')
html = html.replace('An independent studio crafting brands, products, and the systems that connect them.', 'A creative frontend developer turning imaginative ideas into clean, interactive, and functional code.')

# Portfolio Replacements
portfolio_html = """<ul class="portfolio-grid" style="display:grid; grid-template-columns:1fr; gap:1.5rem;">
        <!-- Card 1 -->
        <li class="reveal-up" data-reveal style="transition-delay:0ms;">
          <a href="https://shivplayzone.vercel.app" target="_blank" class="group" style="display:block;">
            <article class="group-hover-lift port-card">
              <div style="display:flex; justify-content:space-between; font-size:0.75rem; text-transform:uppercase; letter-spacing:0.025em; color:rgba(255,255,255,.45); position:relative; z-index:10;">
                <span>Game — Puzzle</span>
                <div class="group-hover-badge" style="width:2.75rem; height:2.75rem; display:grid; place-items:center; border-radius:9999px; background:rgba(255,255,255,.1); color:#fff; box-shadow:inset 0 0 0 1px rgba(255,255,255,.15);">
                  <svg viewBox="0 0 24 24" style="width:1.25rem; height:1.25rem; stroke:currentColor; stroke-width:2; stroke-linecap:round; fill:none;"><path d="M7 17 17 7M8 7h9v9"/></svg>
                </div>
              </div>
              <div style="position:absolute; inset:0; display:grid; place-items:center; pointer-events:none; z-index:1;">
                <svg viewBox="0 0 48 48" style="width:4.5rem; height:4.5rem; fill:rgba(255,255,255,.9); position:relative;">
                  <path d="M24 2c2.2 13.8 7.9 19.6 22 22-14.1 2.4-19.8 8.2-22 22-2.2-13.8-7.9-19.6-22-22 14.1-2.4 19.8-8.2 22-22Z"/>
                </svg>
              </div>
              <div class="port-bottom">
                <h3 style="font-size:clamp(1.5rem, 3vw, 1.875rem); font-weight:500; letter-spacing:-0.01em;">ShivPlayzone</h3>
                <p style="margin-top:0.5rem; max-width:28rem; font-size:0.875rem; color:rgba(255,255,255,.55);">A dynamic image puzzle grid game where challenge increases over time.</p>
                <div style="margin-top:1.25rem; display:flex; flex-wrap:wrap; gap:0.5rem;">
                  <span class="tag-chip light">Game Logic</span><span class="tag-chip light">JS</span><span class="tag-chip light">CSS Grid</span>
                </div>
              </div>
            </article>
          </a>
        </li>
        <!-- Card 2 -->
        <li class="reveal-up" data-reveal style="transition-delay:90ms;">
          <a href="https://shivanimate.vercel.app" target="_blank" class="group" style="display:block;">
            <article class="group-hover-lift port-card">
              <div style="display:flex; justify-content:space-between; font-size:0.75rem; text-transform:uppercase; letter-spacing:0.025em; color:rgba(255,255,255,.45); position:relative; z-index:10;">
                <span>Creative — Canvas</span>
                <div class="group-hover-badge" style="width:2.75rem; height:2.75rem; display:grid; place-items:center; border-radius:9999px; background:rgba(255,255,255,.1); color:#fff; box-shadow:inset 0 0 0 1px rgba(255,255,255,.15);">
                  <svg viewBox="0 0 24 24" style="width:1.25rem; height:1.25rem; stroke:currentColor; stroke-width:2; stroke-linecap:round; fill:none;"><path d="M7 17 17 7M8 7h9v9"/></svg>
                </div>
              </div>
              <div style="position:absolute; inset:0; display:grid; place-items:center; pointer-events:none; z-index:1;">
                <svg viewBox="0 0 48 48" style="width:4.5rem; height:4.5rem; fill:rgba(255,255,255,.9); position:relative;">
                  <path d="M24 2c2.2 13.8 7.9 19.6 22 22-14.1 2.4-19.8 8.2-22 22-2.2-13.8-7.9-19.6-22-22 14.1-2.4 19.8-8.2 22-22Z"/>
                </svg>
              </div>
              <div class="port-bottom">
                <h3 style="font-size:clamp(1.5rem, 3vw, 1.875rem); font-weight:500; letter-spacing:-0.01em;">ShivAnimate</h3>
                <p style="margin-top:0.5rem; max-width:28rem; font-size:0.875rem; color:rgba(255,255,255,.55);">Create name animations and play with interactive canvas text drawing.</p>
                <div style="margin-top:1.25rem; display:flex; flex-wrap:wrap; gap:0.5rem;">
                  <span class="tag-chip light">Canvas API</span><span class="tag-chip light">Animation</span>
                </div>
              </div>
            </article>
          </a>
        </li>
        <!-- Card 3 -->
        <li class="reveal-up" data-reveal style="transition-delay:180ms;">
          <a href="https://Edu-Play-Gold.vercel.app" target="_blank" class="group" style="display:block;">
            <article class="group-hover-lift port-card">
              <div style="display:flex; justify-content:space-between; font-size:0.75rem; text-transform:uppercase; letter-spacing:0.025em; color:rgba(255,255,255,.45); position:relative; z-index:10;">
                <span>EdTech — Platform</span>
                <div class="group-hover-badge" style="width:2.75rem; height:2.75rem; display:grid; place-items:center; border-radius:9999px; background:rgba(255,255,255,.1); color:#fff; box-shadow:inset 0 0 0 1px rgba(255,255,255,.15);">
                  <svg viewBox="0 0 24 24" style="width:1.25rem; height:1.25rem; stroke:currentColor; stroke-width:2; stroke-linecap:round; fill:none;"><path d="M7 17 17 7M8 7h9v9"/></svg>
                </div>
              </div>
              <div style="position:absolute; inset:0; display:grid; place-items:center; pointer-events:none; z-index:1;">
                <svg viewBox="0 0 48 48" style="width:4.5rem; height:4.5rem; fill:rgba(255,255,255,.9); position:relative;">
                  <path d="M24 2c2.2 13.8 7.9 19.6 22 22-14.1 2.4-19.8 8.2-22 22-2.2-13.8-7.9-19.6-22-22 14.1-2.4 19.8-8.2 22-22Z"/>
                </svg>
              </div>
              <div class="port-bottom">
                <h3 style="font-size:clamp(1.5rem, 3vw, 1.875rem); font-weight:500; letter-spacing:-0.01em;">Edu-Play-Gold</h3>
                <p style="margin-top:0.5rem; max-width:28rem; font-size:0.875rem; color:rgba(255,255,255,.55);">Gamified educational platform customized to make learning immersive and rewarding.</p>
                <div style="margin-top:1.25rem; display:flex; flex-wrap:wrap; gap:0.5rem;">
                  <span class="tag-chip light">Gamification</span><span class="tag-chip light">EdTech</span>
                </div>
              </div>
            </article>
          </a>
        </li>
        <!-- Card 4 -->
        <li class="reveal-up" data-reveal style="transition-delay:270ms;">
          <a href="https://shivtegs-snake.vercel.app" target="_blank" class="group" style="display:block;">
            <article class="group-hover-lift port-card">
              <div style="display:flex; justify-content:space-between; font-size:0.75rem; text-transform:uppercase; letter-spacing:0.025em; color:rgba(255,255,255,.45); position:relative; z-index:10;">
                <span>Game — Retro</span>
                <div class="group-hover-badge" style="width:2.75rem; height:2.75rem; display:grid; place-items:center; border-radius:9999px; background:rgba(255,255,255,.1); color:#fff; box-shadow:inset 0 0 0 1px rgba(255,255,255,.15);">
                  <svg viewBox="0 0 24 24" style="width:1.25rem; height:1.25rem; stroke:currentColor; stroke-width:2; stroke-linecap:round; fill:none;"><path d="M7 17 17 7M8 7h9v9"/></svg>
                </div>
              </div>
              <div style="position:absolute; inset:0; display:grid; place-items:center; pointer-events:none; z-index:1;">
                <svg viewBox="0 0 48 48" style="width:4.5rem; height:4.5rem; fill:rgba(255,255,255,.9); position:relative;">
                  <path d="M24 2c2.2 13.8 7.9 19.6 22 22-14.1 2.4-19.8 8.2-22 22-2.2-13.8-7.9-19.6-22-22 14.1-2.4 19.8-8.2 22-22Z"/>
                </svg>
              </div>
              <div class="port-bottom">
                <h3 style="font-size:clamp(1.5rem, 3vw, 1.875rem); font-weight:500; letter-spacing:-0.01em;">Shivteg's Snake Game</h3>
                <p style="margin-top:0.5rem; max-width:28rem; font-size:0.875rem; color:rgba(255,255,255,.55);">Modernized arcade retro snake game with local high score tracking.</p>
                <div style="margin-top:1.25rem; display:flex; flex-wrap:wrap; gap:0.5rem;">
                  <span class="tag-chip light">Arcade</span><span class="tag-chip light">HTML5</span><span class="tag-chip light">Vanilla JS</span>
                </div>
              </div>
            </article>
          </a>
        </li>
      </ul>"""
html = re.sub(r'<ul class="portfolio-grid".*?</ul>', portfolio_html, html, flags=re.DOTALL)

# Services Replacements
services_html = """<ul style="display:flex; flex-direction:column;">
        <li class="reveal-up" data-reveal style="transition-delay:0ms;">
          <a href="#" style="display:block;" class="row-group">
            <div style="display:flex; align-items:center; gap:1rem; border-radius:1.25rem; padding-block:1.5rem;" class="svc-row">
              <span class="svc-num">01</span>
              <h3 class="svc-title">Frontend Development</h3>
              <p class="svc-desc">Crafting responsive, clean, and user-friendly interfaces.</p>
              <div class="row-group-badge svc-badge">
                <svg viewBox="0 0 24 24" style="width:1.25rem; height:1.25rem; stroke:currentColor; stroke-width:2; stroke-linecap:round; fill:none;"><path d="M7 17 17 7M8 7h9v9"/></svg>
              </div>
            </div>
          </a>
        </li>
        <li class="reveal-up" data-reveal style="border-top:1px solid var(--line); transition-delay:80ms;">
          <a href="#" style="display:block;" class="row-group">
            <div style="display:flex; align-items:center; gap:1rem; border-radius:1.25rem; padding-block:1.5rem;" class="svc-row">
              <span class="svc-num">02</span>
              <h3 class="svc-title">Creative Animations</h3>
              <p class="svc-desc">Interactive Canvas API and SVG Graphic Design.</p>
              <div class="row-group-badge svc-badge">
                <svg viewBox="0 0 24 24" style="width:1.25rem; height:1.25rem; stroke:currentColor; stroke-width:2; stroke-linecap:round; fill:none;"><path d="M7 17 17 7M8 7h9v9"/></svg>
              </div>
            </div>
          </a>
        </li>
        <li class="reveal-up" data-reveal style="border-top:1px solid var(--line); transition-delay:160ms;">
          <a href="#" style="display:block;" class="row-group">
            <div style="display:flex; align-items:center; gap:1rem; border-radius:1.25rem; padding-block:1.5rem;" class="svc-row">
              <span class="svc-num">03</span>
              <h3 class="svc-title">Web Games</h3>
              <p class="svc-desc">Game logic, physics, and retro arcade systems in JS.</p>
              <div class="row-group-badge svc-badge">
                <svg viewBox="0 0 24 24" style="width:1.25rem; height:1.25rem; stroke:currentColor; stroke-width:2; stroke-linecap:round; fill:none;"><path d="M7 17 17 7M8 7h9v9"/></svg>
              </div>
            </div>
          </a>
        </li>
        <li class="reveal-up" data-reveal style="border-top:1px solid var(--line); transition-delay:240ms;">
          <a href="#" style="display:block;" class="row-group">
            <div style="display:flex; align-items:center; gap:1rem; border-radius:1.25rem; padding-block:1.5rem;" class="svc-row">
              <span class="svc-num">04</span>
              <h3 class="svc-title">Edu-Tech Platforms</h3>
              <p class="svc-desc">Gamified educational platforms for immersive learning.</p>
              <div class="row-group-badge svc-badge">
                <svg viewBox="0 0 24 24" style="width:1.25rem; height:1.25rem; stroke:currentColor; stroke-width:2; stroke-linecap:round; fill:none;"><path d="M7 17 17 7M8 7h9v9"/></svg>
              </div>
            </div>
          </a>
        </li>
      </ul>"""
html = re.sub(r'<ul style="display:flex; flex-direction:column;">\s*<li class="reveal-up" data-reveal.*?</ul>', services_html, html, flags=re.DOTALL)

# Stats Replacements
stats_html = """<ul class="stats-grid" style="margin-top:3.5rem; display:grid; grid-template-columns:repeat(2,1fr); column-gap:2rem; row-gap:3rem;">
          <li class="reveal-up stat-item" data-reveal style="transition-delay:0ms;">
            <div style="font-size:clamp(3rem, 6vw, 4.5rem); font-weight:600; letter-spacing:-0.02em;">
              <span class="stat-num" data-target="7">0</span>+
            </div>
            <div style="margin-top:0.75rem; font-size:0.875rem; color:rgba(255,255,255,.55);">Live Web Apps</div>
          </li>
          <li class="reveal-up stat-item" data-reveal style="transition-delay:90ms;">
            <div style="font-size:clamp(3rem, 6vw, 4.5rem); font-weight:600; letter-spacing:-0.02em;">
              <span class="stat-num" data-target="100">0</span>%
            </div>
            <div style="margin-top:0.75rem; font-size:0.875rem; color:rgba(255,255,255,.55);">Self-Taught</div>
          </li>
          <li class="reveal-up stat-item" data-reveal style="transition-delay:180ms;">
            <div style="font-size:clamp(3rem, 6vw, 4.5rem); font-weight:600; letter-spacing:-0.02em;">
              <span class="stat-num" data-target="24">0</span>/7
            </div>
            <div style="margin-top:0.75rem; font-size:0.875rem; color:rgba(255,255,255,.55);">Daily Learner</div>
          </li>
          <li class="reveal-up stat-item" data-reveal style="transition-delay:270ms;">
            <div style="font-size:clamp(3rem, 6vw, 4.5rem); font-weight:600; letter-spacing:-0.02em;">
              <span class="stat-num" data-target="100">0</span>+
            </div>
            <div style="margin-top:0.75rem; font-size:0.875rem; color:rgba(255,255,255,.55);">Creative Ideas</div>
          </li>
        </ul>"""
html = re.sub(r'<ul class="stats-grid".*?</ul>', stats_html, html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
