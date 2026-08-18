<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ORBIT — Crew Operations System</title>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

:root {
    --bg: #05070c;
    --panel: #0b1018;
    --panel2: #0e1520;
    --border: rgba(255,255,255,.08);
    --text: #e8eef7;
    --muted: #738197;
    --blue: #4da3ff;
    --cyan: #55e6ff;
    --green: #4de1a1;
    --yellow: #f4c95d;
    --red: #ff5f6d;
    --purple: #9d7cff;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    background:
        radial-gradient(circle at 75% 10%, rgba(52,105,170,.12), transparent 30%),
        radial-gradient(circle at 10% 80%, rgba(89,74,180,.08), transparent 25%),
        var(--bg);
    color: var(--text);
    font-family: Inter, sans-serif;
    min-height: 100vh;
    overflow-x: hidden;
}

body::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    background-image:
        linear-gradient(rgba(255,255,255,.015) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,.015) 1px, transparent 1px);
    background-size: 45px 45px;
}

/* ---------- APP ---------- */

.app {
    display: flex;
    min-height: 100vh;
}

/* ---------- SIDEBAR ---------- */

.sidebar {
    width: 245px;
    min-height: 100vh;
    background: rgba(7,11,17,.94);
    border-right: 1px solid var(--border);
    padding: 25px 16px;
    position: fixed;
    left: 0;
    top: 0;
    bottom: 0;
    z-index: 10;
    backdrop-filter: blur(20px);
}

.logo {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 36px;
    padding-left: 8px;
}

.logo-mark {
    width: 34px;
    height: 34px;
    border: 1px solid var(--cyan);
    border-radius: 50%;
    position: relative;
    box-shadow: 0 0 18px rgba(85,230,255,.2);
}

.logo-mark::before {
    content: "";
    position: absolute;
    width: 10px;
    height: 10px;
    background: var(--cyan);
    border-radius: 50%;
    top: 11px;
    left: 11px;
    box-shadow: 0 0 15px var(--cyan);
}

.logo-mark::after {
    content: "";
    position: absolute;
    width: 42px;
    height: 14px;
    border: 1px solid rgba(85,230,255,.55);
    border-radius: 50%;
    transform: rotate(-25deg);
    left: -5px;
    top: 8px;
}

.logo h1 {
    font-family: "Space Grotesk";
    font-size: 19px;
    letter-spacing: 3px;
}

.logo span {
    color: var(--cyan);
}

.nav-label {
    color: #435166;
    font-size: 10px;
    letter-spacing: 1.7px;
    margin: 22px 10px 9px;
    text-transform: uppercase;
}

.nav-item {
    display: flex;
    align-items: center;
    gap: 12px;
    color: #7e8da2;
    padding: 11px 12px;
    border-radius: 8px;
    cursor: pointer;
    margin-bottom: 3px;
    font-size: 13px;
    transition: .2s;
}

.nav-item:hover {
    background: rgba(255,255,255,.04);
    color: white;
}

.nav-item.active {
    color: white;
    background: linear-gradient(90deg, rgba(77,163,255,.14), transparent);
    border-left: 2px solid var(--blue);
}

.nav-icon {
    width: 17px;
    text-align: center;
    font-size: 14px;
}

.sidebar-bottom {
    position: absolute;
    bottom: 22px;
    left: 16px;
    right: 16px;
}

.connection {
    padding: 13px;
    border: 1px solid var(--border);
    background: rgba(255,255,255,.02);
    border-radius: 9px;
}

.connection-title {
    display: flex;
    justify-content: space-between;
    font-size: 11px;
    color: #8c9aae;
    margin-bottom: 8px;
}

.live {
    color: var(--green);
}

.live::before {
    content: "●";
    margin-right: 5px;
    font-size: 8px;
}

/* ---------- MAIN ---------- */

.main {
    margin-left: 245px;
    width: calc(100% - 245px);
    padding: 28px 34px 45px;
}

/* ---------- HEADER ---------- */

.topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 27px;
}

.eyebrow {
    color: var(--cyan);
    font-size: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 6px;
}

.title {
    font-family: "Space Grotesk";
    font-size: 28px;
    font-weight: 600;
}

.subtitle {
    color: var(--muted);
    font-size: 12px;
    margin-top: 5px;
}

.top-actions {
    display: flex;
    gap: 9px;
    align-items: center;
}

.icon-button {
    width: 38px;
    height: 38px;
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 8px;
    color: #9aa7ba;
    cursor: pointer;
}

.commander {
    display: flex;
    align-items: center;
    gap: 10px;
    padding-left: 14px;
    margin-left: 3px;
    border-left: 1px solid var(--border);
}

