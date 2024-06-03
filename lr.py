from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
from pandas import Series, DataFrame

data = pd.read_csv('my-progress.csv')
fig = make_subplots(
    rows=2, cols=1,
    subplot_titles=('Weight', 'Measurements')
    )

# Add weight vs. time
fig.add_trace(
    go.Scatter(
        x=list(data.index),
        y=data['Weight'],
        mode='lines+markers+text',
        line=dict(color='cyan', width=3),
        marker=dict(size=4, symbol='circle-x',
            line=dict(width=2, color='DarkSlateGrey')),
        text=data['Weight'],
        textposition='bottom center',
        name='Weight'
    ),
    row=1, col=1
)

# Add waistline vs. time
fig.add_trace(
    go.Scatter(
        x=list(data.index),
        y=data['Waist (in.)'],
        mode='lines+markers+text',
        line=dict(color='royalblue', width=3),
        marker=dict(size=4, symbol='star-triangle-up',
            line=dict(width=2, color='white')),
        text=data['Waist (in.)'],
        textposition='bottom center',
        name='Waist (in.)'
    ),
    row=2, col=1
)

# Add hip size vs. time
fig.add_trace(
    go.Scatter(
        x=list(data.index),
        y=data['Hips (in.)'],
        mode='lines+markers+text',
        line=dict(color='skyblue', width=3),
        marker=dict(size=4, symbol='circle', 
            line=dict(width=2, color='DarkSlateGrey')),
        text=data['Hips (in.)'],
        textposition='bottom center',
        name='Hips (in.)'
    ),
    row=2, col=1
)

fig.update_xaxes(title_text="Weeks")

fig.update_yaxes(title_text="Lbs.", row=1, col=1)
fig.update_yaxes(title_text="Inches", row=2, col=1)

fig.update_layout(
    title_text='12-Week Transformation and Progress'
    )

fig.show()