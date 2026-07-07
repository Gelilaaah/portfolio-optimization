from pmdarima import auto_arima
import matplotlib.pyplot as plt

# Find optimal ARIMA parameters
model_arima = auto_arima(train, seasonal=False, trace=True, error_action='ignore', suppress_warnings=True)

print(model_arima.summary())

# Forecast
n_periods = len(test)
forecast_arima = model_arima.predict(n_periods=n_periods)

# Plot
plt.figure(figsize=(12,6))
plt.plot(train.index, train, label='Train')
plt.plot(test.index, test, label='Test')
plt.plot(test.index, forecast_arima, label='ARIMA Forecast')
plt.legend()
plt.show()
