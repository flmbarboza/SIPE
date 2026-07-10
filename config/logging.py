"""
Configuração do Loguru.
"""

from pathlib import Path

from loguru import logger

from config.paths import LOG_DIR


LOG_FILE = Path(LOG_DIR) / "sipe.log"

ERROR_FILE = Path(LOG_DIR) / "errors.log"


logger.remove()

logger.add(
    LOG_FILE,
    level="INFO",
    rotation="10 MB",
    retention="30 days",
    encoding="utf-8",
)

logger.add(
    ERROR_FILE,
    level="ERROR",
    rotation="10 MB",
    retention="30 days",
    encoding="utf-8",
)

logger.add(
    sink=lambda msg: print(msg, end=""),
    level="INFO",
)

app_logger = logger
