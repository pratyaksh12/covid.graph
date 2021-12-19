import pandas as PD
import plotly_express as PX

df=PD.read_csv('covid.csv')
fig=PX.scatter(df,x='date',y='cases',color='country')
fig.show()