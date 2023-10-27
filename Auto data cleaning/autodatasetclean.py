import pandas as pd
import numpy as np
import os
from scipy import stats

files = [f for f in os.listdir() if(os.path.isfile(f))]
fileTypes = (".csv", "xlsx")


for file in files:
    if(not file.lower().endswith(fileTypes)): continue
    
    # Convert into dataframe
    data = pd.read_csv(file) if(file.endswith(".csv")) else pd.read_excel(file)
    data.dropna(inplace=True)

    # Try create a results folder
    try: os.mkdir("Results")
    except: pass
    
    # Save results in the correct format
    saveLoc = "Results/cleaned_"+file
    try: data.to_csv(saveLoc) if(file.endswith(".csv")) else data.to_excel(saveLoc)
    except: pass
    
    
