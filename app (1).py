import streamlit as st
import math

st.set_page_config(
    page_title="Code as a Tool · Class 7",
    page_icon="🖥️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ── CSS — scoped tightly so it doesn't fight Streamlit's own widget styles ────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@500;700;800&family=Nunito:wght@400;600;700&display=swap');

/* Page shell */
.stApp { background: #f4f5fb; }
.block-container { padding-top: 1.8rem !important; max-width: 780px; }

/* Hide chrome */
#MainMenu, footer, header { visibility: hidden; }

/* Banners */
.banner {
    padding: 22px 28px; border-radius: 16px;
    color: white; margin-bottom: 20px;
}
.banner h2 {
    margin: 0 0 4px; font-size: 1.55rem;
    font-family: 'Baloo 2', cursive; font-weight: 800;
}
.banner p  { margin: 0; opacity: 0.88; font-size: 0.92rem; }
.banner-home       { background: linear-gradient(135deg, #1e1b4b 0%, #4338ca 60%, #7c3aed 100%); }
.banner-shapes     { background: linear-gradient(135deg, #4338ca, #7c3aed); }
.banner-speed      { background: linear-gradient(135deg, #0d9488, #0891b2); }
.banner-attendance { background: linear-gradient(135deg, #d97706, #dc2626); }

/* Think box */
.think-box {
    background: #eef2ff; border-left: 5px solid #4f46e5;
    padding: 14px 18px; border-radius: 0 10px 10px 0;
    margin: 16px 0 20px; font-size: 0.94rem; line-height: 1.75;
    color: #1f2937;
}
.think-box b { color: #3730a3; }
.think-box ol { margin: 8px 0 0; padding-left: 18px; }

/* Formula box */
.formula-box {
    background: #1e1b4b; color: #c7d2fe;
    padding: 14px 20px; border-radius: 10px;
    font-family: 'Courier New', monospace;
    font-size: 0.9rem; line-height: 1.85; margin: 14px 0;
}
.formula-box .flabel {
    color: #818cf8; font-size: 0.72rem;
    text-transform: uppercase; letter-spacing: 0.08em;
    font-family: 'Nunito', sans-serif;
}

/* Result card wrapper */
.result-card {
    background: white; border: 1px solid #e2e8f0;
    border-radius: 14px; padding: 20px 24px;
    box-shadow: 0 2px 12px rgba(79,70,229,0.07);
    margin-top: 10px;
}

/* Metric chips */
.chip-row { display: flex; gap: 14px; flex-wrap: wrap; margin: 14px 0 0; }
.chip {
    border-radius: 10px; padding: 14px 22px;
    text-align: center; color: white; flex: 1; min-width: 120px;
}
.chip .clabel { font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.08em; opacity: 0.85; font-family: 'Nunito', sans-serif; }
.chip .cvalue { font-size: 1.55rem; font-weight: 800; font-family: 'Baloo 2', cursive; }
.chip-purple { background: linear-gradient(135deg, #4338ca, #7c3aed); }
.chip-purple2 { background: linear-gradient(135deg, #6d28d9, #9333ea); }
.chip-teal   { background: linear-gradient(135deg, #0d9488, #0891b2); }
.chip-amber  { background: linear-gradient(135deg, #d97706, #dc2626); }

/* Journey table */
.jtable { width:100%; border-collapse:collapse; font-size:0.88rem; margin-bottom:14px; }
.jtable th { background:#0d9488; color:white; padding:10px 13px; text-align:left; }
.jtable td { padding:10px 13px; border-bottom:1px solid #f0f0f0; color:#1f2937; }
.jtable tr:nth-child(even) td { background:#f0fdfa; }
.jtable td:nth-child(3), .jtable td:nth-child(4), .jtable th:nth-child(3), .jtable th:nth-child(4) { text-align:center; }

/* Speed bar */
.sbar-wrap { display:flex; align-items:center; gap:10px; }
.sbar { height:13px; border-radius:4px; background:linear-gradient(90deg,#0d9488,#0891b2); min-width:4px; }

/* Rank card */
.rank-card {
    background:#f0fdfa; border:1px solid #99f6e4;
    border-radius:10px; padding:14px 18px; margin-top:12px;
}
.rank-card h4 { color:#0d9488; margin:0 0 8px; font-family:'Baloo 2',cursive; }
.rank-card ol { margin:0; padding-left:18px; line-height:2.1; font-size:0.91rem; color:#1f2937; }

/* Attendance row */
.att-row {
    display:flex; align-items:center; gap:10px;
    background:white; border-radius:10px; padding:11px 16px;
    margin-bottom:8px; box-shadow:0 1px 4px rgba(0,0,0,0.05);
}
.att-day  { font-weight:700; color:#374151; min-width:100px; font-size:0.92rem; }
.att-pct  { font-weight:800; font-size:1.05rem; font-family:'Baloo 2',cursive; min-width:55px; text-align:right; }
.att-badge { font-size:1.1rem; min-width:28px; text-align:center; }
.att-bg   { flex:1; height:10px; background:#f1f5f9; border-radius:5px; }
.att-fill { height:10px; border-radius:5px; }

/* Overall badge */
.overall-badge {
    display:inline-block; color:white;
    padding:14px 22px; border-radius:12px;
    font-size:1.1rem; font-weight:700;
    font-family:'Baloo 2',cursive; margin:14px 0;
}

/* Notice */
.notice-box {
    background:#fffbeb; border:1px solid #fbbf24;
    padding:12px 16px; border-radius:8px;
    font-size:0.87rem; margin-top:16px; line-height:1.65; color:#1f2937;
}

/* Summary table (home tab) */
.stbl { width:100%; border-collapse:collapse; font-size:0.9rem; }
.stbl th { background:#1e1b4b; color:#a5b4fc; padding:10px 14px; text-align:left; }
.stbl td { padding:10px 14px; border-bottom:1px solid #e2e8f0; color:#1f2937; }
.stbl tr:nth-child(even) td { background:#f8f9ff; }

/* Column headers for attendance input */
.col-header {
    font-size:0.74rem; font-weight:700; color:#9ca3af;
    text-transform:uppercase; letter-spacing:0.07em;
    text-align:center; margin-bottom:2px;
}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# APP HEADER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="banner banner-home">
  <h2>🖥️ Code as a Tool</h2>
  <p>Class 7 &nbsp;·&nbsp; Mathematics &amp; Science &nbsp;·&nbsp;
     Three activities showing how code solves problems you already know</p>
</div>
""", unsafe_allow_html=True)

tab_home, tab1, tab2, tab3 = st.tabs([
    "🏠 How it Works",
    "📐 Activity 1 — Shapes",
    "🚀 Activity 2 — Speed",
    "📅 Activity 3 — Attendance"
])

# ══════════════════════════════════════════════════════════════════════════════
# HOME
# ══════════════════════════════════════════════════════════════════════════════
with tab_home:
    st.markdown("""
    <p style="font-size:1.02rem; color:#374151; line-height:1.85; margin-bottom:20px;">
    Every time you solve a problem — finding the area of a shape, calculating speed,
    or working out attendance — you follow a set of steps.<br><br>
    You take some <b>inputs</b>, do some <b>processing</b>, and get an <b>output</b>.
    That is <em>exactly</em> what a computer program does.
    </p>
    <table class="stbl">
      <thead><tr><th>Step</th><th>What it means</th><th>Example from today</th></tr></thead>
      <tbody>
        <tr><td><b>📥 Input</b></td><td>Data you provide</td><td>Side length, distance, days attended</td></tr>
        <tr><td><b>⚙️ Process</b></td><td>Rules / formula applied</td><td>Area = side², Speed = d ÷ t, % = (a÷t)×100</td></tr>
        <tr><td><b>📤 Output</b></td><td>The result</td><td>Area in cm², speed in km/h, percentage</td></tr>
      </tbody>
    </table>
    <div class="think-box" style="margin-top:20px; border-left-color:#7c3aed; background:#f5f3ff;">
      <b>The formula was never the hard part — you already know the formulas.</b><br>
      What programming adds is the ability to apply that formula <em>instantly</em>,
      <em>repeatedly</em>, and <em>without error</em>.
      That is what you will see in the three activities.
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# ACTIVITY 1 — SHAPES
# ══════════════════════════════════════════════════════════════════════════════
with tab1:
    st.markdown("""
    <div class="banner banner-shapes">
      <h2>📐 Area &amp; Perimeter of Shapes</h2>
      <p>Mathematics · Chapter 11 · Class 7</p>
    </div>
    <div class="think-box">
      <b>🤔 Think First — answer these before changing anything:</b>
      <ol>
        <li>If a square has a side of 5 cm, what is its area? What is its perimeter?</li>
        <li>What measurements do you need for a rectangle? For a circle?</li>
        <li>What is the difference between area and perimeter in plain words?</li>
      </ol>
    </div>
    """, unsafe_allow_html=True)

    shape = st.selectbox("Select a shape",
                         ["Square", "Rectangle", "Triangle (Equilateral)", "Circle"])

    if shape == "Square":
        side = st.number_input("Side length (cm)", min_value=0.1, value=5.0, step=0.5)
        area, perim = round(side**2, 2), round(4*side, 2)
        f_area  = f"side × side = {side} × {side} = <b>{area} cm²</b>"
        f_perim = f"4 × side = 4 × {side} = <b>{perim} cm</b>"

    elif shape == "Rectangle":
        c1, c2 = st.columns(2)
        with c1: length = st.number_input("Length (cm)", min_value=0.1, value=8.0, step=0.5)
        with c2: width  = st.number_input("Width (cm)",  min_value=0.1, value=5.0, step=0.5)
        area, perim = round(length*width, 2), round(2*(length+width), 2)
        f_area  = f"length × width = {length} × {width} = <b>{area} cm²</b>"
        f_perim = f"2 × (l + w) = 2 × ({length} + {width}) = <b>{perim} cm</b>"

    elif shape == "Triangle (Equilateral)":
        side = st.number_input("Side length (cm)", min_value=0.1, value=6.0, step=0.5)
        area, perim = round((math.sqrt(3)/4)*side**2, 2), round(3*side, 2)
        f_area  = f"(√3 / 4) × side² = (√3/4) × {side}² ≈ <b>{area} cm²</b>"
        f_perim = f"3 × side = 3 × {side} = <b>{perim} cm</b>"

    else:  # Circle
        radius = st.number_input("Radius (cm)", min_value=0.1, value=7.0, step=0.5)
        area, perim = round(math.pi*radius**2, 2), round(2*math.pi*radius, 2)
        f_area  = f"π × r² = π × {radius}² ≈ <b>{area} cm²</b>"
        f_perim = f"2 × π × r = 2 × π × {radius} ≈ <b>{perim} cm</b>"

    st.markdown(f"""
    <div class="result-card">
      <div class="formula-box">
        <div class="flabel">Area formula</div>
        {f_area}
        <div class="flabel" style="margin-top:10px;">Perimeter / Circumference formula</div>
        {f_perim}
      </div>
      <div class="chip-row">
        <div class="chip chip-purple">
          <div class="clabel">Area</div>
          <div class="cvalue">{area} cm²</div>
        </div>
        <div class="chip chip-purple2">
          <div class="clabel">Perimeter</div>
          <div class="cvalue">{perim} cm</div>
        </div>
      </div>
    </div>
    <div class="notice-box">
      🔍 <b>Notice:</b> The program used the exact same formula from your textbook.
      The only difference — it didn't need a pencil.
      Try changing the value above and watch the result update instantly.
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# ACTIVITY 2 — SPEED
# ══════════════════════════════════════════════════════════════════════════════
with tab2:
    st.markdown("""
    <div class="banner banner-speed">
      <h2>🚀 Speed Calculator — Five Journeys</h2>
      <p>Science · Motion and Time · Class 7</p>
    </div>
    <div class="think-box" style="border-left-color:#0d9488; background:#f0fdfa;">
      <b>🤔 Think First:</b>
      <ol>
        <li>How do we calculate the speed of a moving object?</li>
        <li>If a bus travels 120 km in 2 hours, what is its speed?</li>
        <li>Two cars travel the same distance — one takes 1 hour, the other 3 hours.
            Which is faster? How do you know <em>without</em> calculating?</li>
      </ol>
    </div>
    """, unsafe_allow_html=True)

    journeys = [
        {"name": "School Bus",      "from": "Village",   "to": "School",   "dist": 12,  "time": 30},
        {"name": "Family Car Trip", "from": "Srinagar",  "to": "Gulmarg",  "dist": 56,  "time": 90},
        {"name": "Cyclist",         "from": "Home",      "to": "Market",   "dist": 4,   "time": 20},
        {"name": "Express Train",   "from": "Delhi",     "to": "Agra",     "dist": 200, "time": 100},
        {"name": "Walking",         "from": "Park Gate", "to": "Fountain", "dist": 1.5, "time": 18},
    ]

    rows = "".join(f"""<tr>
        <td><b>{j['name']}</b></td>
        <td>{j['from']} → {j['to']}</td>
        <td>{j['dist']} km</td>
        <td>{j['time']} min</td>
    </tr>""" for j in journeys)

    st.markdown(f"""
    <table class="jtable">
      <thead><tr><th>Journey</th><th>Route</th><th>Distance</th><th>Time</th></tr></thead>
      <tbody>{rows}</tbody>
    </table>
    """, unsafe_allow_html=True)

    if st.button("⚡ Calculate All Speeds", type="primary"):
        results = [{**j, "speed": round(j["dist"] / (j["time"]/60), 2)} for j in journeys]
        max_spd  = max(r["speed"] for r in results)
        ranked   = sorted(results, key=lambda x: x["speed"], reverse=True)
        medals   = {0:"🥇", 1:"🥈", 2:"🥉", 3:"4th", 4:"5th"}

        speed_rows = "".join(f"""<tr>
            <td><b>{r['name']}</b></td>
            <td>
              <div class="sbar-wrap">
                <div class="sbar" style="width:{int((r['speed']/max_spd)*200)}px;"></div>
                <b style="color:#0d9488;">{r['speed']} km/h</b>
              </div>
            </td>
        </tr>""" for r in results)

        rank_items = "".join(
            f"<li>{medals[i]} <b>{r['name']}</b> — {r['speed']} km/h</li>"
            for i, r in enumerate(ranked)
        )

        st.markdown(f"""
        <div class="result-card">
          <div class="formula-box">
            <div class="flabel">Formula used for every journey</div>
            Speed = Distance ÷ Time (converted to hours)
          </div>
          <table class="jtable" style="margin-bottom:0">
            <thead><tr><th>Journey</th><th>Computed Speed</th></tr></thead>
            <tbody>{speed_rows}</tbody>
          </table>
          <div class="rank-card">
            <h4>🏆 Ranked by Speed</h4>
            <ol>{rank_items}</ol>
          </div>
        </div>
        <div class="notice-box">
          🔍 <b>Notice:</b> The program applied <em>Speed = Distance ÷ Time</em> five times in a row.
          This is called <b>repetition</b> — the same operation on different inputs.
          In programming, this is what a <b>loop</b> does.
        </div>
        """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# ACTIVITY 3 — ATTENDANCE
# ══════════════════════════════════════════════════════════════════════════════
with tab3:
    st.markdown("""
    <div class="banner banner-attendance">
      <h2>📅 Attendance Percentage Calculator</h2>
      <p>Mathematics · Percentages · Class 7</p>
    </div>
    <div class="think-box" style="border-left-color:#d97706; background:#fffbeb;">
      <b>🤔 Think First:</b>
      <ol>
        <li>If your school has 6 periods and you attended 5, what percentage is that?</li>
        <li>What does a percentage actually tell us? Why is it more useful than a fraction?</li>
        <li>If you attended 80% on Monday but only 50% on Friday, what does that tell you?</li>
      </ol>
    </div>
    """, unsafe_allow_html=True)

    # Column headers
    h1, h2, h3 = st.columns([2, 1.2, 1.2])
    with h2: st.markdown('<div class="col-header">Attended</div>', unsafe_allow_html=True)
    with h3: st.markdown('<div class="col-header">Total</div>', unsafe_allow_html=True)

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    attended_vals, total_vals = [], []

    for day in days:
        c1, c2, c3 = st.columns([2, 1.2, 1.2])
        with c1:
            st.markdown(f"<p style='font-weight:700;color:#374151;margin:8px 0 0;'>{day}</p>",
                        unsafe_allow_html=True)
        with c2:
            att = st.number_input("Attended", 0, 12, 5, key=f"a_{day}",
                                  label_visibility="collapsed")
        with c3:
            tot = st.number_input("Total", 1, 12, 6, key=f"t_{day}",
                                  label_visibility="collapsed")
        attended_vals.append(att)
        total_vals.append(tot)

    st.markdown("---")
    st.markdown("### 📊 Results")

    att_rows   = ""
    grand_att  = sum(attended_vals)
    grand_tot  = sum(total_vals)

    for i, day in enumerate(days):
        pct = round((attended_vals[i] / total_vals[i]) * 100, 1)
        if   pct >= 75: color, badge = "#16a34a", "✅"
        elif pct >= 50: color, badge = "#d97706", "⚠️"
        else:           color, badge = "#dc2626", "❌"

        att_rows += f"""
        <div class="att-row">
          <div class="att-day">{day}</div>
          <div class="att-bg"><div class="att-fill" style="width:{int(pct)}%;background:{color};"></div></div>
          <div class="att-pct" style="color:{color};">{pct}%</div>
          <div class="att-badge">{badge}</div>
        </div>"""

    overall = round((grand_att / grand_tot) * 100, 1)
    oc = "#16a34a" if overall >= 75 else ("#d97706" if overall >= 50 else "#dc2626")

    st.markdown(f"""
    <div class="result-card">
      <div class="formula-box">
        <div class="flabel">Formula used for each day</div>
        Percentage = (Classes Attended ÷ Total Classes) × 100
      </div>
      {att_rows}
      <div class="overall-badge" style="background:{oc};">
        📌 Overall Weekly Attendance: {overall}%
        &nbsp;({grand_att} of {grand_tot} periods)
      </div>
    </div>
    <div class="notice-box">
      🔍 <b>Notice:</b> The same formula was applied to each day, then all five days
      were <b>accumulated</b> to give the weekly total.
      This is how your school office calculates attendance — just automated.
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<hr style="margin-top:36px; border-color:#e2e8f0;">
<p style="text-align:center; color:#9ca3af; font-size:0.8rem; padding-bottom:8px;">
  Grade 7 Technology &amp; Thinking Curriculum &nbsp;·&nbsp; CQAI / TLL
</p>
""", unsafe_allow_html=True)