.avatar {
    width: 34px;
    height: 34px;
    border-radius: 50%;
    background: linear-gradient(145deg,#253b55,#0d1724);
    border: 1px solid rgba(255,255,255,.15);
    display: grid;
    place-items: center;
    font-size: 12px;
    font-weight: 600;
}

.commander-name {
    font-size: 12px;
    font-weight: 600;
}

.commander-role {
    font-size: 10px;
    color: var(--muted);
    margin-top: 2px;
}

/* ---------- STATUS CARDS ---------- */

.status-grid {
    display: grid;
    grid-template-columns: repeat(4,1fr);
    gap: 12px;
    margin-bottom: 17px;
}

.status-card {
    background: linear-gradient(145deg, rgba(14,21,32,.94), rgba(8,13,20,.94));
    border: 1px solid var(--border);
    border-radius: 11px;
    padding: 17px;
    position: relative;
    overflow: hidden;
}

.status-card::after {
    content: "";
    position: absolute;
    right: -20px;
    bottom: -30px;
    width: 80px;
    height: 80px;
    border-radius: 50%;
    background: var(--blue);
    opacity: .04;
    filter: blur(10px);
}

.status-label {
    color: #65748a;
    font-size: 10px;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.status-value {
    font-family: "Space Grotesk";
    font-size: 23px;
    margin-top: 9px;
}

.status-foot {
    margin-top: 7px;
    font-size: 10px;
    color: var(--muted);
}

.green { color: var(--green); }
.yellow { color: var(--yellow); }
.red { color: var(--red); }
.blue { color: var(--blue); }

/* ---------- GRID ---------- */

.dashboard-grid {
    display: grid;
    grid-template-columns: 1.55fr 1fr;
    gap: 15px;
}

.panel {
    background: linear-gradient(145deg, rgba(12,18,27,.96), rgba(8,12,19,.96));
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
}

.panel-header {
    padding: 15px 17px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid var(--border);
}

.panel-title {
    font-family: "Space Grotesk";
    font-size: 13px;
    letter-spacing: .3px;
}

.panel-meta {
    font-size: 10px;
    color: #58677b;
}

.panel-body {
    padding: 17px;
}

/* ---------- STATION MAP ---------- */

.station {
    height: 395px;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    background:
        radial-gradient(circle, rgba(77,163,255,.07), transparent 30%);
}

.station::before {
    content: "";
    position: absolute;
    width: 300px;
    height: 300px;
    border: 1px dashed rgba(77,163,255,.14);
    border-radius: 50%;
}

.station::after {
    content: "";
    position: absolute;
    width: 450px;
    height: 450px;
    border: 1px solid rgba(255,255,255,.025);
    border-radius: 50%;
}

.module {
    position: absolute;
    width: 112px;
    height: 66px;
    border: 1px solid rgba(255,255,255,.13);
    background: rgba(14,22,33,.96);
    border-radius: 9px;
    padding: 10px;
    cursor: pointer;
    z-index: 2;
    transition: .25s;
}

.module:hover {
    transform: scale(1.04);
    border-color: var(--cyan);
    box-shadow: 0 0 22px rgba(85,230,255,.08);
}

.module.science { top: 55px; left: 50%; transform: translateX(-50%); }
.module.engineering { left: 45px; top: 170px; }
.module.central { left: 50%; top: 164px; transform: translateX(-50%); width: 126px; height: 78px; border-color: rgba(85,230,255,.25); }
.module.life { right: 45px; top: 170px; }
.module.habitat { bottom: 53px; left: 50%; transform: translateX(-50%); }

.module:hover.science,
.module:hover.central,
.module:hover.habitat {
    transform: translateX(-50%) scale(1.04);
}

.module-name {
    font-size: 9px;
    color: #68788e;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.module-person {
    font-size: 11px;
    margin-top: 6px;
}

.module-status {
    font-size: 8px;
    margin-top: 4px;
    color: var(--green);
}

.connector {
    position: absolute;
    background: rgba(85,230,255,.15);
    z-index: 1;
}

.line-h {
    height: 1px;
}

.line-v {
    width: 1px;
}

.l1 { width: 110px; left: 155px; top: 202px; }
.l2 { width: 105px; right: 160px; top: 202px; }
.l3 { height: 72px; left: 50%; top: 113px; }
.l4 { height: 70px; left: 50%; bottom: 113px; }

.station-core {
    position: absolute;
    z-index: 3;
    color: var(--cyan);
    font-size: 8px;
    letter-spacing: 1px;
    top: 203px;
    left: 50%;
    transform: translateX(-50%);
}

/* ---------- RIGHT COLUMN ---------- */

.alert {
    padding: 14px;
    border: 1px solid rgba(255,95,109,.18);
    background: rgba(255,95,109,.035);
    border-radius: 9px;
    margin-bottom: 10px;
}

.alert.yellow-alert {
    border-color: rgba(244,201,93,.18);
    background: rgba(244,201,93,.025);
}

.alert-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.priority {
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 1px;
}

.alert-title {
    font-size: 12px;
    margin-top: 7px;
    font-weight: 600;
}

.alert-description {
    color: var(--muted);
    font-size: 10px;
    line-height: 1.5;
    margin-top: 5px;
}

.alert-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 12px;
}

.time {
    color: #8491a3;
    font-size: 9px;
}

.small-btn {
    background: rgba(255,255,255,.04);
    border: 1px solid var(--border);
    color: #cbd5e3;
    border-radius: 6px;
    padding: 6px 9px;
    font-size: 9px;
    cursor: pointer;
}

.small-btn:hover {
    background: rgba(255,255,255,.08);
}

/* ---------- CREW ---------- */

.crew-grid {
    display: grid;
    grid-template-columns: repeat(2,1fr);
    gap: 8px;
}

.crew-card {
    padding: 11px;
    border: 1px solid var(--border);
    border-radius: 8px;
    background: rgba(255,255,255,.015);
    cursor: pointer;
    transition: .2s;
}

.crew-card:hover {
    border-color: rgba(77,163,255,.35);
}

.crew-top {
    display: flex;
    justify-content: space-between;
}

.crew-name {
    font-size: 11px;
    font-weight: 600;
}

.crew-role {
    font-size: 8px;
    color: var(--muted);
    margin-top: 3px;
}

.status-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    margin-top: 3px;
}

