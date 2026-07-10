# SIPE – Sistema Integrado de Planejamento Estratégico

**Versão:** 0.1.0

---

# 1. Objetivo

Este documento define o modelo de dados oficial do SIPE.

Todos os módulos do sistema deverão utilizar estas entidades.

Nenhuma alteração estrutural poderá ser realizada sem atualização deste documento.

---

# 2. Conceito Fundamental

O SIPE trabalha com um conceito central:

> **Um Projeto Estratégico**

Todo o restante do sistema pertence a um projeto.

```
Projeto Estratégico

├── Empresa
├── Diagnóstico
├── Planejamento
├── Financeiro
├── Riscos
├── Plano de Ação
├── Dashboard
└── Relatórios
```

---

# 3. Estrutura de Diretórios

Cada projeto possuirá sua própria pasta.

```
data/

projects/

    projeto_uuid/

        project.json

        reports/

        exports/

        backups/

        attachments/
```

Assim o SIPE poderá administrar dezenas de empresas ao mesmo tempo.

---

# 4. Identificação

Todos os registros possuirão UUID.

Nunca utilizaremos IDs sequenciais.

Exemplo

```
550e8400-e29b-41d4-a716-446655440000
```

---

# 5. Entidades do Sistema

O domínio do SIPE será composto pelas seguintes entidades.

## Empresa

Representa a organização objeto do planejamento.

Campos

| Campo         | Tipo     |
| ------------- | -------- |
| id            | UUID     |
| razao_social  | string   |
| nome_fantasia | string   |
| cnpj          | string   |
| segmento      | string   |
| setor         | string   |
| porte         | string   |
| cidade        | string   |
| uf            | string   |
| pais          | string   |
| website       | string   |
| email         | string   |
| telefone      | string   |
| data_cadastro | datetime |

---

## Projeto Estratégico

Representa um planejamento estratégico.

Campos

| Campo       | Tipo    |
| ----------- | ------- |
| id          | UUID    |
| titulo      | string  |
| descricao   | string  |
| empresa_id  | UUID    |
| versao      | string  |
| data_inicio | date    |
| data_fim    | date    |
| horizonte   | inteiro |
| status      | enum    |
| responsavel | string  |

---

## Canvas

Representa o Business Model Canvas.

Campos

```
proposta_valor

segmentos_clientes

canais

relacionamento

receitas

recursos

atividades

parcerias

custos
```

---

## PESTEL

Campos

```
politico

economico

social

tecnologico

ambiental

legal
```

Cada item conterá

```
descrição

impacto

probabilidade

prioridade

observações
```

---

## Cinco Forças de Porter

Campos

```
concorrencia

clientes

fornecedores

entrantes

substitutos
```

Cada força possuirá

```
nota

descrição

evidências

prioridade
```

---

## Benchmarking

Cada registro representa um concorrente.

Campos

```
empresa

cidade

site

produto

preço

marketing

atendimento

forças

fraquezas

observações
```

---

## SWOT

Quatro listas independentes.

```
forças

fraquezas

oportunidades

ameaças
```

Cada item possuirá

```
id

descrição

peso

prioridade
```

---

## SWOT Cruzada

Representa estratégias.

```
FO

FA

WO

WT
```

Cada estratégia possuirá

```
id

titulo

descrição

prioridade

origem
```

---

## Identidade Organizacional

Campos

```
negocio

missao

visao

valores

proposito

posicionamento
```

---

## Objetivos Estratégicos

Cada objetivo pertence a uma perspectiva do BSC.

Campos

| Campo       | Tipo   |
| ----------- | ------ |
| id          | UUID   |
| titulo      | string |
| descricao   | string |
| perspectiva | enum   |
| prioridade  | enum   |
| prazo       | date   |
| responsavel | string |
| status      | enum   |

---

## KPI

Cada KPI pertence a um objetivo.

Campos

| Campo         | Tipo   |
| ------------- | ------ |
| id            | UUID   |
| objetivo_id   | UUID   |
| nome          | string |
| unidade       | string |
| formula       | string |
| meta          | float  |
| atual         | float  |
| periodicidade | enum   |

---

## Projeto Estratégico (Iniciativa)

Representa ações para atingir objetivos.

Campos

```
id

objetivo_id

titulo

descrição

responsável

início

fim

status

investimento
```

---

## Plano de Ação

Modelo 5W2H.

Campos

```
what

why

where

when

who

how

how_much
```

---

## Gestão de Riscos

Campos

```
id

categoria

descrição

probabilidade

impacto

nível

resposta

responsável

status
```

---

## Financeiro

Campos

```
receita

custos

despesas

investimentos

fluxo_caixa

payback

vpl

tir

ponto_equilibrio
```

---

## Relatórios

Campos

```
id

tipo

data

arquivo

versão
```

---

# 6. Relacionamentos

```
Empresa

↓

Projeto

↓

Canvas

↓

Diagnóstico

↓

Planejamento

↓

Objetivos

↓

KPIs

↓

Projetos Estratégicos

↓

Plano de Ação

↓

Dashboard

↓

Relatórios
```

---

# 7. Enumeradores

## Status do Projeto

```
Planejamento

Em andamento

Concluído

Arquivado
```

---

## Prioridade

```
Baixa

Média

Alta

Crítica
```

---

## Perspectivas do BSC

```
Financeira

Clientes

Processos Internos

Aprendizado e Crescimento
```

---

## Status da Iniciativa

```
Não iniciada

Em andamento

Concluída

Cancelada
```

---

# 8. Estrutura do JSON

Cada projeto será salvo em um único arquivo.

```
project.json
```

Estrutura oficial:

```json
{
  "metadata": {},
  "empresa": {},
  "projeto": {},
  "canvas": {},
  "pestel": {},
  "porter": {},
  "benchmarking": [],
  "swot": {},
  "swot_cruzada": {},
  "identidade": {},
  "objetivos": [],
  "kpis": [],
  "iniciativas": [],
  "plano_acao": [],
  "financeiro": {},
  "riscos": [],
  "dashboard": {},
  "relatorios": []
}
```

---

# 9. Convenções

Todos os arquivos JSON utilizarão UTF-8.

Datas seguirão ISO 8601.

Valores monetários serão armazenados como números.

Não haverá HTML armazenado no JSON.

Todos os identificadores serão UUID.

---

# 10. Evolução do Modelo

Novos campos poderão ser adicionados.

Campos existentes nunca deverão ser removidos sem migração de versão.

Toda alteração deverá atualizar o número da versão do modelo.

Versão atual:

**0.1.0**
