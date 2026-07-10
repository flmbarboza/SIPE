# SIPE – Sistema Integrado de Planejamento Estratégico

**Versão:** 1.0 (Arquitetura)
**Data:** Julho/2026
**Autor:** Flávio Luiz de Moraes Barboza
**Tecnologia:** Python + Streamlit

---

# 1. Objetivo

O SIPE (Sistema Integrado de Planejamento Estratégico) é uma plataforma web desenvolvida em Streamlit destinada a apoiar empreendedores, consultores, professores e estudantes na elaboração completa do planejamento estratégico de empresas.

O sistema integra, em um único ambiente, ferramentas clássicas de administração estratégica, planejamento financeiro, gestão de projetos e geração automática de relatórios.

---

# 2. Objetivos Específicos

O sistema deverá permitir:

- cadastrar empresas;
- elaborar o Business Model Canvas;
- realizar análises PESTEL;
- realizar análise das Cinco Forças de Porter;
- realizar Benchmarking;
- construir a SWOT;
- gerar automaticamente a SWOT Cruzada;
- definir Missão, Visão e Valores;
- elaborar Objetivos Estratégicos;
- construir o Balanced Scorecard;
- cadastrar KPIs;
- acompanhar metas;
- elaborar Plano de Ação (5W2H);
- gerenciar riscos;
- construir cronogramas;
- elaborar Plano Financeiro;
- gerar dashboards executivos;
- gerar automaticamente um relatório final em Word e PDF.

---

# 3. Público-Alvo

- Pequenos empresários
- Startups
- Franquias
- Consultores
- Professores
- Alunos de Administração
- Incubadoras
- Empresas Juniores
- Sebrae

---

# 4. Arquitetura Geral

```text
                 SIPE

                 Home
                   │
───────────────────┼────────────────────
                   │
             Cadastro Projeto
                   │
         Diagnóstico Estratégico
                   │
───────────────────┼────────────────────
Canvas
PESTEL
Porter
Benchmarking
SWOT
SWOT Cruzada
                   │
───────────────────┼────────────────────
Planejamento Estratégico
                   │
Identidade Organizacional
Objetivos Estratégicos
Balanced Scorecard
KPIs
Projetos Estratégicos
                   │
───────────────────┼────────────────────
Plano Operacional
Plano Financeiro
Gestão de Pessoas
Gestão de Riscos
Plano de Ação
                   │
───────────────────┼────────────────────
Dashboard Executivo
                   │
Relatório Final
```

---

# 5. Arquitetura Técnica

Framework

- Streamlit

Persistência

- JSON

Visualização

- Plotly
- Plotly Express

Manipulação

- Pandas

Relatórios

- python-docx
- ReportLab

Diagramas

- NetworkX

Cronogramas

- Plotly Timeline

Exportação

- Excel
- Word
- PDF
- JSON

---

# 6. Estrutura de Pastas

```
SIPE/

app.py

requirements.txt

README.md

LICENSE

.gitignore

assets/

pages/

utils/

templates/

reports/

data/

tests/
```

---

# 7. Estrutura das Páginas

## Home

Resumo executivo

KPIs

Projetos

Pendências

Dashboard

---

## Projeto

Cadastro da empresa

Responsável

Cidade

UF

Segmento

Missão do projeto

Horizonte estratégico

---

## Canvas

9 blocos editáveis

Exportação

Importação

---

## PESTEL

Editor

Gráficos

Impacto

Priorização

---

## Porter

Cinco Forças

Radar

Pontuação

Comentários

---

## Benchmarking

Tabela dinâmica

Comparações

Ranking

---

## SWOT

Editor

Forças

Fraquezas

Oportunidades

Ameaças

---

## SWOT Cruzada

Automática

FO

FA

WO

WT

---

## Identidade Organizacional

Negócio

Missão

Visão

Valores

Propósito

Posicionamento

---

## Objetivos Estratégicos

Tabela

Prioridade

Perspectiva

Prazo

Responsável

---

