from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Carrega o modelo na inicialização da API
model = joblib.load('artefatos/modelo.pkl')
model_features = model.feature_names_in_  # pega as features que o modelo espera

@app.route('/prevê', methods=['POST'])
def preve():
    # Recebe JSON com features
    data = request.get_json()
    
    # Verifica se o JSON é válido
    if not data:
        return jsonify({'error': 'JSON inválido ou vazio'}), 400

    # Verifica se todas as features obrigatórias estão no JSON
    missing_features = [f for f in model_features if f not in data]
    if missing_features:
        return jsonify({'error': f'Features faltando: {missing_features}'}), 400

    # Cria dataframe para previsão
    df = pd.DataFrame([data])

    # Garante que o dataframe tem as mesmas colunas (one-hot etc)
    df = pd.get_dummies(df)
    
    # Ajusta colunas que faltam
    for col in model_features:
        if col not in df.columns:
            df[col] = 0
    
    # Reordena as colunas para o mesmo padrão do modelo
    df = df[model_features]
    
    # Faz a previsão da probabilidade
    proba = model.predict_proba(df)[:, 1][0]
    
    return jsonify({'proba': float(proba)})

if __name__ == '__main__':
    app.run(debug=True)
