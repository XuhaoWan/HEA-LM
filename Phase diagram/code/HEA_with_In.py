#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: xhwan

#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: xhwan

#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: xhwan

#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: xhwan

from itertools import combinations
import math
import pandas as pd
import numpy as np


file_name = 'data.csv'

names = ['ID','enthalpy']
data = pd.read_csv(file_name, names=names)
data['ID'].astype('string')
data['enthalpy'].astype('float')


num_elements = 10
ratio = 1/num_elements


class einHEA:
    def __init__(self, name, number, radius):
        self.name = name
        self.number = number
        self.radius = radius

Ga = einHEA('Ga', 100, 126)
Fe = einHEA('Fe', 100, 125)
Co = einHEA('Co', 100, 126)
Ni = einHEA('Ni', 100, 121)
Cu = einHEA('Cu', 100, 138)
Mn = einHEA('Mn', 100, 139)
Ru = einHEA('Ru', 100, 126)
Rh = einHEA('Rh', 100, 135)
Pd = einHEA('Pd', 100, 131)
Pt = einHEA('Pt', 100, 128)
In = einHEA('In', 100, 144)
Sn = einHEA('Sn', 100, 141)
Mg = einHEA('Mg', 100, 130)
Au = einHEA('Au', 100, 144)
Ag = einHEA('Ag', 100, 153)
W = einHEA('W', 100, 146)
Cr = einHEA('Cr', 100, 127)



HEA_e_list = [Fe, Co, Ni, Cu, Mn, Mg, Au, Ag, W, Cr]
HEA_list = list(combinations(HEA_e_list, num_elements-1))

In = (In,)

for i in range(len(HEA_list)):
    HEA_list[i] = In + HEA_list[i]


N_all = num_elements*100

R_ave = 0

S_all = 0
for i in range(num_elements):
    S_all += 100*math.log(ratio)

S = S_all/N_all

dS = -S * (8.314/96488)
print(dS)

deltas = []
HEAIDs = []
Hs = []
Ss = []
for HEA in HEA_list:
    HEA_name = ''
    R_all = 0
    N = 0
    delta = 0
    for HEA_e in HEA:
        R_all += HEA_e.number*HEA_e.radius
        HEA_name += HEA_e.name

    R_ave = R_all/N_all
    for HEA_e in HEA:
        N += HEA_e.number*math.pow((1-HEA_e.radius/R_ave), 2)
    N_d = N / N_all
    delta = math.sqrt(N_d)
    delta = delta*100
    HEAIDs.append(HEA_name)
    deltas.append(delta)
    Ss.append(dS)

    Energy_e_list = list(combinations(HEA, 2))
    e_name = ''
    H = 0
    for Energy_e in Energy_e_list:
        e_name = Energy_e[0].name + Energy_e[1].name
        E0 = data[data.ID == e_name].values[0][1]
        E = 4*E0*ratio*ratio
        H = H + E
    Hs.append(H)

HEAIDs = np.array(HEAIDs)
Hs= np.array(Hs)
deltas = np.array(deltas)
Ss = np.array(Ss)
name1='HEAIDs'+str(num_elements)+'.txt'
name2='Hs'+str(num_elements)+'.txt'
name3='deltas'+str(num_elements)+'.txt'
name4='Ss'+str(num_elements)+'.txt'
np.savetxt(name1, HEAIDs,  fmt='%s')
np.savetxt(name2, Hs,  fmt='%s')
np.savetxt(name3, deltas,  fmt='%s')
np.savetxt(name4, Ss,  fmt='%s')

