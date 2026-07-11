"""
SIPE
Sistema Integrado de Planejamento Estratégico

Página de gerenciamento de projetos.
"""

import streamlit as st

from domain.models.project import Project
from services.project_service import ProjectService


class ProjectPage:

    def __init__(self):

        self.service = ProjectService()

    # ======================================================
    # Cabeçalho
    # ======================================================

    def header(self):

        st.title("📁 Projetos")

        st.caption(
            "Crie, abra e gerencie projetos estratégicos."
        )

    # ======================================================
    # Novo Projeto
    # ======================================================

    def new_project(self):

        with st.expander(
            "➕ Novo Projeto",
            expanded=True,
        ):

            title = st.text_input(
                "Título do Projeto",
                key="new_project_title",
            )

            description = st.text_area(
                "Descrição",
                key="new_project_description",
            )

            company = st.text_input(
                "Empresa",
                key="new_project_company",
            )

            responsible = st.text_input(
                "Responsável",
                key="new_project_responsible",
            )

            if st.button(
                "Criar Projeto",
                use_container_width=True,
            ):

                project = Project()

                project.title = title

                project.description = description

                project.responsible = responsible

                project.company.trade_name = company

                project = self.service.create_project(
                    title=title,
                    description=description,
                    company=company,
                    responsible=responsible,
                )
                
                st.success("Projeto criado com sucesso.")

                st.rerun()

    # ======================================================
    # Lista
    # ======================================================

    def list_projects(self):

        st.subheader("Projetos cadastrados")

        projects = self.service.list_projects()

        if len(projects) == 0:

            st.info(
                "Nenhum projeto encontrado."
            )

            return

        for project in projects:

            with st.container(border=True):

                c1, c2, c3, c4 = st.columns(
                    [4, 2, 2, 2]
                )

                with c1:

                    st.markdown(
                        f"### {project.title}"
                    )

                    st.caption(
                        project.company.trade_name
                    )

                    st.write(
                        project.description
                    )

                with c2:

                    st.metric(
                        "Objetivos",
                        project.total_objectives,
                    )

                with c3:

                    st.metric(
                        "KPIs",
                        project.total_kpis,
                    )

                with c4:

                    st.metric(
                        "Iniciativas",
                        project.total_initiatives,
                    )

                c1, c2, c3, c4 = st.columns(4)

                # --------------------------------------------

                with c1:

                    if st.button(
                        "📂 Abrir",
                        key=f"open_{project.id}",
                        use_container_width=True,
                    ):

                        self.service.open(
                            project.id
                        )

                        st.success(
                            "Projeto carregado."
                        )

                        st.rerun()

                # --------------------------------------------

                with c2:

                    if st.button(
                        "📑 Duplicar",
                        key=f"dup_{project.id}",
                        use_container_width=True,
                    ):

                        self.service.save_as(
                            project.title + " (Cópia)"
                        )

                        st.success(
                            "Projeto duplicado."
                        )

                        st.rerun()

                # --------------------------------------------

                with c3:

                    if st.button(
                        "🗑 Excluir",
                        key=f"del_{project.id}",
                        use_container_width=True,
                    ):

                        self.service.delete(
                            project.id
                        )

                        st.success(
                            "Projeto removido."
                        )

                        st.rerun()

                # --------------------------------------------

                with c4:

                    if (
                        self.service.has_project()
                        and self.service.get_current().id
                        == project.id
                    ):

                        st.success("Projeto Aberto")

    # ======================================================
    # Informações
    # ======================================================

    def current_project(self):

        st.divider()

        st.subheader("Projeto Atual")

        if not self.service.has_project():

            st.info(
                "Nenhum projeto aberto."
            )

            return

        project = self.service.get_current()

        c1, c2 = st.columns(2)

        with c1:

            st.write(
                "**Projeto:**",
                project.title,
            )

            st.write(
                "**Empresa:**",
                project.company.trade_name,
            )

            st.write(
                "**Responsável:**",
                project.responsible,
            )

        with c2:

            st.write(
                "**Objetivos:**",
                project.total_objectives,
            )

            st.write(
                "**KPIs:**",
                project.total_kpis,
            )

            st.write(
                "**Iniciativas:**",
                project.total_initiatives,
            )

    # ======================================================
    # Render
    # ======================================================

    def render(self):

        self.header()

        self.new_project()

        st.divider()

        self.list_projects()

        self.current_project()
