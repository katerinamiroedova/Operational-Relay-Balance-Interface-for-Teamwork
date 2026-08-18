import streamlit as st
from datetime import datetime, timedelta
import time

# ============================================================
# ORBIT
# Operational Relay & Balance Interface for Teamwork
# MISSION 07 — CLIMATE MONITORING EXPEDITION
# ============================================================

st.set_page_config(
    page_title="ORBIT — Mission Control",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CONSTANTS
# ============================================================

MISSION_TIME = "14:32 UTC"
STATION_ALTITUDE = "412 km"
EARTH_LATENCY = "0.8 s"

# ============================================================
# SESSION STATE
# ============================================================

defaults = {
    "page": "Command Center",
    "quiet_orbit": True,
    "earth_link": True,
    "emergency_mode": False,
    "selected_crew": None,
    "selected_channel": None,
    "mediation": False,
    "notifications": [],
    "decision_log": [
        {
            "time": "14:18",
            "actor": "ORBIT",
            "action": "Protected D. Kim's rest period",
            "type": "SYSTEM"
        },
        {
            "time": "14:11",
            "actor": "COMMAND",
            "action": "Mediation protocol initiated",
            "type": "COMMAND"
        },
        {
            "time": "13:52",
            "actor": "ENGINEERING",
            "action": "Life Support inspection scheduled",
            "type": "SYSTEM"
        }
    ],
    "messages": [],
    "last_action": "",
    "mission_alerts": {
        "life_support": True,
        "mediation": True,
        "earth_request": True
    }
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# CREW DATA
# ============================================================

crew = {
    "A. Ivanov": {
        "role": "Systems Engineer",
        "module": "Engineering",
        "status": "WORKING",
        "availability": "LIMITED",
        "load": 81,
        "rest": "16:40 UTC",
        "specialty": "Life Support / Mechanical Systems",
        "contact": "Priority",
        "color": "red"
    },
    "S. Smirnova": {
        "role": "Climate Scientist",
        "module": "Science",
        "status": "EXPERIMENT",
        "availability": "BUSY",
        "load": 63,
        "rest": "18:10 UTC",
        "specialty": "Atmospheric Monitoring",
        "contact": "Scheduled",
        "color": "yellow"
    },
    "D. Kim": {
        "role": "Life Support Specialist",
        "module": "Life Support",
        "status": "REST",
        "availability": "PROTECTED",
        "load": 42,
        "rest": "15:20 UTC",
        "specialty": "Life Support / Environmental Control",
        "contact": "Async only",
        "color": "green"
    },
    "M. Orlova": {
        "role": "Flight Specialist",
        "module": "Habitat",
        "status": "AVAILABLE",
        "availability": "AVAILABLE",
        "load": 51,
        "rest": "21:30 UTC",
        "specialty": "Flight Operations / Navigation",
        "contact": "Direct",
        "color": "green"
    },
    "R. Chen": {
        "role": "Data Systems Engineer",
        "module": "Science",
        "status": "WORKING",
        "availability": "AVAILABLE",
        "load": 58,
        "rest": "19:00 UTC",
        "specialty": "Telemetry / Data Processing",
        "contact": "Direct",
        "color": "green"
    },
    "E. Volkov": {
        "role": "Biomedical Specialist",
        "module": "Habitat",
        "status": "AVAILABLE",
        "availability": "AVAILABLE",
        "load": 47,
        "rest": "20:40 UTC",
        "specialty": "Crew Health / Biomedical Systems",
        "contact": "Direct",
        "color": "green"
    },
    "L. Adams": {
        "role": "Climate Systems Engineer",
        "module": "Science",
        "status": "WORKING",
        "availability": "AVAILABLE",
        "load": 67,
        "rest": "17:50 UTC",
        "specialty": "Sensor Architecture",
        "contact": "Scheduled",
        "color": "yellow"
    },
    "N. Petrova": {
        "role": "Communications Specialist",
        "module": "Command",
        "status": "AVAILABLE",
        "availability": "AVAILABLE",
        "load": 39,
        "rest": "22:00 UTC",
        "specialty": "Communications / Earth Link",
        "contact": "Direct",
        "color": "green"
    }
}


# ============================================================
# HELPERS
# ============================================================

def add_log(actor, action, log_type="SYSTEM"):
    now = datetime.utcnow().strftime("%H:%M")
    st.session_state.decision_log.insert(
        0,
        {
            "time": now,
            "actor": actor,
            "action": action,
            "type": log_type
        }
    )


def notify(message):
    st.session_state.notifications.insert(0, message)


def status_color(status):
    if status in ["REST", "AVAILABLE"]:
        return "#48e0a0"
    if status in ["WORKING", "EXPERIMENT"]:
        return "#55b7ff"
    if status in ["LIMITED", "BUSY"]:
        return "#f3c95d"
    return "#ff6674"


def load_color(load):
    if load >= 75:
        return "#ff6674"
    if load >= 60:
        return "#f3c95d"
    return "#48e0a0"


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: Inter, sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 80% 0%,
            rgba(48, 113, 177, 0.12),
            transparent 30%
        ),
        radial-gradient(
            circle at 15% 80%,
            rgba(83, 59, 150, 0.08),
            transparent 30%
        ),
        #05080d;
    color: #e7eef7;
}

.block-container {
    max-width: 1550px;
    padding-top: 2rem;
    padding-bottom: 5rem;
}

