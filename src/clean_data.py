import pandas as pd
import zipfile

def read_data_compute_df(data_file):
    # Read zipped file
    zf = zipfile.ZipFile(data_file)
    # Parse csv content without unzipping
    df = pd.read_csv(zf.open(str(13100111)+'.csv'),low_memory=False)
    
    return df


file_name = "2JbKmPs"
cancer_data = read_data_compute_df(file_name)

clean_cancer_data = cancer_data.drop(columns = 
                                    ["DGUID", "UOM_ID","UOM", "SCALAR_ID","VECTOR","COORDINATE","STATUS",\
                                    "TERMINATED","DECIMALS","SYMBOL"])
print(clean_cancer_data.head())