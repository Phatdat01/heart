import plotly.graph_objects as go
import numpy as np
import plotly.express as px
import pandas as pd
from tkinter import Tk
from IPython.core.display import HTML

win= Tk()
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

def semicircle(r, h, k):
    x0 = h - r  # determine x start
    x1 = h + r  # determine x finish
    x = np.linspace(x0, x1, 10000)  # many points to solve for y

    # use numpy for array solving of the semicircle equation
    y = k + np.sqrt(abs(r**2 - (x - h)**2))  
    return x, y

def textVector(df):
    df2=pd.DataFrame()
    #L
    for i in np.arange(0,0.4,0.01):
      df2=pd.concat([df2, pd.DataFrame.from_records([{'x': 0,'y':0,'z':i}])])
    for i in np.arange(0,0.2,0.01):
      df2=pd.concat([df2, pd.DataFrame.from_records([{'x': i,'y':0,'z':0}])])
    #
    for i in np.arange(0,0.2,0.01):
      df2=pd.concat([df2, pd.DataFrame.from_records([{'x': 0.3,'y':0,'z':i}])])
    for i in np.arange(0.3,0.35,0.01):
      df2=pd.concat([df2, pd.DataFrame.from_records([{'x': 0.3,'y':0,'z':i}])])
    #
    for i in np.arange(0,0.24,0.01):
      df2=pd.concat([df2, pd.DataFrame.from_records([{'x': 0.4,'y':0,'z':i}])])
    for i in np.arange(0,0.125,0.01):
      df2=pd.concat([df2, pd.DataFrame.from_records([{'x': 0.566,'y':0,'z':i}])])
    x, y = semicircle(0.083, 0.483, 0.25/2)
    dfTemp=pd.DataFrame()
    dfTemp['x']=x
    dfTemp['y']=0
    dfTemp['z']=y
    df2 = pd.concat([df2, dfTemp])
    #
    for i in np.arange(0,0.4,0.01):
      df2=pd.concat([df2, pd.DataFrame.from_records([{'x':  0.666,'y':0,'z':i}])])
    for i in np.arange(0,0.125,0.01):
      df2=pd.concat([df2, pd.DataFrame.from_records([{'x': 0.832,'y':0,'z':i}])])
    x, y = semicircle(0.083, 0.749, 0.25/2)
    dfTemp=pd.DataFrame()
    dfTemp['x']=x
    dfTemp['y']=0
    dfTemp['z']=y
    df2 = pd.concat([df2, dfTemp])
    #
    df2['x']=df2['x']-0.832/2
    df = pd.concat([df, df2])
    return df


def get_zvalue(a, b, x, y):
    constant = x ** 2 + ((1 + b) * y) ** 2 - 1
    c0 = constant ** 3
    c1 = 0.0
    c2 = 3 * (constant ** 2)
    c3 = -(a * (y ** 2) + x ** 2)
    c4 = 3 * constant
    c5 = 0.0
    c6 = 1.0

    coefficients = [c6, c5, c4, c3, c2, c1, c0]
    rts = np.roots(coefficients)
    z = rts[~np.iscomplex(rts)]

    if len(z) > 0:
        zreal = z.real
        return zreal
    else:
        return []

def importData(a, b, grid):
    x = np.arange(-2, 2, grid)
    y = x

    all_triplets = []
    for i in x:
        for j in y:
            zaxis = get_zvalue(a, b, i, j)
            for k in zaxis:
                triplet = [i, j, k]
                all_triplets.append(triplet)
    results = np.array(all_triplets).transpose()

    # Save the triplets in a data frame
    xaxis = results[0]
    yaxis = results[1]
    zaxis = results[2]
    df = pd.DataFrame({'x': xaxis, 'y': yaxis, 'z': zaxis})
    df=textVector(df)
    return df

def draw_heart(palette='viridis'):
    df=importData(9/200,0.01, 0.10)
    # Draw
    fig = go.Figure(data=px.scatter_3d(df, x='x', y='y', z='z',
                                       color='z',
                                       color_continuous_scale=palette,
                                       height=screen_height, width=screen_width,
                                       template="plotly_dark"))

    fig.update(layout_coloraxis_showscale=False)

    fig.update_layout(
        # title='$\hbox{A Perfect Valentine: } (x^2 + (1+b)^2y^2 +z^2 -1)^3 -(x^2 +ay^2 )z^3$',
        scene=dict(
            xaxis=dict(showticklabels=False, showgrid=False,visible=False),
            yaxis=dict(showticklabels=False, showgrid=False,visible=False),
            zaxis=dict(showticklabels=False, showgrid=False,visible=False)),hovermode=False
        )
    fig.show()

draw_heart(palette='twilight')