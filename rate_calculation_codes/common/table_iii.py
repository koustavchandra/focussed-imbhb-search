import numpy, pandas as pd

file = 'combined_pipelines.csv'
df = pd.read_csv(file)

def nsf(num):
    """2-Significant Figures"""
    #print(float(numstr))
    return ("%.2g" % num)

def f2(x):
  if x > 1 and x != 1.5:
    return "1/"+str(int(x))
  elif x == 1.5:
    return "2/3"
  else:
    return "1"

def f3(x):
  return ("%d" % x)

def f4(x):
  if x == 0.00:
    return ("%d" % x)
  else:
    return ("%.2g" % x)  

df['mtotal'] = df['mass1_source'] + df['mass2_source']    
df['q'] = df['mass1_source'] / df['mass2_source']

headers = ['mtotal', 'q', 'chi_eff', 'chi_p', 'sim_id', 'max_redshift', 'VT_sen', 'R'] 
df2 = df.round(2)
print(df2.to_latex(index=False, 
                   columns=headers,
                   formatters={'mtotal': f3, 'chi_eff' : f4, 'chi_p' : f4, 'q':f2, 'VT_sen' : nsf, 'R':nsf}))
