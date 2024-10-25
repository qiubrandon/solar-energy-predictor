import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

def train_model(datapath):
    data = pd.read_csv(datapath)

    X = data[['irradiance', 'temperature','humidity']]
    y = data['energy_output']

    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)

    return model, mae

def save_mode(model, path="models/trained.pkl"):
    import joblib
    joblib.dump(model,path)


    