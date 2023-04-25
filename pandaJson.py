import pandas as pd
import json
import matplotlib.pyplot as plt
from pandas import json_normalize

data = pd.json_normalize(json.load(open('elprod.json')))
print(data.to_string())
df = pd.read_json('elprod.json')
print(df.to_string())

df1 = df['datetime']
print(df1.to_string())



#data.plot(x='datetime', y='powerProductionTotal', kind='line')
data.plot(x='datetime', y='powerProductionBreakdown.biomass', kind='line')
plt.show()



