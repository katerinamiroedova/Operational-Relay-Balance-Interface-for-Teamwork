import streamlit as st
from datetime import datetime

# ============================================================
# ORBIT
# Crew Operations & Communication Management System
# ============================================================

st.set_page_config(
    page_title="ORBIT | Crew Operations",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "Command Center"

if "quiet_orbit" not in st.session_state:
    st.session_state.quiet_orbit = True

if "earth_link" not in st.session_state:
    st.session_state.earth_link = True

if "emergency" not in st.session_state:
    st.session_state.emergency = False

if "selected_crew" not in st.session_state:
    st.session_state.selected_crew = None

if "logs" not in st.session_state:
    st.session_state.logs = [
        {
            "time": "14:18",
            "type": "SYSTEM",
            "source": "ORBIT",
            "message": "Protected D. Kim's rest period",
            "category": "CREW WELLBEING",
        },
        {
            "time": "14:11",
            "type": "COMMAND",
            "source": "COMMAND",
            "message": "Mediation protocol initiated",
            "category": "CONFLICT",
        },
        {
            "time": "13:52",
            "type": "SYSTEM",
            "source": "ENGINEERING",
            "message": "Life Support inspection scheduled",
            "category": "MAINTENANCE",
        },
    ]

# ============================================================
# CREW
# ============================================================

crew = {
    "A. Ivanov": {
        "role": "Systems Engineer",
        "module": "Engineering",
        "status": "WORKING",
        "availability": "LIMITED",
        "load": 81,
        "rest": "16:40",
        "specialty": "Life Support / Mechanical Systems",
    },
    "S. Smirnova": {
        "role": "Climate Scientist",
        "module": "Science",
        "status": "EXPERIMENT",
        "availability": "BUSY",
        "load": 63,
        "rest": "18:10",
        "specialty": "Atmospheric Monitoring",
    },
    "D. Kim": {
        "role": "Life Support Specialist",
        "module": "Life Support",
        "status": "REST",
        "availability": "PROTECTED",
        "load": 42,
        "rest": "15:20",
        "specialty": "Environmental Control",
    },
    "M. Orlova": {
        "role": "Flight Specialist",
        "module": "Habitat",
        "status": "AVAILABLE",
        "availability": "AVAILABLE",
        "load": 51,
        "rest": "21:30",
        "specialty": "Flight Operations",
    },
    "R. Chen": {
        "role": "Data Systems Engineer",
        "module": "Science",
        "status": "WORKING",
        "availability": "AVAILABLE",
        "load": 58,
        "rest": "19:00",
        "specialty": "Telemetry / Data Processing",
    },
    "E. Volkov": {
        "role": "Biomedical Specialist",
        "module": "Habitat",
        "status": "AVAILABLE",
        "availability": "AVAILABLE",
        "load": 47,
        "rest": "20:40",
        "specialty": "Crew Health",
    },
    "L. Adams": {
        "role": "Climate Systems Engineer",
        "module": "Science",
        "status": "WORKING",
        "availability": "AVAILABLE",
        "load": 67,
        "rest": "17:50",
        "specialty": "Sensor Architecture",
    },
    "N. Petrova": {
        "role": "Communications Specialist",
        "module": "Command",
        "status": "AVAILABLE",
        "availability": "AVAILABLE",
        "load": 39,
        "rest": "22:00",
        "specialty": "Communications / Earth Link",
    },
}

# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background: #05080d;
        color: #e8eef5;
    }

    [data-testid="stSidebar"] {
        background: #080c12;
        border-right: 1px solid #18212c;
    }

    .block-container {
        max-width: 1500px;
        padding-top: 30px;
        padding-bottom: 50px;
    }

    h1, h2, h3 {
        font-family: Arial, sans-serif;
    }

    .orbit-title {
        font-size: 32px;
        font-weight: 700;
        letter-spacing: 5px;
        color: #eaf5ff;
        margin-bottom: 3px;
    }

    .orbit-title span {
        color: #58dfff;
    }

    .eyebrow {
        color: #58dfff;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 2px;
        margin-bottom: 5px;
    }

    .muted {
        color: #617084;
        font-size: 11px;
    }

    .card {
        background: #0b1119;
        border: 1px solid #1a2633;
        border-radius: 10px;
        padding: 18px;
        min-height: 95px;
        margin-bottom: 12px;
    }

    .card-label {
        color: #617084;
        font-size: 9px;
        font-weight: 700;
        letter-spacing: 1.5px;
    }

    .card-number {
        font-size: 23px;
        font-weight: 700;
        margin-top: 8px;
    }

    .card-description {
        color: #59697c;
        font-size: 9px;
        margin-top: 5px;
    }

    .panel {
        background: #0a1018;
        border: 1px solid #182430;
        border-radius: 11px;
        padding: 18px;
        margin-bottom: 15px;
    }

    .panel-title {
        font-size: 14px;
        font-weight: 700;
        color: #dce8f3;
        margin-bottom: 3px;
    }

    .panel-subtitle {
        color: #536276;
        font-size: 9px;
        margin-bottom: 15px;
    }

    .status-green {
        color: #4ee09c;
    }

    .status-yellow {
        color: #f0c85c;
    }

    .status-red {
        color: #ff6575;
    }

    .status-blue {
        color: #58bfff;
    }

    .crew-box {
        background: #0d141d;
        border: 1px solid #1a2633;
        border-radius: 8px;
        padding: 12px;
        margin-bottom: 8px;
    }

    .crew-name {
        font-weight: 700;
        font-size: 11px;
    }

    .crew-role {
        color: #657488;
        font-size: 9px;
        margin-top: 3px;
    }

    .crew-status {
        font-size: 8px;
        font-weight: 700;
        letter-spacing: 1px;
        margin-top: 7px;
    }

    .bar {
        width: 100%;
        height: 5px;
        background: #1a2430;
        border-radius: 5px;
        margin-top: 9px;
    }

    .bar-fill {
        height: 5px;
        border-radius: 5px;
    }

    .alert-box {
        background: #0c131c;
        border: 1px solid #263341;
        border-radius: 9px;
        padding: 14px;
        margin-bottom: 9px;
    }

    .alert-red {
        border-left: 3px solid #ff6575;
    }

    .alert-yellow {
        border-left: 3px solid #f0c85c;
    }

    .alert-blue {
        border-left: 3px solid #58bfff;
    }

    .alert-title {
        font-size: 11px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .alert-text {
        color: #657488;
        font-size: 9px;
        line-height: 1.5;
    }

    .log {
        background: #0b1119;
        border: 1px solid #192530;
        border-radius: 8px;
        padding: 13px;
        margin-bottom: 8px;
    }

    .log-time {
        color: #58dfff;
        font-size: 9px;
        font-weight: 700;
    }

    .log-type {
        color: #718096;
        font-size: 8px;
        letter-spacing: 1px;
        margin-left: 7px;
    }

    .log-message {
        color: #d5dfe9;
        font-size: 10px;
        font-weight: 600;
        margin-top: 6px;
    }

    .log-source {
        color: #526175;
        font-size: 8px;
        margin-top: 4px;
    }

    .module-box {
        background: #0d151f;
        border: 1px solid #1b2a38;
        border-radius: 9px;
        padding: 14px;
        text-align: center;
        min-height: 105px;
    }

    .module-title {
        color: #657488;
        font-size: 8px;
        letter-spacing: 1px;
        font-weight: 700;
    }

    .module-name {
        color: #e3edf6;
        font-size: 11px;
        font-weight: 700;
        margin-top: 9px;
    }

    .module-status {
        color: #4ee09c;
        font-size: 8px;
        margin-top: 8px;
    }

    .timeline {
        background: #0c131b;
        border: 1px solid #192631;
        border-radius: 8px;
        padding: 12px;
        margin-bottom: 7px;
    }

    .timeline-time {
        color: #58dfff;
        font-size: 10px;
        font-weight: 700;
    }

    .timeline-event {
        color: #dce6ef;
        font-size: 10px;
        font-weight: 600;
        margin-top: 4px;
    }

    .timeline-owner {
        color: #59697b;
        font-size: 8px;
        margin-top: 3px;
    }

    .big-number {
        font-size: 36px;
        font-weight: 700;
        color: #58dfff;
    }

    .protocol-box {
        background: #0d141d;
        border: 1px solid #1a2733;
        border-radius: 9px;
        padding: 16px;
        min-height: 150px;
    }

    .protocol-title {
        color: #dce7f1;
        font-weight: 700;
        font-size: 11px;
    }

    .protocol-text {
        color: #657488;
        font-size: 9px;
        line-height: 1.6;
        margin-top: 8px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# FUNCTIONS
# ============================================================

def add_log(source, message, log_type, category):
    st.session_state.logs.insert(
        0,
        {
            "time": datetime.now().strftime("%H:%M"),
            "type": log_type,
            "source": source,
            "message": message,
            "category": category,
        },
    )


def workload_color(value):
    if value >= 75:
        return "#ff6575"
    if value >= 60:
        return "#f0c85c"
    return "#4ee09c"


def state_color(value):
    if value in ["REST", "AVAILABLE"]:
        return "#4ee09c"
    if value in ["WORKING", "EXPERIMENT"]:
        return "#58bfff"
    return "#f0c85c"


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="orbit-title">OR<span>BIT</span></div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="muted">CREW OPERATIONS SYSTEM</div>',
        unsafe_allow_html=True,
    )

    st.divider()

    st.caption("MISSION NAVIGATION")

    navigation = [
        "Command Center",
        "Crew Control",
        "Communication",
        "Mission Schedule",
        "Mediation",
        "Earth Link",
        "Decision Log",
    ]

    for item in navigation:
        if st.button(
            item,
            key="nav_" + item,
            use_container_width=True,
        ):
            st.session_state.page = item
            st.rerun()

    st.divider()

    st.caption("LIVE PROTOCOLS")

    if st.session_state.quiet_orbit:
        st.success("QUIET ORBIT · ACTIVE")
    else:
        st.warning("QUIET ORBIT · PAUSED")

    if st.session_state.earth_link:
        st.success("EARTH LINK · CONNECTED")
    else:
        st.error("EARTH LINK · OFFLINE")

    st.caption("MISSION TIME")
    st.code("14:32 UTC")

    st.divider()

    if st.button(
        "⚠  P0 EMERGENCY",
        type="primary",
        use_container_width=True,
    ):
        st.session_state.emergency = True
        st.session_state.page = "Command Center"
        st.rerun()


# ============================================================
# TOP INFORMATION BAR
# ============================================================

top_a, top_b, top_c, top_d = st.columns([3, 1, 1, 1])

with top_a:
    st.markdown(
        '<div class="eyebrow">MISSION 07 · CLIMATE MONITORING EXPEDITION</div>',
        unsafe_allow_html=True,
    )

with top_b:
    st.metric("ALTITUDE", "412 km")

with top_c:
    st.metric("EARTH LATENCY", "0.8 s")

with top_d:
    st.metric("CREW", "08 / 08")


# ============================================================
# COMMAND CENTER
# ============================================================

if st.session_state.page == "Command Center":

    st.title("Command Center")

    st.markdown(
        '<div class="muted">Commander overview · mission state · crew coordination · active decisions</div>',
        unsafe_allow_html=True,
    )

    st.write("")

    # STATUS CARDS

    a, b, c, d, e = st.columns(5)

    with a:
        st.markdown(
            """
            <div class="card">
                <div class="card-label">STATION</div>
                <div class="card-number status-green">NOMINAL</div>
                <div class="card-description">All systems within parameters</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with b:
        st.markdown(
            """
            <div class="card">
                <div class="card-label">CREW</div>
                <div class="card-number status-blue">08 / 08</div>
                <div class="card-description">All crew accounted for</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c:
        st.markdown(
            """
            <div class="card">
                <div class="card-label">EARTH</div>
                <div class="card-number status-green">LINKED</div>
                <div class="card-description">Secure ground connection</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with d:
        st.markdown(
            """
            <div class="card">
                <div class="card-label">QUIET ORBIT</div>
                <div class="card-number status-green">ACTIVE</div>
                <div class="card-description">Protected rest enabled</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with e:
        st.markdown(
            """
            <div class="card">
                <div class="card-label">ATTENTION</div>
                <div class="card-number status-yellow">03</div>
                <div class="card-description">Commander actions pending</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    # MAIN TWO COLUMNS

    left, right = st.columns([1.45, 1])

    # --------------------------------------------------------
    # STATION
    # --------------------------------------------------------

    with left:

        st.markdown(
            """
            <div class="panel">
                <div class="panel-title">Station Architecture</div>
                <div class="panel-subtitle">INTERNAL NETWORK · LIVE</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("#### CLIMATE MONITORING STATION")

        r1, r2, r3 = st.columns(3)

        with r1:
            st.markdown(
                """
                <div class="module-box">
                    <div class="module-title">SCIENCE MODULE</div>
                    <div class="module-name">CLIMATE LAB</div>
                    <div class="module-status">● EXPERIMENT ACTIVE</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with r2:
            st.markdown(
                """
                <div class="module-box">
                    <div class="module-title">CENTRAL COMMAND</div>
                    <div class="module-name">ORBIT CORE</div>
                    <div class="module-status">● NOMINAL</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with r3:
            st.markdown(
                """
                <div class="module-box">
                    <div class="module-title">LIFE SUPPORT</div>
                    <div class="module-name">ECLSS</div>
                    <div class="module-status">● STABLE</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.write("")

        r4, r5 = st.columns(2)

        with r4:
            st.markdown(
                """
                <div class="module-box">
                    <div class="module-title">ENGINEERING</div>
                    <div class="module-name">SYSTEMS BAY</div>
                    <div class="module-status" style="color:#f0c85c">
                        ● MAINTENANCE
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with r5:
            st.markdown(
                """
                <div class="module-box">
                    <div class="module-title">HABITAT</div>
                    <div class="module-name">CREW QUARTERS</div>
                    <div class="module-status">● PROTECTED</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.write("")

        st.markdown(
            """
            <div class="panel">
                <div class="panel-title">Operational Principle</div>
                <div class="panel-subtitle">
                    ORBIT prevents the commander from becoming the only
                    communication gateway.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        flow1, flow2, flow3, flow4 = st.columns(4)

        with flow1:
            st.info("REQUEST\n\nCrew member initiates communication.")

        with flow2:
            st.info("FILTER\n\nORBIT checks priority and availability.")

        with flow3:
            st.info("ROUTE\n\nRequest goes to crew or Earth specialist.")

        with flow4:
            st.success("DECISION\n\nCommander intervenes only when needed.")

    # --------------------------------------------------------
    # ATTENTION
    # --------------------------------------------------------

    with right:

        st.markdown(
            """
            <div class="panel">
                <div class="panel-title">Commander Attention</div>
                <div class="panel-subtitle">03 ACTIVE DECISIONS</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="alert-box alert-red">
                <div class="alert-title status-red">
                    P1 · LIFE SUPPORT INSPECTION
                </div>
                <div class="alert-text">
                    Engineering requires access to ECLSS before
                    the next maintenance threshold.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "REVIEW ENGINEERING TASK",
            use_container_width=True,
        ):
            st.session_state.selected_crew = "A. Ivanov"
            st.session_state.page = "Crew Control"
            st.rerun()

        st.markdown(
            """
            <div class="alert-box alert-yellow">
                <div class="alert-title status-yellow">
                    MEDIATION REQUIRED
                </div>
                <div class="alert-text">
                    Science experiment conflicts with engineering
                    maintenance window.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "OPEN MEDIATION",
            use_container_width=True,
        ):
            st.session_state.page = "Mediation"
            st.rerun()

        st.markdown(
            """
            <div class="alert-box alert-blue">
                <div class="alert-title status-blue">
                    EARTH REQUEST
                </div>
                <div class="alert-text">
                    Ground Climate Center requested additional
                    atmospheric telemetry.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "OPEN EARTH LINK",
            use_container_width=True,
        ):
            st.session_state.page = "Earth Link"
            st.rerun()

    # --------------------------------------------------------
    # CREW + TIMELINE
    # --------------------------------------------------------

    st.write("")

    crew_col, timeline_col = st.columns([1.1, 1])

    with crew_col:

        st.markdown(
            """
            <div class="panel-title">Crew Situation</div>
            <div class="panel-subtitle">WORKLOAD · AVAILABILITY · STATE</div>
            """,
            unsafe_allow_html=True,
        )

        for name, person in list(crew.items())[:5]:

            color = workload_color(person["load"])
            state = state_color(person["status"])

            st.markdown(
                f"""
                <div class="crew-box">
                    <div class="crew-name">{name}</div>
                    <div class="crew-role">
                        {person["role"]} · {person["module"]}
                    </div>
                    <div class="crew-status" style="color:{state}">
                        ● {person["status"]}
                    </div>
                    <div class="bar">
                        <div class="bar-fill"
                             style="width:{person["load"]}%;
                                    background:{color};">
                        </div>
                    </div>
                    <div class="crew-role">
                        Workload {person["load"]}% · Next rest {person["rest"]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        if st.button(
            "OPEN FULL CREW CONTROL",
            use_container_width=True,
        ):
            st.session_state.page = "Crew Control"
            st.rerun()

    with timeline_col:

        st.markdown(
            """
            <div class="panel-title">Mission Timeline</div>
            <div class="panel-subtitle">NEXT OPERATIONAL WINDOWS</div>
            """,
            unsafe_allow_html=True,
        )

        events = [
            ("14:45", "ECLSS inspection", "Engineering"),
            ("15:20", "Climate sensor cycle", "Science"),
            ("16:00", "Ground telemetry upload", "Communications"),
            ("18:00", "Crew briefing", "Command"),
            ("19:30", "Maintenance review", "Engineering"),
            ("21:00", "Quiet Orbit begins", "All crew"),
        ]

        for tm, event, owner in events:

            st.markdown(
                f"""
                <div class="timeline">
                    <div class="timeline-time">{tm}</div>
                    <div class="timeline-event">{event}</div>
                    <div class="timeline-owner">{owner}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


# ============================================================
# CREW CONTROL
# ============================================================

elif st.session_state.page == "Crew Control":

    st.title("Crew Control")

    st.markdown(
        '<div class="muted">Manage workload, availability, rest protection and communication access.</div>',
        unsafe_allow_html=True,
    )

    st.write("")

    selected = st.session_state.selected_crew

    if selected:

        person = crew[selected]

        st.markdown(
            f"""
            <div class="panel">
                <div class="eyebrow">CREW PROFILE</div>
                <div class="orbit-title" style="font-size:25px;letter-spacing:1px;">
                    {selected}
                </div>
                <div class="muted">
                    {person["role"]} · {person["module"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        x1, x2, x3, x4 = st.columns(4)

        with x1:
            st.metric("STATUS", person["status"])

        with x2:
            st.metric("WORKLOAD", f'{person["load"]}%')

        with x3:
            st.metric("AVAILABILITY", person["availability"])

        with x4:
            st.metric("NEXT REST", person["rest"])

        st.write("")

        if person["availability"] == "PROTECTED":

            st.warning(
                f"{selected} is currently protected by Quiet Orbit. "
                "Non-critical direct calls are blocked."
            )

            if st.button(
                "SEND ASYNC MESSAGE",
                use_container_width=True,
            ):
                add_log(
                    "COMMAND",
                    f"Async message sent to {selected}",
                    "COMMUNICATION",
                    "CREW",
                )
                st.success("Message queued without interrupting rest.")

        elif person["load"] >= 75:

            st.warning(
                f"{selected} has a workload of {person['load']}%. "
                "ORBIT recommends delegation or scheduled contact."
            )

            if st.button(
                "SCHEDULE CONTACT",
                use_container_width=True,
            ):
                add_log(
                    "COMMAND",
                    f"Scheduled contact with {selected}",
                    "COMMUNICATION",
                    "CREW",
                )
                st.success("Contact window scheduled.")

        else:

            if st.button(
                "START DIRECT CHANNEL",
                use_container_width=True,
            ):
                add_log(
                    "COMMAND",
                    f"Direct communication opened with {selected}",
                    "COMMUNICATION",
                    "CREW",
                )
                st.success("Secure internal channel active.")

        st.write("")

        if st.button("CLOSE PROFILE"):
            st.session_state.selected_crew = None
            st.rerun()

    st.divider()

    st.subheader("All Crew")

    for name, person in crew.items():

        c1, c2, c3 = st.columns([2.4, 1, 1])

        with c1:

            st.markdown(
                f"""
                <div class="crew-box">
                    <div class="crew-name">{name}</div>
                    <div class="crew-role">
                        {person["role"]} · {person["module"]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with c2:

            st.metric(
                "LOAD",
                f'{person["load"]}%'
            )

        with c3:

            if st.button(
                "MANAGE",
                key="manage_" + name,
                use_container_width=True,
            ):
                st.session_state.selected_crew = name
                st.rerun()


# ============================================================
# COMMUNICATION
# ============================================================

elif st.session_state.page == "Communication":

    st.title("Communication Control")

    st.markdown(
        '<div class="muted">A communication system that protects focus, rest and mission-critical response.</div>',
        unsafe_allow_html=True,
    )

    st.write("")

    protocols = [
        (
            "P3 · ASYNC",
            "Non-urgent information",
            "Message is delivered without interrupting work or protected rest.",
        ),
        (
            "P2 · SCHEDULED",
            "Important but not urgent",
            "ORBIT finds the next appropriate communication window.",
        ),
        (
            "P1 · PRIORITY",
            "Operationally important",
            "Crew member is contacted as soon as workload permits.",
        ),
        (
            "P0 · EMERGENCY",
            "Immediate threat",
            "Emergency protocol can override protected rest.",
        ),
    ]

    cols = st.columns(4)

    for col, protocol in zip(cols, protocols):

        with col:

            st.markdown(
                f"""
                <div class="protocol-box">
                    <div class="card-label">{protocol[0]}</div>
                    <div class="protocol-title">
                        {protocol[1]}
                    </div>
                    <div class="protocol-text">
                        {protocol[2]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.write("")
    st.divider()

    st.subheader("Communication Check")

    person_name = st.selectbox(
        "Crew member",
        list(crew.keys()),
    )

    priority = st.selectbox(
        "Priority",
        [
            "P3 · ASYNC",
            "P2 · SCHEDULED",
            "P1 · PRIORITY",
            "P0 · EMERGENCY",
        ],
    )

    reason = st.text_input(
        "Reason",
        placeholder="Why does this person need to be contacted?",
    )

    if st.button(
        "RUN COMMUNICATION CHECK",
        type="primary",
        use_container_width=True,
    ):

        person = crew[person_name]

        if (
            person["availability"] == "PROTECTED"
            and priority != "P0 · EMERGENCY"
        ):

            st.error(
                f"""
                CONTACT BLOCKED.

                {person_name} is currently in protected rest.

                Recommended action:
                send an asynchronous message or schedule contact
                after {person["rest"]}.
                """
            )

            add_log(
                "ORBIT",
                f"Blocked non-critical contact with {person_name}",
                "PROTOCOL",
                "QUIET ORBIT",
            )

        elif person["load"] >= 75 and priority == "P1 · PRIORITY":

            st.warning(
                f"""
                CONTACT FLAGGED.

                {person_name} currently has {person["load"]}% workload.

                Consider delegation before interrupting this crew member.
                """
            )

            add_log(
                "ORBIT",
                f"Flagged high-workload contact for {person_name}",
                "PROTOCOL",
                "WORKLOAD",
            )

        elif priority == "P0 · EMERGENCY":

            st.error(
                "P0 OVERRIDE APPROVED — protected rest may be interrupted."
            )

            add_log(
                "COMMAND",
                f"P0 communication initiated with {person_name}",
                "EMERGENCY",
                "P0",
            )

        else:

            st.success(
                f"CONTACT APPROVED — {person_name} may be contacted."
            )

            add_log(
                "COMMAND",
                f"Communication approved for {person_name}",
                "COMMUNICATION",
                "CONTACT",
            )


# ============================================================
# SCHEDULE
# ============================================================

elif st.session_state.page == "Mission Schedule":

    st.title("Mission Schedule")

    st.markdown(
        '<div class="muted">A schedule designed around mission requirements and human recovery.</div>',
        unsafe_allow_html=True,
    )

    st.write("")

    schedule = [
        ("14:45", "ECLSS inspection", "Engineering", "P1"),
        ("15:20", "Climate sensor cycle", "Science", "P2"),
        ("16:00", "Ground telemetry upload", "Communications", "P2"),
        ("17:15", "Protected meal window", "All crew", "P3"),
        ("18:00", "Crew briefing", "Command", "P2"),
        ("19:30", "Maintenance review", "Engineering", "P2"),
        ("21:00", "QUIET ORBIT", "All crew", "PROTECTED"),
        ("06:30", "Wake cycle", "All crew", "ROUTINE"),
    ]

    for tm, event, owner, priority in schedule:

        c1, c2, c3, c4 = st.columns([0.8, 2.8, 1.5, 1])

        with c1:
            st.markdown(
                f"""
                <div class="timeline">
                    <div class="timeline-time">{tm}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with c2:
            st.markdown(
                f"""
                <div class="timeline">
                    <div class="timeline-event">{event}</div>
                    <div class="timeline-owner">{owner}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with c3:
            st.markdown(
                f"""
                <div class="timeline">
                    <div class="timeline-owner">PROTOCOL</div>
                    <div class="timeline-event">{priority}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with c4:

            if priority == "PROTECTED":

                st.success("🔒 LOCKED")

            else:

                if st.button(
                    "EDIT",
                    key="edit_" + tm,
                    use_container_width=True,
                ):
                    st.info(f"Selected: {event}")


# ============================================================
# MEDIATION
# ============================================================

elif st.session_state.page == "Mediation":

    st.title("Mediation Protocol")

    st.markdown(
        '<div class="muted">Resolve disagreements without forcing every conflict through command authority.</div>',
        unsafe_allow_html=True,
    )

    st.write("")

    st.warning(
        "ACTIVE CONFLICT: Climate experiment overlaps with ECLSS maintenance."
    )

    left, right = st.columns(2)

    with left:

        st.markdown(
            """
            <div class="panel">
                <div class="panel-title">SCIENCE POSITION</div>
                <div class="panel-subtitle">
                    S. Smirnova · Climate Science
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.info(
            "Objective: preserve continuous climate sensor data.\n\n"
            "Risk: interruption may invalidate the current measurement cycle."
        )

    with right:

        st.markdown(
            """
            <div class="panel">
                <div class="panel-title">ENGINEERING POSITION</div>
                <div class="panel-subtitle">
                    A. Ivanov · Systems Engineering
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.warning(
            "Objective: inspect the ECLSS valve before threshold breach.\n\n"
            "Risk: delaying maintenance increases system risk."
        )

    st.divider()

    decision = st.radio(
        "Commander resolution",
        [
            "Delay maintenance",
            "Pause experiment",
            "Modify maintenance procedure",
            "Split the maintenance window",
            "Escalate to Earth",
        ],
    )

    rationale = st.text_area(
        "Decision rationale",
        placeholder="Explain why this resolution best protects the mission.",
    )

    if st.button(
        "RECORD DECISION",
        type="primary",
        use_container_width=True,
    ):

        if not rationale.strip():

            st.error("A rationale is required.")

        else:

            add_log(
                "COMMAND",
                f"Mediation resolved: {decision}",
                "MEDIATION",
                "CONFLICT RESOLUTION",
            )

            st.success(
                "Decision recorded. All involved crew members can now see the resolution."
            )


# ============================================================
# EARTH LINK
# ============================================================

elif st.session_state.page == "Earth Link":

    st.title("Earth Link")

    st.markdown(
        '<div class="muted">Distributed communication with Earth — the commander is not the only gateway.</div>',
        unsafe_allow_html=True,
    )

    st.write("")

    channels = [
        (
            "MISSION CONTROL",
            "COMMAND",
            "Mission decisions and escalation",
        ),
        (
            "CLIMATE CENTER",
            "SCIENCE",
            "Atmospheric data and research",
        ),
        (
            "GROUND ENGINEERING",
            "ENGINEERING",
            "Technical diagnostics",
        ),
        (
            "MEDICAL CONTROL",
            "MEDICAL",
            "Crew health and emergency support",
        ),
    ]

    cols = st.columns(4)

    for col, channel in zip(cols, channels):

        with col:

            st.markdown(
                f"""
                <div class="protocol-box">
                    <div class="card-label">{channel[1]}</div>
                    <div class="protocol-title">{channel[0]}</div>
                    <div class="protocol-text">{channel[2]}</div>
                    <div class="status-green"
                         style="font-size:8px;margin-top:12px;">
                        ● SECURE CHANNEL
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            if st.button(
                "CONNECT",
                key="earth_" + channel[0],
                use_container_width=True,
            ):

                add_log(
                    "COMMAND",
                    f"Connected to {channel[0]}",
                    "EARTH LINK",
                    "GROUND",
                )

                st.success("Channel connected.")

    st.write("")
    st.divider()

    st.subheader("Send Earth Request")

    sender = st.selectbox(
        "Initiated by",
        list(crew.keys()),
    )

    destination = st.selectbox(
        "Destination",
        [
            "Mission Control",
            "Climate Center",
            "Ground Engineering",
            "Medical Control",
        ],
    )

    purpose = st.text_input(
        "Purpose",
        placeholder="Describe the request...",
    )

    if st.button(
        "SEND REQUEST",
        type="primary",
        use_container_width=True,
    ):

        if not purpose.strip():

            st.error("Purpose is required.")

        else:

            add_log(
                sender,
                f"Earth request sent to {destination}: {purpose}",
                "EARTH LINK",
                "GROUND",
            )

            st.success(
                f"Request routed directly to {destination}."
            )


# ============================================================
# DECISION LOG
# ============================================================

elif st.session_state.page == "Decision Log":

    st.title("Decision Log")

    st.caption(
        "Every important operational decision remains traceable."
    )

    st.write("")

    # HEADER
    h1, h2, h3 = st.columns([0.8, 2.8, 1.2])

    with h1:
        st.caption("TIME")

    with h2:
        st.caption("OPERATIONAL DECISION")

    with h3:
        st.caption("SOURCE")

    st.divider()

    # LOG ENTRIES
    if not st.session_state.logs:

        st.info("No operational decisions recorded yet.")

    else:

        for index, item in enumerate(st.session_state.logs):

            col_time, col_main, col_source = st.columns(
                [0.8, 2.8, 1.2]
            )

            with col_time:

                st.markdown(
                    f"**{item['time']}**"
                )

                st.caption(item["type"])

            with col_main:

                st.write(
                    f"**{item['message']}**"
                )

                st.caption(
                    f"Category · {item['category']}"
                )

            with col_source:

                source = item["source"]

                if source == "COMMAND":
                    st.success("COMMAND")

                elif source == "ORBIT":
                    st.info("ORBIT")

                elif source == "ENGINEERING":
                    st.warning("ENGINEERING")

                else:
                    st.caption(source)

            if index < len(st.session_state.logs) - 1:
                st.divider()

    st.write("")

    # LOG STATISTICS
    st.subheader("Log Status")

    s1, s2, s3 = st.columns(3)

    with s1:
        st.metric(
            "TOTAL EVENTS",
            len(st.session_state.logs)
        )

    with s2:
        command_events = sum(
            1
            for item in st.session_state.logs
            if item["type"] == "COMMAND"
        )

        st.metric(
            "COMMAND ACTIONS",
            command_events
        )

    with s3:
        system_events = sum(
            1
            for item in st.session_state.logs
            if item["type"] in ["SYSTEM", "PROTOCOL"]
        )

        st.metric(
            "SYSTEM EVENTS",
            system_events
        )

    st.write("")

    if st.button(
        "CLEAR SESSION LOG",
        use_container_width=True,
    ):

        st.session_state.logs = []

        st.success(
            "Session decision log cleared."
        )

        st.rerun()
        
# ============================================================
# EMERGENCY MODE
# ============================================================

if st.session_state.emergency:

    st.divider()

    st.error("P0 EMERGENCY PROTOCOL")

    st.subheader("Emergency Command")

    st.write(
        "This protocol overrides normal communication rules only when "
        "there is an immediate threat to life, station integrity or mission survival."
    )

    emergency_type = st.selectbox(
        "Emergency classification",
        [
            "Life Support Failure",
            "Fire / Atmospheric Threat",
            "Structural Risk",
            "Medical Emergency",
            "Loss of Earth Communication",
            "Other P0 Threat",
        ],
    )

    required = st.multiselect(
        "Required crew",
        list(crew.keys()),
    )

    earth_notify = st.checkbox(
        "Notify Earth Mission Control immediately",
    )

    confirmation = st.checkbox(
        "I confirm that this qualifies as a P0 emergency.",
    )

    c1, c2 = st.columns(2)

    with c1:

        if st.button(
            "ACTIVATE P0",
            type="primary",
            use_container_width=True,
        ):

            if not confirmation:

                st.error("Commander confirmation required.")

            elif not required:

                st.error("Select at least one crew member.")

            else:

                add_log(
                    "COMMAND",
                    f"P0 activated: {emergency_type}",
                    "EMERGENCY",
                    "P0",
                )

                for person in required:

                    add_log(
                        "ORBIT",
                        f"P0 notification sent to {person}",
                        "EMERGENCY",
                        "P0",
                    )

                if earth_notify:

                    add_log(
                        "ORBIT",
                        "Earth Mission Control notified",
                        "EARTH LINK",
                        "P0",
                    )

                st.session_state.emergency = False

                st.error(
                    "P0 PROTOCOL ACTIVATED. Required personnel notified."
                )

    with c2:

        if st.button(
            "CANCEL",
            use_container_width=True,
        ):

            st.session_state.emergency = False
            st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "ORBIT · OPERATIONAL RELAY & BALANCE INTERFACE FOR TEAMWORK "
    "· MISSION 07 · CLIMATE MONITORING"
)
