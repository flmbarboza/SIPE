"""
SIPE
Sistema Integrado de Planejamento Estratégico

Repositório de Projetos.
"""

from __future__ import annotations

from pathlib import Path

from domain.models.project import Project
from repositories.json_repository import JsonRepository


class ProjectRepository:

    PROJECTS_DIR = Path("data/projects")

    PROJECT_FILE = "project.json"

    def __init__(self):

        self.json = JsonRepository()

        self.PROJECTS_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

    # =====================================================
    # Caminhos
    # =====================================================

    def project_directory(
        self,
        project_id: str,
    ) -> Path:

        return self.PROJECTS_DIR / project_id

    def project_file(
        self,
        project_id: str,
    ) -> Path:

        return (
            self.project_directory(project_id)
            / self.PROJECT_FILE
        )

    # =====================================================
    # Criação
    # =====================================================

    def create(self, project: Project):

        directory = self.project_directory(project.id)

        directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        (directory / "attachments").mkdir(exist_ok=True)

        (directory / "reports").mkdir(exist_ok=True)

        (directory / "exports").mkdir(exist_ok=True)

        (directory / "backups").mkdir(exist_ok=True)

        self.save(project)

    # =====================================================
    # Salvamento
    # =====================================================

    def save(self, project: Project):

        project.touch()

        self.json.save(
            self.project_file(project.id),
            project.to_dict(),
        )

    # =====================================================
    # Leitura
    # =====================================================

    def load(
        self,
        project_id: str,
    ) -> Project:

        data = self.json.load(
            self.project_file(project_id)
        )

        return Project.from_dict(data)

    # =====================================================
    # Existência
    # =====================================================

    def exists(
        self,
        project_id: str,
    ) -> bool:

        return self.json.exists(
            self.project_file(project_id)
        )

    # =====================================================
    # Exclusão
    # =====================================================

    def delete(
        self,
        project_id: str,
    ):

        directory = self.project_directory(
            project_id
        )

        if directory.exists():

            import shutil

            shutil.rmtree(directory)

    # =====================================================
    # Listagem
    # =====================================================

    def list_projects(self):

        projects = []

        for folder in sorted(
            self.PROJECTS_DIR.iterdir()
        ):

            if not folder.is_dir():
                continue

            project_file = (
                folder / self.PROJECT_FILE
            )

            if not project_file.exists():
                continue

            try:

                project = Project.from_dict(
                    self.json.load(project_file)
                )

                projects.append(project)

            except Exception:

                continue

        return sorted(
            projects,
            key=lambda p: p.updated_at,
            reverse=True,
        )

    # =====================================================
    # Pesquisa
    # =====================================================

    def find_by_title(
        self,
        title: str,
    ) -> Project | None:

        title = title.lower()

        for project in self.list_projects():

            if project.title.lower() == title:

                return project

        return None

    # =====================================================
    # Duplicação
    # =====================================================

    def duplicate(
        self,
        project: Project,
        new_title: str,
    ) -> Project:

        from copy import deepcopy
        from uuid import uuid4

        new_project = deepcopy(project)

        new_project.id = str(uuid4())

        new_project.title = new_title

        self.create(new_project)

        return new_project

    # =====================================================
    # Estatísticas
    # =====================================================

    def count(self):

        return len(
            self.list_projects()
        )
