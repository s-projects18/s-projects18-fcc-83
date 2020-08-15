import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
# calculate their BMI by dividing their weight in kilograms by the square of their height in meters. 
df['bmi'] = df['weight'] * 10000 / (df['height']*df['height'])
f_bad = (df['bmi'] > 25)    # > 25 then the person is overweight
df['overweight'] = 0        # 0 for NOT overweight
# SettingWithCopyWarning
# - df['overweight'].loc[f_bad] = 1
# - df['overweight'][f_bad] = 1 
# https://www.dataquest.io/blog/settingwithcopywarning/
# use loc instead
df.loc[f_bad, 'overweight'] = 1 # 1 for overweight


print(df)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = None


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat = None

    # Draw the catplot with 'sns.catplot()'



    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None



    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