.status-dot.green-dot { background: var(--green); box-shadow: 0 0 7px var(--green); }
.status-dot.yellow-dot { background: var(--yellow); }
.status-dot.blue-dot { background: var(--blue); }

.load {
    margin-top: 9px;
    height: 3px;
    background: #1c2532;
    border-radius: 5px;
    overflow: hidden;
}

.load-bar {
    height: 100%;
    border-radius: 5px;
    background: var(--blue);
}

.load-text {
    font-size: 8px;
    color: #637188;
    margin-top: 4px;
}

/* ---------- BOTTOM PANELS ---------- */

.bottom-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 15px;
    margin-top: 15px;
}

.activity {
    display: flex;
    gap: 11px;
    padding: 10px 0;
    border-bottom: 1px solid rgba(255,255,255,.04);
}

.activity:last-child {
    border-bottom: none;
}

.activity-dot {
    width: 7px;
    height: 7px;
    margin-top: 4px;
    border-radius: 50%;
    background: var(--blue);
}

.activity-main {
    font-size: 10px;
    color: #c3ccda;
}

.activity-time {
    font-size: 8px;
    color: #526177;
    margin-top: 3px;
}

/* ---------- CREW BALANCE ---------- */

.balance-row {
    margin-bottom: 14px;
}

.balance-head {
    display: flex;
    justify-content: space-between;
    font-size: 10px;
    margin-bottom: 6px;
}

.balance-head span:last-child {
    color: var(--muted);
}

.balance-track {
    height: 5px;
    background: #19222e;
    border-radius: 10px;
    overflow: hidden;
}

.balance-fill {
    height: 100%;
    border-radius: 10px;
}

/* ---------- MODAL ---------- */

.modal-backdrop {
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,.68);
    backdrop-filter: blur(8px);
    display: none;
    align-items: center;
    justify-content: center;
    z-index: 100;
}

.modal-backdrop.show {
    display: flex;
}

.modal {
    width: 510px;
    max-width: calc(100% - 30px);
    background: #0b111a;
    border: 1px solid rgba(255,255,255,.11);
    border-radius: 14px;
    box-shadow: 0 30px 100px rgba(0,0,0,.55);
    animation: modalIn .25s ease;
}

@keyframes modalIn {
    from { opacity: 0; transform: translateY(12px) scale(.98); }
    to { opacity: 1; transform: none; }
}

.modal-header {
    padding: 18px;
    border-bottom: 1px solid var(--border);
    display: flex;
    justify-content: space-between;
}

.close {
    color: #65748a;
    cursor: pointer;
    font-size: 18px;
}

.modal-body {
    padding: 20px;
}

.modal-title {
    font-family: "Space Grotesk";
    font-size: 19px;
}

.modal-sub {
    color: var(--muted);
    font-size: 10px;
    margin-top: 4px;
}

.modal-section {
    margin-top: 20px;
}

