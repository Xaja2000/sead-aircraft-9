# Imported modules
import numpy as np
import matplotlib.pyplot as plt

# Variables
# Old
xcg = (np.arange(0,40,0.1)- 21.24) / 3.48
xac = (22.35 - 21.24)/ 3.48
sm = 0.05
clalphah = 4.64
clh = -0.58
c = 3.48
lh = 15.3

cmac = -0.12
clah = 0.95
clalphaah = 6.03

deda = 0.308

# Updated
xac_new = (22.46 - 21.24)/ 3.48
cmac_new = -0.11
clah_new = 1.14
clalphaah_new = 6.49

deda_new = 0.2685



# Old
y_cont = (xcg - xac + cmac / clah) * (clah / clh) * (c / lh)
y_stab = (xcg - xac + sm) * (clalphaah / clalphah) * (1 / (1 - deda)) * (c / lh)
y_stab_neut = (xcg - xac) * (clalphaah / clalphah) * (1 / (1 - deda)) * (c / lh)

# Updated
y_cont_up = (xcg - xac_new + cmac / clah_new) * (clah_new / clh) * (c / lh)
y_stab_up = (xcg - xac_new + sm) * (clalphaah_new / clalphah) * (1 / (1 - deda_new)) * (c / lh)
y_stab_neut_up = (xcg - xac_new) * (clalphaah_new / clalphah) * (1 / (1 - deda_new)) * (c / lh)



# Plot 
plt.plot(xcg, y_cont, label='Controllability line')
plt.plot(xcg, y_stab, label='Stability line')
plt.plot(xcg, y_stab_neut, label='Neutral stability line')

plt.plot(xcg, y_cont_up, label='Updated Controllability line', linestyle='-.', color='tab:blue')
plt.plot(xcg, y_stab_up, label='Updated Stability line', linestyle='-.', color='tab:orange')
plt.plot(xcg, y_stab_neut_up, label='Updated Neutral stability line', linestyle='-.', color='g')

plt.grid()
plt.title('Scissor Plot CRJ 1000')
plt.xlabel(r'$\frac{x_{c.g.}}{MAC} \, \mathrm{[-]}$', fontsize=15)
plt.ylabel(r'$\frac{S_{h}}{S} \, \mathrm{[-]}$', fontsize=15)
plt.ylim(0, 0.3)
plt.xlim(-0.3, 0.8)
plt.vlines(0.4255637069, 0, 1,linestyle='dashed', color='black', label='Main landing gear position')

#plt.vlines(-0.0384, 0, 1,linestyle='solid', color='red', label='Foward cg position')
#plt.vlines(0.4066, 0, 1,linestyle='solid', color='red', label='Aft cg position')
#plt.vlines(0.03628, 0, 1,linestyle='solid', color='red', label='Foward cg position')
#plt.vlines(0.5136, 0, 1,linestyle='solid', color='red', label='Aft cg position')

#plt.plot([0.03628, 0.5136], [0.2, 0.2],marker='x', color='red', label='C.g. range')
plt.plot([-0.0384, 0.4066], [0.2, 0.2],marker='x', color='red', label='C.g. range')
#plt.hlines(0.2, 0.03628, 0.5136, linestyle='x-', color='red', label='C.g. range')
#plt.hlines(0.2, 0.03628, 0.5136, linestyle='solid', color='black', label='C.g. range')
#plt.hlines(0.221, -0.0384, 0.8, linestyle='solid', color='green', label='Aft cg position')
plt.legend()



