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
# %%
throws = 20
heads = np.zeros(throws)
for i in range(throws):
    coin = np.random.binomial(n=1, p=0.5)
    heads[i] = coin

Plot_bonito(xlabel="Number of throws", ylabel="Outcomes")
plt.scatter(range(throws), heads, s=10)
plt.yticks([0, 1], ["Tails", "Heads"])
plt.xticks([0,5,10,15,20])
plt.savefig("../images_gifs_videos/coin_flips_outcomes.pdf")
plt.show();plt.close()

n_heads = np.sum(heads)
n_tails = throws-n_heads
p =  n_heads/throws
std = sqrt(p*(1-p))
var = std**2
plt.hist(heads, bins=[-0.5,0.5,1.5], density=True)
# %%

# --- Parameters ---
throws = 20
heads = np.zeros(throws)

# --- Simulate coin tosses ---
for i in range(throws):
    coin = np.random.binomial(n=1, p=0.5)
    heads[i] = coin

# --- Compute stats ---
n_heads = np.sum(heads)
n_tails = throws - n_heads
p_heads = n_heads / throws
p_tails = n_tails / throws

# --- Data for bars ---
expected = [0.5, 0.5]
sampled = [p_tails, p_heads]
labels = ["Tails", "Heads"]
x = np.arange(2)
bar_width = 0.35

# --- Plot ---
Plot_bonito(xlabel="Outcome", ylabel="Probability")

plt.bar(x - bar_width/2, expected, width=bar_width,
        color="lightgray", edgecolor="black", alpha=0.7, label="Expected (p=0.5)")
plt.bar(x + bar_width/2, sampled, width=bar_width,
        color="#66c2a5", edgecolor="black", label=f"Sampled ({throws} throws)")

plt.xticks(x, labels)
plt.ylim(0, 1)
plt.legend(frameon=False)

plt.tight_layout()
plt.savefig("../images_gifs_videos/coin_flip_probabilities.pdf", bbox_inches="tight")
plt.show()
plt.close()
