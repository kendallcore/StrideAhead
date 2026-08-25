# StrideAhead 🏃‍♀️🦵

> **Two-Tier AI Platform for Early Osteoarthritis Detection in the North Eastern Region (NER)**  
> **Official Implementation for Smart India Hackathon (SIH) 2026 — Problem Statement PS 26004**  
> **Nodal Organization**: Ministry of Development of North Eastern Region (MDoNER)  

---

## 📌 Project Overview

**StrideAhead** (formerly SetuJoint) is an offline-first, two-tier AI screening and referral platform designed to tackle the high prevalence of knee Osteoarthritis (OA) in remote and agricultural communities across North Eastern India.

By pairing **Tier 2 low-cost mobile/IMU gait screening** at the village level with **Tier 1 automated X-ray Kellgren-Lawrence (KL 0–4) grading** at district hospitals, StrideAhead creates a non-invasive referral funnel that detects cartilage loss **5 years before** irreversible joint destruction occurs.

---

## 🧭 Repository Navigation & 6-Step Solution Framework

This repository is structured according to the **6-Step Problem Solving & Presentation Framework**:

```
StrideAhead/
├── README.md                          # Master Overview & Project Navigation
├── docs/                              # Detailed Documentation & SIH Submission Materials
│   ├── 01_PROBLEM_UNDERSTANDING.md    # [Step 1] Who, What & Why? (Epidemiology, NER context)
│   ├── 02_EXISTING_SOLUTIONS.md       # [Step 2] Know What Already Exists (X-ray DL & Gait Lit)
│   ├── 03_GAP_ANALYSIS.md             # [Step 3] What is Still Missing? (5 Structural Gaps)
│   ├── 04_ROOT_CAUSE.md               # [Step 4] Root Cause Analysis & Symptom Tree
│   ├── 05_PS_SCORING.md               # [Step 5] Impact, Innovation, Feasibility, Data & Scalability
│   ├── 06_PROBLEM_FIRST_TECH_LATER.md # [Step 6] Architecture & Tech Stack Selection
│   ├── COST_ANALYSIS_AND_BOM.md       # Hardware BOM (₹900 kit) & ₹25–45 per test economics
│   └── SIH_2026_PS26004_PROPOSAL.md   # Official SIH 2026 Hackathon Executive Proposal
├── src/                               # Working Prototype Source Code
│   ├── tier2_gait/                    # Village-level Gait Analysis Engine
│   │   └── gait_analyzer.py
│   ├── risk_engine/                   # Explainable Triage & Risk Matrix
│   │   └── triage_engine.py
│   ├── tier1_xray/                    # District-level X-Ray KL Auto-Grader
│   │   └── kl_grader.py
│   └── main.py                        # Complete End-to-End Simulation Runner
├── tests/                             # Automated Unit Test Suite
│   └── test_stride_ahead.py
└── requirements.txt                   # Project Dependencies
```

---

## 📑 The 6-Step Solution Breakdown

### [1. Understand the Problem — Who, What & Why?](docs/01_PROBLEM_UNDERSTANDING.md)
- **Who**: 29.4% of rural tea-garden workers and elderly adults in NER, disproportionately affecting women (>50.7% prevalence at age 60+).
- **What**: Irreversible degeneration of knee cartilage causing chronic pain, joint space narrowing, and severe mobility loss.
- **Why**: Hilly terrain and heavy manual labor strain knee joints; remote geography prevents timely visits to distant urban hospitals.

---

### [2. Research Existing Solutions — Know What Already Exists](docs/02_EXISTING_SOLUTIONS.md)
- **Clinical Standard**: Kellgren-Lawrence (KL 0–4) grading on weight-bearing X-rays + WOMAC questionnaires.
- **Academic AI Models**: Open-source X-ray CNN models (`DeepKnee`, `OAProgression`, `KNEEL`) for high-compute desktop environments.
- **Gait Research**: Lab-grade accelerometry and pedobarography (eLife 2024 vGRF insoles, UK Biobank accelerometry).

