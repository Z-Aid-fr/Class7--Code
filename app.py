import streamlit as st
import math

st.set_page_config(
    page_title="Code as a Tool · Class 7",
    page_icon="🖥️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@500;700;800&family=Nunito:wght@400;600;700&display=swap');

html, body, [class*="css"], p, li, span, div, label, input {
    font-family: 'Nunito', sans-serif !important;
}
h1, h2, h3, h4 {
    font-family: 'Baloo 2', cursive !important;
}

/* Hide Streamlit chrome */
#MainMenu { visibility: hidden; }
footer    { visibility: hidden; }
header    { visibility: hidden; }

/* Page background */
.stApp { background: #f4f5fb; }

/* Remove default top padding */
.block-container { padding-top: 2rem !important; }

/* ── Banners ── */
.banner {
    padding: 22px 28px;
    border-radius: 16px;
    color: white;
    margin-bottom: 20px;
}
.banner h2  { margin: 0 0 4px; font-size: 1.6rem; font-family: 'Baloo 2', cursive !important; }
.banner p   { margin: 0; opacity: 0.88; font-size: 0.95rem; }
.banner-home       { background: linear-gradient(135deg, #1e1b4b 0%, #4f46e5 60%, #7c3aed 100%); }
.banner-shapes     { background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); }
.banner-speed      { background: linear-gradient(135deg, #0d9488 0%, #0891b2 100%); }
.banner-attendance { background: linear-gradient(135deg, #d97706 0%, #dc2626 100%); }

/* ── Think box ── */
.think-box {
    background: #eef2ff;
    border-left: 5px solid #4f46e5;
    padding: 14px 18px;
    border-radius: 0 10px 10px 0;
    margin: 16px 0 20px;
    font-size: 0.95rem;
    line-height: 1.7;
}
.think-box b { color: #3730a3; }

/* ── Formula box ── */
.formula-box {
    background: #1e1b4b;
    color: #c7d2fe;
    padding: 14px 20px;
    border-radius: 10px;
    font-family: 'Courier New', monospace !important;
    font-size: 0.92rem;
    line-height: 1.8;
    margin: 14px 0;
    letter-spacing: 0.02em;
}
.formula-box .label { color: #818cf8; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.08em; }

/* ── Result card ── */
.result-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    padding: 20px 24px;
    box-shadow: 0 2px 12px rgba(79, 70, 229, 0.07);
    margin-top: 10px;
}

/* ── Metric chips ── */
.chip-row { display: flex; gap: 14px; flex-wrap: wrap; margin: 14px 0; }
.chip {
    border-radius: 10px;
    padding: 14px 22px;
    text-align: center;
    color: white;
    flex: 1;
    min-width: 120px;
}
.chip .chip-label { font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.08em; opacity: 0.85; }
.chip .chip-value { font-size: 1.6rem; font-weight: 700; font-family: 'Baloo 2', cursive !important; }
.chip-purple { background: linear-gradient(135deg, #4f46e5, #7c3aed); }
.chip-teal   { background: linear-gradient(135deg, #0d9488, #0891b2); }
.chip-amber  { background: linear-gradient(135deg, #d97706, #dc2626); }

/* ── Journey table ── */
.journey-table { width: 100%; border-collapse: collapse; font-size: 0.9rem; margin-bottom: 14px; }
.journey-table th {
    background: #0d9488; color: white;
    padding: 10px 14px; text-align: left;
}
.journey-table th:not(:first-child) { text-align: center; }
.journey-table td { padding: 10px 14px; border-bottom: 1px solid #f0f0f0; }
.journey-table td:not(:first-child) { text-align: center; }
.journey-table tr:nth-child(even) td { background: #f0fdfa; }

/* ── Speed result row ── */
.speed-bar-wrap { display: flex; align-items: center; gap: 10px; }
.speed-bar { height: 14px; border-radius: 4px; background: linear-gradient(90deg, #0d9488, #0891b2); min-width: 4px; }

/* ── Attendance row ── */
.att-row {
    display: flex; align-items: center; justify-content: space-between;
    background: white; border-radius: 10px; padding: 12px 18px;
    margin-bottom: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.05);
}
.att-day   { font-weight: 700; color: #374151; width: 110px; }
.att-pct   { font-weight: 800; font-size: 1.1rem; font-family: 'Baloo 2', cursive !important; width: 70px; text-align: right; }
.att-bar-bg { flex: 1; height: 10px; background: #f1f5f9; border-radius: 5px; margin: 0 12px; }
.att-bar-fill { height: 10px; border-radius: 5px; }

/* ── Notice ── */
.notice-box {
    background: #fffbeb;
    border: 1px solid #fbbf24;
    padding: 12px 18px;
    border-radius: 8px;
    font-size: 0.88rem;
    margin-top: 16px;
    line-height: 1.6;
}

/* ── Summary table (home) ── */
.summary-table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
.summary-table th { background: #1e1b4b; color: #a5b4fc; padding: 10px 16px; text-align: left; }
.summary-table td { padding: 10px 16px; border-bottom: 1px solid #e2e8f0; }
.summary-table tr:nth-child(even) td { background: #f8f9ff; }

/* ── Rank list ── */
.rank-card {
    background: #f0fdfa;
    border: 1px solid #99f6e4;
    border-radius: 10px;
    padding: 14px 18px;
    margin-top: 12px;
    font-size: 0.92rem;
}
.rank-card h4 { color: #0d9488; margin: 0 0 8px; font-family: 'Baloo 2', cursive !important; }
.rank-card ol { margin: 0; padding-left: 18px; line-height: 2; }

/* ── Overall badge ── */
.overall-badge {
    display: inline-block;
    color: white;
    padding: 14px 24px;
    border-radius: 12px;
    font-size: 1.15rem;
    font-weight: 700;
    font-family: 'Baloo 2', cursive !important;
    margin: 14px 0;
}

/* Tab styling */
.stTabs [data-baseweb="tab-list"] { gap: 6px; }
.stTabs [data-baseweb="tab"] {
    border-radius: 8px 8px 0 0 !important;
    font-family: 'Nunito', sans-serif !important;
    font-weight: 600;
}

/* Streamlit widget labels */
.stSelectbox label, .stNumberInput label { font-weight: 600 !important; color: #374151 !important; }

/* Button */
.stButton > button {
    font-family: 'Nunito', sans-serif !important;
    font-weight: 700 !important;
    border-radius: 10px !important;
    padding: 8px 24px !important;
}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# HEADER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="banner banner-home">
  <h2>🖥️ Code as a Tool</h2>
  <p>Class 7 &nbsp;·&nbsp; Mathematics & Science &nbsp;·&nbsp;
     Three activities showing how code solves problems you already know</p>
</div>
""", unsafe_allow_html=True)

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab_home, tab1, tab2, tab3 = st.tabs([
    "🏠 How it Works",
    "📐 Activity 1 — Shapes",
    "🚀 Activity 2 — Speed",
    "📅 Activity 3 — Attendance"
])

# ══════════════════════════════════════════════════════════════════════════════
# HOME TAB
# ══════════════════════════════════════════════════════════════════════════════
with tab_home:
    st.markdown("""
    <p style="font-size:1.05rem; color:#374151; line-height:1.8; margin-bottom:20px;">
    Every time you solve a problem — whether it's finding the area of a shape, calculating speed,
    or working out attendance — you follow a set of steps.<br><br>
    You take some <b>inputs</b>, do some <b>processing</b>, and get an <b>output</b>.<br>
    That is <em>exactly</em> what a computer program does.
    </p>

    <table class="summary-table">
      <thead>
        <tr><th>Step</th><th>What it means</th><th>Example</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><b>📥 Input</b></td>
          <td>Data you provide</td>
          <td>Side length, distance, days attended</td>
        </tr>
        <tr>
          <td><b>⚙️ Process</b></td>
          <td>Rules / formula applied</td>
          <td>Area = side², Speed = d/t, % = (a/t)×100</td>
        </tr>
        <tr>
          <td><b>📤 Output</b></td>
          <td>The result</td>
          <td>Area in cm², speed in km/h, percentage</td>
        </tr>
      </tbody>
    </table>

    <div class="think-box" style="margin-top:20px; border-left-color:#7c3aed; background:#f5f3ff;">
      <b>The formula was never the hard part — you already know the formulas.</b><br>
      What programming adds is the ability to apply that formula <em>instantly</em>,
      <em>repeatedly</em>, and <em>without error</em>. That is what you will see in the three activities.
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# ACTIVITY 1 — AREA & PERIMETER
# ══════════════════════════════════════════════════════════════════════════════
with tab1:
    st.markdown("""
    <div class="banner banner-shapes">
      <h2>📐 Area &amp; Perimeter of Shapes</h2>
      <p>Mathematics · Chapter 11 · Class 7</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="think-box">
      <b>🤔 Think First — answer these before changing anything:</b>
      <ol style="margin:8px 0 0; padding-left:18px;">
        <li>If a square has a side of 5 cm, what is its area? What is its perimeter?</li>
        <li>What measurements do you need to find the area of a rectangle? A circle?</li>
        <li>What is the difference between area and perimeter in plain words?</li>
      </ol>
    </div>
    """, unsafe_allow_html=True)

    shape = st.selectbox(
        "Select a shape",
        ["Square", "Rectangle", "Triangle (Equilateral)", "Circle"],
        key="shape_select"
    )

    # ── Dynamic inputs + calculation ─────────────────────────────────────────
    if shape == "Square":
        side = st.number_input("Side length (cm)", min_value=0.1, value=5.0, step=0.5, key="sq_side")
        area  = round(side ** 2, 2)
        perim = round(4 * side, 2)
        formula_area  = f"side × side  =  {side} × {side}  =  <b>{area} cm²</b>"
        formula_perim = f"4 × side  =  4 × {side}  =  <b>{perim} cm</b>"

    elif shape == "Rectangle":
        c1, c2 = st.columns(2)
        with c1:
            length = st.number_input("Length (cm)", min_value=0.1, value=8.0, step=0.5, key="rect_l")
        with c2:
            width  = st.number_input("Width (cm)",  min_value=0.1, value=5.0, step=0.5, key="rect_w")
        area  = round(length * width, 2)
        perim = round(2 * (length + width), 2)
        formula_area  = f"length × width  =  {length} × {width}  =  <b>{area} cm²</b>"
        formula_perim = f"2 × (l + w)  =  2 × ({length} + {width})  =  <b>{perim} cm</b>"

    elif shape == "Triangle (Equilateral)":
        side  = st.number_input("Side length (cm)", min_value=0.1, value=6.0, step=0.5, key="tri_side")
        area  = round((math.sqrt(3) / 4) * side ** 2, 2)
        perim = round(3 * side, 2)
        formula_area  = f"(√3 / 4) × side²  =  (√3 / 4) × {side}²  ≈  <b>{area} cm²</b>"
        formula_perim = f"3 × side  =  3 × {side}  =  <b>{perim} cm</b>"

    elif shape == "Circle":
        radius = st.number_input("Radius (cm)", min_value=0.1, value=7.0, step=0.5, key="circ_r")
        area   = round(math.pi * radius ** 2, 2)
        perim  = round(2 * math.pi * radius, 2)
        formula_area  = f"π × r²  =  π × {radius}²  ≈  <b>{area} cm²</b>"
        formula_perim = f"2 × π × r  =  2 × π × {radius}  ≈  <b>{perim} cm</b>"

    # ── Results ───────────────────────────────────────────────────────────────
    st.markdown(f"""
    <div class="result-card">
      <div class="formula-box">
        <div class="label">Area formula</div>
        {formula_area}<br>
        <div class="label" style="margin-top:10px;">Perimeter formula</div>
        {formula_perim}
      </div>
      <div class="chip-row">
        <div class="chip chip-purple">
          <div class="chip-label">Area</div>
          <div class="chip-value">{area} cm²</div>
        </div>
        <div class="chip chip-purple" style="background:linear-gradient(135deg,#7c3aed,#9333ea);">
          <div class="chip-label">Perimeter</div>
          <div class="chip-value">{perim} cm</div>
        </div>
      </div>
    </div>
    <div class="notice-box">
      🔍 <b>Notice:</b> The program used the same formula from your textbook.
      The only difference? It didn't need a pencil — it just needed the right instructions.
      Change the value above and see how the result updates instantly.
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# ACTIVITY 2 — SPEED CALCULATOR
# ══════════════════════════════════════════════════════════════════════════════
with tab2:
    st.markdown("""
    <div class="banner banner-speed">
      <h2>🚀 Speed Calculator — Five Journeys</h2>
      <p>Science · Motion and Time · Class 7</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="think-box" style="border-left-color:#0d9488; background:#f0fdfa;">
      <b>🤔 Think First:</b>
      <ol style="margin:8px 0 0; padding-left:18px;">
        <li>How do we calculate the speed of a moving object?</li>
        <li>If a bus travels 120 km in 2 hours, what is its speed?</li>
        <li>Two cars travel the same distance — one takes 1 hour, the other 3 hours.
            Which is faster? How do you know <em>without</em> calculating?</li>
      </ol>
    </div>
    """, unsafe_allow_html=True)

    # ── Journey data ──────────────────────────────────────────────────────────
    journeys = [
        {"name": "School Bus",      "from": "Village",   "to": "School",   "dist": 12,  "time": 30},
        {"name": "Family Car Trip", "from": "Srinagar",  "to": "Gulmarg",  "dist": 56,  "time": 90},
        {"name": "Cyclist",         "from": "Home",      "to": "Market",   "dist": 4,   "time": 20},
        {"name": "Express Train",   "from": "Delhi",     "to": "Agra",     "dist": 200, "time": 100},
        {"name": "Walking",         "from": "Park Gate", "to": "Fountain", "dist": 1.5, "time": 18},
    ]

    # Table header
    rows_html = "".join(f"""
    <tr>
      <td><b>{j['name']}</b></td>
      <td>{j['from']} → {j['to']}</td>
      <td>{j['dist']} km</td>
      <td>{j['time']} min</td>
    </tr>""" for j in journeys)

    st.markdown(f"""
    <table class="journey-table">
      <thead>
        <tr>
          <th>Journey</th><th>Route</th><th>Distance</th><th>Time</th>
        </tr>
      </thead>
      <tbody>{rows_html}</tbody>
    </table>
    """, unsafe_allow_html=True)

    if st.button("⚡ Calculate All Speeds", key="speed_btn", type="primary"):
        results = []
        for j in journeys:
            time_hrs = j["time"] / 60
            speed = round(j["dist"] / time_hrs, 2)
            results.append({**j, "speed": speed})

        max_speed = max(r["speed"] for r in results)
        ranked = sorted(results, key=lambda x: x["speed"], reverse=True)

        speed_rows = ""
        medals = {1: "🥇", 2: "🥈", 3: "🥉", 4: "4th", 5: "5th"}
        for i, r in enumerate(results):
            bar_w = int((r["speed"] / max_speed) * 200)
            speed_rows += f"""
            <tr>
              <td><b>{r['name']}</b></td>
              <td>
                <div class="speed-bar-wrap">
                  <div class="speed-bar" style="width:{bar_w}px;"></div>
                  <b style="color:#0d9488;">{r['speed']} km/h</b>
                </div>
              </td>
            </tr>"""

        rank_items = "".join(
            f"<li>{medals[i+1]} <b>{r['name']}</b> — {r['speed']} km/h</li>"
            for i, r in enumerate(ranked)
        )

        st.markdown(f"""
        <div class="result-card">
          <div class="formula-box">
            <div class="label">Formula used for each journey</div>
            Speed = Distance ÷ Time (in hours)
          </div>
          <table class="journey-table" style="margin-bottom:0;">
            <thead>
              <tr><th>Journey</th><th>Speed</th></tr>
            </thead>
            <tbody>{speed_rows}</tbody>
          </table>
          <div class="rank-card">
            <h4>🏆 Ranked by Speed</h4>
            <ol>{rank_items}</ol>
          </div>
        </div>
        <div class="notice-box">
          🔍 <b>Notice:</b> The program applied <em>Speed = Distance ÷ Time</em> five times in a row.
          This is called <b>repetition</b> — doing the same operation on different inputs.
          In programming, this is what a <b>loop</b> does.
        </div>
        """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# ACTIVITY 3 — ATTENDANCE PERCENTAGE
# ══════════════════════════════════════════════════════════════════════════════
with tab3:
    st.markdown("""
    <div class="banner banner-attendance">
      <h2>📅 Attendance Percentage Calculator</h2>
      <p>Mathematics · Percentages · Class 7</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="think-box" style="border-left-color:#d97706; background:#fffbeb;">
      <b>🤔 Think First:</b>
      <ol style="margin:8px 0 0; padding-left:18px;">
        <li>If your school has 6 periods and you attended 5, what percentage is that?</li>
        <li>What does a percentage actually tell us? Why is it useful?</li>
        <li>If you attended 80% on Monday but 50% on Friday, what does that tell you?</li>
      </ol>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style="font-size:0.93rem; color:#6b7280; margin-bottom:12px;">
    Enter the number of periods <b>attended</b> and <b>total periods</b> for each day.
    The percentage updates automatically.
    </p>
    """, unsafe_allow_html=True)

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    day_attended = []
    day_total    = []

    for day in days:
        c1, c2, c3 = st.columns([2, 1.2, 1.2])
        with c1:
            st.markdown(f"<p style='font-weight:700; color:#374151; margin:10px 0 0;'>{day}</p>",
                        unsafe_allow_html=True)
        with c2:
            att = st.number_input("Attended", min_value=0, max_value=12, value=5,
                                  key=f"att_{day}", label_visibility="collapsed")
        with c3:
            tot = st.number_input("Total", min_value=1, max_value=12, value=6,
                                  key=f"tot_{day}", label_visibility="collapsed")
        day_attended.append(att)
        day_total.append(tot)

    st.markdown("<p style='font-size:0.78rem; color:#9ca3af; margin-top:-6px;'>↑ Attended periods &nbsp;&nbsp; ↑ Total periods</p>",
                unsafe_allow_html=True)

    # ── Live results ──────────────────────────────────────────────────────────
    st.markdown("---")
    st.markdown("### 📊 Results")

    att_rows = ""
    total_att, total_periods = 0, 0

    for i, day in enumerate(days):
        att = day_attended[i]
        tot = day_total[i]
        pct = round((att / tot) * 100, 1)
        total_att     += att
        total_periods += tot

        if pct >= 75:
            color, badge = "#16a34a", "✅"
        elif pct >= 50:
            color, badge = "#d97706", "⚠️"
        else:
            color, badge = "#dc2626", "❌"

        bar_w = int(pct)
        att_rows += f"""
        <div class="att-row">
          <div class="att-day">{day}</div>
          <div style="flex:1; display:flex; align-items:center; gap:10px;">
            <div class="att-bar-bg" style="flex:1;">
              <div class="att-bar-fill" style="width:{bar_w}%; background:{color};"></div>
            </div>
          </div>
          <div class="att-pct" style="color:{color};">{pct}%</div>
          <div style="width:28px; text-align:center; font-size:1.1rem;">{badge}</div>
        </div>"""

    overall = round((total_att / total_periods) * 100, 1)
    overall_color = "#16a34a" if overall >= 75 else ("#d97706" if overall >= 50 else "#dc2626")

    st.markdown(f"""
    <div class="result-card">
      <div class="formula-box">
        <div class="label">Formula used for each day</div>
        Percentage = (Classes Attended ÷ Total Classes) × 100
      </div>
      {att_rows}
      <div class="overall-badge" style="background:{overall_color};">
        📌 Overall Weekly Attendance: {overall}%
        &nbsp; ({total_att} of {total_periods} periods)
      </div>
    </div>
    <div class="notice-box">
      🔍 <b>Notice:</b> The same formula was applied to each day, then the totals were
      <em>accumulated</em> to get your weekly percentage.
      This is how your school's actual attendance report works — just automated.
    </div>
    """, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<hr style="margin-top:40px; border-color:#e2e8f0;">
<p style="text-align:center; color:#9ca3af; font-size:0.82rem; padding-bottom:10px;">
  Grade 7 Technology & Thinking Curriculum &nbsp;·&nbsp; CQAI / TLL
</p>
""", unsafe_allow_html=True)
