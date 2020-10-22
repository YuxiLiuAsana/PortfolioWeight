from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
pct_data = pd.DataFrame()


def get_share_history(ticker):
    data = pd.read_csv(ticker+'.csv')
    data.index=data['Date']
    pct_data[ticker] = data['Close'].pct_change()


ticker_list = ['DIA', 'LQD', 'GOVT', 'GLD', 'MBB']
for t in ticker_list:
    get_share_history(t)
pct_data['earn'] = 1
for index, row in pct_data.iterrows():
    pct_data['earn'][index] = 1 + row['DIA'] * 0.5 + row['LQD'] * 0.1 + row['GOVT'] * 0.1 + row['GLD'] * 0.2 + row['MBB'] * 0.1
pct_data['earn'][0] = 1
pct_data['curve'] = pct_data['earn'].cumprod()
plt.plot(pct_data['curve'].tolist())
plt.show()


