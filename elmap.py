import pandas as pd
import json
import matplotlib.pyplot as plt
from pandas import json_normalize

class ElMap():
    def __init__(self):
        pass

    def get_data(self):
        data = pd.json_normalize(json.load(open('elproduction.json')))
        return data
    
    def make_plot(self):
        data = self.get_data()
        data.plot(x='datetime', y=['powerProductionTotal', 'powerProductionBreakdown.gas', 'powerProductionBreakdown.biomass', 'powerProductionBreakdown.coal','powerProductionBreakdown.wind', 'powerProductionBreakdown.solar'], kind='line')
        plt.gcf().autofmt_xdate()
        plt.savefig('static/images/elProduction.png')

if __name__ == "__main__":
    elmap = ElMap()
    data = elmap.get_data()
    print(data.to_string())
    #data.plot(x='datetime', y='powerProductionBreakdown.biomass', kind='line')
    #data.plot(x='datetime', y='powerProductionBreakdown.gas', kind='line')
    #data.plot(x='datetime', y='powerProductionTotal', kind='line')

    data.plot(x='datetime', y=['powerProductionTotal', 'powerProductionBreakdown.gas', 'powerProductionBreakdown.biomass', 'powerProductionBreakdown.coal','powerProductionBreakdown.wind', 'powerProductionBreakdown.solar'], kind='line')
    plt.gcf().autofmt_xdate()
    plt.show()    