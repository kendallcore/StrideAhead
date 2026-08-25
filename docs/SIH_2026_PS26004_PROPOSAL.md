# Smart India Hackathon 2026 — Official Executive Proposal

> **Problem Statement ID**: PS 26004 (S.No 4)  
> **Nodal Ministry**: Ministry of Development of North Eastern Region (MDoNER)  
> **Title**: AI-Assisted Early Detection System for Osteoarthritis (OA) Risk Markers in North Eastern Region (NER)  
> **Proposed Solution**: **StrideAhead — Two-Tier AI Platform for Early OA Risk Stratification**  

---

## Executive Summary

Osteoarthritis (OA) is an irreversible degenerative joint disorder affecting over **29.4%** of adults in hilly, agricultural communities across the North Eastern Region (NER). Because diagnostic X-rays and orthopedic specialists are concentrated in distant urban hospitals, patients present at late stages (KL 3/4) when surgery is the only remaining option.

**StrideAhead** introduces a two-tier referral and screening system:
1. **Tier 2 (Village Level)**: An offline-first mobile app operated by ASHA workers using smartphone video motion analysis or low-cost wearable gait sensors (₹900 DIY IMU). It computes gait symmetry, cadence, and TUG duration in <3 minutes and outputs an interpretable risk score (Low / Watch / Refer).
2. **Tier 1 (District Level)**: A lightweight CPU-only deep learning node installed at district hospitals that automatically crops knee X-rays, grades Kellgren-Lawrence (KL 0–4) severity, measures Joint Space Width (JSW in mm), and provides heatmap overlays for radiologist confirmation.

By screening everyone at the village for **₹25–45 per test** and sending only high-risk candidates to district hospitals, StrideAhead catches cartilage erosion 5 years earlier, preventing costly surgeries and protecting rural livelihoods.

---

## Architectural Workflow

```
[ Village Level ] ──(ASHA Tablet + Sensor)──> [ StrideAhead Tier 2 Edge Engine ]
                                                          │
                                                    High Risk Flagged
                                                          │
                                                          ▼
[ District Hospital ] ──(Radiograph DICOM)──> [ StrideAhead Tier 1 X-Ray Node ]
                                                          │
                                                    KL Grade 0-4 + JSW
                                                          │
                                                          ▼
                                            [ Early Non-Surgical Therapy ]
```

---

## Deliverables & Key Technical Highlights

1. **Offline Edge Engine**: Zero internet dependency; background synchronization queue powered by SQLite/IndexedDB.
2. **Explainable AI**: Provides actionable clinical metrics (asymmetry percentage, stance duration) rather than black-box scores.
3. **Multilingual Voice Guidance**: Built for low-literacy environments with Assamese, Bengali, and Manipuri voice prompts.
4. **Interoperability**: ABDM-compliant referral data structure compatible with National Health Mission standards.
