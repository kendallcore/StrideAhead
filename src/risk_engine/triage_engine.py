from typing import Dict, Any

class TriageEngine:
    """
    Explainable Risk Engine for StrideAhead.
    Evaluates village-level gait metrics and clinical risk factors (age, sex, pain history)
    to classify individuals into LOW, WATCH, or REFER (high risk) categories.
    """

    def __init__(self):
        # Clinical thresholds based on bio-mechanics literature for early Knee OA (KOA)
        self.SPEED_THRESHOLD_M_PER_S = 1.0       # < 1.0 m/s indicates gait decline
        self.SYMMETRY_THRESHOLD_PCT = 15.0      # > 15% asymmetry indicates localized joint unloading
        self.TUG_THRESHOLD_SEC = 12.0           # > 12.0s indicates fall & mobility risk
        self.CADENCE_MIN_STEPS_MIN = 90.0       # < 90 steps/min indicates antalgic gait

    def evaluate_risk(self, gait_metrics: Dict[str, Any], patient_age: int, joint_pain_months: int) -> Dict[str, Any]:
        """
        Evaluate composite OA risk based on gait metrics and clinical context.
        """
        risk_flags = []
        risk_score = 0

        # Check Gait Speed
        speed = gait_metrics.get("gait_speed_m_per_s", 1.2)
        if speed < self.SPEED_THRESHOLD_M_PER_S:
            risk_flags.append(f"Gait speed ({speed} m/s) below threshold ({self.SPEED_THRESHOLD_M_PER_S} m/s)")
            risk_score += 30

        # Check Asymmetry
        asymmetry = gait_metrics.get("symmetry_index_pct", 0.0)
        if asymmetry > self.SYMMETRY_THRESHOLD_PCT:
            risk_flags.append(f"Left-Right gait asymmetry ({asymmetry}%) exceeds limit ({self.SYMMETRY_THRESHOLD_PCT}%)")
            risk_score += 35

        # Check TUG Duration
        tug = gait_metrics.get("tug_duration_sec", 8.0)
        if tug > self.TUG_THRESHOLD_SEC:
            risk_flags.append(f"Timed-Up-and-Go ({tug}s) indicates impaired mobility (> {self.TUG_THRESHOLD_SEC}s)")
            risk_score += 25

        # Clinical Context Flags
        if patient_age >= 50:
            risk_score += 15
        if joint_pain_months >= 3:
            risk_flags.append(f"Chronic joint pain reported for {joint_pain_months} months")
            risk_score += 20

        # Determine Category
        if risk_score >= 50:
            recommendation = "REFER"
            action = "Refer to District Hospital for Tier 1 X-Ray Kellgren-Lawrence auto-grading."
        elif risk_score >= 25:
            recommendation = "WATCH"
            action = "Re-assess in 3 months; recommend quadriceps strengthening exercises."
        else:
            recommendation = "LOW"
            action = "Low risk detected. Continue routine wellness activities."

        return {
            "risk_level": recommendation,
            "risk_score": min(100, risk_score),
            "action_required": action,
            "risk_factors": risk_flags
        }
