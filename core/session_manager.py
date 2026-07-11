"""
SIPE - Sistema Integrado de Planejamento Estratégico

Session Manager

Responsável por controlar todo o estado da aplicação.

Nenhum outro módulo deverá acessar st.session_state diretamente.

Autor:
Flávio Luiz de Moraes Barboza

Versão:
0.1.0
"""

from __future__ import annotations

from typing import Any

import streamlit as st


class SessionManager:
    """
    Gerenciador central da sessão do SIPE.

    Todas as leituras e escritas em st.session_state devem ocorrer
    exclusivamente através desta classe.
    """

    DEFAULT_STATE = {
        # Informações do sistema
        "initialized": False,
        "app_version": "0.1.0",

        # Projeto
        "project": None,
        "project_path": None,
        "project_loaded": False,
        "project_modified": False,

        # Empresa
        "company": None,

        # Navegação
        "current_page": "home",
        "previous_page": None,

        # Interface
        "theme": "light",
        "language": "pt-BR",

        # Mensagens
        "notifications": [],

        # Cache
        "cache": {},

        # Dados temporários
        "temp": {},
    }

    def initialize(self) -> None:
        """
        Inicializa a sessão.

        Este método deve ser executado apenas uma vez,
        durante a inicialização da aplicação.
        """

        if st.session_state.get("initialized", False):
            return

        for key, value in self.DEFAULT_STATE.items():
            st.session_state[key] = value

        st.session_state["initialized"] = True

    # ------------------------------------------------------------------
    # Métodos genéricos
    # ------------------------------------------------------------------

    def get(self, key: str, default: Any = None) -> Any:
        """
        Obtém um valor da sessão.
        """
        return st.session_state.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """
        Define um valor na sessão.
        """
        st.session_state[key] = value

    def exists(self, key: str) -> bool:
        """
        Verifica se uma chave existe.
        """
        return key in st.session_state

    def delete(self, key: str) -> None:
        """
        Remove uma chave da sessão.
        """
        if key in st.session_state:
            del st.session_state[key]

    def clear(self) -> None:
        """
        Remove todos os dados da sessão.
        """

        keys = list(st.session_state.keys())

        for key in keys:
            del st.session_state[key]

        self.initialize()

    # ------------------------------------------------------------------
    # Navegação
    # ------------------------------------------------------------------

    @property
    def current_page(self) -> str:
        return self.get("current_page")

    @current_page.setter
    def current_page(self, page: str) -> None:

        previous = self.current_page

        self.set("previous_page", previous)
        self.set("current_page", page)

    @property
    def previous_page(self) -> str | None:
        return self.get("previous_page")

    # ------------------------------------------------------------------
    # Projeto
    # ------------------------------------------------------------------

    @property
    def project(self):
        return self.get("project")

    @project.setter
    def project(self, value):

        self.set("project", value)
        self.project_modified = True

    @property
    def project_path(self):
        return self.get("project_path")

    @project_path.setter
    def project_path(self, value):

        self.set("project_path", value)

    @property
    def project_loaded(self) -> bool:
        return self.get("project_loaded")

    @project_loaded.setter
    def project_loaded(self, value: bool):

        self.set("project_loaded", value)

    @property
    def project_modified(self) -> bool:
        return self.get("project_modified")

    @project_modified.setter
    def project_modified(self, value: bool):

        self.set("project_modified", value)

    # ------------------------------------------------------------------
    # Empresa
    # ------------------------------------------------------------------

    @property
    def company(self):
        return self.get("company")

    @company.setter
    def company(self, value):

        self.set("company", value)
        self.project_modified = True

    # ------------------------------------------------------------------
    # Notificações
    # ------------------------------------------------------------------

    def notify(self, message: str) -> None:
        """
        Adiciona uma notificação.
        """

        notifications = self.get("notifications")
        notifications.append(message)

        self.set("notifications", notifications)

    def notifications(self) -> list[str]:
        """
        Retorna todas as notificações.
        """

        return self.get("notifications")

    def clear_notifications(self) -> None:

        self.set("notifications", [])

    # ------------------------------------------------------------------
    # Cache
    # ------------------------------------------------------------------

    def cache_set(self, key: str, value: Any) -> None:

        cache = self.get("cache")
        cache[key] = value
        self.set("cache", cache)

    def cache_get(self, key: str, default=None):

        cache = self.get("cache")
        return cache.get(key, default)

    def cache_clear(self):

        self.set("cache", {})

    # ------------------------------------------------------------------
    # Dados Temporários
    # ------------------------------------------------------------------

    def temp_set(self, key: str, value: Any):

        temp = self.get("temp")
        temp[key] = value
        self.set("temp", temp)

    def temp_get(self, key: str, default=None):

        temp = self.get("temp")
        return temp.get(key, default)

    def temp_clear(self):

        self.set("temp", {})

    # ------------------------------------------------------------------
    # Informações
    # ------------------------------------------------------------------

    @property
    def is_dirty(self) -> bool:
        """
        Indica se existem alterações não salvas.
        """
        return self.project_modified

    @property
    def is_initialized(self) -> bool:
        """
        Indica se a sessão foi inicializada.
        """
        return self.get("initialized")

    # ------------------------------------------------------------------
    # Debug
    # ------------------------------------------------------------------

    def dump(self) -> dict:
        """
        Retorna todo o conteúdo da sessão.

        Utilizado para depuração.
        """

        return dict(st.session_state)


# Singleton utilizado em todo o SIPE.
session = SessionManager()