.modal-label {
    color: #627188;
    font-size: 9px;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    margin-bottom: 8px;
}

.option-grid {
    display: grid;
    grid-template-columns: repeat(2,1fr);
    gap: 8px;
}

.option {
    border: 1px solid var(--border);
    padding: 12px;
    border-radius: 8px;
    cursor: pointer;
    background: rgba(255,255,255,.02);
}

.option:hover {
    border-color: var(--blue);
}

.option strong {
    display: block;
    font-size: 11px;
}

.option span {
    display: block;
    color: var(--muted);
    font-size: 9px;
    margin-top: 4px;
}

.modal-actions {
    margin-top: 22px;
    display: flex;
    justify-content: flex-end;
    gap: 8px;
}

.primary-btn {
    background: var(--blue);
    border: none;
    color: #06101b;
    font-weight: 700;
    padding: 9px 15px;
    border-radius: 7px;
    cursor: pointer;
    font-size: 10px;
}

.secondary-btn {
    background: transparent;
    border: 1px solid var(--border);
    color: #aab5c4;
    padding: 9px 15px;
    border-radius: 7px;
    cursor: pointer;
    font-size: 10px;
}

/* ---------- TOAST ---------- */

.toast {
    position: fixed;
    right: 25px;
    bottom: 25px;
    background: #101923;
    border: 1px solid rgba(85,230,255,.2);
    padding: 13px 16px;
    border-radius: 8px;
    font-size: 10px;
    color: #d6e1ed;
    opacity: 0;
    transform: translateY(10px);
    pointer-events: none;
    transition: .25s;
    z-index: 200;
}

.toast.show {
    opacity: 1;
    transform: none;
}

/* ---------- RESPONSIVE ---------- */

@media(max-width:1000px) {
    .sidebar {
        width: 75px;
    }

    .logo h1,
    .nav-label,
    .nav-item span:not(.nav-icon),
    .connection {
        display: none;
    }

    .logo {
        justify-content: center;
    }

    .nav-item {
        justify-content: center;
    }

    .main {
        margin-left: 75px;
        width: calc(100% - 75px);
    }

    .status-grid {
        grid-template-columns: repeat(2,1fr);
    }

    .dashboard-grid,
    .bottom-grid {
        grid-template-columns: 1fr;
    }
}

@media(max-width:650px) {
    .main {
        padding: 20px 15px;
    }

    .status-grid {
        grid-template-columns: 1fr 1fr;
    }

    .commander {
        display: none;
    }

    .station {
        transform: scale(.85);
        transform-origin: center;
    }
}
</style>
</head>

<body>

<div class="app">

<!-- ================= SIDEBAR ================= -->

<aside class="sidebar">

    <div class="logo">
        <div class="logo-mark"></div>
        <h1>OR<span>BIT</span></h1>
    </div>

    <div class="nav-label">Operations</div>

    <div class="nav-item active" onclick="setActive(this)">
        <span class="nav-icon">◈</span>
        <span>Command Center</span>
    </div>

    <div class="nav-item" onclick="showToast('Crew management module opened')">
        <span class="nav-icon">◉</span>
        <span>Crew</span>
    </div>

    <div class="nav-item" onclick="showToast('Station map opened')">
        <span class="nav-icon">⌘</span>
        <span>Station</span>
    </div>

    <div class="nav-item" onclick="showToast('Schedule synchronized')">
        <span class="nav-icon">◷</span>
        <span>Schedule</span>
    </div>

    <div class="nav-label">Coordination</div>

    <div class="nav-item" onclick="openMediation()">
        <span class="nav-icon">⇄</span>
        <span>Mediation</span>
    </div>

    <div class="nav-item" onclick="openEarth()">
        <span class="nav-icon">⊕</span>
        <span>Earth Link</span>
    </div>

    <div class="nav-item" onclick="showToast('Quiet Orbit protection active')">
        <span class="nav-icon">◌</span>
        <span>Quiet Orbit</span>
    </div>

    <div class="nav-label">System</div>

    <div class="nav-item" onclick="showToast('Activity log opened')">
        <span class="nav-icon">≡</span>
        <span>Activity Log</span>
    </div>

    <div class="sidebar-bottom">
        <div class="connection">
            <div class="connection-title">
                <span>EARTH LINK</span>
                <span class="live">LIVE</span>
            </div>
            <div style="font-size:9px;color:#536176">
                Latency 0.8 sec
            </div>
        </div>
    </div>

</aside>


<!-- ================= MAIN ================= -->

<main class="main">

