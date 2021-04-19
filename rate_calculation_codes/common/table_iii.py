import numpy, pandas as pd

file = 'combined_pipelines.csv'
df = pd.read_csv(file)

df['cWB_VT_sen'] = df['cWB_N_rec']/df['N_tot']*df['VT_tot']
df['PyCBC_VT_sen'] = df['PyCBC_N_rec']/df['N_tot']*df['VT_tot']
df['GstLAL_VT_sen'] = df['GstLAL_N_rec']/df['N_tot']*df['VT_tot']


df2 = df[['M_tot', 'q', 'chieff', 
          'chip', 'SIM_ID', 
          'z', 'N_tot', 'VT_tot' , 
          'N_rec' , 'PyCBC_N_rec', 
          'GstLAL_N_rec', 'VT_sen',
          'GstLAL_VT_sen', 'PyCBC_VT_sen', 
          'cWB_VT_sen']]

df['R'] = df['R_n_0']
df['R'][6] = df['R_n_1'][6]
drop_bins = [0, 25, 30]
df2 = df.drop(drop_bins)

def f2(x):
  if x > 1 and x != 1.5:
    return "1/"+str(int(x))
  elif x == 1.5:
    return "2/3"
  else:
    return "1"

df2 = df2.round(2)
headers = ['M_tot', 'q', 'chieff', 'chip', 'SIM_ID', 'z', 'VT_sen', 'R'] 
print(df2.to_latex(index=False, 
                   columns=headers,
                   formatters={'q':f2}))

print(df2[headers].to_markdown(index=False))
