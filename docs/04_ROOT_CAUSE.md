# Step 4: Find the Root Cause — Don't Solve Just the Symptom

---

## 1. Symptom vs. Root Cause Analysis

> **Symptom**: Patients in the North Eastern Region present at district hospitals with severe, irreversible late-stage Osteoarthritis (KL Grade 3/4) requiring surgery.

| Level | Finding |
|---|---|
| **Surface Level (Symptom)** | Knee joint pain is ignored until the patient can no longer walk. |
| **Intermediate Level** | Rural health centres (PHCs/HWCs) lack diagnostic equipment and specialists. |
| **Systemic Level** | X-rays are only ordered when pain is acute; early functional micro-instability goes unnoticed. |
| **ROOT CAUSE** | **Lack of an early, sub-clinical screening threshold at the village level** paired with **geographical and financial barriers to hospital visits**. |

---

## 2. Root Cause Diagram

```
                    Late Presentation (KL 3/4 Surgery Required)
                                      ▲
                                      │
                   ┌──────────────────┴──────────────────┐
                   │                                     │
    Financial & Geographical Friction           Absence of Village Screening
    - Travel cost to district hospital          - No objective risk markers
    - Wage loss during travel days             - ASHA workers lack tools
    - Ignored as "normal aging pain"            - Asymptomatic cartilage loss
                   │                                     │
                   └──────────────────┬──────────────────┘
                                      │
                                  ROOT CAUSE
             "No early, non-invasive risk detection mechanism exists 
               where people live, leading to late-stage discovery."
```

---

## 3. Why Technology Alone Doesn't Fix the Root Cause

Building a fancy 3D deep learning model or buying expensive MRI scanners does **not** solve the root cause because:
1. **Access Friction Remains**: Patients still won't travel 50 km for early, mild stiffness.
2. **Infrastructure Deficit**: Small PHCs cannot afford ₹50 Lakh diagnostic setups.
3. **Specialist Bottleneck**: Radiologists will still be overburdened.

### The True Root-Cause Solution: StrideAhead Philosophy
To solve the root cause, we must **decouple screening from hospital infrastructure**:
- **Screen everyone cheaply at the village level** (using accessible mobile devices & low-cost sensors operated by ASHA workers).
- **Confirm precisely at the district level** (using automated X-ray KL auto-grading nodes at district hospitals).
- **Only flag and transport individuals with true risk**, eliminating unnecessary travel and ensuring early intervention (KL 1/2).
