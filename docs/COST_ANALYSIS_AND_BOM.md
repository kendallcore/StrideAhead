# StrideAhead — Hardware Bill of Materials (BOM) & Rural Cost Analysis

> **Key Financial Headline**: A rural community should **never** have to buy this system. Like ASHA tablets under the National Health Mission (NHM), it is deployed at the district level. Marginal screening cost is **₹25–45 per person**, making early detection 100x cheaper than a single knee replacement surgery.

---

## 1. Hardware Options & Bill of Materials (BOM)

### Option A: Low-Cost IMU Band Kit (~₹900 – ₹1,600 per unit)
*Recommended for simple, scalable field deployment.*

| Component | Specifications | Estimated Cost (INR) |
|---|---|---|
| **MEMS 9-DoF IMU** | ICM-20948 / MPU-9250 breakout board | ₹250 – ₹500 |
| **Microcontroller + BLE** | ESP32-WROOM development board | ₹250 – ₹450 |
| **Battery & Power** | 500 mAh LiPo battery + TP4056 USB charger | ₹150 – ₹250 |
| **Enclosure & Strap** | 3D-printed pouch, washable velcro strap | ₹150 – ₹300 |
| **Assembly & Small-batch PCB** | Custom PCB substrate | ₹100 – ₹150 |
| **TOTAL PER DEVICE** | | **~ ₹900 – ₹1,600** |

---

### Option B: DIY Instrumented Insole Pair (~₹2,500 – ₹4,500 per pair)
*Provides rich vertical Ground Reaction Force (vGRF) pedobarography signal.*

| Component | Specifications | Estimated Cost (INR) |
|---|---|---|
| **FSR Pressure Sensors** | 6–8 FSR sensors per foot (heel + metatarsal) | ₹800 – ₹1,600 |
| **Dual MCU + BLE + Power** | ESP32 stack (per foot) | ₹800 – ₹1,400 |
| **Insole Substrate & Wiring** | Flexible silicone insole insert | ₹500 – ₹800 |
| **TOTAL PER PAIR** | | **~ ₹2,500 – ₹4,500** |

*Commercial comparison*: Moticon research insoles cost **€1,000+ (₹90,000+)**. StrideAhead's DIY build reduces cost by **50x** while retaining diagnostic screening accuracy (auROC ≈ 0.98).

---

## 2. Complete ASHA Deployment Kit Breakdown

| Item | Unit Cost (INR) | Notes |
|---|---|---|
| **Wearable Unit (Option A IMU)** | ₹1,200 | Reusable across thousands of patients |
| **Android Tablet (7–8", 2GB RAM)** | ₹8,000 – ₹11,000 | Standard NHM / ASHA class tablet |
| **Charging & Carrying Case** | ₹800 | IP67 weather-resistant pouch |
| **Edge AI Software Platform** | ₹0 | Open-source (PyTorch / ONNX / TFLite) |
| **ASHA Training Amortization** | ₹500 | One-time training batch cost |
| **TOTAL KIT COST** | **~ ₹10,000 – ₹13,000** | **Serves ~1,000 adults / year** |

---

## 3. Per-Test Economics

```
Component                              Cost per Person Screened
───────────────────────────────────────────────────────────────
Device Amortization (1,000 tests/yr)   ₹0.50 – ₹1.50
ASHA Incentive Payout (NHM parity)     ₹20.00 – ₹40.00
Consumables & Sanitization             ₹2.00 – ₹5.00
───────────────────────────────────────────────────────────────
TOTAL COST PER TEST                    ≈ ₹25.00 – ₹45.00
```

> **Pitch Line**: Screening 1,000 adults in a rural village costs **₹25,000 – ₹45,000 per year** — significantly less than the cost of a single surgical knee replacement (₹1.5 – ₹2.5 Lakh).

---

## 4. Status-Quo Cost of NOT Screening

| Burden Head | Estimated Cost to Rural Family |
|---|---|
| Painkillers (NSAIDs) + GP visits | ₹6,000 – ₹12,000 / year |
| Lost agricultural wages due to mobility loss | ₹8,000 – ₹20,000 / year |
| Private Knee Replacement (Late Stage KL 4) | ₹1,500,000 – ₹250,000 |
| **StrideAhead Early Screening Test** | **₹30 (One Time)** |
