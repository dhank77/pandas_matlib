import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv('data/HistoricalData.csv')

df['Average'] = df['High'].str.replace('$', '').astype(float) + df['Low'].str.replace('$', '').astype(float) / 2

df['Date'] = df["Date"].apply(lambda x: datetime.strptime(x, "%m/%d/%Y").strftime("%d %B %Y")) 
df_sorted = df.sort_values(by='Date', ascending=False)
print(df_sorted)

fig, axs = plt.subplots(1, 1, figsize=(15, 5))

axs.plot(df_sorted['Date'], df_sorted['Average'])
axs.set_ylabel('Avarege')
axs.set_xlabel('Date')

fig.suptitle('FINANCIAL DATA ANALYSIS')
fig.autofmt_xdate()
plt.show()