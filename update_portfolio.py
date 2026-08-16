import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. New Portfolio
portfolio_html = """<ul class="portfolio-grid" style="display:grid; grid-template-columns:1fr; gap:1.5rem;">
        <!-- Card 1 -->
        <li class="reveal-up" data-reveal style="transition-delay:0ms;">
          <a href="#" class="group" style="display:block;">
            <article class="group-hover-lift port-card">
              <div style="display:flex; justify-content:space-between; font-size:0.75rem; text-transform:uppercase; letter-spacing:0.025em; color:rgba(255,255,255,.45); position:relative; z-index:10;">
                <span>Full-Stack — Next.js</span>
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
                <h3 style="font-size:clamp(1.5rem, 3vw, 1.875rem); font-weight:500; letter-spacing:-0.01em;">School Dashboard</h3>
                <p style="margin-top:0.5rem; max-width:28rem; font-size:0.875rem; color:rgba(255,255,255,.55);">Next.js + TypeScript + Supabase full-stack administration dashboard for school campus management.</p>
                <div style="margin-top:1.25rem; display:flex; flex-wrap:wrap; gap:0.5rem;">
                  <span class="tag-chip light">Next.js</span><span class="tag-chip light">TypeScript</span><span class="tag-chip light">Supabase</span>
                </div>
              </div>
            </article>
          </a>
        </li>
        <!-- Card 2 -->
        <li class="reveal-up" data-reveal style="transition-delay:90ms;">
          <a href="#" class="group" style="display:block;">
            <article class="group-hover-lift port-card">
              <div style="display:flex; justify-content:space-between; font-size:0.75rem; text-transform:uppercase; letter-spacing:0.025em; color:rgba(255,255,255,.45); position:relative; z-index:10;">
                <span>Admin App — Web</span>
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
                <h3 style="font-size:clamp(1.5rem, 3vw, 1.875rem); font-weight:500; letter-spacing:-0.01em;">ShivAdmin</h3>
                <p style="margin-top:0.5rem; max-width:28rem; font-size:0.875rem; color:rgba(255,255,255,.55);">Dedicated administration & classroom control app with registered student/teacher secure login.</p>
                <div style="margin-top:1.25rem; display:flex; flex-wrap:wrap; gap:0.5rem;">
                  <span class="tag-chip light">Admin Control</span><span class="tag-chip light">Auth</span><span class="tag-chip light">RBAC</span>
                </div>
              </div>
            </article>
          </a>
        </li>
        <!-- Card 3 -->
        <li class="reveal-up" data-reveal style="transition-delay:180ms;">
          <a href="#" class="group" style="display:block;">
            <article class="group-hover-lift port-card">
              <div style="display:flex; justify-content:space-between; font-size:0.75rem; text-transform:uppercase; letter-spacing:0.025em; color:rgba(255,255,255,.45); position:relative; z-index:10;">
                <span>SPA — Realtime</span>
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
                <h3 style="font-size:clamp(1.5rem, 3vw, 1.875rem); font-weight:500; letter-spacing:-0.01em;">ShivClassrooms</h3>
                <p style="margin-top:0.5rem; max-width:28rem; font-size:0.875rem; color:rgba(255,255,255,.55);">Zero-compilation SPA check-in app allowing students to join active classrooms and submit real-time emoji check-ins.</p>
                <div style="margin-top:1.25rem; display:flex; flex-wrap:wrap; gap:0.5rem;">
                  <span class="tag-chip light">HTML/JS</span><span class="tag-chip light">Supabase Realtime</span><span class="tag-chip light">EdTech</span>
                </div>
              </div>
            </article>
          </a>
        </li>
        <!-- Card 4 -->
        <li class="reveal-up" data-reveal style="transition-delay:270ms;">
          <a href="#" class="group" style="display:block;">
            <article class="group-hover-lift port-card">
              <div style="display:flex; justify-content:space-between; font-size:0.75rem; text-transform:uppercase; letter-spacing:0.025em; color:rgba(255,255,255,.45); position:relative; z-index:10;">
                <span>AI System — Gemini</span>
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
                <h3 style="font-size:clamp(1.5rem, 3vw, 1.875rem); font-weight:500; letter-spacing:-0.01em;">AI Class Report Engine</h3>
                <p style="margin-top:0.5rem; max-width:28rem; font-size:0.875rem; color:rgba(255,255,255,.55);">Google Gemini integration allowing teachers to convert raw feedback into actionable lesson plans seamlessly.</p>
                <div style="margin-top:1.25rem; display:flex; flex-wrap:wrap; gap:0.5rem;">
                  <span class="tag-chip light">Google Gemini</span><span class="tag-chip light">AI Agents</span><span class="tag-chip light">Analytics</span>
                </div>
              </div>
            </article>
          </a>
        </li>
      </ul>"""
