"""Model LinearRegression."""

"""Modelo Preço de Casas"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

# Exemplo de Dados de Treino:
# [Tamanho | Quartos | Vagas]
X = np.array(
    [
        [100, 3, 2],
        [150, 4, 3],
        [120, 2, 1],
        [300, 5, 4],
        [200, 3, 2],
        [250, 4, 3],
        [180, 3, 2],
        [140, 2, 1],
        [320, 5, 4],
        [210, 3, 0],
    ]
)

# Valores das casas
y = np.array(
    [200000, 300000, 180000, 500000, 400000, 450000, 360000, 220000, 520000, 410000]
)

# Divisão dos dados de treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Criando o modelo
model = LinearRegression()

# Treinando o modelo
model.fit(X_train, y_train)

# Avaliando o modelo com os dados de teste
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"MSE:, {mse}")

# Salvando o modelo treinado
joblib.dump(model, "model.pkl")
