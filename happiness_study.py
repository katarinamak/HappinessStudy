import pandas as pd
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

from plotly.offline import download_plotlyjs, init_notebook_mode, plot

# read from a csv file
df = pd.read_csv("./WorldHappinessData/2019.csv")
otherdf = pd.read_csv("/Users/katarinamakivic/Downloads/Refactored_Py_DS_ML_Bootcamp-master/09-Geographical-Plotting"
                      "/2014_World_GDP")

df['Code'] = otherdf['CODE'].values
# write to a csv file
# df.to_csv('/Users/katarinamakivic/Downloads/World Happiness data/2019.csv', index=False)
#
# write to Excel file
# df.to_excel('/Users/katarinamakivic/Downloads/Excel_Sample.xlsx', sheet_name='NewSheet')

print(df)
# data variable
fig = go.Figure(data=go.Choropleth(
    locations=df['Code'],
    z=df['Score'],
    text=df['Country or region'],
    colorscale='Reds',
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar={'title': 'Happiness Score'}
))

# layout variable
fig.update_layout(title='2019 World Happiness Study',
                  geo=dict(showframe=False,
                           projection={'type': 'equirectangular'}))

# fig.show()

plt.figure(0)
sns.pairplot(df)
plt.show()

variables = ['GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices',
             'Generosity', 'Perceptions of corruption']

correlations = []
for i in variables:
    correlations.append(df['Score'].corr(df[i]))

print("The following table shows the correlation between the happiness score of a country and all the other factors "
      "considered. The goal of this is to see which factors have the greatest impact on a nation's happiness.")
corr_table = pd.DataFrame(correlations, variables, columns=['correlation'])
print(corr_table)
