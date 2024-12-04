def train_model(datapath):
    import pandas as pd
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_absolute_error
    import joblib

    data = pd.read_csv(datapath)

    X = data[['Temperature', 'Relative Humidity', 'Cloud Type', 'Solar Zenith Angle', 'Pressure', 'Wind Speed']]
    y = data['GHI']  # Target variable: Global Horizontal Irradiance

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

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
    model_path = "model/trained.pkl"

    if model_path:
        joblib.dump(model, model_path)
        print(f"Model saved to {model_path}")

    return model, mae