section[data-testid="stSidebar"] {
    background: #070b11;
    border-right: 1px solid rgba(255,255,255,.06);
}

section[data-testid="stSidebar"] > div {
    padding-top: 1.4rem;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* ---------- TEXT ---------- */

.brand {
    font-family: "Space Grotesk";
    font-size: 26px;
    font-weight: 700;
    letter-spacing: 5px;
    color: #e9f4ff;
}

.brand span {
    color: #5be4ff;
}

.eyebrow {
    font-size: 9px;
    letter-spacing: 2.4px;
    color: #55dfff;
    text-transform: uppercase;
    margin-bottom: 5px;
}

.title {
    font-family: "Space Grotesk";
    font-size: 34px;
    font-weight: 600;
    letter-spacing: -.8px;
}

.subtitle {
    color: #637187;
    font-size: 11px;
    margin-top: 4px;
}

.section-title {
    font-family: "Space Grotesk";
    font-size: 14px;
    font-weight: 600;
}

.muted {
    color: #59687d;
}

/* ---------- BUTTONS ---------- */

.stButton > button {
    background: rgba(255,255,255,.025);
    color: #aab7c8;
    border: 1px solid rgba(255,255,255,.075);
    border-radius: 7px;
    min-height: 38px;
    font-size: 10px;
    transition: .18s ease;
}

.stButton > button:hover {
    color: #ffffff;
    border-color: rgba(85,223,255,.4);
    background: rgba(85,223,255,.055);
}

.stButton > button[kind="primary"] {
    background: rgba(85,223,255,.08);
    border-color: rgba(85,223,255,.35);
    color: #72e8ff;
}

/* ---------- SIDEBAR ---------- */

.side-label {
    color: #4f6074;
    font-size: 8px;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    margin-top: 25px;
    margin-bottom: 7px;
}

.side-divider {
    height: 1px;
    background: rgba(255,255,255,.06);
    margin: 18px 0;
}

.side-status {
    padding: 12px;
    border-radius: 8px;
    background: rgba(255,255,255,.02);
    border: 1px solid rgba(255,255,255,.055);
}

.side-status-title {
    color: #596a80;
    font-size: 8px;
    letter-spacing: 1.4px;
}

.side-status-value {
    font-family: "Space Grotesk";
    font-size: 14px;
    margin-top: 7px;
}

/* ---------- CARDS ---------- */

.card {
    background:
        linear-gradient(
            145deg,
            rgba(14,22,32,.96),
            rgba(7,12,18,.96)
        );
    border: 1px solid rgba(255,255,255,.065);
    border-radius: 10px;
    padding: 16px;
}

.card-label {
    color: #58697f;
    font-size: 8px;
    letter-spacing: 1.7px;
    text-transform: uppercase;
}

.card-value {
    font-family: "Space Grotesk";
    font-size: 23px;
    margin-top: 8px;
}

.card-sub {
    color: #5f6e82;
    font-size: 8px;
    margin-top: 6px;
}

/* ---------- PANEL ---------- */

.panel {
    background:
        linear-gradient(
            145deg,
            rgba(12,19,29,.97),
            rgba(7,12,18,.97)
        );
    border: 1px solid rgba(255,255,255,.065);
    border-radius: 11px;
    padding: 17px;
    margin-bottom: 13px;
}

.panel-head {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 13px;
}

.panel-meta {
    color: #46566b;
    font-size: 8px;
    letter-spacing: 1.4px;
}

/* ---------- ALERT ---------- */

.alert {
    padding: 13px;
    border: 1px solid rgba(255,255,255,.06);
    background: rgba(255,255,255,.018);
    border-radius: 8px;
    margin-bottom: 9px;
}

.alert-critical {
    border-color: rgba(255,102,116,.22);
}

.alert-warning {
    border-color: rgba(243,201,93,.20);
}

.alert-info {
    border-color: rgba(85,183,255,.20);
}

.alert-tag {
    font-size: 8px;
    letter-spacing: 1.2px;
    font-weight: 700;
}

.alert-title {
    font-size: 11px;
    font-weight: 600;
    margin-top: 6px;
}

.alert-description {
    color: #66768a;
    font-size: 9px;
    line-height: 1.55;
    margin-top: 5px;
}

/* ---------- CREW ---------- */

.crew-row {
    padding: 12px;
    background: rgba(255,255,255,.018);
    border: 1px solid rgba(255,255,255,.055);
    border-radius: 8px;
    margin-bottom: 8px;
}

.crew-name {
    font-size: 11px;
    font-weight: 600;
}

.crew-role {
    color: #637187;
    font-size: 8px;
    margin-top: 3px;
}

.crew-state {
    font-size: 8px;
    margin-top: 7px;
    letter-spacing: .8px;
}

.progress {
    height: 4px;
    background: #18212c;
    border-radius: 10px;
    margin-top: 8px;
}

.progress-fill {
    height: 4px;
    border-radius: 10px;
}

/* ---------- STATION MAP ---------- */

.station {
    position: relative;
    height: 445px;
    overflow: hidden;
    background:
        radial-gradient(
            circle at center,
            rgba(76,160,255,.08),
            transparent 32%
        );
}

.orbit1 {
    position: absolute;
    width: 260px;
    height: 260px;
    border: 1px dashed rgba(85,223,255,.14);
    border-radius: 50%;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%);
}

.orbit2 {
    position: absolute;
    width: 390px;
    height: 390px;
    border: 1px solid rgba(255,255,255,.025);
    border-radius: 50%;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%);
}

