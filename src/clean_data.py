import pandas as pd
import zipfile
from time import sleep

def read_data_compute_df(data_file):
    # Read zipped file
    print("Reading zipped file...")
    zf = zipfile.ZipFile(data_file)
    # Parse csv content without unzipping
    df = pd.read_csv(zf.open(str(13100111)+'.csv'),low_memory=False)
    sleep(2)
    print("Done")
    return df

def main():
    file_name = "2JbKmPs"
    cancer_df = read_data_compute_df(file_name)
    print("Cleaning data...")
    clean_cancer_df = cancer_df.drop(columns = 
                                    ["DGUID", "UOM_ID","UOM", "SCALAR_ID","VECTOR","COORDINATE","STATUS",\
                                    "TERMINATED","DECIMALS","SYMBOL"])
    clean_cancer_df.rename(columns={'Age group':'Age_group'}, inplace=True)
    sleep(3)
    print("Done")
    print("Cleaning NaN values...")
    clean_cancer_df.dropna(inplace=True, subset=['REF_DATE','GEO','Age_group','Sex','Primary types of cancer (ICD-O-3)','Characteristics','SCALAR_FACTOR','VALUE'])
    sleep(3)
    print("Done")
    print("Creating new csv file to visualize the cleanup...")
    clean_cancer_df.to_csv(file_name+"_clean.csv", index=False)
    sleep(2)
    print("Done")


if __name__ == "__main__":
    main()