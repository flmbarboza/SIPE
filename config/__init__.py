"""
Pacote de configuração do SIPE.
"""

from .settings import settings
from .theme import theme
from .logging import app_logger
from .paths import *

__all__ = [
    "settings",
    "theme",
    "app_logger",
]
