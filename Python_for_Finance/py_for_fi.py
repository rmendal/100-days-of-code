import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

style.use('ggplot')

start = dt.datetime(2015, 1, 1)
end = dt.datetime.now()

df = web.DataReader("GOOGL", 'morningstar', start, end)

df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
df = df.drop("Symbol", axis=1)
#df.to_csv('googl.csv')

#df.plot()
#plt.show()
#print(df.head())

df = pd.read_csv('googl.csv', parse_dates=True, index_col=0)

#df['100ma'] = df['Adj Close'].rolling(window=100).mean()

#print(df.head())