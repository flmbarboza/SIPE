"""
Configurações globais do SIPE.

Todas as configurações da aplicação devem ser centralizadas neste arquivo.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Configurações gerais da aplicação."""

    # ======================================================
    # Aplicação
    # ======================================================

    APP_NAME: str = "SIPE"

    APP_FULL_NAME: str = "Sistema Integrado de Planejamento Estratégico"

    APP_ICON: "📊"

    VERSION: str = "0.1.0"

    AUTHOR: str = "Flávio Luiz de Moraes Barboza"

    ORGANIZATION: str = "UFU"

    # ======================================================
    # Internacionalização
    # ======================================================

    LANGUAGE: str = "pt-BR"

    TIMEZONE: str = "America/Sao_Paulo"

    DATE_FORMAT: str = "%d/%m/%Y"

    DATETIME_FORMAT: str = "%d/%m/%Y %H:%M"

    # ======================================================
    # Financeiro
    # ======================================================

    CURRENCY: str = "BRL"

    CURRENCY_SYMBOL: str = "R$"

    DECIMAL_PLACES: int = 2

    # ======================================================
    # Sistema
    # ======================================================

    DEBUG: bool = True

    AUTO_SAVE: bool = True

    AUTO_BACKUP: bool = True

    PROJECTS_DIRECTORY: str = "data/projects"

    EXPORT_DIRECTORY: str = "exports"

    REPORT_DIRECTORY: str = "reports"

    BACKUP_DIRECTORY: str = "backups"

    # ======================================================
    # Streamlit
    # ======================================================

    PAGE_LAYOUT: str = "wide"

    SIDEBAR_STATE: str = "expanded"


settings = Settings()
