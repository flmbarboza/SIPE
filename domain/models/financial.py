"""
SIPE
Planejamento Financeiro
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict


@dataclass
class FinancialProjection:

    year: int = 1

    revenue: float = 0.0

    costs: float = 0.0

    expenses: float = 0.0

    investments: float = 0.0

    cash_flow: float = 0.0

    profit: float = 0.0

    def to_dict(self):

        return asdict(self)


@dataclass
class Financial:

    projections: list[FinancialProjection] = field(default_factory=list)

    discount_rate: float = 0.0

    npv: float = 0.0

    irr: float = 0.0

    payback: float = 0.0

    breakeven: float = 0.0

    observations: str = ""

    def validate(self):

        return True

    def to_dict(self):

        return asdict(self)

    @classmethod
    def from_dict(cls, data):

        obj = cls()

        obj.discount_rate = data.get("discount_rate", 0)

        obj.npv = data.get("npv", 0)

        obj.irr = data.get("irr", 0)

        obj.payback = data.get("payback", 0)

        obj.breakeven = data.get("breakeven", 0)

        obj.observations = data.get("observations", "")

        obj.projections = [
            FinancialProjection(**p)
            for p in data.get("projections", [])
        ]

        return obj
