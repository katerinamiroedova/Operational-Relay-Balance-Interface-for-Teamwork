import streamlit as st

st.set_page_config(
    page_title="ORBIT",
    page_icon="🛰️",
    layout="wide"
)

st.title("🛰️ ORBIT")
st.subheader("Crew Operations System")

st.success("SYSTEM ONLINE")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("STATION", "NOMINAL")

with col2:
    st.metric("CREW", "8 / 8")

with col3:
    st.metric("EARTH LINK", "ACTIVE")

st.divider()

st.header("Crew Status")

crew = [
    ("A. Ivanov", "Systems Engineer", "WORKING"),
    ("S. Smirnova", "Climate Scientist", "EXPERIMENT"),
    ("D. Kim", "Life Support", "MAINTENANCE"),
    ("M. Orlova", "Flight Specialist", "AVAILABLE"),
]

for name, role, status in crew:
    st.write(f"**{name}** — {role} — 🟢 {status}")

st.divider()

st.header("Communication")

if st.button("📡 Contact Earth"):
    st.success("Earth communication channel activated.")

if st.button("🤝 Open Mediation"):
    st.warning("Mediation protocol initiated.")

if st.button("🌙 Quiet Orbit"):
    st.info("Protected rest protocol is active.")

st.divider()

st.header("Mission Status")

st.info(
    "Climate monitoring mission is operating normally. "
    "All primary communication channels are available."
)