<header class="topbar">

    <div>
        <div class="eyebrow">Mission 07 · Climate Monitoring</div>
        <div class="title">Command Center</div>
        <div class="subtitle">
            Orbital Crew Operations & Coordination System
        </div>
    </div>

    <div class="top-actions">

        <button class="icon-button"
                onclick="openEmergency()"
                title="Emergency">
            !
        </button>

        <button class="icon-button"
                onclick="openEarth()"
                title="Earth Link">
            ⊕
        </button>

        <div class="commander">
            <div class="avatar">CM</div>
            <div>
                <div class="commander-name">Commander</div>
                <div class="commander-role">Primary authority · ONLINE</div>
            </div>
        </div>

    </div>

</header>


<!-- ================= STATUS ================= -->

<section class="status-grid">

    <div class="status-card">
        <div class="status-label">Station</div>
        <div class="status-value green">NOMINAL</div>
        <div class="status-foot">All systems operational</div>
    </div>

    <div class="status-card">
        <div class="status-label">Earth Link</div>
        <div class="status-value green">ACTIVE</div>
        <div class="status-foot">0.8 sec communication latency</div>
    </div>

    <div class="status-card">
        <div class="status-label">Crew</div>
        <div class="status-value">08 / 08</div>
        <div class="status-foot">4 working · 2 rest · 2 available</div>
    </div>

    <div class="status-card">
        <div class="status-label">Attention</div>
        <div class="status-value yellow">03</div>
        <div class="status-foot">1 critical · 1 mediation · 1 request</div>
    </div>

</section>


<!-- ================= MAIN GRID ================= -->

<section class="dashboard-grid">

<!-- STATION -->

<div class="panel">

    <div class="panel-header">
        <div class="panel-title">Station Architecture</div>
        <div class="panel-meta">ORBITAL MODULE VIEW · LIVE</div>
    </div>

    <div class="station">

        <div class="connector line-h l1"></div>
        <div class="connector line-h l2"></div>
        <div class="connector line-v l3"></div>
        <div class="connector line-v l4"></div>

        <div class="module science"
             onclick="openCrew('Dr. Smirnova','Climate Scientist','EXPERIMENT','63%')">
            <div class="module-name">Science</div>
            <div class="module-person">S. Smirnova</div>
            <div class="module-status">● EXPERIMENT</div>
        </div>

        <div class="module engineering"
             onclick="openCrew('A. Ivanov','Systems Engineer','WORKING','81%')">
            <div class="module-name">Engineering</div>
            <div class="module-person">A. Ivanov</div>
            <div class="module-status">● WORKING</div>
        </div>

        <div class="module central">
            <div class="module-name">Central Hub</div>
            <div class="module-person">COMMAND</div>
            <div class="module-status">● NOMINAL</div>
        </div>

        <div class="module life"
             onclick="openCrew('D. Kim','Life Support','MAINTENANCE','42%')">
            <div class="module-name">Life Support</div>
            <div class="module-person">D. Kim</div>
            <div class="module-status">● MAINTENANCE</div>
        </div>

        <div class="module habitat"
             onclick="openCrew('M. Orlova','Flight Specialist','AVAILABLE','51%')">
            <div class="module-name">Habitat</div>
            <div class="module-person">M. Orlova</div>
            <div class="module-status">● AVAILABLE</div>
        </div>

        <div class="station-core">ORBIT CORE</div>

    </div>

</div>


<!-- ALERTS -->

<div class="panel">

    <div class="panel-header">
        <div class="panel-title">Attention Queue</div>
        <div class="panel-meta">3 ACTIVE</div>
    </div>

    <div class="panel-body">

        <div class="alert">

            <div class="alert-top">
                <span class="priority red">P1 · CRITICAL</span>
                <span class="time">18 MIN</span>
            </div>

            <div class="alert-title">
                Life Support Valve Inspection
            </div>

            <div class="alert-description">
                Engineering action required before system maintenance window closes.
            </div>

            <div class="alert-footer">
                <span class="time">Assigned: A. Ivanov</span>
                <button class="small-btn"
                        onclick="showToast('Critical task opened')">
                    Open
                </button>
            </div>

        </div>


        <div class="alert yellow-alert">

            <div class="alert-top">
                <span class="priority yellow">MEDIATION</span>
                <span class="time">34 MIN</span>
            </div>

            <div class="alert-title">
                Experiment vs. Maintenance
            </div>

            <div class="alert-description">
                Science and Engineering have conflicting operational priorities.
            </div>

            <div class="alert-footer">
                <span class="time">2 participants</span>
                <button class="small-btn"
                        onclick="openMediation()">
                    Mediate
                </button>
            </div>

        </div>


        <div class="alert">

            <div class="alert-top">
                <span class="priority blue">P2 · REQUEST</span>
                <span class="time">09 MIN</span>
            </div>

            <div class="alert-title">
                Climate Sensor Data Review
            </div>

            <div class="alert-description">
                Science module requested engineering support.
            </div>

            <div class="alert-footer">
                <span class="time">Requester: S. Smirnova</span>
                <button class="small-btn"
                        onclick="showToast('Request assigned to available specialist')">
                    Assign
                </button>
            </div>

        </div>

    </div>