.module {
    position: absolute;
    width: 132px;
    padding: 11px;
    border-radius: 8px;
    background: rgba(9,16,25,.98);
    border: 1px solid rgba(255,255,255,.11);
    text-align: center;
}

.module-core {
    border-color: rgba(85,223,255,.4);
    width: 140px;
}

.module-label {
    color: #53647a;
    font-size: 7px;
    letter-spacing: 1.4px;
}

.module-name {
    font-family: "Space Grotesk";
    font-size: 10px;
    margin-top: 5px;
}

.module-state {
    font-size: 7px;
    margin-top: 5px;
}

.module-science {
    left: 50%;
    top: 22px;
    transform: translateX(-50%);
}

.module-engineering {
    left: 20px;
    top: 165px;
}

.module-core {
    left: 50%;
    top: 157px;
    transform: translateX(-50%);
}

.module-life {
    right: 20px;
    top: 165px;
}

.module-habitat {
    left: 50%;
    bottom: 20px;
    transform: translateX(-50%);
}

.line-h1 {
    position: absolute;
    height: 1px;
    width: 110px;
    left: 151px;
    top: 212px;
    background: rgba(85,223,255,.15);
}

.line-h2 {
    position: absolute;
    height: 1px;
    width: 110px;
    right: 151px;
    top: 212px;
    background: rgba(85,223,255,.15);
}

.line-v1 {
    position: absolute;
    width: 1px;
    height: 72px;
    left: 50%;
    top: 93px;
    background: rgba(85,223,255,.15);
}

.line-v2 {
    position: absolute;
    width: 1px;
    height: 72px;
    left: 50%;
    bottom: 93px;
    background: rgba(85,223,255,.15);
}

/* ---------- TIMELINE ---------- */

.timeline-item {
    display: flex;
    gap: 15px;
    padding: 10px 0;
    border-bottom: 1px solid rgba(255,255,255,.045);
}

.timeline-time {
    width: 55px;
    color: #55dfff;
    font-family: "Space Grotesk";
    font-size: 10px;
}

.timeline-name {
    font-size: 10px;
    font-weight: 600;
}

.timeline-desc {
    color: #596a80;
    font-size: 8px;
    margin-top: 3px;
}

/* ---------- COMMUNICATION ---------- */

.protocol {
    padding: 13px;
    border-radius: 8px;
    background: rgba(255,255,255,.018);
    border: 1px solid rgba(255,255,255,.055);
    margin-bottom: 8px;
}

.protocol-title {
    font-size: 10px;
    font-weight: 600;
}

.protocol-desc {
    color: #637187;
    font-size: 8px;
    line-height: 1.5;
    margin-top: 4px;
}

/* ---------- LOG ---------- */

.log-row {
    padding: 10px 0;
    border-bottom: 1px solid rgba(255,255,255,.045);
}

.log-time {
    color: #4b5b70;
    font-size: 8px;
}

.log-main {
    color: #b8c4d2;
    font-size: 9px;
    margin-top: 3px;
}

.log-source {
    color: #4f6075;
    font-size: 7px;
    margin-top: 3px;
}

/* ---------- FOOTER ---------- */

