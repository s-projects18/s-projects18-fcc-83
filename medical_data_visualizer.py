import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv",  index_col=0)
# [0a] check NaN
# Any time a variable is set to 'None', make sure to set it to the correct code.
#for k in df.columns:
#  print(k, df[k].unique())
# no 'None' here...

# [0b] Clean the data 
# Filter out the following patient segments that represent incorrect data:
# diastolic pressure is higher then systolic (Keep the correct data with df['ap_lo'] <= df['ap_hi']))
f_diast = (df['ap_lo'] <= df['ap_hi']) # correct

# height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
f_height = (df['height'] >= df['height'].quantile(0.025))

# height is more than the 97.5th percentile
f_height2 = (df['height'] <= df['height'].quantile(0.975))

# weight is less then the 2.5th percentile
f_weight = (df['weight'] >= df['weight'].quantile(0.025))

# weight is more than the 97.5th percentile
f_weight2 = (df['weight'] <= df['weight'].quantile(0.975))

cond = (~f_diast | ~f_height | ~f_height2 | ~f_weight | ~f_weight2)
# index must be set for df!
df.drop(index = df[cond].index, inplace=True) 


# [1] Add 'overweight' column
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

# [2] Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
f_chol = (df["cholesterol"]>1)
f_gluc = (df["gluc"]>1)

# this works cause f_chol is yet executed and not modified
# if we would execute f_chol again, all values would be: 0
df.loc[f_chol, "cholesterol"] = 1
#f_chol = (df["cholesterol"]>1) # wrong
df.loc[~f_chol, "cholesterol"] = 0

df.loc[f_gluc, "gluc"] = 1
df.loc[~f_gluc, "gluc"] = 0


# [3] Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = None


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat = None

    # Draw the catplot with 'sns.catplot()'



    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# [4] Draw Heat Map
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
