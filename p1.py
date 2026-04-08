
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
from pmdarima import auto_arima

data = pd.read_csv("Electric_Production.csv")

# Convert Date column
data['DATE'] = pd.to_datetime(data['DATE'], format='%m/%d/%Y')
data['IPG2211A2N'] = pd.to_numeric(data['IPG2211A2N'], errors='coerce')
# Set Date as index
data.set_index('DATE', inplace=True)

# Create time series
ts_data = data['IPG2211A2N']

# Fit ARIMA model
model = ARIMA(ts_data, order=(4, 1, 2))
model_fit = model.fit()
 
# Forecast next 20 steps
forecast = model_fit.forecast(steps=20)
auto_model = auto_arima(ts_data,seasonal=False,trace=True)

print(auto_model.summary())
# Print forecast
print(forecast)

# Plot
plt.figure()
plt.plot(ts_data, label='Original')
plt.plot(forecast, label='Forecast', color='red')
plt.legend()
plt.title("Temperature Forecasting")
plt.xlabel("Date")
plt.ylabel("IPG2211A2N")
plt.show()

