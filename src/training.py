import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

def train_model(datapath):
    data = pd.read_csv(datapath)

    X = data[['Clearsky GHI', 'Clearsky DHI',  
            'Solar Zenith Angle', 'Cloud Type', 
            'Relative Humidity', 'Temperature']]
    
    y = data['GHI']

    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(
    n_estimators=200,
    max_depth=10,
    min_samples_split=5,
    min_samples_leaf=3,
    max_features='sqrt',
    random_state=42
)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)

    return model, mae

def save_model(model, path="models/trained.pkl"):
    import joblib
    joblib.dump(model,path)


    