import pandas as pd
import zipfile

def read_data_compute_df(data_file):
    # Read zipped file
    zf = zipfile.ZipFile(data_file)
    # Parse csv content without unzipping
    df = pd.read_csv(zf.open(str(13100111)+'.csv'),low_memory=False)
    
    return df


file_name = "2JbKmPs"
cancer_df = read_data_compute_df(file_name)

clean_cancer_df = cancer_df.drop(columns = 
                                    ["DGUID", "UOM_ID","UOM", "SCALAR_ID","VECTOR","COORDINATE","STATUS",\
                                    "TERMINATED","DECIMALS","SYMBOL"])
#print(clean_cancer_df.info())
#print(clean_cancer_df.describe())
#print(clean_cancer_df.columns)
#print(clean_cancer_df.isnull().values.any())
#print(clean_cancer_df.isnull().sum().sum())

# Rename column
clean_cancer_df.rename(columns={'Age group':'Age_group'}, inplace=True)