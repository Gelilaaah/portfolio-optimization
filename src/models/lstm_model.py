import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Scale data
scaler = MinMaxScaler()
scaled_train = scaler.fit_transform(train.values.reshape(-1,1))
scaled_test = scaler.transform(test.values.reshape(-1,1))

# Prepare sequences
def create_sequences(data, window=60):
    X, y = [], []
    for i in range(window, len(data)):
        X.append(data[i-window:i, 0])
        y.append(data[i, 0])
    return np.array(X), np.array(y)

X_train, y_train = create_sequences(scaled_train)
X_test, y_test = create_sequences(np.concatenate((scaled_train[-60:], scaled_test), axis=0))

# Reshape for LSTM [samples, timesteps, features]
X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

# Build LSTM model
model_lstm = Sequential([
    LSTM(50, return_sequences=True, input_shape=(X_train.shape[1],1)),
    LSTM(50),
    Dense(1)
])

model_lstm.compile(optimizer='adam', loss='mean_squared_error')
model_lstm.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.1)

# Forecast
pred_lstm = model_lstm.predict(X_test)
pred_lstm = scaler.inverse_transform(pred_lstm)

# Plot
plt.figure(figsize=(12,6))
plt.plot(test.index, test.values, label='Actual TSLA')
plt.plot(test.index, pred_lstm, label='LSTM Forecast')
plt.legend()
plt.show()
