# -*- coding: utf-8 -*-
"""O3_IMBH_Paper_Tables.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DVRUTEHf4NmSOhh_EI-K8Nf8pdC8qnzO
"""

import pylab, pandas as pd, numpy
from IPython.display import display, Math, Latex

"""### Table I"""

events = ['GW190521',
         'S200114f',
         'S200214br']

GPS_Time = ['1242442967.5', 
            '1263002916.2',
            '1265755544.5',]

PyCBC_IFAR = [726.65, #https://ldas-jobs.gw.iucaa.in/~koustav.chandra/o3/production/imbh/a2_INITIAL/7._open_box_result/7.02_loudest_events_followup/#A51
              1.159e-3, #https://ldas-jobs.ligo-wa.caltech.edu/~veronica.villa/o3/production/imbh/a8_INITIAL/7._open_box_result/#A2
              numpy.nan] # Not found in box 8

pycbc_livetime = 0.7466364303822118
PyCBC_FAP = []
for ifar in PyCBC_IFAR:
  PyCBC_FAP.append(1 - numpy.exp(-pycbc_livetime/ifar))


# The cWB and GstLAL results are obtained from the table 
# https://git.ligo.org/publications/O3/o3-cbc-burst-imbh/-/wikis/IMBH-candidate-events

cWB_IFAR = [4903.45, 
           17.27,
           7.61]
cWB_livetime = 0.7343

cWB_FAP = []
for ifar in cWB_IFAR:
  cWB_FAP.append(1-numpy.exp(-cWB_livetime/ifar))

GstLAL_IFAR = [518.2,
               2.78e-5,
               numpy.nan]

GstLAL_FAP = [0.001685,
              1,
              numpy.nan]

table_1 = pd.DataFrame()

table_1['Events'] = events
table_1['GPS Time'] = GPS_Time

table_1['PyCBC IFAR'] = PyCBC_IFAR
table_1['PyCBC FAR'] = 1/table_1['PyCBC IFAR']
table_1['PyCBC FAP'] = PyCBC_FAP

table_1['cWB IFAR'] = cWB_IFAR
table_1['cWB FAR'] = 1/table_1['cWB IFAR']
table_1['cWB FAP'] = cWB_FAP

table_1['GstLAL IFAR'] = GstLAL_IFAR
table_1['GstLAL FAR'] = 1/table_1['GstLAL IFAR']
table_1['GstLAL FAP'] = GstLAL_FAP

table_1['min FAP'] =  table_1[['cWB FAP','PyCBC FAP', 'GstLAL FAP']].min(axis=1)
trials_factor = 3
table_1['Combined FAP'] = 1 - numpy.power((1- table_1['min FAP']),trials_factor)
table_1['Detectors'] = ['HLV', 'HLV', 'HL']

def f1(x):
  if numpy.isnan(x):
    return '-'
  elif x < 1:
    x = "{:.1E}".format(x)
    a = str(x).replace('E-0', r'\times 10^{-') + '}' 
    return '$'+str(a) + '$'
  elif x > 1:
    x = "{:.1E}".format(x)
    a = str(x).replace('E+0', r'\times 10^{+') + '}' 
    return '$'+str(a) + '$'
headers = ['Events', 
           'GPS Time', 
           'cWB FAR',
           'PyCBC FAR', 
           'GstLAL FAR',
           'Combined FAP']

print(table_1.to_latex(index=False,
                       columns=headers, 
                       formatters={'cWB FAR' : f1,
                                   'PyCBC FAR': f1,
                                   'GstLAL FAR' : f1,
                                   'Combined FAP':f1},
                       escape=False))

"""### Table II"""

event = ['GW190408\_181802',
         'GW190413\_052954',
         'GW190413\_134308',
         'GW190421\_213856',
         'GW190503\_185404',
         'GW190512\_180714',
         'GW190513\_205428',
         'GW190514\_065416',
         'GW190517\_055101',
         'GW190519\_153544',
         'GW190521',
         'GW190521\_074359',
         'GW190602\_175927',
         'GW190701\_203306',
         'GW190706\_222641',
         'GW190727\_060333',
         'GW190731\_140936',
         'GW190803\_022701',
         'GW190828\_063405',
         'GW190915\_235702',
         'GW190929\_012149']

cWB_FAR = [9.5e-4,
           numpy.nan,
           numpy.nan,
           3.0e-1,
           1.8e-3,
           8.8e-3,
           numpy.nan,
           numpy.nan,
           8.0e-3,
           3.061e-4,
           2.039e-4,
           1.0e-4,
           1.5e-2,
           0.32,
           1.0e-3,
           8.8e-2,
           numpy.nan,
           numpy.nan,
           9.6e-4,
           1.0e-4,
           numpy.nan
           ]

PyCBC_FAR = [2.5e-5,
             numpy.nan,
             numpy.nan,
             1.9,
             3.7e-2,
             3.8e-5,
             3.7e-4,
             numpy.nan,
             1.8e-2,
             1.8e-5,
             1.1,
             1.8e-5,
             numpy.nan,
             numpy.nan,
             6.7e-5,
             3.5e-5,
             numpy.nan,
             numpy.nan,
             1.0e-5,
             8.6e-4,
             numpy.nan
             ] 