.footer {
    text-align: center;
    color: #334154;
    font-size: 8px;
    letter-spacing: 1.5px;
    margin-top: 30px;
    padding: 20px;
}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="brand">OR<span>BIT</span></div>',
        unsafe_allow_html=True
    )

    st.caption("OPERATIONAL RELAY & BALANCE INTERFACE")

    st.markdown('<div class="side-divider"></div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="side-label">MISSION NAVIGATION</div>',
        unsafe_allow_html=True
    )

    pages = [
        ("◈", "Command Center"),
        ("◉", "Crew Control"),
        ("⌁", "Communication"),
        ("◷", "Mission Schedule"),
        ("⇄", "Mediation"),
        ("⊕", "Earth Link"),
        ("≡", "Decision Log")
    ]

    for icon, page_name in pages:

        if st.button(
            f"{icon}  {page_name}",
            key=f"nav_{page_name}",
            use_container_width=True
        ):
            st.session_state.page = page_name
            st.rerun()

    st.markdown('<div class="side-divider"></div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="side-label">MISSION PROTOCOLS</div>',
        unsafe_allow_html=True
    )

    quiet_text = (
        "● ACTIVE"
        if st.session_state.quiet_orbit
        else "○ PAUSED"
    )

    earth_text = (
        "● LINKED"
        if st.session_state.earth_link
        else "○ OFFLINE"
    )

    st.markdown(
        f"""
        <div class="side-status">
            <div class="side-status-title">QUIET ORBIT</div>
            <div class="side-status-value"
                 style="color:#48e0a0">
                {quiet_text}
            </div>
            <div class="card-sub">
                Protected crew rest
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown(
        f"""
        <div class="side-status">
            <div class="side-status-title">EARTH LINK</div>
            <div class="side-status-value"
                 style="color:#55dfff">
                {earth_text}
            </div>
            <div class="card-sub">
                Mission Control · {EARTH_LATENCY}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="side-divider"></div>', unsafe_allow_html=True)

    if st.button(
        "⚠  OPEN P0 EMERGENCY",
        type="primary",
        use_container_width=True
    ):
        st.session_state.emergency_mode = True
        st.session_state.page = "Command Center"
        st.rerun()


# ============================================================
# TOP BAR
# ============================================================

top1, top2, top3, top4 = st.columns([3, 1, 1, 1])

with top1:
    st.markdown(
        '<div class="eyebrow">MISSION 07 · CLIMATE MONITORING EXPEDITION</div>',
        unsafe_allow_html=True
    )

with top2:
    st.markdown(
        f"""
        <div class="card" style="padding:9px">
            <div class="card-label">ORBIT</div>
            <div style="font-size:10px;margin-top:3px">
                {STATION_ALTITUDE}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with top3:
    st.markdown(
        f"""
        <div class="card" style="padding:9px">
            <div class="card-label">EARTH LINK</div>
            <div style="font-size:10px;color:#48e0a0;margin-top:3px">
                ● {EARTH_LATENCY}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with top4:
    st.markdown(
        f"""
        <div class="card" style="padding:9px">
            <div class="card-label">MISSION TIME</div>
            <div style="font-size:10px;margin-top:3px">
                {MISSION_TIME}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# COMMAND CENTER
# ============================================================

if st.session_state.page == "Command Center":

    st.markdown(
        '<div class="title">Command Center</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Commander overview · mission state · crew coordination · active decisions'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    # --------------------------------------------------------
    # SYSTEM STATUS
    # --------------------------------------------------------

    s1, s2, s3, s4, s5 = st.columns(5)

    status_cards = [
        ("STATION", "NOMINAL", "All systems within parameters", "#48e0a0"),
        ("CREW", "08 / 08", "All crew accounted for", "#55dfff"),
        ("EARTH", "LINKED", "Secure ground connection", "#48e0a0"),
        ("QUIET ORBIT", "ACTIVE", "Rest protection enabled", "#48e0a0"),
        ("ATTENTION", "03", "Commander actions pending", "#f3c95d")
    ]

    for column, (label, value, sub, color) in zip(
        [s1, s2, s3, s4, s5],
        status_cards
    ):

        with column:
            st.markdown(
                f"""
                <div class="card">
                    <div class="card-label">{label}</div>
                    <div class="card-value"
                         style="color:{color}">
                        {value}
                    </div>
                    <div class="card-sub">{sub}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.write("")

    # --------------------------------------------------------
    # MAIN COMMAND GRID
    # --------------------------------------------------------

    station_col, attention_col = st.columns([1.45, 1])

    with station_col:

        st.markdown(
            """
            <div class="panel">
                <div class="panel-head">
                    <div class="section-title">
                        Station Architecture
                    </div>
                    <div class="panel-meta">
                        INTERNAL NETWORK · LIVE
                    </div>
                </div>

                <div class="station">

                    <div class="orbit1"></div>
                    <div class="orbit2"></div>

                    <div class="line-h1"></div>
                    <div class="line-h2"></div>
                    <div class="line-v1"></div>
                    <div class="line-v2"></div>

                    <div class="module module-science">
                        <div class="module-label">SCIENCE MODULE</div>
                        <div class="module-name">CLIMATE LAB</div>
                        <div class="module-state"
                             style="color:#55b7ff">
                            ● EXPERIMENT
                        </div>
                    </div>

                    <div class="module module-engineering">
                        <div class="module-label">ENGINEERING</div>
                        <div class="module-name">SYSTEMS BAY</div>
                        <div class="module-state"
                             style="color:#f3c95d">
                            ● MAINTENANCE
                        </div>
                    </div>

                    <div class="module module-core">
                        <div class="module-label">CENTRAL COMMAND</div>
                        <div class="module-name">ORBIT CORE</div>
                        <div class="module-state"
                             style="color:#48e0a0">
                            ● NOMINAL
                        </div>
                    </div>

                    <div class="module module-life">
                        <div class="module-label">LIFE SUPPORT</div>
                        <div class="module-name">ECLSS</div>
                        <div class="module-state"
                             style="color:#48e0a0">
                            ● STABLE
                        </div>
                    </div>

                    <div class="module module-habitat">
                        <div class="module-label">HABITAT</div>
                        <div class="module-name">CREW QUARTERS</div>
                        <div class="module-state"
                             style="color:#48e0a0">
                            ● PROTECTED
                        </div>
                    </div>

                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with attention_col:

        st.markdown(
            """
            <div class="panel">
                <div class="panel-head">
                    <div class="section-title">
                        Commander Attention
                    </div>
                    <div class="panel-meta">
                        03 ACTIVE
                    </div>
                </div>
            """,
            unsafe_allow_html=True
        )

        # Alert 1
        st.markdown(
            """
            <div class="alert alert-critical">
                <div class="alert-tag"
                     style="color:#ff6674">
                    P1 · CRITICAL
                </div>
                <div class="alert-title">
                    Life Support Valve Inspection
                </div>
                <div class="alert-description">
                    Engineering requires access to ECLSS before
                    the next maintenance threshold.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "REVIEW P1 TASK",
            key="review_p1",
            use_container_width=True
        ):
            st.session_state.selected_crew = "A. Ivanov"
            st.info(
                "A. Ivanov is assigned. Cognitive load: 81%. "
                "Consider delegation to another qualified specialist."
            )

        st.markdown(
            """
            <div class="alert alert-warning">
                <div class="alert-tag"
                     style="color:#f3c95d">
                    MEDIATION
                </div>
                <div class="alert-title">
                    Experiment / Maintenance Conflict
                </div>
                <div class="alert-description">
                    Science experiment overlaps with engineering
                    maintenance window.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "OPEN MEDIATION",
            key="open_med",
            use_container_width=True
        ):
            st.session_state.page = "Mediation"
            st.rerun()

        st.markdown(
            """
            <div class="alert alert-info">
                <div class="alert-tag"
                     style="color:#55b7ff">
                    EARTH REQUEST
                </div>
                <div class="alert-title">
                    Sensor Data Review
                </div>
                <div class="alert-description">
                    Ground Climate Center requested additional
                    atmospheric telemetry.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "OPEN EARTH LINK",
            key="open_earth",
            use_container_width=True
        ):
            st.session_state.page = "Earth Link"
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    # --------------------------------------------------------
    # CREW + TIMELINE
    # --------------------------------------------------------

    crew_col, timeline_col = st.columns([1.1, 1])

    with crew_col:

        st.markdown(
            """
            <div class="panel">
                <div class="panel-head">
                    <div class="section-title">
                        Crew Situation
                    </div>
                    <div class="panel-meta">
                        REAL-TIME
                    </div>
                </div>
            """,
            unsafe_allow_html=True
        )

        for name, person in list(crew.items())[:4]:

            color = load_color(person["load"])

            st.markdown(
                f"""
                <div class="crew-row">

                    <div style="
                        display:flex;
                        justify-content:space-between;
                    ">
                        <div>
                            <div class="crew-name">
                                {name}
                            </div>

                            <div class="crew-role">
                                {person["role"]} · {person["module"]}
                            </div>
                        </div>

                        <div style="
                            color:{status_color(person["status"])};
                            font-size:8px;
                        ">
                            ● {person["status"]}
                        </div>
                    </div>

                    <div class="progress">
                        <div class="progress-fill"
                             style="
                                width:{person["load"]}%;
                                background:{color};
                             ">
                        </div>
                    </div>

                    <div class="crew-role">
                        Workload {person["load"]}% ·
                        Contact: {person["contact"]}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                f"OPEN {name.upper()}",
                key=f"command_crew_{name}",
                use_container_width=True
            ):
                st.session_state.selected_crew = name
                st.session_state.page = "Crew Control"
                st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    with timeline_col:

        st.markdown(
            """
            <div class="panel">
                <div class="panel-head">
                    <div class="section-title">
                        Mission Timeline
                    </div>
                    <div class="panel-meta">
                        NEXT 08 HOURS
                    </div>
                </div>
            """,
            unsafe_allow_html=True
        )

        timeline = [
            ("14:45", "ECLSS inspection", "Engineering"),
            ("15:20", "Climate sensor cycle", "Science"),
            ("16:00", "Ground telemetry upload", "Communications"),
            ("18:00", "Crew briefing", "Command"),
            ("19:30", "Maintenance review", "Engineering"),
            ("21:00", "Quiet Orbit begins", "All crew"),
        ]

        for tm, name, who in timeline:

            st.markdown(
                f"""
                <div class="timeline-item">
                    <div class="timeline-time">{tm}</div>
                    <div>
                        <div class="timeline-name">
                            {name}
                        </div>
                        <div class="timeline-desc">
                            {who}
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# CREW CONTROL
# ============================================================

elif st.session_state.page == "Crew Control":

    st.markdown(
        '<div class="eyebrow">CREW OPERATIONS</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="title">Crew Control</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Workload · availability · protected rest · communication access'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    # selected profile
    if st.session_state.selected_crew:

        name = st.session_state.selected_crew
        person = crew[name]

        st.markdown(
            f"""
            <div class="panel">

                <div class="eyebrow">
                    CREW PROFILE
                </div>

                <div class="title">
                    {name}
                </div>

                <div class="subtitle">
                    {person["role"]} · {person["module"]}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        p1, p2, p3, p4 = st.columns(4)

        with p1:
            st.metric("STATUS", person["status"])

        with p2:
            st.metric("LOAD", f'{person["load"]}%')

        with p3:
            st.metric("AVAILABILITY", person["availability"])

        with p4:
            st.metric("NEXT REST", person["rest"])

        st.write("")

        left, right = st.columns(2)

        with left:

            st.markdown(
                """
                <div class="panel">
                    <div class="section-title">
                        Communication Decision
                    </div>
                    <div class="card-sub">
                        ORBIT checks crew state before permitting contact.
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            if person["availability"] == "PROTECTED":

                st.warning(
                    "QUIET ORBIT: direct non-critical contact is blocked."
                )

                if st.button(
                    "SEND ASYNC MESSAGE",
                    key="profile_async",
                    use_container_width=True
                ):
                    add_log(
                        "COMMAND",
                        f"Async message sent to {name}",
                        "COMMUNICATION"
                    )
                    st.success("Message queued.")

                if st.button(
                    "REQUEST OVERRIDE",
                    key="profile_override",
                    use_container_width=True
                ):
                    st.error(
                        "Override requires P0 emergency justification."
                    )

            elif person["load"] >= 75:

                st.warning(
                    f"{name} is operating at {person['load']}% workload."
                )

                if st.button(
                    "SCHEDULE CONTACT",
                    key="profile_schedule",
                    use_container_width=True
                ):
                    add_log(
                        "COMMAND",
                        f"Scheduled contact with {name}",
                        "COMMUNICATION"
                    )
                    st.success("Contact window created.")

            else:

                if st.button(
                    "START DIRECT CALL",
                    key="profile_direct",
                    use_container_width=True
                ):
                    add_log(
                        "COMMAND",
                        f"Direct call initiated with {name}",
                        "COMMUNICATION"
                    )
                    st.success("Secure internal channel active.")

        with right:

            st.markdown(
                """
                <div class="panel">
                    <div class="section-title">
                        Operational Profile
                    </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="protocol">
                    <div class="protocol-title">
                        PRIMARY SPECIALTY
                    </div>
                    <div class="protocol-desc">
                        {person["specialty"]}
                    </div>
                </div>

                <div class="protocol">
                    <div class="protocol-title">
                        MODULE
                    </div>
                    <div class="protocol-desc">
                        {person["module"]}
                    </div>
                </div>

                <div class="protocol">
                    <div class="protocol-title">
                        CONTACT POLICY
                    </div>
                    <div class="protocol-desc">
                        {person["contact"]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                "CLOSE PROFILE",
                key="close_profile",
                use_container_width=True
            ):
                st.session_state.selected_crew = None
                st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)

    # full crew
    st.write("")

    for name, person in crew.items():

        c1, c2, c3 = st.columns([2.3, 1.2, 1])

        with c1:

            st.markdown(
                f"""
                <div class="crew-row">
                    <div class="crew-name">{name}</div>
                    <div class="crew-role">
                        {person["role"]} · {person["module"]}
                    </div>
                    <div class="crew-state"
                         style="color:{status_color(person["status"])}">
                        ● {person["status"]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with c2:

            st.markdown(
                f"""
                <div class="crew-row">
                    <div class="card-label">
                        COGNITIVE LOAD
                    </div>
                    <div style="
                        margin-top:8px;
                        font-family:'Space Grotesk';
                        font-size:15px;
                    ">
                        {person["load"]}%
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with c3:

            if st.button(
                "MANAGE",
                key=f"manage_{name}",
                use_container_width=True
            ):
                st.session_state.selected_crew = name
                st.rerun()


# ============================================================
# COMMUNICATION
# ============================================================

elif st.session_state.page == "Communication":

    st.markdown(
        '<div class="eyebrow">COMMUNICATION CONTROL</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="title">Communication Protocol</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'ORBIT determines how and when distributed crew members should be contacted.'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown(
        """
        <div class="panel">
            <div class="section-title">
                Communication hierarchy
            </div>
            <div class="card-sub">
                The commander is not required to be the only communication node.
                ORBIT routes requests to the appropriate crew member or ground team.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    protocols = [
        (
            "P3 · ASYNC",
            "Non-urgent information",
            "Message is delivered without interrupting current work or rest."
        ),
        (
            "P2 · SCHEDULED",
            "Important but not time-critical",
            "ORBIT finds the next appropriate communication window."
        ),
        (
            "P1 · PRIORITY",
            "Operationally important",
            "Crew member is contacted as soon as workload permits."
        ),
        (
            "P0 · EMERGENCY",
            "Immediate threat to life or station",
            "Protected rest may be overridden and Earth escalation begins."
        )
    ]

    cols = st.columns(4)

    for col, (name, title, description) in zip(cols, protocols):

        with col:

            st.markdown(
                f"""
                <div class="protocol"
                     style="min-height:155px">

                    <div class="card-label">
                        {name}
                    </div>

                    <div class="protocol-title"
                         style="margin-top:10px">
                        {title}
                    </div>

                    <div class="protocol-desc"
                         style="margin-top:9px">
                        {description}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    st.write("")

    # communication simulator
    st.markdown(
        """
        <div class="panel">
            <div class="section-title">
                Contact Request
            </div>
            <div class="card-sub">
                Simulate a communication decision.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    person_name = st.selectbox(
        "Crew member",
        list(crew.keys())
    )

    priority = st.selectbox(
        "Priority",
        ["P3 · ASYNC", "P2 · SCHEDULED", "P1 · PRIORITY", "P0 · EMERGENCY"]
    )

    reason = st.text_input(
        "Reason",
        placeholder="e.g. Request climate sensor review"
    )

    if st.button(
        "RUN COMMUNICATION CHECK",
        type="primary",
        use_container_width=True
    ):

        person = crew[person_name]

        if person["availability"] == "PROTECTED" and priority != "P0 · EMERGENCY":

            st.error(
                f"""
                CONTACT BLOCKED

                {person_name} is currently in protected rest.

                Recommended action: send an asynchronous message
                or schedule contact after {person['rest']}.
                """
            )

            add_log(
                "ORBIT",
                f"Blocked non-critical contact with {person_name}",
                "PROTOCOL"
            )

        elif person["load"] >= 75 and priority == "P1 · PRIORITY":

            st.warning(
                f"""
                CONTACT DELAYED

                {person_name} has a cognitive workload of
                {person['load']}%.

                ORBIT recommends delegation or scheduled contact.
                """
            )

            add_log(
                "ORBIT",
                f"Flagged high-load contact with {person_name}",
                "PROTOCOL"
            )

        elif priority == "P0 · EMERGENCY":

            st.error(
                "P0 OVERRIDE — protected rest is suspended."
            )

            add_log(
                "COMMAND",
                f"P0 emergency contact initiated with {person_name}",
                "EMERGENCY"
            )

            notify(
                f"P0 channel opened for {person_name}"
            )

        else:

            st.success(
                f"""
                CONTACT APPROVED

                {person_name} may be contacted under {priority}.
                """
            )

            add_log(
                "COMMAND",
                f"Communication approved for {person_name}",
                "COMMUNICATION"
            )


# ============================================================
# SCHEDULE
# ============================================================

elif st.session_state.page == "Mission Schedule":

    st.markdown(
        '<div class="eyebrow">CREW RHYTHM MANAGEMENT</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="title">Mission Schedule</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'The schedule protects both mission performance and human recovery.'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    schedule = [
        ("14:45", "ECLSS inspection", "Engineering", "WORK", "P1"),
        ("15:20", "Climate sensor cycle", "Science", "WORK", "P2"),
        ("16:00", "Ground telemetry upload", "Communications", "WORK", "P2"),
        ("17:15", "Protected meal window", "All crew", "REST", "P3"),
        ("18:00", "Crew briefing", "All crew", "COMMAND", "P2"),
        ("19:30", "Maintenance review", "Engineering", "WORK", "P2"),
        ("21:00", "Quiet Orbit begins", "All crew", "PROTECTED", "P3"),
        ("06:30", "Wake cycle", "All crew", "ROUTINE", "P3")
    ]

    for tm, event, owner, category, priority in schedule:

        c1, c2, c3, c4 = st.columns([.8, 3, 1.5, .8])

        with c1:
            st.markdown(
                f"""
                <div class="card">
                    <div style="
                        font-family:'Space Grotesk';
                        color:#55dfff;
                        font-size:13px;
                    ">
                        {tm}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with c2:
            st.markdown(
                f"""
                <div class="card">
                    <div style="
                        font-size:10px;
                        font-weight:600;
                    ">
                        {event}
                    </div>
                    <div class="card-sub">
                        {owner} · {category}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with c3:
            st.markdown(
                f"""
                <div class="card">
                    <div class="card-label">PROTOCOL</div>
                    <div style="font-size:10px;margin-top:6px">
                        {priority}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with c4:

            if category == "PROTECTED":
                st.markdown(
                    """
                    <div class="card">
                        <div style="
                            color:#48e0a0;
                            font-size:9px;
                            margin-top:7px;
                        ">
                            🔒 LOCKED
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:

                if st.button(
                    "EDIT",
                    key=f"edit_{tm}_{event}",
                    use_container_width=True
                ):
                    st.info(
                        f"Schedule event selected: {event}"
                    )

    st.write("")

    st.markdown(
        """
        <div class="panel">
            <div class="section-title">
                Quiet Orbit Rule
            </div>
            <div class="card-sub">
                Non-critical communication requests cannot
                automatically interrupt protected rest.
                P0 emergency protocol is the only exception.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# MEDIATION
# ============================================================

elif st.session_state.page == "Mediation":

    st.markdown(
        '<div class="eyebrow">CONFLICT RESOLUTION ENGINE</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="title">Mediation Protocol</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Resolve operational conflicts without relying exclusively on command authority.'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown(
        """
        <div class="alert alert-warning">

            <div class="alert-tag"
                 style="color:#f3c95d">
                ACTIVE CONFLICT
            </div>

            <div class="alert-title">
                Climate Experiment vs. ECLSS Maintenance
            </div>

            <div class="alert-description">
                Engineering requires temporary access to a subsystem
                currently used by the Science team.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    left, right = st.columns(2)

    with left:

        st.markdown(
            """
            <div class="panel">

                <div class="section-title">
                    Science Position
                </div>

                <div class="protocol">
                    <div class="protocol-title">
                        OBJECTIVE
                    </div>
                    <div class="protocol-desc">
                        Preserve continuous climate sensor data.
                    </div>
                </div>

                <div class="protocol">
                    <div class="protocol-title">
                        RISK
                    </div>
                    <div class="protocol-desc">
                        Interrupting the experiment may invalidate
                        the current measurement cycle.
                    </div>
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with right:

        st.markdown(
            """
            <div class="panel">

                <div class="section-title">
                    Engineering Position
                </div>

                <div class="protocol">
                    <div class="protocol-title">
                        OBJECTIVE
                    </div>
                    <div class="protocol-desc">
                        Inspect the ECLSS valve before threshold breach.
                    </div>
                </div>

                <div class="protocol">
                    <div class="protocol-title">
                        RISK
                    </div>
                    <div class="protocol-desc">
                        Delaying maintenance increases system risk.
                    </div>
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="panel">
            <div class="section-title">
                ORBIT Resolution Matrix
            </div>
            <div class="card-sub">
                Select the action that best balances mission continuity,
                system safety and crew workload.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    decision = st.radio(
        "Commander decision",
        [
            "A · Delay maintenance",
            "B · Pause experiment",
            "C · Modify maintenance procedure",
            "D · Escalate to Earth",
            "E · Commander override"
        ]
    )

    justification = st.text_area(
        "Decision rationale",
        placeholder="Briefly explain why this option was selected."
    )

    if st.button(
        "RECORD MEDIATION DECISION",
        type="primary",
        use_container_width=True
    ):

        if not justification.strip():
            st.error(
                "Decision rationale is required."
            )
        else:

            add_log(
                "COMMAND",
                f"Mediation resolved: {decision}",
                "MEDIATION"
            )

            notify(
                f"Mediation decision recorded: {decision}"
            )

            st.success(
                "Decision recorded in the mission log."
            )


# ============================================================
# EARTH LINK
# ============================================================

elif st.session_state.page == "Earth Link":

    st.markdown(
        '<div class="eyebrow">GROUND NETWORK</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="title">Earth Link</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Distributed communication with Earth without making the commander a single point of failure.'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    e1, e2, e3, e4 = st.columns(4)

    earth_channels = [
        (
            "MISSION CONTROL",
            "COMMAND",
            "Mission decisions / escalation"
        ),
        (
            "CLIMATE CENTER",
            "SCIENCE",
            "Atmospheric data / research"
        ),
        (
            "GROUND ENGINEERING",
            "ENGINEERING",
            "Technical diagnostics"
        ),
        (
            "MEDICAL CONTROL",
            "MEDICAL",
            "Crew health / emergency support"
        )
    ]

    for col, (name, category, description) in zip(
        [e1, e2, e3, e4],
        earth_channels
    ):

        with col:

            st.markdown(
                f"""
                <div class="panel"
                     style="min-height:160px">

                    <div class="card-label">
                        {category}
                    </div>

                    <div style="
                        font-size:11px;
                        font-weight:600;
                        margin-top:8px;
                    ">
                        {name}
                    </div>

                    <div class="card-sub"
                         style="line-height:1.5">
                        {description}
                    </div>

                    <div style="
                        color:#48e0a0;
                        font-size:8px;
                        margin-top:14px;
                    ">
                        ● SECURE CHANNEL
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                "CONNECT",
                key=f"connect_{category}",
                use_container_width=True
            ):

                add_log(
                    "COMMAND",
                    f"Connected to Earth: {name}",
                    "EARTH LINK"
                )

                st.success(
                    f"{name} channel active."
                )

    st.write("")

    st.markdown(
        """
        <div class="panel">
            <div class="section-title">
                Earth Communication Request
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    sender = st.selectbox(
        "Request initiated by",
        list(crew.keys())
    )

    destination = st.selectbox(
        "Earth destination",
        [
            "Mission Control",
            "Climate Research Center",
            "Ground Engineering",
            "Medical Control"
        ]
    )

    earth_reason = st.text_input(
        "Purpose"
    )

    if st.button(
        "SEND EARTH REQUEST",
        type="primary",
        use_container_width=True
    ):

        if earth_reason.strip():

            add_log(
                sender,
                f"Earth request sent to {destination}: {earth_reason}",
                "EARTH LINK"
            )

            st.success(
                f"Request routed directly to {destination}."
            )

        else:

            st.error(
                "Purpose is required."
            )


# ============================================================
# DECISION LOG
# ============================================================

elif st.session_state.page == "Decision Log":

    st.markdown(
        '<div class="eyebrow">MISSION MEMORY</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="title">Decision Log</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Every important operational decision remains traceable.'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    if st.session_state.notifications:

        st.markdown(
            """
            <div class="panel">
                <div class="section-title">
                    Recent System Events
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        for notification in st.session_state.notifications[:5]:

            st.info(notification)

    for item in st.session_state.decision_log:

        st.markdown(
            f"""
            <div class="log-row">

                <div class="log-time">
                    {item["time"]} · {item["type"]}
                </div>

                <div class="log-main">
                    {item["action"]}
                </div>

                <div class="log-source">
                    SOURCE · {item["actor"]}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    if st.button(
        "CLEAR SESSION EVENTS",
        use_container_width=True
    ):
        st.session_state.notifications = []
        st.success("Session notifications cleared.")


# ============================================================
# EMERGENCY OVERLAY
# ============================================================

if st.session_state.emergency_mode:

    st.divider()

    st.markdown(
        '<div class="eyebrow" style="color:#ff6674">'
        'P0 · EMERGENCY PROTOCOL'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="title" style="color:#ff6674">'
        'Emergency Command'
        '</div>',
        unsafe_allow_html=True
    )

    st.error(
        """
        P0 PROTOCOL OVERRIDES NORMAL COMMUNICATION PRIORITIES.

        Protected rest may be interrupted only when there is
        an immediate threat to life, station integrity or mission survival.
        """
    )

    emergency_reason = st.selectbox(
        "Emergency classification",
        [
            "Life Support Failure",
            "Fire / Atmospheric Threat",
            "Station Structural Risk",
            "Medical Emergency",
            "Loss of Earth Communication",
            "Other P0 Threat"
        ]
    )

    required = st.multiselect(
        "Required crew",
        list(crew.keys()),
        default=["A. Ivanov", "D. Kim"]
    )

    earth_escalation = st.checkbox(
        "Automatically notify Earth Mission Control"
    )

    confirm = st.checkbox(
        "I confirm that this situation meets P0 emergency criteria."
    )

    if st.button(
        "ACTIVATE P0",
        type="primary",
        use_container_width=True
    ):

        if not confirm:

            st.error(
                "Commander confirmation required."
            )

        elif not required:

            st.error(
                "Select at least one required crew member."
            )

        else:

            st.session_state.emergency_mode = False

            add_log(
                "COMMAND",
                f"P0 activated: {emergency_reason}",
                "EMERGENCY"
            )

            for person in required:

                add_log(
                    "ORBIT",
                    f"P0 notification sent to {person}",
                    "EMERGENCY"
                )

            if earth_escalation:

                add_log(
                    "ORBIT",
                    "Earth Mission Control notified",
                    "EARTH LINK"
                )

            st.error(
                "P0 PROTOCOL ACTIVE — required personnel notified."
            )

            st.balloons()

    if st.button(
        "CANCEL P0",
        use_container_width=True
    ):

        st.session_state.emergency_mode = False
        st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        ORBIT · OPERATIONAL RELAY & BALANCE INTERFACE FOR TEAMWORK
        · MISSION 07 · CLIMATE MONITORING
    </div>
    """,
    unsafe_allow_html=True
)
