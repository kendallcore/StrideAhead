# Step 6: Don't Start With Technology — Problem First, Technology Later

---

## 1. Core Design Principle

> **"Screen everyone cheaply at the village level; confirm precisely at the district level."**

Technology is an enabler, not the starting point. We design the system around the existing healthcare workflow in India:
`ASHA Worker → Village HWC → PHC → District Hospital`

---

## 2. Two-Tier System Architecture

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

## 3. Technology Stack Choice Driven by Constraints

| Constraint | Solution Chosen | Why? |
|---|---|---|
| **No Internet in Village** | **Offline-First PWA + SQLite/IndexedDB** | Runs 100% offline; queues sync records when signal is available. |
| **Low-End Android Hardware** | **Quantized ONNX / TFLite Models** | Executes in <50 ms on 2GB RAM Android tablets. |
| **Language & Literacy Barrier** | **Voice-First UI (Sarvam TTS integration pattern)** | Spoken instructions in Assamese, Bengali, Manipuri, and Nagamese. |
| **No Radiologist at Village** | **Automated KL Grading at District Hospital** | Converts 15-minute radiologist inspection into a 10-second verification. |
| **Affordability Requirement** | **Commodity Hardware & Open-Source Pipeline** | Hardware kit total ₹1,200; per-test cost ≈ ₹25–45. |

---

## 4. End-to-End ASHA Field Workflow (<8 Minutes)

1. **Step 1 — Setup (<1 min)**: ASHA worker places the lightweight IMU band above the patient's ankle or opens the guided AR camera overlay.
2. **Step 2 — Voice Instructions (<1 min)**: App speaks instructions in the local dialect ("Please walk 20 meters straight and sit back down").
3. **Step 3 — Test Execution (2 mins)**: Patient completes 20m walk + Timed-Up-and-Go (TUG) sequence.
4. **Step 4 — Instant Risk Result (30 secs)**: App generates an interpretable score (Low / Watch / Refer) with explicit breakdown ("Right stance phase 14% shorter").
5. **Step 5 — Referral Slip Generation (1 min)**: If risk is high, auto-generates a referral QR code/slip for the District Hospital Tier 1 X-ray confirmation.
