import numpy as np
import unittest

def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)

def compute_aggregated_threat_score(departments):
    total_weighted_score = 0
    total_weight = 0
    for department in departments:
        importance = department["importance"]
        scores = department["scores"]
        avg_score = np.mean(scores)
        total_weighted_score += importance * avg_score
        total_weight += importance
    return total_weighted_score / total_weight if total_weight > 0 else 0

# Unit-тесты
class TestCybersecurityScore(unittest.TestCase):
    def test_compute_aggregated_threat_score(self):
        departments = [{"importance": 3, "scores": [10, 20, 30, 40]}]
        self.assertAlmostEqual(compute_aggregated_threat_score(departments), 25.0)

        departments = [
            {"importance": 1, "scores": [10, 20, 30]},
            {"importance": 1, "scores": [40, 50, 60]},
        ]
        self.assertAlmostEqual(compute_aggregated_threat_score(departments), 35.0)

        departments = [
            {"importance": 1, "scores": [10, 20, 30]},
            {"importance": 3, "scores": [40, 50, 60]},
        ]
        self.assertAlmostEqual(compute_aggregated_threat_score(departments), 47.5)

    def test_edge_cases(self):
        departments = [{"importance": 3, "scores": [0, 0, 0]}]
        self.assertEqual(compute_aggregated_threat_score(departments), 0)

        departments = [{"importance": 3, "scores": [90, 90, 90]}]
        self.assertEqual(compute_aggregated_threat_score(departments), 90)

        departments = []
        self.assertEqual(compute_aggregated_threat_score(departments), 0)

# Функциональные тесты
class TestFunctionalCybersecurityScore(unittest.TestCase):
    def test_functional_cases(self):
        # Случай 1: Одинаковые департаменты
        departments = [
            {"importance": 1, "scores": generate_random_data(45, 5, 100)},
            {"importance": 1, "scores": generate_random_data(50, 5, 100)},
        ]
        score = compute_aggregated_threat_score(departments)
        self.assertTrue(0 <= score <= 90)

        departments = [
            {"importance": 1, "scores": generate_random_data(30, 10, 100)},
            {"importance": 5, "scores": generate_random_data(70, 10, 100)},
        ]
        score = compute_aggregated_threat_score(departments)
        self.assertTrue(0 <= score <= 90)

        departments = [
            {"importance": 1, "scores": generate_random_data(20, 5, 100)},
            {"importance": 2, "scores": generate_random_data(85, 2, 50)},
        ]
        score = compute_aggregated_threat_score(departments)
        self.assertTrue(0 <= score <= 90)

        departments = [
            {"importance": 2, "scores": generate_random_data(40, 10, 50)},
            {"importance": 3, "scores": generate_random_data(60, 15, 200)},
        ]
        score = compute_aggregated_threat_score(departments)
        self.assertTrue(0 <= score <= 90)

        departments = [
            {"importance": 3, "scores": [0]},
            {"importance": 1, "scores": [90]},
        ]
        score = compute_aggregated_threat_score(departments)
        self.assertTrue(0 <= score <= 90)

if __name__ == "__main__":
    unittest.main()
