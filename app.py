import streamlit as st
from datetime import datetime

# ============================================================
# ORBIT — CREW OPERATIONS SYSTEM
# ============================================================

st.set_page_config(
    page_title="ORBIT — Crew Operations",
    page_icon="◉",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Command Center"

if "toast" not in st.session_state:
    st.session_state.toast = ""

if "selected_crew" not in st.session_state:
    st.session_state.selected_crew = None

if "mediation_open" not in st.session_state:
    st.session_state.mediation_open = False

if "earth_open" not in st.session_state:
    st.session_state.earth_open = False

if "emergency_open" not in st.session_state:
    st.session_state.emergency_open = False

if "quiet_orbit" not in st.session_state:
    st.session_state.quiet_orbit = True


# ============================================================
# DATA
# ============================================================

crew = [
    {
        "name": "A. Ivanov",
        "role": "Systems Engineer",
        "module": "ENGINEERING",
        "status": "WORKING",
        "load": 81,
    },
    {
        "name": "S. Smirnova",
        "role": "Climate Scientist",
        "module": "SCIENCE",
        "status": "EXPERIMENT",
        "load": 63,
    },
    {
        "name": "D. Kim",
        "role": "Life Support",
        "module": "LIFE SUPPORT",
        "status": "MAINTENANCE",
        "load": 42,
    },
    {
        "name": "M. Orlova",
        "role": "Flight Specialist",
        "module": "HABITAT",
        "status": "AVAILABLE",
        "load": 51,
    },
]


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 80% 0%, rgba(43,95,150,0.18), transparent 30%),
        radial-gradient(circle at 10% 80%, rgba(73,55,145,0.10), transparent 28%),
        #05080d;
    color: #e9f0f8;
}

.block-container {
    max-width: 1500px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: #070b11;
    border-right: 1px solid rgba(255,255,255,0.07);
}

section[data-testid="stSidebar"] > div {
    padding-top: 1.5rem;
}

.logo {
    font-family: 'Space Grotesk';
    font-size: 25px;
    font-weight: 700;
    letter-spacing: 5px;
    padding: 10px 5px 28px 5px;
}

.logo span {
    color: #55e6ff;
}

