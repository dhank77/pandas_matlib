import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

df = pd.read_csv('data/HistoricalData.csv')

df['Average'] = df['High'].str.replace('$', '').astype(float) + df['Low'].str.replace('$', '').astype(float) / 2

# df['Date'] = pd.to_datetime(df['Date'], format="%m/%d/%Y")
df_sorted = df.sort_values(by='Date', ascending=False)

fig, ax = plt.subplots(1, 1, figsize=(15, 5))

ax.bar(df_sorted['Date'], df_sorted['Average'])

ax.set_ylabel('Avarege')
ax.set_xlabel('Date')

fig.suptitle('FINANCIAL DATA ANALYSIS')
fig.autofmt_xdate()

plt.show()