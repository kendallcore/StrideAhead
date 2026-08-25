# Step 5: Score the PS — Impact, Innovation, Feasibility, Data & Scalability

---

## 1. Problem Statement Evaluation Matrix

| Criterion | Evaluation & Score (1–10) | Detailed Justification |
|---|---|---|
| **Impact** | **10 / 10** | • Prevents irreversible disability for millions in rural NER.<br>• Catches OA at KL Grade 1/2 when conservative therapy works.<br>• Reduces out-of-pocket medical expenditure by up to **₹2 Lakh per family** (cost of joint replacement). |
| **Innovation** | **9.5 / 10** | • First **two-tier multimodal referral funnel** linking mobile gait metrics to X-ray AI.<br>• Ultra-low-cost hardware alternative (₹900 DIY IMU vs €1,000 commercial insoles).<br>• Uses **Gramian Angular Field (GAF)** transform to turn IMU time-series into 2D edge-AI vision inputs. |
| **Feasibility** | **9.5 / 10** | • Operates on **existing ASHA Android tablets** (2GB RAM) without requiring internet.<br>• Zero new hospital hardware: Tier 1 runs CPU-only on existing district X-ray PCs.<br>• Short ASHA training workflow (<8 minutes end-to-end test). |
| **Data Strategy** | **9.0 / 10** | • Pre-trained on massive public benchmarks (**OAI: 4,800+ patients**, **MOST: 3,000+ patients**, UK Biobank accelerometry).<br>• Local transfer learning pipeline designed for NER regional medical college validation cohorts. |
| **Scalability** | **10 / 10** | • Highly scalable across 150+ districts in North Eastern states.<br>• Marginal screening cost of **₹25–45 per test**.<br>• ABDM-ready integration pattern matching national digital health standards. |

---

## 2. Quantitative Impact Projection

```
┌────────────────────────────────────────────────────────────────────────┐
│                        PROPOSED DEPLOYMENT (1 DISTRICT)                 │
├───────────────────────────────────────┬────────────────────────────────┤
│ Target Population Screened            │ 150,000 adults / year          │
│ ASHA Deployment Kits (150 ASHA blocks)│ ₹15 - 20 Lakh total setup      │
│ Expected Early Detection (KL 1/2)     │ ~15,000 - 22,500 individuals   │
│ Prevented Late-Stage Surgeries        │ ~3,000 cases / 5 years         │
│ Direct Family Savings                 │ ₹45 - 75 Crore cumulative      │
└───────────────────────────────────────┴────────────────────────────────┘
```

---

## 3. Risk Assessment & Mitigation

| Potential Risk | Severity | Mitigation Strategy |
|---|---|---|
| **Gait signal non-specificity** (neuropathy, age, obesity) | Medium | Mobile test acts strictly as a **risk stratification flag**, never a definitive medical diagnosis. Tier 1 X-ray always confirms. |
| **Hardware durability in humid/hilly NER environment** | Low | IP67 3D-printed enclosure pouches, modular plug-and-play sensors (₹300 replacement cost). |
| **ASHA worker technology adoption barrier** | Medium | Multi-lingual voice coaching (Assamese, Bengali, Manipuri), single-button interface, offline voice feedback. |
| **Internet disconnection in remote villages** | Low | **100% offline-first architecture** with SQLite / IndexedDB sync queues that auto-upload when near cellular signal. |