</div>

</section>


<!-- ================= CREW ================= -->

<section class="panel" style="margin-top:15px">

    <div class="panel-header">
        <div class="panel-title">Crew Status</div>
        <div class="panel-meta">REAL-TIME AVAILABILITY</div>
    </div>

    <div class="panel-body">

        <div class="crew-grid">

            <div class="crew-card"
                 onclick="openCrew('A. Ivanov','Systems Engineer','WORKING','81%')">
                <div class="crew-top">
                    <div>
                        <div class="crew-name">A. Ivanov</div>
                        <div class="crew-role">Systems Engineer</div>
                    </div>
                    <div class="status-dot green-dot"></div>
                </div>
                <div class="load">
                    <div class="load-bar" style="width:81%"></div>
                </div>
                <div class="load-text">WORK · load 81%</div>
            </div>


            <div class="crew-card"
                 onclick="openCrew('S. Smirnova','Climate Scientist','EXPERIMENT','63%')">
                <div class="crew-top">
                    <div>
                        <div class="crew-name">S. Smirnova</div>
                        <div class="crew-role">Climate Scientist</div>
                    </div>
                    <div class="status-dot blue-dot"></div>
                </div>
                <div class="load">
                    <div class="load-bar" style="width:63%"></div>
                </div>
                <div class="load-text">EXPERIMENT · load 63%</div>
            </div>


            <div class="crew-card"
                 onclick="openCrew('D. Kim','Life Support','MAINTENANCE','42%')">
                <div class="crew-top">
                    <div>
                        <div class="crew-name">D. Kim</div>
                        <div class="crew-role">Life Support</div>
                    </div>
                    <div class="status-dot yellow-dot"></div>
                </div>
                <div class="load">
                    <div class="load-bar" style="width:42%"></div>
                </div>
                <div class="load-text">MAINTENANCE · load 42%</div>
            </div>


            <div class="crew-card"
                 onclick="openCrew('M. Orlova','Flight Specialist','AVAILABLE','51%')">
                <div class="crew-top">
                    <div>
                        <div class="crew-name">M. Orlova</div>
                        <div class="crew-role">Flight Specialist</div>
                    </div>
                    <div class="status-dot green-dot"></div>
                </div>
                <div class="load">
                    <div class="load-bar" style="width:51%"></div>
                </div>
                <div class="load-text">AVAILABLE · load 51%</div>
            </div>

        </div>

    </div>

</section>


<!-- ================= BOTTOM ================= -->

<section class="bottom-grid">


<div class="panel">

    <div class="panel-header">
        <div class="panel-title">Crew Balance</div>
        <div class="panel-meta">COGNITIVE LOAD</div>
    </div>

    <div class="panel-body">

        <div class="balance-row">
            <div class="balance-head">
                <span>A. Ivanov</span>
                <span>81%</span>
            </div>
            <div class="balance-track">
                <div class="balance-fill"
                     style="width:81%;background:var(--red)"></div>
            </div>
        </div>

        <div class="balance-row">
            <div class="balance-head">
                <span>S. Smirnova</span>
                <span>63%</span>
            </div>
            <div class="balance-track">
                <div class="balance-fill"
                     style="width:63%;background:var(--yellow)"></div>
            </div>
        </div>

        <div class="balance-row">
            <div class="balance-head">
                <span>M. Orlova</span>
                <span>51%</span>
            </div>
            <div class="balance-track">
                <div class="balance-fill"
                     style="width:51%;background:var(--blue)"></div>
            </div>
        </div>

        <div class="balance-row" style="margin-bottom:0">
            <div class="balance-head">
                <span>D. Kim</span>
                <span>42%</span>
            </div>
            <div class="balance-track">
                <div class="balance-fill"
                     style="width:42%;background:var(--green)"></div>
            </div>
        </div>

    </div>

</div>


