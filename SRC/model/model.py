import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Carregando os dados
data = pd.read_csv('./data.csv', sep=';')

# Separando dataset(Variáveis preditoras e target)
X = data.drop('total', axis=1)
y = data['total']

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
print(f'MSE: {mse}')

# Salvando o modelo treinado
joblib.dump(model, './model.pkl')
# joblib.dump(model, "../../model.pkl")