---

### [3. Find the GAP — What is Still Missing?](docs/03_GAP_ANALYSIS.md)
- **Zero NER-specific repositories**: No open-source project targets PS 26004 or rural Indian field deployment.
- **Siloed Technologies**: Hospital X-ray AI and lab gait analysis operate in silos with no connecting referral funnel.
- **Cost Barrier**: Commercial gait insoles (€1,000+) are unaffordable for rural public healthcare.

---

### [4. Find the Root Cause — Don't Solve Just the Symptom](docs/04_ROOT_CAUSE.md)
- **Root Cause**: Lack of an early, non-invasive risk detection mechanism where people live, combined with travel and financial friction.
- **Strategy**: Decouple screening from hospital infrastructure. Screen at the village; confirm at the district.

---

### [5. Score the PS — Impact, Innovation, Feasibility, Data & Scalability](docs/05_PS_SCORING.md)
- **Impact (10/10)**: Prevents permanent disability and saves rural families ₹1.5–2.5 Lakh per surgery.
- **Innovation (9.5/10)**: First two-tier multimodal funnel linking mobile gait metrics to X-ray AI.
- **Feasibility (9.5/10)**: Runs 100% offline on standard 2GB RAM ASHA Android tablets.
- **Data (9/10)**: Trained on OAI (4,800+ patients) & MOST (3,000+ patients) public benchmarks.
- **Scalability (10/10)**: Marginal screening cost of **₹25–45 per test**.

---

### [6. Don't Start With Technology — Problem First, Technology Later](docs/06_PROBLEM_FIRST_TECH_LATER.md)

```
========================================================================================
                          VILLAGE SCREENING LAYER (TIER 2)
========================================================================================
  [ ASHA Worker ] + [ Smartphone Camera / Low-Cost IMU Band (₹900) ]
        │
        ▼
  [ StrideAhead PWA ] (Offline-First, Edge AI)
   ├── 20m Walk & Timed-Up-and-Go (TUG) Capture
   ├── Local Gait Kinematics Engine (Cadence, Symmetry Index, Gait Speed)
   └── Deterministic Explainable Risk Score (LOW / WATCH / REFER)
        │
        ▼ (Only Flagged Positive Cases ~15-20% Travel)
========================================================================================
                         DISTRICT CONFIRMATION LAYER (TIER 1)
========================================================================================
  [ District Hospital X-Ray Machine ]
        │
        ▼
  [ StrideAhead Tier 1 Node ] (Runs CPU-Only on Existing Hospital Workstation)
   ├── KNEEL Hourglass Joint Localization & Crop
   ├── ResNet/DenseNet Kellgren-Lawrence (KL 0-4) Classification Head
   ├── Joint Space Width (JSW in mm) Regression Head
   └── Heatmap Overlay & Radiologist Verification Portal
```

---

## 💡 Quick Start & Local Execution

### 1. Execute End-to-End Simulation
```bash
python3 -m src.main
```

### 2. Run Automated Unit Tests
```bash
python3 -m unittest discover -s tests
```

---

## 💰 Cost & Deployment Snapshot
- **DIY Hardware BOM**: **~₹900 – ₹1,600** per IMU unit (vs ₹90,000+ commercial insoles).
- **Kit Cost per ASHA**: **₹10,000 – ₹13,000** (serves ~1,000 adults / year).
- **Per-Test Cost**: **₹25 – ₹45** (underwritten via NHM / MDoNER budget).

---

## 📜 References & Citation
1. Jorhat (Assam) Tea-Garden Knee OA Epidemiological Study (2019–2020).
2. India Elderly Knee OA Meta-Analysis (PMC12178484).
3. eLife 2024: Pedobarographic vertical GRF early OA detection (auROC 0.98).
4. UK Biobank Accelerometry Study (2026): Early KOA movement signatures.
5. Osteoarthritis Initiative (OAI) & MOST Radiographic Datasets.
