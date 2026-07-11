"""
SIPE
Página do Business Model Canvas.
"""

import streamlit as st

from services.project_service import ProjectService
from ui.forms.canvas_form import CanvasForm


class CanvasPage:

    def __init__(self):

        self.service = ProjectService()

    # ==========================================================
    # Cabeçalho
    # ==========================================================

    def header(self):

        st.title("🧩 Business Model Canvas")

        st.caption(
            "Construa ou revise o modelo de negócios da organização."
        )

    # ==========================================================
    # Barra superior
    # ==========================================================

    def toolbar(self):

        c1, c2, c3, c4 = st.columns([2, 2, 2, 4])

        with c1:

            if st.button(
                "💾 Salvar",
                use_container_width=True,
            ):

                self.service.save()

                st.success("Projeto salvo com sucesso.")

        with c2:

            if st.button(
                "↺ Recarregar",
                use_container_width=True,
            ):

                st.rerun()

        with c3:

            if st.button(
                "🧹 Limpar Canvas",
                use_container_width=True,
            ):

                project = self.service.get_current()

                project.canvas.key_partnerships.clear()
                project.canvas.key_activities.clear()
                project.canvas.key_resources.clear()
                project.canvas.value_proposition.clear()
                project.canvas.customer_relationships.clear()
                project.canvas.channels.clear()
                project.canvas.customer_segments.clear()
                project.canvas.cost_structure.clear()
                project.canvas.revenue_streams.clear()

                self.service.mark_dirty()

                st.rerun()

    # ==========================================================
    # Página
    # ==========================================================

    def render(self):

        self.header()

        if not self.service.has_project():

            st.warning(
                "Nenhum projeto aberto."
            )

            st.info(
                "Crie ou abra um projeto antes de editar o Canvas."
            )

            return

        project = self.service.get_current()

        st.info(
            f"Projeto: **{project.title or 'Novo Projeto'}**"
        )

        self.toolbar()

        st.divider()

        form = CanvasForm(project.canvas)

        form.render()

        form.statistics()

        self.service.mark_dirty()

        st.divider()

        c1, c2 = st.columns([1, 5])

        with c1:

            if st.button(
                "💾 Salvar Projeto",
                use_container_width=True,
            ):

                self.service.save()

                st.success("Projeto salvo.")

        with c2:

            if self.service.is_dirty():

                st.warning(
                    "Existem alterações ainda não salvas."
                )

            else:

                st.success(
                    "Todas as alterações foram salvas."
                )
