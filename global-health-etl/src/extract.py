import requests
import pandas as pd


def extract_data():
    # extact data from the source
    api_url =  "https://huggingface.co/api/datasets/deepset/covid_qa_deepset/parquet/covid_qa_deepset/train"

    #making a get request to the api url
    response = requests.get(api_url)
    response.raise_for_status()  # check if the request was successful
    
    #get the json which is just a list of dictionaries with the url of the parquet file
    data = response.json()
    
    # get the url of the parquet file
    parquet_url = data[0]
    print(f"Downloading parquet from: {parquet_url}")
    
    # read the parquet file and convert it to a pandas dataframe
    df = pd.read_parquet(parquet_url)
    
    print(f"Dataframe extracted successfully. Shape: {df.shape}")
    return df

if __name__ == "__main__":
    df = extract_data()
    print(df.head())

