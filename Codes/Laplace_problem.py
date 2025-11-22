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
# %% Possible uncertainty scenarios in Laplace's problem
p_m = 0.5097
ps = np.linspace(0.495,0.52,1000)
sigma_1 = 0.0001
n1 = 1/(np.pi*sigma_1**2*2)*exp(-((ps - p_m)**2)/(2*sigma_1**2))
Plot_bonito(xlabel=r"$ p$", ylabel=r"$ P(p)$", x_size=2.5, y_size=2)
plt.plot(ps,n1,color="black")
plt.plot([p_m,p_m],[0, max(n1)], linestyle="--", color="red")
plt.yscale("log")
plt.yticks([])
plt.xticks([0.5,p_m,0.52],[0.5,r"$\hat{p}$",0.52])
plt.savefig("../images_gifs_videos/Laplace_problem_S1.pdf", bbox_inches='tight', transparent=True)
plt.show();plt.close()

ps = np.linspace(0.4,0.6,1000)
sigma_2 = 0.15
n2 = 1/(np.pi*sigma_2**2*2)*exp(-((ps - p_m)**2)/(2*sigma_2**2))
Plot_bonito(xlabel=r"$ p$", ylabel=r"$ P(p)$", x_size=2.5, y_size=2)
plt.plot(ps,n2,color="black")
plt.plot([p_m,p_m],[0, max(n2)], linestyle="--", color="red")
plt.xticks([0.4,0.5,0.6],[0.4,0.5,0.6])
plt.yticks([])
plt.savefig("../images_gifs_videos/Laplace_problem_S2.pdf", bbox_inches='tight', transparent=True)
plt.show();plt.close()

# %% Posterior using flat distribution as prior
N = 493472
nb = 251527
ps = np.linspace(0.495,0.52,1000)
dp = ps[1] - ps[0]
posterior = exp(log(ps)*nb + log(1 - ps)*(N - nb)+342054) #+342054 to avoid underflow
Z = np.sum(posterior)*dp
posterior = posterior / Z
p_m = 0.5097 #Method of moments
print("normalized=", np.sum(posterior)*dp)
Plot_bonito(xlabel=r"$ p$", ylabel=r"$ P(p|N_b)$", x_size=2.5, y_size=2)
plt.plot(ps,posterior,color="black",lw=1)
plt.plot([p_m,p_m],[0, max(posterior)], linestyle="--", color="red",lw=1)
plt.savefig("../images_gifs_videos/Laplace_problem_posterior_flat_prior.pdf", bbox_inches='tight', transparent=True)
plt.show();plt.close()
# %%