<div class="panel">

    <div class="panel-header">
        <div class="panel-title">Activity Log</div>
        <div class="panel-meta">LAST 4 EVENTS</div>
    </div>

    <div class="panel-body">

        <div class="activity">
            <div class="activity-dot"></div>
            <div>
                <div class="activity-main">
                    Earth Link synchronized with Climate Lab.
                </div>
                <div class="activity-time">14:32 · SYSTEM</div>
            </div>
        </div>

        <div class="activity">
            <div class="activity-dot"></div>
            <div>
                <div class="activity-main">
                    S. Smirnova requested engineering support.
                </div>
                <div class="activity-time">14:27 · SCIENCE</div>
            </div>
        </div>

        <div class="activity">
            <div class="activity-dot"></div>
            <div>
                <div class="activity-main">
                    Quiet Orbit protected D. Kim's rest period.
                </div>
                <div class="activity-time">14:18 · SYSTEM</div>
            </div>
        </div>

        <div class="activity">
            <div class="activity-dot"></div>
            <div>
                <div class="activity-main">
                    Mediation protocol initiated.
                </div>
                <div class="activity-time">14:11 · COMMAND</div>
            </div>
        </div>

    </div>

</div>

</section>

</main>

</div>


<!-- ================= MODAL ================= -->

<div class="modal-backdrop" id="modalBackdrop">

    <div class="modal">

        <div class="modal-header">
            <div>
                <div class="modal-title" id="modalTitle">
                    ORBIT
                </div>
                <div class="modal-sub" id="modalSubtitle">
                    Operational interface
                </div>
            </div>

            <div class="close" onclick="closeModal()">×</div>
        </div>

        <div class="modal-body" id="modalBody"></div>

    </div>

</div>


<div class="toast" id="toast"></div>


<script>

/* ================= BASIC UI ================= */

function setActive(element) {
    document.querySelectorAll('.nav-item')
        .forEach(item => item.classList.remove('active'));

    element.classList.add('active');
}


/* ================= MODAL ================= */

function openModal(title, subtitle, body) {

    document.getElementById('modalTitle').innerText = title;
    document.getElementById('modalSubtitle').innerText = subtitle;
    document.getElementById('modalBody').innerHTML = body;

    document.getElementById('modalBackdrop')
        .classList.add('show');
}

function closeModal() {
    document.getElementById('modalBackdrop')
        .classList.remove('show');
}


/* ================= CREW ================= */

function openCrew(name, role, status, load) {

    openModal(
        name,
        role + ' · ' + status,
        `
        <div class="modal-section">
            <div class="modal-label">Current status</div>

            <div style="
                padding:14px;
                border:1px solid var(--border);
                border-radius:8px;
                background:rgba(255,255,255,.02)
            ">
                <strong style="font-size:13px">${status}</strong>

                <div style="
                    color:var(--muted);
                    font-size:10px;
                    margin-top:6px
                ">
                    Cognitive load: ${load}
                </div>
            </div>
        </div>

        <div class="modal-section">
            <div class="modal-label">Communication</div>

            <div class="option-grid">

                <div class="option"
                     onclick="showToast('Message prepared for ${name}')">
                    <strong>Message</strong>
                    <span>Asynchronous communication</span>
                </div>

                <div class="option"
                     onclick="showToast('Call request sent to ${name}')">
                    <strong>Call</strong>
                    <span>Real-time communication</span>
                </div>

                <div class="option"
                     onclick="showToast('Task request created')">
                    <strong>Request</strong>
                    <span>Assign operational task</span>
                </div>

                <div class="option"
                     onclick="openEmergency()">
                    <strong style="color:var(--red)">
                        Emergency
                    </strong>
                    <span>Interrupt protocol</span>
                </div>

            </div>
        </div>

        <div class="modal-section">

            <div class="modal-label">Availability rule</div>

            <div style="
                font-size:10px;
                line-height:1.6;
                color:#8794a8
            ">
                ORBIT automatically evaluates workload,
                current activity and protected rest periods
                before delivering a non-critical request.
            </div>

        </div>
        `
    );
}


/* ================= MEDIATION ================= */