PyCBC_BBH_FAR = [7.9e-5,
                 7.2e-2,
                 4.4e-2,
                 6.6e-3,
                 7.9e-5,
                 5.7e-5,
                 5.7e-5,
                 0.53,
                 5.7e-5,
                 5.7e-5,
                 numpy.nan,
                 5.7e-5,
                 1.5e-2,
                 numpy.nan,
                 4.6e-5,
                 3.7e-5,
                 0.28,
                 2.7e-2,
                 3.3e-5,
                 3.3e-5,
                 numpy.nan
                 ]

PyCBC_IMBH_FAR = [1.6e-2,
                  0.56,
                  0.14,
                  6.1e-3,
                  2.5e-3,
                  39.87,
                  5.0e-2,
                  1.12,
                  8.7e-4,
                  1.1e-4,
                  1.4e-3,
                  2.3e-5,
                  1.1e-3,
                  1.93e-4,
                  1.1e-4,
                  1.2e-4,
                  0.64,
                  0.17,
                  7.0e-5,
                  3.8e-4,
                  0.31]

GstLAL_FAR = [1.0e-5,
              numpy.nan,
              0.38,
              7.7e-4,
              1.0e-5,
              1.0e-5,
              1.0e-5,
              numpy.nan,
              9.6e-4,
              1.0e-5,
              1.2e-3,
              1.0e-5,
              1.1e-5,
              1.1e-2,
              1.0e-5,
              1.0e-5,
              0.21,
              3.2e-2,
              1.0e-5,
              1.0e-5,
              2.0e-2]

GstLAL_IMBH_FAR = [1.0e-5,
                   5.4e3,
                   1.2e3,
                   1.8,
                   0.17,
                   1.0e-5,
                   0.21,
                   7.6e2,
                   2.7e-2,
                   3.9e-3,
                   1.9e-3,
                   1.0e-5,
                   1.0e-5,
                   3.8e-2,
                   2.4e-3,
                   4.5e-4,
                   2.1,
                   3.0,
                   1.0e-5,
                   0.47,
                   2.9e1]

table_2 = pd.DataFrame()
table_2['Event'] = event
table_2['cWB FAR'] = cWB_FAR
table_2['PyCBC Broad FAR'] = PyCBC_FAR
table_2['PyCBC BBH FAR'] = PyCBC_BBH_FAR
table_2['PyCBC Heavy FAR'] = PyCBC_IMBH_FAR
table_2['GstLAL FAR'] = GstLAL_FAR
table_2['GstLAL IMBH FAR'] = GstLAL_IMBH_FAR

GstLAL_Ta = 0.874
table_2['PyCBC FAP'] = 1-numpy.exp(-table_2['PyCBC Heavy FAR']*pycbc_livetime)
table_2['cWB FAP'] = 1-numpy.exp(-table_2['cWB FAR']*cWB_livetime)
table_2['GstLAL FAP'] = 1-numpy.exp(-table_2['GstLAL IMBH FAR']*GstLAL_Ta)

table_2['min FAP'] =  table_2[['cWB FAP','PyCBC FAP', 'GstLAL FAP']].min(axis=1)
trials_factor = 3
table_2['Combined FAP'] = 1 - numpy.power((1- table_2['min FAP']),trials_factor)


def f2(x):
  if (x == 2.5e-5 or x ==1.8e-5 
      or x == 1.0e-5 or x == 7.9e-5 
      or x == 5.7e-5 or x == 3.3e-5 
      or x == 1.0e-4 or x == 1.0e-3 
      or x == 9.6e-4):
    x = "{:.1E}".format(x)
    a = str(x).replace('E-0', r'\times 10^{-') + '}' 
    return '$<'+str(a) + '$'
  elif numpy.isnan(x):
    return '-'
  elif (x < 1):
    x = "{:.1E}".format(x)
    a = str(x).replace('E-0', r'\times 10^{-') + '}'
    return '$'+str(a) + '$'
  elif (x > 1):
    x = "{:.1E}".format(x)
    a = str(x).replace('E+0', r'\times 10^{+') + '}'
    return '$'+str(a) + '$'
    
def f3(x):
  if x < 1.0e-4:
    return r'$ < 1.0 \times 10^{-4}$'
  elif (x < 1):
    x = "{:.1E}".format(x)
    a = str(x).replace('E-0', r'\times 10^{-') + '}'
    return '$'+str(a) + '$'
  elif (x > 1):
    x = "{:.1E}".format(x)
    a = str(x).replace('E+0', r'\times 10^{+') + '}'
    return '$'+str(a) + '$'

headers = ['Event', 
           'cWB FAR', 
           'PyCBC Broad FAR',
           'PyCBC BBH FAR',
           'PyCBC Heavy FAR',
           'GstLAL FAR',
           'GstLAL IMBH FAR',
           'Combined FAP']

print(table_2.to_latex(index=False,
                       columns=headers, 
                       formatters={'cWB FAR' : f2,
                                   'PyCBC Broad FAR': f2,
                                   'PyCBC BBH FAR' : f2,
                                   'PyCBC Heavy FAR': f2,
                                   'GstLAL FAR' : f2,
                                   'GstLAL IMBH FAR' : f2,
                                   'Combined FAP': f3},
                       escape=False))