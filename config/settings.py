"""
Configurações globais do SIPE.

Todas as configurações da aplicação devem ser centralizadas neste arquivo.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Configurações gerais da aplicação."""

    APP_NAME: str = "SIPE"
    APP_FULL_NAME: str = "Sistema Integrado de Planejamento Estratégico"

    VERSION: str = "0.1.0"

    AUTHOR: str = "Flávio Luiz de Moraes Barboza"

    ORGANIZATION: str = "UFU"

    LANGUAGE: str = "pt-BR"

    TIMEZONE: str = "America/Sao_Paulo"

    DATE_FORMAT: str = "%d/%m/%Y"

    DATETIME_FORMAT: str = "%d/%m/%Y %H:%M"

    CURRENCY: str = "BRL"

    CURRENCY_SYMBOL: str = "R$"

    DECIMAL_PLACES: int = 2

    DEBUG: bool = True

    AUTO_SAVE: bool = True

    AUTO_BACKUP: bool = True


settings = Settings()