.mission-label {
    color: #55e6ff;
    font-size: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.sidebar-line {
    height: 1px;
    background: rgba(255,255,255,0.07);
    margin: 20px 0;
}

/* BUTTONS */

.stButton > button {
    width: 100%;
    background: rgba(255,255,255,0.025);
    color: #8c9aae;
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 7px;
    text-align: left;
    transition: all .2s ease;
}

.stButton > button:hover {
    color: white;
    border-color: rgba(85,230,255,.35);
    background: rgba(85,230,255,.05);
}

/* HEADERS */

.eyebrow {
    color: #55e6ff;
    font-size: 10px;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    margin-bottom: 5px;
}

.page-title {
    font-family: 'Space Grotesk';
    font-size: 34px;
    font-weight: 600;
    letter-spacing: -.5px;
}

.page-subtitle {
    color: #6d7c90;
    font-size: 12px;
    margin-top: 4px;
}

/* STATUS CARDS */

.card {
    background: linear-gradient(
        145deg,
        rgba(15,23,34,.95),
        rgba(8,13,20,.95)
    );
    border: 1px solid rgba(255,255,255,.07);
    border-radius: 11px;
    padding: 18px;
    min-height: 108px;
}

.card-label {
    color: #637188;
    font-size: 9px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}

.card-value {
    font-family: 'Space Grotesk';
    font-size: 24px;
    margin-top: 9px;
}

.card-sub {
    color: #627087;
    font-size: 9px;
    margin-top: 7px;
}

.green {
    color: #4de1a1;
}

.yellow {
    color: #f4c95d;
}

.red {
    color: #ff5f6d;
}

.blue {
    color: #4da3ff;
}

/* PANELS */

.panel {
    background: linear-gradient(
        145deg,
        rgba(12,18,27,.97),
        rgba(7,12,18,.97)
    );
    border: 1px solid rgba(255,255,255,.07);
    border-radius: 11px;
    padding: 18px;
    margin-bottom: 15px;
}

.panel-title {
    font-family: 'Space Grotesk';
    font-size: 13px;
    letter-spacing: .4px;
}

.panel-meta {
    color: #536176;
    font-size: 9px;
    letter-spacing: 1px;
}

/* STATION */

.station-wrapper {
    position: relative;
    height: 390px;
    display: flex;
    justify-content: center;
    align-items: center;
    background:
        radial-gradient(
            circle at center,
            rgba(77,163,255,.09),
            transparent 33%
        );
    overflow: hidden;
}

.station-ring-1 {
    position: absolute;
    width: 260px;
    height: 260px;
    border: 1px dashed rgba(85,230,255,.15);
    border-radius: 50%;
}

.station-ring-2 {
    position: absolute;
    width: 410px;
    height: 410px;
    border: 1px solid rgba(255,255,255,.025);
    border-radius: 50%;
}

.module-box {
    position: absolute;
    width: 125px;
    padding: 12px;
    background: rgba(11,18,28,.97);
    border: 1px solid rgba(255,255,255,.12);
    border-radius: 9px;
    text-align: center;
}

.module-box.center {
    width: 135px;
    border-color: rgba(85,230,255,.35);
}

.module-top {
    color: #637188;
    font-size: 8px;
    letter-spacing: 1.3px;
}

.module-name {
    font-family: 'Space Grotesk';
    font-size: 11px;
    margin-top: 6px;
}

.module-state {
    color: #4de1a1;
    font-size: 8px;
    margin-top: 5px;
}

.science {
    top: 32px;
    left: 50%;
    transform: translateX(-50%);
}

.engineering {
    left: 30px;
    top: 160px;
}

.center {
    top: 155px;
    left: 50%;
    transform: translateX(-50%);
}

.life {
    right: 30px;
    top: 160px;
}

.habitat {
    bottom: 32px;
    left: 50%;
    transform: translateX(-50%);
}

/* CONNECTORS */

.connector-h {
    position: absolute;
    height: 1px;
    background: rgba(85,230,255,.18);
    width: 150px;
}

.connector-v {
    position: absolute;
    width: 1px;
    background: rgba(85,230,255,.18);
    height: 80px;
}

.ch1 {
    left: 155px;
    top: 193px;
}

.ch2 {
    right: 155px;
    top: 193px;
}

.cv1 {
    top: 100px;
    left: 50%;
}

.cv2 {
    bottom: 100px;
    left: 50%;
}

/* ALERTS */

.alert {
    border: 1px solid rgba(255,255,255,.07);
    border-radius: 9px;
    padding: 14px;
    margin-bottom: 10px;
    background: rgba(255,255,255,.018);
}

.alert-critical {
    border-color: rgba(255,95,109,.2);
}

.alert-warning {
    border-color: rgba(244,201,93,.18);
}

.alert-title {
    font-weight: 600;
    font-size: 12px;
    margin-top: 7px;
}

.alert-text {
    color: #6f7d90;
    font-size: 9px;
    line-height: 1.55;
    margin-top: 5px;
}

.priority {
    font-size: 8px;
    letter-spacing: 1px;
    font-weight: 700;
}

/* CREW */

.crew-card {
    background: rgba(255,255,255,.018);
    border: 1px solid rgba(255,255,255,.07);
    border-radius: 9px;
    padding: 13px;
    margin-bottom: 10px;
}

.crew-name {
    font-size: 11px;
    font-weight: 600;
}

.crew-role {
    color: #647287;
    font-size: 8px;
    margin-top: 3px;
}

.crew-status {
    font-size: 8px;
    margin-top: 8px;
}

.load-track {
    height: 4px;
    width: 100%;
    background: #19232f;
    border-radius: 10px;
    margin-top: 8px;
}

.load-fill {
    height: 4px;
    border-radius: 10px;
}

/* LOG */

.log-item {
    padding: 10px 0;
    border-bottom: 1px solid rgba(255,255,255,.04);
}

.log-text {
    font-size: 9px;
    color: #b9c4d2;
}

.log-time {
    color: #526176;
    font-size: 8px;
    margin-top: 3px;
}

/* EARTH */

.earth-card {
    border: 1px solid rgba(77,225,161,.15);
    background: rgba(77,225,161,.025);
    border-radius: 9px;
    padding: 15px;
}

/* FOOTER */

.system-footer {
    color: #3f4d60;
    font-size: 8px;
    letter-spacing: 1px;
    text-align: center;
    padding: 20px;
}

/* HIDE STREAMLIT BRANDING */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
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
        '<div class="logo">OR<span>BIT</span></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="mission-label">MISSION 07</div>',
        unsafe_allow_html=True
    )

    st.caption("CLIMATE MONITORING EXPEDITION")

    st.markdown('<div class="sidebar-line"></div>', unsafe_allow_html=True)

    if st.button("◈  Command Center", use_container_width=True):
        st.session_state.page = "Command Center"

    if st.button("◉  Crew", use_container_width=True):
        st.session_state.page = "Crew"

    if st.button("⌘  Station", use_container_width=True):
        st.session_state.page = "Station"

    if st.button("◷  Schedule", use_container_width=True):
        st.session_state.page = "Schedule"

    st.markdown(
        '<div class="sidebar-line"></div>',
        unsafe_allow_html=True
    )

    if st.button("⇄  Mediation", use_container_width=True):
        st.session_state.mediation_open = True

    if st.button("⊕  Earth Link", use_container_width=True):
        st.session_state.earth_open = True

    if st.button("◌  Quiet Orbit", use_container_width=True):
        st.session_state.quiet_orbit = not st.session_state.quiet_orbit

    st.markdown(
        '<div class="sidebar-line"></div>',
        unsafe_allow_html=True
    )

    if st.button("≡  Activity Log", use_container_width=True):
        st.session_state.page = "Activity Log"

    st.markdown("<br>", unsafe_allow_html=True)

    quiet_status = "ACTIVE" if st.session_state.quiet_orbit else "PAUSED"

    st.markdown(
        f"""
        <div class="panel">
            <div class="card-label">EARTH LINK</div>
            <div style="margin-top:7px;color:#4de1a1;font-size:11px">
                ● LIVE
            </div>
            <div class="card-sub">
                Latency 0.8 sec
            </div>
        </div>

        <div class="panel">
            <div class="card-label">QUIET ORBIT</div>
            <div style="margin-top:7px;color:#55e6ff;font-size:11px">
                ● {quiet_status}
            </div>
            <div class="card-sub">
                Protected rest protocol
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# HEADER
# ============================================================

col1, col2 = st.columns([4, 1])

with col1:

    st.markdown(
        '<div class="eyebrow">MISSION 07 · CLIMATE MONITORING</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-title">Command Center</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        'Orbital Crew Operations & Coordination System'
        '</div>',
        unsafe_allow_html=True
    )

with col2:

    if st.button("⚠ EMERGENCY", use_container_width=True):
        st.session_state.emergency_open = True


st.write("")


# ============================================================
# STATUS CARDS
# ============================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        """
        <div class="card">
            <div class="card-label">STATION</div>
            <div class="card-value green">NOMINAL</div>
            <div class="card-sub">All systems operational</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        """
        <div class="card">
            <div class="card-label">EARTH LINK</div>
            <div class="card-value green">ACTIVE</div>
            <div class="card-sub">0.8 sec communication latency</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        """
        <div class="card">
            <div class="card-label">CREW</div>
            <div class="card-value">08 / 08</div>
            <div class="card-sub">4 working · 2 rest · 2 available</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        """
        <div class="card">
            <div class="card-label">ATTENTION</div>
            <div class="card-value yellow">03</div>
            <div class="card-sub">1 critical · 1 mediation · 1 request</div>
        </div>
        """,
        unsafe_allow_html=True
    )


