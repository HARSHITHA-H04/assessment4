import pandas as pd
import numpy as np

data = {'name':['Jai','Price','Gaurav','Anuj'],
         'age':['5','10','7','6'],
         'Qualification':['Msc','MA','MCA','Phd']}

df = pd.DataFrame.from_dict(data)
df
