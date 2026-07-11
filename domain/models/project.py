"""
SIPE
Sistema Integrado de Planejamento Estratégico

Modelo principal do Projeto Estratégico.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import Any
from uuid import uuid4


# ==========================================================
# Projeto Estratégico
# ==========================================================

@dataclass
class Project:

    # ======================================================
    # Metadados
    # ======================================================

    id: str = field(default_factory=lambda: str(uuid4()))

    version: str = "0.1.0"

    created_at: str = field(
        default_factory=lambda: datetime.now().isoformat()
    )

    updated_at: str = field(
        default_factory=lambda: datetime.now().isoformat()
    )

    # ======================================================
    # Informações Gerais
    # ======================================================

    title: str = ""

    description: str = ""

    status: str = "Planejamento"

    planning_horizon: int = 5

    responsible: str = ""

    # ======================================================
    # Empresa
    # ======================================================

    company: dict[str, Any] = field(default_factory=dict)

    # ======================================================
    # Diagnóstico
    # ======================================================

    canvas: dict[str, Any] = field(default_factory=dict)

    pestel: dict[str, Any] = field(default_factory=dict)

    porter: dict[str, Any] = field(default_factory=dict)

    benchmarking: list = field(default_factory=list)

    swot: dict[str, Any] = field(default_factory=dict)

    swot_cross: dict[str, Any] = field(default_factory=dict)

    identity: dict[str, Any] = field(default_factory=dict)

    # ======================================================
    # Planejamento
    # ======================================================

    objectives: list = field(default_factory=list)

    kpis: list = field(default_factory=list)

    initiatives: list = field(default_factory=list)

    action_plan: list = field(default_factory=list)

    # ======================================================
    # Gestão
    # ======================================================

    risks: list = field(default_factory=list)

    financial: dict[str, Any] = field(default_factory=dict)

    dashboard: dict[str, Any] = field(default_factory=dict)

    reports: list = field(default_factory=list)

    # ======================================================
    # Métodos
    # ======================================================

    def update_timestamp(self) -> None:
        """
        Atualiza a data de modificação.
        """

        self.updated_at = datetime.now().isoformat()

    # ------------------------------------------------------

    def to_dict(self) -> dict:
        """
        Converte o objeto para dicionário.
        """

        return asdict(self)

    # ------------------------------------------------------

    @classmethod
    def from_dict(cls, data: dict) -> "Project":
        """
        Constrói um Project a partir de um dicionário.
        """

        return cls(**data)

    # ------------------------------------------------------

    def touch(self):
        """
        Atualiza somente o timestamp.
        """

        self.update_timestamp()

    # ------------------------------------------------------

    @property
    def is_new(self):

        return self.title == ""

    # ------------------------------------------------------

    @property
    def filename(self):

        if self.title.strip():

            name = (
                self.title
                .lower()
                .replace(" ", "_")
                .replace("/", "_")
                .replace("\\", "_")
            )

            return f"{name}.json"

        return f"{self.id}.json"

    # ------------------------------------------------------

    def __str__(self):

        return self.title

    # ------------------------------------------------------

    def summary(self):

        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "version": self.version,
            "updated_at": self.updated_at,
        }
