import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def load_data(filepath):
    return pd.read_csv(filepath)

def prepare_data(df):
    # Exemplo: codificar variáveis categóricas, escolher features e target
    df = df.copy()
    df = pd.get_dummies(df, columns=['category', 'weekday'], drop_first=True)
    X = df.drop(columns=['bought_again_90d', 'order_id', 'customer_id', 'order_date', 'order_value'])
    y = df['bought_again_90d']
    return train_test_split(X, y, test_size=0.3, random_state=42)

def train_model(X_train, y_train):
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f'Acurácia: {acc:.4f}')
    return acc

import pandas as pd
import joblib

def predict_single(dict_features, model_path='artefatos/modelo.pkl'):
    # Carrega o modelo
    model = joblib.load(model_path)
    
    # Transforma o dicionário em DataFrame
    df = pd.DataFrame([dict_features])

    # Garante que as colunas estão no mesmo formato (One Hot Encoding)
    df = pd.get_dummies(df)

    # Ajusta as colunas que faltam ou sobram
    model_features = model.feature_names_in_
    for col in model_features:
        if col not in df.columns:
            df[col] = 0  # adiciona colunas faltantes com 0
    df = df[model_features]  # garante ordem correta

    # Faz a previsão de probabilidade
    proba = model.predict_proba(df)[:, 1][0]  # pega a probabilidade de classe 1
    return proba
