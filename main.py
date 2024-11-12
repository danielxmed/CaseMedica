import spacy
from googleapiclient.discovery import build
from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do .env
load_dotenv()

# Inicialize o spaCy para português
nlp = spacy.load("pt_core_news_sm")

def extract_keywords_pt(text):
    """Extrai palavras-chave usando o spaCy."""
    doc = nlp(text)
    keywords = [chunk.text for chunk in doc.noun_chunks]
    return list(set(keywords))  # Remove duplicados

def search_web_pt(query, api_key, cse_id):
    """Realiza uma busca na web em português usando a API do Google."""
    try:
        service = build("customsearch", "v1", developerKey=api_key)
        results = service.cse().list(q=query, cx=cse_id, lr="lang_pt").execute()
        return [
            {
                "title": item.get("title"),
                "url": item.get("link"),
                "snippet": item.get("snippet", "")
            }
            for item in results.get("items", [])
        ]
    except Exception as e:
        print(f"Erro na busca: {e}")
        return []

def filter_results(results, keywords):
    """Filtra os resultados com base nas palavras-chave."""
    filtered_results = []
    for result in results:
        if any(keyword.lower() in result["snippet"].lower() for keyword in keywords):
            filtered_results.append(result)
    return filtered_results

# Configurações do Flask
app = Flask(__name__)

# Obtenha as chaves da API de variáveis de ambiente
API_KEY = os.getenv("GOOGLE_API_KEY")
CSE_ID = os.getenv("GOOGLE_CSE_ID")

@app.route("/processar", methods=["POST"])
def process_text_pt():
    """Rota para processar o texto e retornar palavras-chave e resultados da web."""
    data = request.json
    texto = data.get("texto", "").strip()

    if not texto:
        return jsonify({"erro": "Texto não fornecido. Envie um campo 'texto' no corpo da requisição."}), 400

    # Extrai palavras-chave
    palavras_chave = extract_keywords_pt(texto)

    # Busca na web para cada palavra-chave
    resultados = []
    for palavra in palavras_chave:
        resultados.extend(search_web_pt(palavra, API_KEY, CSE_ID))

    # Filtra os resultados
    resultados_filtrados = filter_results(resultados, palavras_chave)

    # Retorna o JSON estruturado
    return jsonify({
        "texto_entrada": texto,
        "palavras_chave": palavras_chave,
        "resultados": resultados_filtrados
    })

if __name__ == "__main__":
    app.run(debug=True)
