"""Minimal health-check primitives for template projects."""

from typing import Any


def health_summary(service: str = "application") -> dict[str, Any]:
    """Return a machine-readable liveness summary."""
    if not service.strip():
        raise ValueError("service must not be empty")
    return {"service": service, "status": "ok"}