function openMediation() {

    openModal(
        'Mediation Protocol',
        'SCIENCE ↔ ENGINEERING · PENDING',
        `
        <div class="modal-section">

            <div class="modal-label">Conflict</div>

            <div style="
                padding:14px;
                border:1px solid rgba(244,201,93,.18);
                background:rgba(244,201,93,.025);
                border-radius:8px
            ">

                <div style="font-size:12px;font-weight:600">
                    Experiment vs. Maintenance
                </div>

                <div style="
                    color:var(--muted);
                    font-size:10px;
                    margin-top:7px;
                    line-height:1.5
                ">
                    Engineering requires a temporary shutdown.
                    Science reports that the shutdown may invalidate
                    the current climate experiment.
                </div>

            </div>

        </div>

        <div class="modal-section">

            <div class="modal-label">
                ORBIT decision sequence
            </div>

            <div style="display:grid;gap:7px">

                <div class="option">
                    <strong>01 · Define</strong>
                    <span>Identify the shared operational problem.</span>
                </div>

                <div class="option">
                    <strong>02 · Compare</strong>
                    <span>Evaluate risks and mission impact.</span>
                </div>

                <div class="option">
                    <strong>03 · Propose</strong>
                    <span>Generate alternatives.</span>
                </div>

                <div class="option">
                    <strong>04 · Resolve</strong>
                    <span>Reach agreement or escalate.</span>
                </div>

            </div>

        </div>

        <div class="modal-actions">

            <button class="secondary-btn"
                    onclick="showToast('Conflict escalated to Commander')">
                Escalate
            </button>

            <button class="primary-btn"
                    onclick="showToast('Mediation agreement recorded')">
                Record Agreement
            </button>

        </div>
        `
    );
}


/* ================= EARTH ================= */

function openEarth() {

    openModal(
        'Earth Link',
        'GROUND COMMUNICATION NETWORK · ACTIVE',
        `
        <div class="modal-section">

            <div style="
                display:flex;
                justify-content:space-between;
                align-items:center;
                padding:15px;
                border:1px solid rgba(77,225,161,.15);
                border-radius:8px;
                background:rgba(77,225,161,.025)
            ">

                <div>
                    <div style="font-size:12px;font-weight:600">
                        Ground Network
                    </div>

                    <div style="
                        color:var(--muted);
                        font-size:9px;
                        margin-top:4px
                    ">
                        Climate Research Coordination Center
                    </div>
                </div>

                <div class="live">
                    ONLINE
                </div>

            </div>

        </div>

        <div class="modal-section">

            <div class="modal-label">
                Direct specialist channels
            </div>

            <div class="option-grid">

                <div class="option"
                     onclick="showToast('Science channel connected')">
                    <strong>Science</strong>
                    <span>Climate Research Team</span>
                </div>

                <div class="option"
                     onclick="showToast('Engineering channel connected')">
                    <strong>Engineering</strong>
                    <span>Systems Ground Team</span>
                </div>

                <div class="option"
                     onclick="showToast('Medical channel connected')">
                    <strong>Medical</strong>
                    <span>Ground Medical Officer</span>
                </div>

                <div class="option"
                     onclick="showToast('Commander channel connected')">
                    <strong>Command</strong>
                    <span>Mission Control</span>
                </div>

            </div>

        </div>

        <div class="modal-section">

            <div class="modal-label">
                Communication principle
            </div>

            <div style="
                color:#8794a8;
                font-size:10px;
                line-height:1.7
            ">
                ORBIT removes unnecessary communication bottlenecks:
                specialists may contact the appropriate Earth team
                directly while mission-critical decisions remain
                visible to command.
            </div>

        </div>
        `
    );
}


/* ================= EMERGENCY ================= */

function openEmergency() {

    openModal(
        'Emergency Protocol',
        'P0 · LIFE / STATION SAFETY',
        `
        <div style="
            padding:16px;
            border:1px solid rgba(255,95,109,.25);
            background:rgba(255,95,109,.035);
            border-radius:8px
        ">

            <div style="
                color:var(--red);
                font-size:10px;
                font-weight:700;
                letter-spacing:1px
            ">
                EMERGENCY CHANNEL
            </div>

            <div style="
                font-size:16px;
                margin-top:8px;
                font-family:'Space Grotesk'
            ">
                Immediate crew interruption
            </div>

            <div style="
                color:var(--muted);
                font-size:10px;
                line-height:1.6;
                margin-top:7px
            ">
                This protocol overrides Quiet Orbit and protected
                rest periods when life or station safety is at risk.
            </div>

        </div>

        <div class="modal-actions">

            <button class="secondary-btn"
                    onclick="closeModal()">
                Cancel
            </button>

            <button class="primary-btn"
                    style="background:var(--red);color:white"
                    onclick="
                        closeModal();
                        showToast('Emergency protocol activated — crew notified');
                    ">
                ACTIVATE P0
            </button>

        </div>
        `
    );
}


/* ================= TOAST ================= */

let toastTimer;

function showToast(message) {

    const toast = document.getElementById('toast');

    toast.innerText = message;

    toast.classList.add('show');

    clearTimeout(toastTimer);

    toastTimer = setTimeout(() => {
        toast.classList.remove('show');
    }, 2800);
}


/* ================= BACKDROP ================= */

document.getElementById('modalBackdrop')
    .addEventListener('click', function(e) {

        if (e.target === this) {
            closeModal();
        }

    });

</script>

</body>
</html>
