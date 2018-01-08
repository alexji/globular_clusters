import pandas as pd
import numpy as np
from astropy.io import ascii

def load_master_table():
    df1 = ascii.read("mwgc1.dat").to_pandas()
    df1.index = df1["ID"]
    df2 = ascii.read("mwgc2.dat").to_pandas()
    df2.index = df2["ID"]
    df3 = ascii.read("mwgc3.dat").to_pandas()
    df3.index = df3["ID"]
    df = pd.concat([df1,df2,df3], axis=1)
    return df

if __name__=="__main__":
    df = load_master_table()

