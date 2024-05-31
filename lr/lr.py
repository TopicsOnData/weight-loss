from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
from pandas import Series, DataFrame

data = pd.read_csv('my-progress.csv')
fig = make_subplots(rows=2, cols=1)

# Add weight vs. time
fig.add_trace(go.Scatter(
        x=list(data.index),
        y=data['Weight'],
        line=dict(color='cyan', width=3),
        marker=dict(size=4, symbol='circle-x',
            line=dict(width=2, color="DarkSlateGrey")),
        mode='lines+markers',
        name='Weight'
    ),
    row=1, col=1
)

# Add waistline vs. time
fig.add_trace(go.Scatter(
        x=list(data.index),
        y=data['Waist (in.)'],
        line=dict(color='royalblue', width=3),
        marker=dict(size=4, symbol='star-triangle-up',
            line=dict(width=2, color="white")),
        mode='lines+markers',
        name='Waist (in.)'
    ),
    row=2, col=1
)

# Add hip size vs. time
fig.add_trace(go.Scatter(
        x=list(data.index),
        y=data['Hips (in.)'],
        line=dict(color='skyblue', width=3),
        marker=dict(size=4, symbol='circle', 
            line=dict(width=2, color="DarkSlateGrey")),
        mode='lines+markers',
        name='Hips (in.)'
    ),
    row=2, col=1
)

fig.show()