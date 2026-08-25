import math
from typing import Dict, List, Any

class GaitAnalyzer:
    """
    Tier 2 Village Screening Gait Analyzer.
    Processes IMU accelerometry/gyroscope time series or smartphone pose data
    to calculate biomechanical markers associated with early knee osteoarthritis (OA).
    """

    def __init__(self, sample_rate_hz: float = 50.0):
        self.sample_rate_hz = sample_rate_hz

    def analyze_walk(self, accel_z_left: List[float], accel_z_right: List[float], tug_duration_sec: float) -> Dict[str, Any]:
        """
        Analyze 20m walking trial data and Timed-Up-and-Go (TUG) duration.
        
        Args:
            accel_z_left: Acceleration time-series for left leg/foot.
            accel_z_right: Acceleration time-series for right leg/foot.
            tug_duration_sec: Measured TUG test time in seconds.
            
        Returns:
            Dictionary containing extracted gait metrics (speed, cadence, stance ratio, symmetry index).
        """
        num_samples_left = len(accel_z_left)
        num_samples_right = len(accel_z_right)
        
        duration_sec_left = num_samples_left / self.sample_rate_hz
        duration_sec_right = num_samples_right / self.sample_rate_hz
        
        # Peak detection for step counting
        peaks_left = self._count_peaks(accel_z_left)
        peaks_right = self._count_peaks(accel_z_right)
        total_steps = peaks_left + peaks_right
        
        total_time_min = (duration_sec_left + duration_sec_right) / 2.0 / 60.0
        cadence_steps_per_min = (total_steps / total_time_min) if total_time_min > 0 else 0.0
        
        # Stance / Swing ratio estimation (simplified energy-based metric)
        mean_power_left = sum(x**2 for x in accel_z_left) / max(1, num_samples_left)
        mean_power_right = sum(x**2 for x in accel_z_right) / max(1, num_samples_right)
        
        # Symmetry Index calculation: 2 * |L - R| / (L + R) * 100
        if (mean_power_left + mean_power_right) > 0:
            symmetry_index_pct = (2.0 * abs(mean_power_left - mean_power_right) / (mean_power_left + mean_power_right)) * 100.0
        else:
            symmetry_index_pct = 0.0

        # Estimated gait speed (assuming 20m distance)
        gait_speed_m_per_s = (20.0 / duration_sec_left) if duration_sec_left > 0 else 0.0

        return {
            "cadence_steps_per_min": round(cadence_steps_per_min, 1),
            "symmetry_index_pct": round(symmetry_index_pct, 2),
            "gait_speed_m_per_s": round(gait_speed_m_per_s, 2),
            "tug_duration_sec": round(tug_duration_sec, 1),
            "left_step_count": peaks_left,
            "right_step_count": peaks_right,
            "total_steps": total_steps
        }

    def _count_peaks(self, data: List[float], threshold_std_mult: float = 0.5) -> int:
        if not data:
            return 0
        mean_val = sum(data) / len(data)
        variance = sum((x - mean_val)**2 for x in data) / len(data)
        std_val = math.sqrt(variance)
        threshold = mean_val + (threshold_std_mult * std_val)
        
        peaks = 0
        for i in range(1, len(data) - 1):
            if data[i] > threshold and data[i] > data[i-1] and data[i] > data[i+1]:
                peaks += 1
        return peaks
