#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: xhwan

import math



class einHEA:
    def __init__(self, name, number, radius):
        self.name = name
        self.number = number
        self.radius = radius



Ga = einHEA('Ga', 0, 126)
Fe = einHEA('Fe', 0, 125)
Mn = einHEA('Mn', 0, 139)
Cu = einHEA('Cu', 0, 138)
Ni = einHEA('Ni', 0, 121)
Ti = einHEA('Ti', 0, 136)
In = einHEA('In', 0, 144)
Rh = einHEA('Rh', 0, 135)
Sn = einHEA('Sn', 27, 141)
Pt = einHEA('Pt', 0, 128)
Pd = einHEA('Pd', 27, 131)
Ru = einHEA('Ru', 0, 126)
Au = einHEA('Au', 0, 144)
Zn = einHEA('Zn', 0, 131)

N_all = Ga.number + Fe.number + Mn.number + Cu.number + Ni.number + Ti.number + In.number + Rh.number + Sn.number + \
        Pt.number + Pd.number + Ru.number + Au.number + Zn.number
print(N_all)


R_ave = (Ga.number*Ga.radius + Fe.number*Fe.radius + Mn.number*Mn.radius + Cu.number*Cu.radius + Ni.number*Ni.radius + \
        Ti.number*Ti.radius + In.number*In.radius + Rh.number*Rh.radius + Sn.number*Sn.radius + Pt.number*Pt.radius +
         Pd.number*Pd.radius + Ru.number*Ru.radius + Au.number*Au.radius + Zn.number*Zn.radius)/N_all
print(R_ave)

N = Ga.number*math.pow((1-Ga.radius/R_ave), 2) + Fe.number*math.pow((1-Fe.radius/R_ave), 2) + \
    Mn.number*math.pow((1-Mn.radius/R_ave), 2) + Cu.number*math.pow((1-Cu.radius/R_ave), 2) + \
    Ni.number*math.pow((1-Ni.radius/R_ave), 2) + Ti.number*math.pow((1-Ti.radius/R_ave), 2) + \
    In.number*math.pow((1-In.radius/R_ave), 2) + Rh.number*math.pow((1-Rh.radius/R_ave), 2) + \
    Sn.number*math.pow((1-Sn.radius/R_ave), 2) + Pt.number*math.pow((1-Pt.radius/R_ave), 2) + \
    Pd.number*math.pow((1-Pd.radius/R_ave), 2) + Ru.number*math.pow((1-Ru.radius/R_ave), 2) + \
    Au.number*math.pow((1-Au.radius/R_ave), 2) + Zn.number*math.pow((1-Zn.radius/R_ave), 2)

N_d = N/N_all

delta = math.sqrt(N_d)

print(delta)