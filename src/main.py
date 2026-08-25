import os
import sys
import json

from src.tier2_gait.gait_analyzer import GaitAnalyzer
from src.risk_engine.triage_engine import TriageEngine
from src.tier1_xray.kl_grader import KLGrader

def run_stride_ahead_demo():
    print("=" * 70)
    print("      STRIDEAHEAD: TWO-TIER OA RISK-STRATIFICATION PLATFORM      ")
    print("         SIH 2026 Solution for Problem Statement PS 26004         ")
    print("=" * 70)
    print()

    # 1. Simulate Tier 2 Village Gait Screening
    print("--- [TIER 2 VILLAGE SCREENING: ASHA FIELD TEST] ---")
    
    # Sample IMU accelerometry data (simulating antalgic gait with asymmetry)
    sample_accel_left = [0.1, 0.5, 1.8, 2.4, 0.6, 0.2, 0.1, 0.4, 1.7, 2.3, 0.5, 0.2] * 20
    sample_accel_right = [0.1, 0.3, 0.9, 1.1, 0.3, 0.1, 0.1, 0.2, 0.8, 1.0, 0.2, 0.1] * 20
    simulated_tug_sec = 13.5
    
    analyzer = GaitAnalyzer(sample_rate_hz=50.0)
    gait_metrics = analyzer.analyze_walk(sample_accel_left, sample_accel_right, simulated_tug_sec)
    
    print("Captured Gait Metrics:")
    for k, v in gait_metrics.items():
        print(f"  • {k}: {v}")
    print()

    # 2. Risk Triage Engine Evaluation
    print("--- [EDGE RISK ENGINE EVALUATION] ---")
    triage = TriageEngine()
    patient_age = 54
    joint_pain_months = 6
    
    risk_result = triage.evaluate_risk(gait_metrics, patient_age=patient_age, joint_pain_months=joint_pain_months)
    
    print(f"Risk Classification Result: [{risk_result['risk_level']}] (Score: {risk_result['risk_score']}/100)")
    print(f"Action: {risk_result['action_required']}")
    print("Identified Risk Factors:")
    for rf in risk_result["risk_factors"]:
        print(f"  ⚠️  {rf}")
    print()

    # 3. Simulate Tier 1 District Hospital X-Ray Auto-Grading (if REFER)
    if risk_result["risk_level"] == "REFER":
        print("--- [TIER 1 DISTRICT HOSPITAL: RADIOGRAPH CONFIRMATION] ---")
        grader = KLGrader()
        # Simulate radiograph evaluation with Joint Space Width = 2.8mm (Early KL Grade 2)
        radiograph_result = grader.grade_radiograph(
            image_path="samples/knee_xray_patient_001.png",
            simulated_jsw_mm=2.8
        )
        
        print(f"Radiograph Processed: {radiograph_result['image_processed']}")
        print(f"Kellgren-Lawrence Grade: KL {radiograph_result['kl_grade']} ({radiograph_result['kl_description']})")
        print(f"Measured Joint Space Width (JSW): {radiograph_result['joint_space_width_mm']} mm")
        print(f"Model Confidence: {radiograph_result['model_confidence'] * 100}%")
        print(f"Clinical Guidance: {radiograph_result['clinical_guidance']}")
        print("=" * 70)

if __name__ == "__main__":
    run_stride_ahead_demo()