## Balanced Scorecard

Financeiro

Clientes

Processos

Aprendizado

Mapa Estratégico

---

## KPIs

Indicador

Meta

Atual

Responsável

Periodicidade

---

## Projetos Estratégicos

Kanban

Cronograma

Status

---

## Financeiro

Investimento

Fluxo de Caixa

Ponto de Equilíbrio

Payback

VPL

TIR

---

## Gestão de Riscos

Registro

Heatmap

Plano de resposta

---

## Plano de Ação

5W2H

Cronograma

Gantt

---

## Dashboard

Radar Estratégico

KPIs

Metas

Semáforos

Gráficos

---

## Relatório

DOCX

PDF

Exportação

---

# 8. Fluxo do Usuário

```text
Cadastrar empresa

↓

Canvas

↓

PESTEL

↓

Porter

↓

Benchmarking

↓

SWOT

↓

SWOT Cruzada

↓

Missão

↓

Visão

↓

Valores

↓

Objetivos Estratégicos

↓

Balanced Scorecard

↓

KPIs

↓

Projetos

↓

Plano Financeiro

↓

Plano de Ação

↓

Dashboard

↓

Relatório Final
```

---

# 9. Modelo de Dados

```text
Empresa

Projeto

Canvas

PESTEL

Porter

Benchmarking

SWOT

Objetivos

KPIs

Projetos

Riscos

Plano Financeiro
```

Cada empresa possuirá um único arquivo JSON.

---

# 10. Estrutura do JSON

```json
{
    "empresa": {},
    "canvas": {},
    "pestel": {},
    "porter": {},
    "benchmarking": {},
    "swot": {},
    "identidade": {},
    "objetivos": [],
    "kpis": [],
    "projetos": [],
    "financeiro": {},
    "riscos": {},
    "plano_acao": {}
}
```

---

# 11. Roadmap

## Sprint 1

Infraestrutura

Persistência

Navegação

Tema

---

## Sprint 2

Projeto

Cadastro

Empresa

---

## Sprint 3

Canvas

---

## Sprint 4

PESTEL

---

## Sprint 5

Porter

---

## Sprint 6

Benchmarking

---

## Sprint 7

SWOT

---

## Sprint 8

SWOT Cruzada

---

## Sprint 9

Identidade Organizacional

---

## Sprint 10

Objetivos Estratégicos

---

## Sprint 11

Balanced Scorecard

---

## Sprint 12

KPIs

---

## Sprint 13

Projetos Estratégicos

---

## Sprint 14

Plano Financeiro

---

## Sprint 15

Plano de Ação

---

## Sprint 16

Dashboard

---

## Sprint 17

Relatórios

---

# 12. Backlog do Produto

MVP

- Cadastro
- Canvas
- SWOT
- PESTEL
- Porter
- Dashboard
- Relatório

Versão 2

- Inteligência Artificial
- Sugestão automática de estratégias
- Benchmark automático
- Chat estratégico

Versão 3

- Multiusuário
- Banco PostgreSQL
- Controle de permissões
- API REST
- Aplicativo Mobile

---

# 13. Padrões de Desenvolvimento

PEP8

Type Hint

Docstrings

Black

Pytest

GitFlow

Commits semânticos

---

# 14. Critérios de Aceite

Cada módulo somente será considerado concluído quando:

- Interface pronta
- Dados persistidos
- Testes executados
- Documentação atualizada
- Integração realizada
- Exportação funcionando

---

# 15. Futuras Integrações

OpenAI

Google Gemini

Power BI

Looker Studio

Google Drive

Dropbox

OneDrive

Google Maps

Receita Federal

IBGE

Banco Central

---

# 16. Licença

MIT License

---

# 17. Próxima Sprint

Sprint 1

Objetivo:

Construir toda a infraestrutura do SIPE.

Entregáveis:

- Estrutura do projeto
- Navegação
- Tema visual
- Persistência JSON
- Cadastro da empresa
- Configuração inicial
- Primeiro commit no GitHub
