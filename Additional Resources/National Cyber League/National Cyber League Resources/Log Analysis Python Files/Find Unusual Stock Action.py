"""
The following information is found by this program. It shows the amount of change that happens and sort out the one with the most changes. This all belongs to one stock finding the solution.

Abnormal behavior detected for the following tickers:
          Time Ticker   Price  Change  AbsChange
5462  11:31:02   FMIR  127.95    -3.0        3.0
5466  11:31:06   FMIR  124.95    -3.0        3.0
5491  11:31:31   FMIR  121.95    -3.0        3.0
5493  11:31:33   FMIR  118.95    -3.0        3.0
5569  11:32:49   FMIR  115.95    -3.0        3.0
5570  11:32:50   FMIR  112.95    -3.0        3.0
5584  11:33:04   FMIR  109.95    -3.0        3.0
5612  11:33:32   FMIR  106.95    -3.0        3.0
5660  11:34:20   FMIR  103.95    -3.0        3.0
"""

import pandas as pd

# Load the log file into a DataFrame
def load_log(file_path):
    # Read the log file and parse it into a DataFrame
    data = pd.read_csv(file_path, delim_whitespace=True, header=0)
    return data

# Define what constitutes abnormal behavior
def identify_abnormal_behavior(df, threshold=2.0):
    # Calculate the absolute change in price
    df['AbsChange'] = df['Change'].abs()

    # Find tickers with changes greater than the threshold
    abnormal_tickers = df[df['AbsChange'] > threshold]

    return abnormal_tickers[['Time', 'Ticker', 'Price', 'Change', 'AbsChange']]

# Main function
def main():
    file_path = 'stocks.log'

    # Load the stock data
    stock_data = load_log(file_path)

    # Identify abnormal behavior
    abnormal_stocks = identify_abnormal_behavior(stock_data)

    if not abnormal_stocks.empty:
        print("Abnormal behavior detected for the following tickers:")
        print(abnormal_stocks)
    else:
        print("No abnormal behavior detected.")

if __name__ == "__main__":
    main()
