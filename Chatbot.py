import json
import random
import logging
from datetime import datetime
from flask import Flask, request, jsonify

===== LOG =====

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(name)

===== CHATBOT =====

class ChatbotTI:
def init(self):
self.chamadas = 0
self.historico = []
self.respostas = self.carregar_base()

def carregar_base(self):  
    try:  
        with open("respostas.json", "r", encoding="utf-8") as f:  
            return json.load(f)  
    except:  
        base = self.base_padrao()  
        with open("respostas.json", "w", encoding="utf-8") as f:  
            json.dump(base, f, indent=2, ensure_ascii=False)  
        return base  

def base_padrao(self):  
    return {  
        "internet": [{  
            "solucao": "Reinicie o roteador e execute ipconfig /renew",  
            "sucesso": "Internet normal"  
        }],  
        "lento": [{  
            "solucao": "Feche programas e reinicie o PC",  
            "sucesso": "PC mais rápido"  
        }],  
        "senha": [{  
            "solucao": "Ctrl+Alt+Del → Alterar senha",  
            "sucesso": "Senha alterada"  
        }],  
        "impressora": [{  
            "solucao": "Reinicie impressora e reinstale driver",  
            "sucesso": "Impressora funcionando"  
        }],  
        "email": [{  
            "solucao": "Limpe cache ou use aba anônima",  
            "sucesso": "Email acessado"  
        }],  
        "arquivo": [{  
            "solucao": "Verifique lixeira ou OneDrive",  
            "sucesso": "Arquivo encontrado"  
        }]  
    }  

def buscar_resposta(self, msg):  
    msg = msg.lower()  

    for chave in self.respostas:  
        if chave in msg:  
            item = random.choice(self.respostas[chave])  
            return {  
                "tema": chave.upper(),  
                "solucao": item["solucao"],  
                "sucesso": item["sucesso"]  
            }  

    return {  
        "tema": "SUPORTE",  
        "solucao": "Abra chamado no suporte (ramal 1234)",  
        "sucesso": "Encaminhado"  
    }  

def processar(self, msg):  
    self.chamadas += 1  
    resp = self.buscar_resposta(msg)  

    log = {  
        "id": self.chamadas,  
        "msg": msg,  
        "tema": resp["tema"],  
        "data": datetime.now().isoformat()  
    }  

    self.historico.append(log)  
    logger.info(log)  

    return resp

===== CLI =====

def rodar_cli(bot):
print("🤖 Suporte TI (digite 'sair')")

while True:  
    msg = input("Você: ")  

    if msg.lower() == "sair":  
        break  

    resp = bot.processar(msg)  

    print(f"Bot: {resp['tema']}")  
    print(resp["solucao"])  
    print("✅", resp["sucesso"])  
    print("-" * 40)

===== API =====

app = Flask(name)
bot = ChatbotTI()

@app.route("/chat", methods=["POST"])
def chat():
data = request.json
msg = data.get("mensagem", "")

if not msg:  
    return jsonify({"erro": "mensagem vazia"}), 400  

resp = bot.processar(msg)  

return jsonify(resp)

@app.route("/stats")
def stats():
total = len(bot.historico)
return jsonify({
"total": total,
"ultimas": bot.historico[-5:]
})

===== MAIN =====

if name == "main":
modo = input("1-CLI | 2-API: ")

if modo == "2":  
    app.run(port=5000)  
else:  
    rodar_cli(bot)

O que esse código faz?
