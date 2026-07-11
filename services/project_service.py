"""
SIPE
Sistema Integrado de Planejamento Estratégico

Serviço de gerenciamento de projetos.
"""

from __future__ import annotations

from domain.models.project import Project
from repositories.project_repository import ProjectRepository


class ProjectService:

    def __init__(self):

        self.repository = ProjectRepository()

        self.current: Project | None = None

        self.dirty = False

    # =====================================================
    # Novo Projeto
    # =====================================================

    def new_project(self) -> Project:

        project = Project()

        self.repository.create(project)

        self.current = project

        self.dirty = False

        return project

    # =====================================================
    # Abrir Projeto
    # =====================================================

    def open(self, project_id: str) -> Project:

        self.current = self.repository.load(project_id)

        self.dirty = False

        return self.current

    # =====================================================
    # Salvar
    # =====================================================

    def save(self):

        if self.current is None:

            return

        self.repository.save(self.current)

        self.dirty = False

    # =====================================================
    # Salvar Como
    # =====================================================

    def save_as(self, new_title: str):

        if self.current is None:

            return None

        new_project = self.repository.duplicate(
            self.current,
            new_title,
        )

        self.current = new_project

        self.dirty = False

        return new_project

    # =====================================================
    # Fechar
    # =====================================================

    def close(self):

        self.current = None

        self.dirty = False

    # =====================================================
    # Excluir
    # =====================================================

    def delete(self, project_id: str):

        if (
            self.current
            and self.current.id == project_id
        ):

            self.close()

        self.repository.delete(project_id)

    # =====================================================
    # Listagem
    # =====================================================

    def list_projects(self):

        return self.repository.list_projects()

    # =====================================================
    # Projeto Atual
    # =====================================================

    def has_project(self):

        return self.current is not None

    def get_current(self):

        return self.current

    # =====================================================
    # Controle
    # =====================================================

    def mark_dirty(self):

        self.dirty = True

    def is_dirty(self):

        return self.dirty

    # =====================================================
    # Estatísticas
    # =====================================================

    def count_projects(self):

        return self.repository.count()
