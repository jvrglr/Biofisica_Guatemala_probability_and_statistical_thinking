# %%
%reset
import sys
import matplotlib
from scipy.optimize import curve_fit
from scipy import stats
from scipy.stats import pearsonr
from scipy.stats import linregress
import numpy as np
from numpy import exp as exp
from numpy import log as log
from numpy import sqrt as sqrt
import networkx as nx
import matplotlib.pyplot as plt
import time
import math
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.patches as patches
matplotlib.rcParams.update({'figure.autolayout': True})
matplotlib.rcParams['mathtext.fontset'] = 'custom'
matplotlib.rcParams['mathtext.rm'] = 'Bitstream Vera Sans'
matplotlib.rcParams['mathtext.it'] = 'Bitstream Vera Sans:italic'
matplotlib.rcParams['mathtext.bf'] = 'Bitstream Vera Sans:bold'
matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
matplotlib.rcParams.update({'font.size':12})
matplotlib.rcParams['axes.linewidth']=1 #Mattia had 2 -> Grosor del marco (doble del standard)
def Plot_bonito(xlabel=r" $ x$",ylabel=r"$ y$",label_font_size=15,ticks_size=12,y_size=2.4,x_size=3.2):
    plt.figure(figsize=(x_size,y_size))
    plt.tick_params(labelsize=24)
    plt.xlabel(xlabel,fontsize=label_font_size)
    plt.ylabel(ylabel,fontsize=label_font_size)
    plt.xticks(fontsize=ticks_size)
    plt.yticks(fontsize=ticks_size)
    plt.locator_params(axis="both", nbins=5,tight=True)
def axis_bonito(ax,xlabel=r" $ x$",ylabel=r"$ y$",label_font_size=15,ticks_size=12):
    ax.set_xlabel(xlabel,fontsize=label_font_size)
    ax.set_ylabel(ylabel,fontsize=label_font_size)
    ax.tick_params(axis="x", labelsize=ticks_size)
    ax.tick_params(axis="y", labelsize=ticks_size)
    # For two column figure that fits in one column of a two-columns paper:
        #fig, (ax1,ax2) = plt.subplots(1, 2,figsize=(4.2,1.8))
    # For three rows figure without space between plots:
        #fig, (ax1,ax2,ax3) = plt.subplots(3, 1,sharex=True,figsize=(2,3.6))
        #fig.tight_layout()
       # #-----plots--------
        # ax1.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False) #to remove x ticks in pdf file
        #plt.subplots_adjust(hspace=0)


#%%
d = pd.read_csv("/Users/javieraguilarsanchez/Documents/My_science/Lectures_notes/ICTP_school_Guatemala/datasets/galton-height.tab",sep="\t") # Load the dataset
children_height = d["height"].to_numpy()
boys_height = d[d["male"]==1.0]["height"].to_numpy()
father_heights = d['father'].to_numpy()
mother_heights = d['mother'].to_numpy()
midparent_heights = 0.5 * (father_heights + mother_heights)
var_children_height = np.var(children_height)
var_midparent_heights = np.var(midparent_heights)

Plot_bonito(ylabel="Children height (inches)",xlabel="Sample number",x_size=4,y_size=3)
permuted_height = np.random.permutation(children_height) # It seems that row data is ordered by height, so we permute it to have a better visualization
plt.scatter(np.arange(len(children_height)),permuted_height,s=2,alpha=0.5,marker="^",color="dodgerblue")
plt.savefig("../images_gifs_videos/row_data_galton_children_heights.pdf",bbox_inches='tight')
plt.show();plt.close()

# --- Compute Pearson correlation and regression ---
r, p = pearsonr(midparent_heights, children_height)
slope, intercept, r_value, p_value, std_err = linregress(midparent_heights, children_height)

# --- Print statistics ---
print(f"Pearson's r (height) = {r:.3f}, p = {p:.3e}")
print(f"Regression line (height): y = {slope:.3f}x + {intercept:.3f}")

# --- Make the plot ---
Plot_bonito(
    ylabel="Children height (inches)",
    xlabel="Midparent height (inches)",
    x_size=4,
    y_size=3
)

# Scatter plot of data
plt.scatter(midparent_heights, children_height, 
            s=5, alpha=0.8, marker="^", color="salmon", label="Data")

# Regression line
x_vals = np.linspace(min(midparent_heights), max(midparent_heights), 100)
y_vals = slope * x_vals + intercept
plt.plot(x_vals, y_vals, color="steelblue", linewidth=2,ls="--")
plt.savefig("../images_gifs_videos/row_data_galton_midparent_vs_children_heights.pdf", bbox_inches='tight')
plt.show()
plt.close()


Plot_bonito(xlabel="Children height (inches)",ylabel="Frequencies",x_size=4,y_size=3)
plt.hist(children_height,bins=10,alpha=0.5,color="dodgerblue")
mean = np.mean(children_height)
std = np.var(children_height)**0.5
plt.plot([mean,mean],[0,200],color="red",linestyle="--",label="Mean")
plt.savefig("../images_gifs_videos/histogram_galton_children_heights.pdf",bbox_inches='tight')
plt.show();plt.close()

Plot_bonito(xlabel="Boys height (inches)",ylabel="Frequencies",x_size=4,y_size=3)
plt.hist(boys_height,bins=15,alpha=0.5,color="dodgerblue")
mean = np.mean(boys_height)
std = np.var(boys_height)**0.5
plt.plot([mean,mean],[0,120],color="red",linestyle="--",label="Mean")
plt.savefig("../images_gifs_videos/histogram_galton_boys_heights.pdf",bbox_inches='tight')
plt.show();plt.close()



# %% Correlation of midparent and children deviations from the mean height
# --- Compute Pearson correlation and regression ---
r, p = pearsonr(midparent_heights, var_children_height)
slope, intercept, r_value, p_value, std_err = linregress(midparent_heights, var_children_height)

# --- Print statistics ---
print(f"Pearson's r (height) = {r:.3f}, p = {p:.3e}")
print(f"Regression line (height): y = {slope:.3f}x + {intercept:.3f}")

# --- Make the plot ---
Plot_bonito(
    ylabel="Children height (inches)",
    xlabel="Midparent height (inches)",
    x_size=4,
    y_size=3
)

# Scatter plot of data
plt.scatter(midparent_heights, var_children_height, 
            s=5, alpha=0.8, marker="^", color="salmon", label="Data")

# Regression line
x_vals = np.linspace(min(midparent_heights), max(midparent_heights), 100)
y_vals = slope * x_vals + intercept
plt.plot(x_vals, y_vals, color="steelblue", linewidth=2,ls="--")
plt.savefig("../images_gifs_videos/row_data_galton_midparent_vs_var_children_heights.pdf", bbox_inches='tight')
plt.show()
plt.close()