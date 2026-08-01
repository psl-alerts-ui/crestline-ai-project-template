"""Regression tests for the template health check."""

import unittest

from src.health import health_summary


class HealthSummaryTests(unittest.TestCase):
    def test_reports_healthy_service(self) -> None:
        self.assertEqual(
            health_summary("automation"),
            {"service": "automation", "status": "ok"},
        )

    def test_rejects_empty_service(self) -> None:
        with self.assertRaises(ValueError):
            health_summary("  ")


if __name__ == "__main__":
    unittest.main()