html = re.sub(r'<ul class="portfolio-grid".*?</ul>', portfolio_html, html, flags=re.DOTALL)

# 2. New Services
services_html = """<ul style="display:flex; flex-direction:column;">
        <li class="reveal-up" data-reveal style="transition-delay:0ms;">
          <a href="#" style="display:block;" class="row-group">
            <div style="display:flex; align-items:center; gap:1rem; border-radius:1.25rem; padding-block:1.5rem;" class="svc-row">
              <span class="svc-num">01</span>
              <h3 class="svc-title">Full-Stack Development</h3>
              <p class="svc-desc">End-to-end web apps with Next.js, TypeScript & Supabase.</p>
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
              <h3 class="svc-title">Real-time Systems</h3>
              <p class="svc-desc">Live synchronization using Supabase Realtime sockets.</p>
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
              <h3 class="svc-title">RBAC Administration</h3>
              <p class="svc-desc">Secure role-based access control and dashboard tooling.</p>
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
              <h3 class="svc-title">AI Agents Integration</h3>
              <p class="svc-desc">Implementing Google Gemini models for smart analytics.</p>
              <div class="row-group-badge svc-badge">
                <svg viewBox="0 0 24 24" style="width:1.25rem; height:1.25rem; stroke:currentColor; stroke-width:2; stroke-linecap:round; fill:none;"><path d="M7 17 17 7M8 7h9v9"/></svg>
              </div>
            </div>
          </a>
        </li>
      </ul>"""
html = re.sub(r'<ul style="display:flex; flex-direction:column;">\s*<li class="reveal-up" data-reveal.*?</ul>', services_html, html, flags=re.DOTALL)

# 3. New Stats
stats_html = """<ul class="stats-grid" style="margin-top:3.5rem; display:grid; grid-template-columns:repeat(2,1fr); column-gap:2rem; row-gap:3rem;">
          <li class="reveal-up stat-item" data-reveal style="transition-delay:0ms;">
            <div style="font-size:clamp(3rem, 6vw, 4.5rem); font-weight:600; letter-spacing:-0.02em;">
              <span class="stat-num" data-target="12">0</span>+
            </div>
            <div style="margin-top:0.75rem; font-size:0.875rem; color:rgba(255,255,255,.55);">Active Repositories</div>
          </li>
          <li class="reveal-up stat-item" data-reveal style="transition-delay:90ms;">
            <div style="font-size:clamp(3rem, 6vw, 4.5rem); font-weight:600; letter-spacing:-0.02em;">
              <span class="stat-num" data-target="4">0</span>
            </div>
            <div style="margin-top:0.75rem; font-size:0.875rem; color:rgba(255,255,255,.55);">RBAC User Roles</div>
          </li>
          <li class="reveal-up stat-item" data-reveal style="transition-delay:180ms;">
            <div style="font-size:clamp(3rem, 6vw, 4.5rem); font-weight:600; letter-spacing:-0.02em;">
              <span class="stat-num" data-target="100">0</span>%
            </div>
            <div style="margin-top:0.75rem; font-size:0.875rem; color:rgba(255,255,255,.55);">Real-time Sync</div>
          </li>
          <li class="reveal-up stat-item" data-reveal style="transition-delay:270ms;">
            <div style="font-size:clamp(3rem, 6vw, 4.5rem); font-weight:600; letter-spacing:-0.02em;">
              <span class="stat-num" data-target="24">0</span>/7
            </div>
            <div style="margin-top:0.75rem; font-size:0.875rem; color:rgba(255,255,255,.55);">AI Integration</div>
          </li>
        </ul>"""
html = re.sub(r'<ul class="stats-grid".*?</ul>', stats_html, html, flags=re.DOTALL)


# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
