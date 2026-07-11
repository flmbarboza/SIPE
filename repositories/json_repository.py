"""
SIPE
Sistema Integrado de Planejamento Estratégico

Repositório JSON genérico.
"""

from __future__ import annotations

import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any


class JsonRepository:
    """
    Classe base para persistência em arquivos JSON.
    """

    def __init__(self, indent: int = 4):

        self.indent = indent

    # =====================================================
    # Diretórios
    # =====================================================

    def ensure_directory(self, directory: Path) -> None:
        """
        Cria o diretório caso não exista.
        """
        directory.mkdir(parents=True, exist_ok=True)

    # =====================================================
    # Existência
    # =====================================================

    def exists(self, file_path: str | Path) -> bool:

        return Path(file_path).exists()

    # =====================================================
    # Leitura
    # =====================================================

    def load(self, file_path: str | Path) -> dict[str, Any]:

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(path)

        with path.open(
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    # =====================================================
    # Escrita
    # =====================================================

    def save(
        self,
        file_path: str | Path,
        data: dict[str, Any],
        create_backup: bool = True,
    ) -> None:

        path = Path(file_path)

        self.ensure_directory(path.parent)

        if create_backup and path.exists():
            self.create_backup(path)

        with path.open(
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=self.indent,
                ensure_ascii=False,
            )

    # =====================================================
    # Exclusão
    # =====================================================

    def delete(self, file_path: str | Path):

        path = Path(file_path)

        if path.exists():
            path.unlink()

    # =====================================================
    # Cópia
    # =====================================================

    def copy(
        self,
        source: str | Path,
        destination: str | Path,
    ):

        shutil.copy2(source, destination)

    # =====================================================
    # Backup
    # =====================================================

    def create_backup(self, file_path: str | Path):

        path = Path(file_path)

        backup_dir = path.parent / "backups"

        self.ensure_directory(backup_dir)

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        backup_name = (
            f"{path.stem}_{timestamp}{path.suffix}"
        )

        shutil.copy2(
            path,
            backup_dir / backup_name,
        )

    # =====================================================
    # Listagem
    # =====================================================

    def list_files(
        self,
        directory: str | Path,
        pattern: str = "*.json",
    ) -> list[Path]:

        path = Path(directory)

        if not path.exists():
            return []

        return sorted(path.glob(pattern))

    # =====================================================
    # Informações
    # =====================================================

    def size(self, file_path: str | Path) -> int:

        return Path(file_path).stat().st_size

    def modified(self, file_path: str | Path):

        return datetime.fromtimestamp(
            Path(file_path).stat().st_mtime
        )

    # =====================================================
    # Utilidades
    # =====================================================

    def read_text(
        self,
        file_path: str | Path,
    ) -> str:

        return Path(file_path).read_text(
            encoding="utf-8"
        )

    def write_text(
        self,
        file_path: str | Path,
        text: str,
    ):

        path = Path(file_path)

        self.ensure_directory(path.parent)

        path.write_text(
            text,
            encoding="utf-8",
        )
