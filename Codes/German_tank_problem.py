# %%
%reset
import sys
import matplotlib
from scipy.optimize import curve_fit
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
# %% Naive version: continuous numbers with repetitions
n_experiments = 20
N = 100000 #number of tanks
ns = np.logspace(1,3,n_experiments) #number of observed tanks
N_moments = np.zeros(n_experiments)
N_MLE = np.zeros(n_experiments)
for i in range(n_experiments):
    observations = np.random.uniform(0,N,round(ns[i]))
    max_observation = np.max(observations) #MLE estimator
    mean_observations = np.mean(observations) #Method of moments estimator
    N_MLE[i] = max_observation
    N_moments[i] = 2*mean_observations
err_MLE = np.abs(N_MLE - N)/N
err_moments = np.abs(N_moments - N)/N

Plot_bonito(xlabel=r"$ n/N $", ylabel=r" $|\hat{N}-N|/N$", x_size=3, y_size=2)
plt.scatter(ns/N, err_moments, label="moments", color="blue", s=10)
plt.plot(ns/N, err_moments, color="blue", lw=1)
plt.scatter(ns/N, err_MLE, label="MLE", color="red", s=10, marker="s")
plt.plot(ns/N, err_MLE, color="red", lw=1)
plt.xscale("log")
plt.yscale("log")

# ---- NEW: create a separate legend figure, do NOT add legend to main plot ----
handles, labels = plt.gca().get_legend_handles_labels()

fig_leg = plt.figure()
fig_leg.legend(handles, labels, loc='center', frameon=False, fontsize=12)
fig_leg.savefig("../images_gifs_videos/German_tank_legend.pdf",
                bbox_inches='tight', transparent=True)
plt.close(fig_leg)
# -----------------------------------------------------------------------------#

# NOTE: no plt.legend() here, so main PDF has no legend
plt.savefig("../images_gifs_videos/German_tank_naive_problem_comparison.pdf",
            bbox_inches='tight', transparent=True)
plt.show(); plt.close()


