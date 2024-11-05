# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:16:32 2020

@author: ikulikov
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import rc
import numpy as np

exp_data_1 = pd.read_csv('E2+_Kr.txt', sep="	", header=None)
exp_data_3 = pd.read_csv('E2+_Sr.txt', sep="	", header=None)
exp_data_5 = pd.read_csv('E2+_Zr.txt', sep="	", header=None)
exp_data_7 = pd.read_csv('E2+_Mo.txt', sep="	", header=None)

exp_data_1.columns = ["Z","A","N", "E2+", "E4+"]
exp_data_3.columns = ["Z","A","N", "E2+", "E4+"]
exp_data_5.columns = ["Z","A","N", "E2+", "E4+"]
exp_data_7.columns = ["Z","A","N", "E2+", "E4+"]

a=0
fig, ax = plt.subplots(1)
#ax.errorbar(exp_data_1["N"], exp_data_1["E2+"], fmt='--o', elinewidth=2, c='red')
#ax.errorbar(exp_data_3["N"], exp_data_3["E2+"], fmt='--o', elinewidth=2, c='green')
ax.errorbar(exp_data_5["N"], exp_data_5["E2+"], fmt='--o', elinewidth=2, c='black')
#ax.errorbar(exp_data_7["N"], exp_data_7["E2+"], fmt='--o', elinewidth=2, c='black')
#ax.text(63.0 ,1100 , '$\ _{36}Kr$' , rotation=0, fontsize=15,  color='red')
#ax.text(63.0 ,1300 , '$\ _{38}Sr$' , rotation=0, fontsize=15,  color='green')
ax.text(61.0 ,1500 , '$\ _{40}Zr$' , rotation=0, fontsize=15,  color='black')
#ax.text(63.0 ,1700 , '$\ _{42}Mo$' , rotation=0, fontsize=15,  color='black')
#exp_data.plot('Nuclei','mass2', c='k', marker='o',ax=ax)
#exp_data.plot.scatter('Nuclei','mass2', yerr='err2', c='b', marker='o',ax=ax)
#ax.fill_between(exp_data["Nuclei"],upper_limit1,lower_limit2, color='c')
#exp_data.plot('Nuclei',"mass2", yerr='err2', c='yellow', marker='*', ax=ax)
ax.xaxis.set_ticks(np.arange(56, 63, 1))

ax.set_xlabel('Neutron number N',fontsize=20)
ax.set_ylabel('E(2$^+$) (keV)',fontsize=20)
plt.tick_params(
    bottom=True,      # ticks along the bottom edge are off
    top=True,
    right=True,          # ticks along the top edge are off
    labelbottom=True) # labels along the bottom edge are off
#ax.set_xlabel("   ",fontsize=20)

#ax.text(4.0,40,  ' TOF-ICR', ha='center', va='center', rotation=0, fontsize=12, )
#plt.text(1, -85,'orange - ISOLTRAP \n blue - AME2016',fontsize=9)

#plt.title('$\ ^{70} $As ToF-ICR',fontsize=25)
#ax.legend(('fit','data'),loc='lower right')
#plt.text(-2.3, 80,'T$\ _{rf.}$= 100 ms',fontsize=9)
#plt.text(-2, 123,'$\ ^{70} As\ ^{+}$',fontsize=20)
#ax.xaxis.set_ticks(np.arange(-2, 2.5, 0.5))
#ax.yaxis.set_ticks(np.arange(80, 130, 5))
plt.tight_layout()
plt.savefig("E2+_Zr.pdf")
plt.show()