import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

# --- STEP 1: LOAD AND FILTER ---
# We use the cleaned stock dataset from Task 1
df = pd.read_csv('cleaned_dataset.csv')

# Time series works best on one subject. Let's pick Apple (AAPL).
stock_data = df[df['symbol'] == 'AAPL'].copy()

# Convert date to a format Python understands and set it as the index
stock_data['date'] = pd.to_datetime(stock_data['date'])
stock_data = stock_data.sort_values('date')
stock_data.set_index('date', inplace=True)

# --- STEP 2: RAW DATA PLOTTING (Objective 1) ---
plt.figure(figsize=(12, 6))
plt.plot(stock_data['close'], color='#1f77b4', label='AAPL Close Price')
plt.title('Apple Stock Price (2014-2017)')
plt.xlabel('Year')
plt.ylabel('Price ($)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('1_raw_stock_plot.png')
plt.show()

# --- STEP 3: DECOMPOSITION (Objective 2) ---
# This breaks the price into Trend, Seasonality, and Noise
# 252 is the average number of trading days in a year
result = seasonal_decompose(stock_data['close'], model='additive', period=252)

# We plot the components separately
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10), sharex=True)
result.trend.plot(ax=ax1, title='Trend (Long-term direction)')
result.seasonal.plot(ax=ax2, title='Seasonality (Repeating patterns)')
result.resid.plot(ax=ax3, title='Residuals (Random noise/Unexplained events)')
plt.tight_layout()
plt.savefig('2_decomposition_plot.png')
plt.show()

# --- STEP 4: MOVING AVERAGE SMOOTHING (Objective 3) ---
# This helps us see the trend through the daily "noise"
stock_data['MA30'] = stock_data['close'].rolling(window=30).mean() # Monthly trend
stock_data['MA100'] = stock_data['close'].rolling(window=100).mean() # Quarterly trend

plt.figure(figsize=(12, 6))
plt.plot(stock_data['close'], label='Original Price', alpha=0.3)
plt.plot(stock_data['MA30'], label='30-Day Moving Average', color='orange')
plt.plot(stock_data['MA100'], label='100-Day Moving Average', color='red')
plt.title('Stock Price Smoothing (Moving Averages)')
plt.legend()
plt.savefig('3_moving_average_plot.png')
plt.show()

print("Task 2 complete! Check your folder for the 3 plot images.")