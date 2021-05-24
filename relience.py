import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('RELIANCE.NS.csv')
print(df)

po= df.iloc[1:,1]
ph= df.iloc[1:,2]
pl= df.iloc[1:,3]
pc= df.iloc[1:,4]


plt.plot(pc, label="previous close")
plt.plot(po, label="previous open")
plt.plot(ph, label="high")
plt.plot(pl, label="low")
plt.legend()

plt.show()