st.write("")


# ============================================================
# PAGE: COMMAND CENTER
# ============================================================

if st.session_state.page == "Command Center":

    left, right = st.columns([1.55, 1])

    # --------------------------------------------------------
    # STATION
    # --------------------------------------------------------

    with left:

        st.markdown(
            """
            <div class="panel">
                <div style="display:flex;justify-content:space-between">
                    <div class="panel-title">
                        Station Architecture
                    </div>
                    <div class="panel-meta">
                        ORBITAL MODULE VIEW · LIVE
                    </div>
                </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="station-wrapper">

                <div class="station-ring-1"></div>
                <div class="station-ring-2"></div>

                <div class="connector-h ch1"></div>
                <div class="connector-h ch2"></div>

                <div class="connector-v cv1"></div>
                <div class="connector-v cv2"></div>

                <div class="module-box science">
                    <div class="module-top">SCIENCE</div>
                    <div class="module-name">S. Smirnova</div>
                    <div class="module-state">● EXPERIMENT</div>
                </div>

                <div class="module-box engineering">
                    <div class="module-top">ENGINEERING</div>
                    <div class="module-name">A. Ivanov</div>
                    <div class="module-state">● WORKING</div>
                </div>

                <div class="module-box center">
                    <div class="module-top">CENTRAL HUB</div>
                    <div class="module-name">COMMAND</div>
                    <div class="module-state">● NOMINAL</div>
                </div>

                <div class="module-box life">
                    <div class="module-top">LIFE SUPPORT</div>
                    <div class="module-name">D. Kim</div>
                    <div class="module-state">● MAINTENANCE</div>
                </div>

                <div class="module-box habitat">
                    <div class="module-top">HABITAT</div>
                    <div class="module-name">M. Orlova</div>
                    <div class="module-state">● AVAILABLE</div>
                </div>

            </div>

            <div style="
                text-align:center;
                color:#3f5066;
                font-size:8px;
                letter-spacing:2px;
                padding:4px 0 2px 0;
            ">
                ORBIT CORE · INTERNAL NETWORK
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # --------------------------------------------------------
    # ATTENTION
    # --------------------------------------------------------

    with right:

        st.markdown(
            """
            <div class="panel">
                <div style="display:flex;justify-content:space-between">
                    <div class="panel-title">Attention Queue</div>
                    <div class="panel-meta">03 ACTIVE</div>
                </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="alert alert-critical">
                <div class="priority red">
                    P1 · CRITICAL
                </div>

                <div class="alert-title">
                    Life Support Valve Inspection
                </div>

                <div class="alert-text">
                    Engineering action required before system
                    maintenance window closes.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "OPEN CRITICAL TASK",
            key="critical_task",
            use_container_width=True
        ):
            st.warning(
                "P1 task opened. Assigned specialist: A. Ivanov."
            )


        st.markdown(
            """
            <div class="alert alert-warning">
                <div class="priority yellow">
                    MEDIATION
                </div>

                <div class="alert-title">
                    Experiment vs. Maintenance
                </div>

                <div class="alert-text">
                    Science and Engineering have conflicting
                    operational priorities.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "OPEN MEDIATION",
            key="mediation",
            use_container_width=True
        ):
            st.session_state.mediation_open = True


        st.markdown(
            """
            <div class="alert">
                <div class="priority blue">
                    P2 · REQUEST
                </div>

                <div class="alert-title">
                    Climate Sensor Data Review
                </div>

                <div class="alert-text">
                    Science module requested engineering support.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "ASSIGN AVAILABLE SPECIALIST",
            key="assign",
            use_container_width=True
        ):
            st.success(
                "Request assigned to M. Orlova."
            )

        st.markdown("</div>", unsafe_allow_html=True)


    # ========================================================
    # CREW
    # ========================================================

    st.write("")

    st.markdown(
        """
        <div class="panel">
            <div style="display:flex;justify-content:space-between">
                <div class="panel-title">Crew Status</div>
                <div class="panel-meta">
                    REAL-TIME AVAILABILITY
                </div>
            </div>
        """,
        unsafe_allow_html=True
    )

    crew_cols = st.columns(4)

    for i, member in enumerate(crew):

        with crew_cols[i]:

            if member["load"] >= 75:
                color = "#ff5f6d"
            elif member["load"] >= 60:
                color = "#f4c95d"
            else:
                color = "#4de1a1"

            st.markdown(
                f"""
                <div class="crew-card">

                    <div class="crew-name">
                        {member["name"]}
                    </div>

                    <div class="crew-role">
                        {member["role"]}
                    </div>

                    <div class="crew-status"
                         style="color:{color}">
                        ● {member["status"]}
                    </div>

                    <div class="load-track">
                        <div class="load-fill"
                             style="width:{member["load"]}%;
                                    background:{color}">
                        </div>
                    </div>

                    <div class="crew-role">
                        Cognitive load {member["load"]}%
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                "OPEN PROFILE",
                key=f"profile_{i}",
                use_container_width=True
            ):
                st.session_state.selected_crew = member


    st.markdown("</div>", unsafe_allow_html=True)


    # ========================================================
    # LOWER SECTION
    # ========================================================

    low1, low2 = st.columns(2)

    with low1:

        st.markdown(
            """
            <div class="panel">

                <div style="display:flex;justify-content:space-between">
                    <div class="panel-title">
                        Crew Balance
                    </div>

                    <div class="panel-meta">
                        COGNITIVE LOAD
                    </div>
                </div>
            """,
            unsafe_allow_html=True
        )

        for member in crew:

            if member["load"] >= 75:
                color = "#ff5f6d"
            elif member["load"] >= 60:
                color = "#f4c95d"
            else:
                color = "#4da3ff"

            st.markdown(
                f"""
                <div style="margin-top:14px">

                    <div style="
                        display:flex;
                        justify-content:space-between;
                        font-size:9px;
                        color:#aab5c4;
                    ">
                        <span>{member["name"]}</span>
                        <span>{member["load"]}%</span>
                    </div>

                    <div class="load-track">
                        <div class="load-fill"
                             style="
                                width:{member["load"]}%;
                                background:{color};
                             ">
                        </div>
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("</div>", unsafe_allow_html=True)


    with low2:

        st.markdown(
            """
            <div class="panel">

                <div style="display:flex;justify-content:space-between">
                    <div class="panel-title">
                        Activity Log
                    </div>

                    <div class="panel-meta">
                        LIVE
                    </div>
                </div>
            """,
            unsafe_allow_html=True
        )

        logs = [
            ("Earth Link synchronized with Climate Lab.", "14:32 · SYSTEM"),
            ("S. Smirnova requested engineering support.", "14:27 · SCIENCE"),
            ("Quiet Orbit protected D. Kim's rest period.", "14:18 · SYSTEM"),
            ("Mediation protocol initiated.", "14:11 · COMMAND"),
        ]

        for text, time in logs:

            st.markdown(
                f"""
                <div class="log-item">
                    <div class="log-text">● &nbsp; {text}</div>
                    <div class="log-time">{time}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# CREW PAGE
# ============================================================

elif st.session_state.page == "Crew":

    st.markdown(
        '<div class="eyebrow">ORBIT OPERATIONS</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-title">Crew Management</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        'Availability · workload · communication permissions'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    for member in crew:

        col1, col2, col3 = st.columns([2, 2, 1])

        with col1:
            st.markdown(
                f"""
                <div class="panel">
                    <div class="crew-name">{member["name"]}</div>
                    <div class="crew-role">{member["role"]}</div>
                    <div class="crew-status green">
                        ● {member["status"]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:

            color = (
                "#ff5f6d"
                if member["load"] >= 75
                else "#f4c95d"
                if member["load"] >= 60
                else "#4de1a1"
            )

            st.markdown(
                f"""
                <div class="panel">
                    <div class="card-label">
                        COGNITIVE LOAD
                    </div>

                    <div class="load-track"
                         style="margin-top:13px">
                        <div class="load-fill"
                             style="width:{member["load"]}%;
                                    background:{color}">
                        </div>
                    </div>

                    <div class="card-sub">
                        {member["load"]}% · monitored
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col3:

            if st.button(
                "MESSAGE",
                key=f"message_{member['name']}"
            ):
                st.info(
                    f"Message channel prepared for {member['name']}."
                )


# ============================================================
# STATION PAGE
# ============================================================

elif st.session_state.page == "Station":

    st.markdown(
        '<div class="eyebrow">ORBITAL ARCHITECTURE</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-title">Station Systems</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown(
        """
        <div class="panel">

            <div class="panel-title">
                Station Network
            </div>

            <div class="card-sub">
                Internal communication architecture
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.info(
        "All station modules are connected through the ORBIT Core."
    )


# ============================================================
# SCHEDULE PAGE
# ============================================================

elif st.session_state.page == "Schedule":

    st.markdown(
        '<div class="eyebrow">CREW RHYTHM</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-title">Mission Schedule</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        'Protected work · rest · communication windows'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    schedule = [
        ("06:30", "Crew Wake Cycle", "ALL CREW", "ROUTINE"),
        ("07:00", "Systems Inspection", "ENGINEERING", "WORK"),
        ("09:30", "Climate Experiment", "SCIENCE", "WORK"),
        ("12:00", "Shared Meal", "ALL CREW", "REST"),
        ("14:00", "Maintenance Window", "ENGINEERING", "WORK"),
        ("18:00", "Crew Briefing", "ALL CREW", "COMMAND"),
        ("21:00", "Quiet Orbit", "ALL CREW", "PROTECTED"),
    ]

    for time, task, people, kind in schedule:

        st.markdown(
            f"""
            <div class="panel"
                 style="padding:14px;margin-bottom:8px">

                <div style="
                    display:flex;
                    align-items:center;
                    gap:25px;
                ">

                    <div style="
                        font-family:'Space Grotesk';
                        font-size:13px;
                        color:#55e6ff;
                        width:55px;
                    ">
                        {time}
                    </div>

                    <div style="flex:1">

                        <div style="
                            font-size:11px;
                            font-weight:600;
                        ">
                            {task}
                        </div>

                        <div class="crew-role">
                            {people}
                        </div>

                    </div>

                    <div class="card-label">
                        {kind}
                    </div>

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# ACTIVITY PAGE
# ============================================================

elif st.session_state.page == "Activity Log":

    st.markdown(
        '<div class="eyebrow">SYSTEM MEMORY</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-title">Activity Log</div>',
        unsafe_allow_html=True
    )

    st.write("")

    events = [
        ("14:32", "Earth Link", "Ground connection synchronized."),
        ("14:27", "Science", "Climate data review requested."),
        ("14:18", "ORBIT", "Quiet Orbit protected rest period."),
        ("14:11", "Command", "Mediation protocol initiated."),
        ("13:52", "Engineering", "Life Support inspection scheduled."),
        ("13:41", "ORBIT", "Crew workload recalculated."),
    ]

    for time, source, event in events:

        st.markdown(
            f"""
            <div class="panel"
                 style="padding:14px">

                <div style="
                    display:flex;
                    gap:20px;
                    align-items:center;
                ">

                    <div style="
                        color:#55e6ff;
                        font-size:10px;
                        width:45px;
                    ">
                        {time}
                    </div>

                    <div style="flex:1">

                        <div style="
                            font-size:10px;
                            font-weight:600;
                        ">
                            {event}
                        </div>

                        <div class="crew-role">
                            SOURCE · {source}
                        </div>

                    </div>

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# CREW PROFILE MODAL-LIKE PANEL
# ============================================================

if st.session_state.selected_crew:

    member = st.session_state.selected_crew

    st.divider()

    st.markdown(
        '<div class="eyebrow">CREW PROFILE</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="page-title">{member["name"]}</div>',
        unsafe_allow_html=True
    )

    st.caption(
        f'{member["role"]} · {member["module"]}'
    )

    p1, p2, p3 = st.columns(3)

    with p1:
        st.metric("STATUS", member["status"])

    with p2:
        st.metric("LOAD", f'{member["load"]}%')

    with p3:
        availability = (
            "LIMITED"
            if member["load"] >= 75
            else "AVAILABLE"
        )
        st.metric("CONTACT", availability)

    st.info(
        "ORBIT evaluates workload and protected rest periods "
        "before allowing non-critical interruptions."
    )

    b1, b2, b3 = st.columns(3)

    with b1:
        if st.button("SEND MESSAGE", key="profile_message"):
            st.success("Asynchronous message queued.")

    with b2:
        if st.button("REQUEST CALL", key="profile_call"):
            st.info(
                "Call request submitted. ORBIT is checking availability."
            )

    with b3:
        if st.button("CLOSE PROFILE", key="profile_close"):
            st.session_state.selected_crew = None
            st.rerun()


# ============================================================
# MEDIATION PANEL
# ============================================================

if st.session_state.mediation_open:

    st.divider()

    st.markdown(
        '<div class="eyebrow">CONFLICT RESOLUTION</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-title">Mediation Protocol</div>',
        unsafe_allow_html=True
    )

    st.warning(
        "SCIENCE ↔ ENGINEERING · Experiment vs. Maintenance"
    )

    st.markdown(
        """
        <div class="panel">

            <div class="card-label">
                STEP 01 · DEFINE
            </div>

            <div style="
                font-size:11px;
                margin-top:7px;
            ">
                Engineering requires a temporary module shutdown.
                Science reports that the shutdown may invalidate
                the current experiment.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    m1, m2 = st.columns(2)

    with m1:

        st.markdown(
            """
            <div class="panel">

                <div class="card-label">
                    ENGINEERING POSITION
                </div>

                <div class="card-sub"
                     style="margin-top:10px">
                    Maintenance must occur before
                    the system reaches its next
                    operational threshold.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with m2:

        st.markdown(
            """
            <div class="panel">

                <div class="card-label">
                    SCIENCE POSITION
                </div>

                <div class="card-sub"
                     style="margin-top:10px">
                    Experiment data may become
                    unusable if the climate sensor
                    cycle is interrupted.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("### Decision")

    decision = st.radio(
        "Select resolution",
        [
            "Delay maintenance",
            "Pause experiment",
            "Find alternative procedure",
            "Escalate to Commander"
        ],
        horizontal=False
    )

    if st.button(
        "RECORD DECISION",
        use_container_width=True
    ):

        st.success(
            f"Decision recorded: {decision}"
        )

        st.session_state.mediation_open = False


# ============================================================
# EARTH LINK PANEL
# ============================================================

if st.session_state.earth_open:

    st.divider()

    st.markdown(
        '<div class="eyebrow">GROUND NETWORK</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-title">Earth Link</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="earth-card">

            <div style="
                display:flex;
                justify-content:space-between;
            ">

                <div>

                    <div style="
                        font-size:12px;
                        font-weight:600;
                    ">
                        Climate Research Coordination Center
                    </div>

                    <div class="card-sub">
                        Ground network · secure channel
                    </div>

                </div>

                <div class="green">
                    ● ONLINE
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    earth1, earth2, earth3, earth4 = st.columns(4)

    channels = [
        ("SCIENCE", "Climate Research Team"),
        ("ENGINEERING", "Systems Ground Team"),
        ("MEDICAL", "Ground Medical Officer"),
        ("COMMAND", "Mission Control"),
    ]

    for column, (name, description) in zip(
        [earth1, earth2, earth3, earth4],
        channels
    ):

        with column:

            st.markdown(
                f"""
                <div class="panel">

                    <div class="card-label">
                        {name}
                    </div>

                    <div style="
                        font-size:10px;
                        margin-top:8px;
                    ">
                        {description}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                "CONNECT",
                key=f"earth_{name}"
            ):
                st.success(
                    f"{name} channel connected."
                )

    st.info(
        "ORBIT allows specialists to communicate directly "
        "with the appropriate Earth team while keeping "
        "mission-critical decisions visible to command."
    )

    if st.button("CLOSE EARTH LINK"):
        st.session_state.earth_open = False
        st.rerun()


# ============================================================
# EMERGENCY PANEL
# ============================================================

if st.session_state.emergency_open:

    st.divider()

    st.markdown(
        '<div class="eyebrow">P0 · EMERGENCY CHANNEL</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-title red">Emergency Protocol</div>',
        unsafe_allow_html=True
    )

    st.error(
        """
        LIFE / STATION SAFETY PROTOCOL

        This action overrides Quiet Orbit and protected rest
        periods when immediate intervention is required.
        """
    )

    confirm = st.checkbox(
        "I confirm that this is a genuine P0 emergency."
    )

    if confirm:

        if st.button(
            "ACTIVATE P0 PROTOCOL",
            use_container_width=True
        ):

            st.session_state.emergency_open = False

            st.success(
                "P0 ACTIVATED — required crew members notified."
            )

            st.balloons()

    if st.button("CANCEL EMERGENCY"):
        st.session_state.emergency_open = False
        st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="system-footer">
        ORBIT · OPERATIONAL RELAY & BALANCE INTERFACE FOR TEAMWORK
        · MISSION 07 · CLIMATE MONITORING
    </div>
    """,
    unsafe_allow_html=True
)
