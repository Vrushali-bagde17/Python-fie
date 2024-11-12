# Train a time series forecasting model
def train_forecasting_model(data):
    model = ExponentialSmoothing(data['demand'], seasonal='add', seasonal_periods=12)
    fit_model = model.fit()
    return fit_model

# Evaluate the model
def evaluate_model(model, test_data):
    forecast = model.forecast(len(test_data))
    mse = mean_squared_error(test_data['demand'], forecast)
    print(f"Mean Squared Error: {mse}")
    return mse
