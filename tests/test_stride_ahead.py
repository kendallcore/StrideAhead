import unittest
from src.tier2_gait.gait_analyzer import GaitAnalyzer
from src.risk_engine.triage_engine import TriageEngine
from src.tier1_xray.kl_grader import KLGrader

class TestStrideAhead(unittest.TestCase):

    def setUp(self):
        self.gait_analyzer = GaitAnalyzer(sample_rate_hz=50.0)
        self.triage_engine = TriageEngine()
        self.kl_grader = KLGrader()

    def test_gait_analysis_metrics(self):
        left_accel = [0.1, 0.5, 2.0, 0.5, 0.1] * 20
        right_accel = [0.1, 0.5, 2.0, 0.5, 0.1] * 20
        metrics = self.gait_analyzer.analyze_walk(left_accel, right_accel, tug_duration_sec=9.0)
        
        self.assertIn("cadence_steps_per_min", metrics)
        self.assertIn("symmetry_index_pct", metrics)
        self.assertIn("gait_speed_m_per_s", metrics)
        self.assertEqual(metrics["symmetry_index_pct"], 0.0)

    def test_triage_engine_referral(self):
        metrics = {
            "gait_speed_m_per_s": 0.8,
            "symmetry_index_pct": 22.0,
            "tug_duration_sec": 14.0
        }
        result = self.triage_engine.evaluate_risk(metrics, patient_age=55, joint_pain_months=6)
        self.assertEqual(result["risk_level"], "REFER")
        self.assertGreaterEqual(result["risk_score"], 50)

    def test_kl_grader_early_oa(self):
        result = self.kl_grader.grade_radiograph("dummy.png", simulated_jsw_mm=2.8)
        self.assertEqual(result["kl_grade"], 2)
        self.assertTrue(result["requires_radiologist_review"])

if __name__ == "__main__":
    unittest.main()
