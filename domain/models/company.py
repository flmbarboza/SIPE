"""
SIPE
Sistema Integrado de Planejamento Estratégico

Modelo da Empresa.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass
class Company:
    """
    Representa a empresa objeto do planejamento estratégico.
    """

    legal_name: str = ""
    trade_name: str = ""
    cnpj: str = ""

    sector: str = ""
    segment: str = ""
    size: str = ""

    address: str = ""
    city: str = ""
    state: str = ""
    country: str = "Brasil"
    zip_code: str = ""

    website: str = ""
    email: str = ""
    phone: str = ""

    description: str = ""

    # --------------------------------------------------

    def validate(self) -> bool:
        """
        Validação básica do cadastro.
        """
        return self.trade_name.strip() != ""

    # --------------------------------------------------

    def to_dict(self) -> dict:
        return asdict(self)

    # --------------------------------------------------

    @classmethod
    def from_dict(cls, data: dict) -> "Company":
        return cls(**data)

    # --------------------------------------------------

    def __str__(self):
        return self.trade_name or self.legal_name
