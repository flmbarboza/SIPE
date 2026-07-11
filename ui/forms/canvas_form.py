"""
SIPE
Sistema Integrado de Planejamento Estratégico

Formulário do Business Model Canvas.
"""

import streamlit as st

from domain.models.canvas import Canvas


class CanvasForm:
    """
    Formulário de edição do Business Model Canvas.
    """

    def __init__(self, canvas: Canvas):
        self.canvas = canvas

    # ==========================================================
    # Conversões
    # ==========================================================

    @staticmethod
    def _list_to_text(items: list[str]) -> str:
        if not items:
            return ""

        return "\n".join(items)

    @staticmethod
    def _text_to_list(text: str) -> list[str]:
        return [
            item.strip()
            for item in text.splitlines()
            if item.strip()
        ]

    # ==========================================================
    # Bloco
    # ==========================================================

    def _editor(
        self,
        title: str,
        value: list[str],
        key: str,
        height: int = 240,
    ) -> list[str]:

        text = st.text_area(
            title,
            value=self._list_to_text(value),
            height=height,
            key=key,
        )

        return self._text_to_list(text)

    # ==========================================================
    # Renderização
    # ==========================================================

    def render(self):

        st.subheader("Business Model Canvas")

        st.caption(
            "Digite um item por linha em cada bloco."
        )

        c1, c2, c3, c4, c5 = st.columns(5)

        # ======================================================
        # Linha Superior
        # ======================================================

        with c1:

            self.canvas.key_partnerships = self._editor(
                "🤝 Parcerias-Chave",
                self.canvas.key_partnerships,
                "canvas_key_partnerships",
            )

        with c2:

            self.canvas.key_activities = self._editor(
                "⚙️ Atividades-Chave",
                self.canvas.key_activities,
                "canvas_key_activities",
            )

        with c3:

            self.canvas.value_proposition = self._editor(
                "💎 Proposta de Valor",
                self.canvas.value_proposition,
                "canvas_value_proposition",
            )

        with c4:

            self.canvas.customer_relationships = self._editor(
                "❤️ Relacionamento",
                self.canvas.customer_relationships,
                "canvas_relationships",
            )

        with c5:

            self.canvas.customer_segments = self._editor(
                "👥 Segmentos de Clientes",
                self.canvas.customer_segments,
                "canvas_segments",
            )

        st.divider()

        c1, c2 = st.columns(2)

        with c1:

            self.canvas.key_resources = self._editor(
                "📦 Recursos-Chave",
                self.canvas.key_resources,
                "canvas_resources",
                height=180,
            )

            self.canvas.cost_structure = self._editor(
                "💰 Estrutura de Custos",
                self.canvas.cost_structure,
                "canvas_costs",
                height=180,
            )

        with c2:

            self.canvas.channels = self._editor(
                "🚚 Canais",
                self.canvas.channels,
                "canvas_channels",
                height=180,
            )

            self.canvas.revenue_streams = self._editor(
                "💵 Fontes de Receita",
                self.canvas.revenue_streams,
                "canvas_revenue",
                height=180,
            )

        return self.canvas

    # ==========================================================
    # Estatísticas
    # ==========================================================

    def statistics(self):

        st.divider()

        total = (
            len(self.canvas.key_partnerships)
            + len(self.canvas.key_activities)
            + len(self.canvas.key_resources)
            + len(self.canvas.value_proposition)
            + len(self.canvas.customer_relationships)
            + len(self.canvas.channels)
            + len(self.canvas.customer_segments)
            + len(self.canvas.cost_structure)
            + len(self.canvas.revenue_streams)
        )

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Blocos",
                "9",
            )

        with c2:
            st.metric(
                "Itens cadastrados",
                total,
            )

        with c3:

            completos = 0

            campos = [
                self.canvas.key_partnerships,
                self.canvas.key_activities,
                self.canvas.key_resources,
                self.canvas.value_proposition,
                self.canvas.customer_relationships,
                self.canvas.channels,
                self.canvas.customer_segments,
                self.canvas.cost_structure,
                self.canvas.revenue_streams,
            ]

            for campo in campos:
                if len(campo) > 0:
                    completos += 1

            st.metric(
                "Blocos preenchidos",
                f"{completos}/9",
            )
