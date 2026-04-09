CHAT BOT para suporte em TI

1. VISAO GERAL DO SISTEMA

O Chatbot de Suporte TI Automatico e uma aplicacao de linha de comando (CLI) desenvolvida em Python para atendimento de primeiro nivel (N1) de chamados de suporte tecnico.

O sistema interpreta palavras-chave digitadas pelo usuario e retorna orientacoes praticas de forma imediata, sem necessidade de intervencao da equipe de TI para problemas recorrentes.

Problemas atendidos:

internet → Reiniciar roteador / Verificar cabo / Testar outro PC

lento → Fechar programas / Limpar lixeira / Reiniciar PC

senha → Ctrl+Alt+Del / Acionar RH / Modo seguro (F8)

impressora → Verificar papel / Reiniciar impressora / Atualizar driver

email → Testar rede / Ctrl+F5 / Modo anonimo

oi → Saudacao inicial

ajuda → Lista de comandos



---

2. ARQUITETURA DO SISTEMA

2.1 Componentes

respostas → Base de conhecimento (dict)

mostrar_cabecalho() → Exibe banner

while True → Loop principal

random.choice() → Escolhe resposta aleatoria

time.sleep(0.5) → Simula processamento



---

2.2 Fluxo de execucao

1. Inicializacao (banner)


2. Leitura do usuario


3. Normalizacao (lower)


4. Matching de palavras-chave


5. Resposta


6. Pausa


7. Loop ou encerramento




---

3. INSTALACAO E EXECUCAO

3.1 Requisitos

Python 3.6+

Sistema: Windows / Linux / macOS

Terminal (CMD ou shell)


Sem necessidade de instalar bibliotecas externas.


---

3.2 Execucao

python --version
python chatbot.py


---

4. DOCUMENTACAO DAS FUNCOES

4.1 mostrar_cabecalho()

Entrada: nenhuma

Saida: nenhuma

Funcao: imprime o banner



---

4.2 Dicionario respostas

Estrutura:

dict[str, list[str]]

Temas:

internet

lento

senha

impressora

email

oi

ajuda



---

4.3 Loop principal

Tipo: while True

Entrada: input do usuario

Saida: print no terminal

Encerramento: "sair" ou "tchau"


⚠️ Bug identificado: Variavel chamadas nao declarada → gera erro (NameError)


---

5. EXEMPLOS DE USO

Entrada → Saida

oi → Em que ajudo?

minha internet caiu → Reinicie roteador

pc lento → Feche programas

trocar senha → Ctrl+Alt+Del

impressora nao imprime → Verifique papel

monitor nao liga → Nao entendi

tchau → erro (bug)



---

⚠️ BUG IDENTIFICADO

Problema:

print(f"Total: {chamadas}")

Correção:

chamadas = 0
chamadas += 1


---

6. MELHORIAS RECOMENDADAS

Alta prioridade

Corrigir variavel chamadas

Adicionar try/except


Media prioridade

Usar JSON para respostas

Criar logs

Normalizar texto


Baixa prioridade

Multiplas palavras-chave

API Web (Flask / FastAPI)

Integracao com GLPI / ServiceNow



---

7. CODIGO ANOTADO (RESUMO)

import time
import random

respostas = { ... }

while True:
    msg = input().lower()

    if msg in ["sair", "tchau"]:
        break

    for palavra in respostas:
        if palavra in msg:
            print(random.choice(respostas[palavra]))


---

8. CONSIDERACOES FINAIS

O chatbot atende bem suporte N1 com uma solucao simples e sem dependencias externas.

Melhorias importantes:

corrigir bugs

adicionar logs

migrar para API web



---

9. HISTORICO

Versao 1.0 — Marco 2026
Equipe de TI


---

REFERENCIAS

https://docs.python.org/3

https://docs.python.org/3/library/random.html

https://docs.python.org/3/library/time.html
