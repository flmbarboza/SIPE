"""
Gerenciamento dos diretórios do SIPE.
"""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"

PROJECTS_DIR = DATA_DIR / "projects"

BACKUP_DIR = DATA_DIR / "backups"

REPORTS_DIR = PROJECT_ROOT / "reports"

EXPORTS_DIR = REPORTS_DIR / "exports"

GENERATED_REPORTS_DIR = REPORTS_DIR / "generated"

TEMPLATES_DIR = PROJECT_ROOT / "templates"

ASSETS_DIR = PROJECT_ROOT / "assets"

CSS_DIR = ASSETS_DIR / "css"

IMAGES_DIR = ASSETS_DIR / "images"

ICONS_DIR = ASSETS_DIR / "icons"

LOG_DIR = PROJECT_ROOT / "logs"


def create_directories():
    """
    Cria automaticamente todos os diretórios necessários.
    """

    directories = [
        DATA_DIR,
        PROJECTS_DIR,
        BACKUP_DIR,
        REPORTS_DIR,
        EXPORTS_DIR,
        GENERATED_REPORTS_DIR,
        TEMPLATES_DIR,
        ASSETS_DIR,
        CSS_DIR,
        IMAGES_DIR,
        ICONS_DIR,
        LOG_DIR,
    ]

    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
