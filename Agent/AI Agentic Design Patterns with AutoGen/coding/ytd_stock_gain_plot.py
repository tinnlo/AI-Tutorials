# filename: ytd_stock_gain_plot.py
import yfinance as yf
import matplotlib.pyplot as plt

# Fetch data for NVDA and TSLA
stocks = ['NVDA', 'TSLA']
data = yf.download(stocks, start="2023-12-29", end="2024-10-08")

# Calculate the YTD percentage gain
initial_prices = data['Close'].iloc[0]
current_prices = data['Close'].iloc[-1]
ytd_gains = ((current_prices - initial_prices) / initial_prices) * 100

# Create a bar plot
plt.figure(figsize=(10, 6))
ytd_gains.plot(kind='bar', color=['blue', 'green'])
plt.title('YTD Stock Gains (%) as of 2024-10-07')
plt.ylabel('Percentage Gain')
plt.grid(True)

# Save the plot to a file
plt.savefig('ytd_stock_gains.png')

# Making sure to show plot in a script (not necessary for file saving)
plt.show()