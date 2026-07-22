from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Plan:
    name: str
    monthly_limit: int


class BillingService:
    def __init__(self) -> None:
        self._plans = {
            "free": Plan(name="free", monthly_limit=10),
            "pro": Plan(name="pro", monthly_limit=1000),
        }

    def get_plan(self, name: str) -> Plan:
        return self._plans[name]

    def get_available_plans(self) -> list[Plan]:
        return list(self._plans.values())
