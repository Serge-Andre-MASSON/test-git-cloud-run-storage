from io import BytesIO
import streamlit as st
from google.cloud import storage
import pandas as pd


client = storage.Client()

BUCKET_NAME = "artifacts.test-git-cloud-run-storage.appspot.com"
BUCKET = client.bucket(BUCKET_NAME)
DATA_ACCESS = 'google clood'

st.write("hello streamlit!")
path = "data/famille.csv"
csv_path  = BytesIO(BUCKET.blob(path).download_as_bytes())
famille = pd.read_csv(csv_path)
st.write(famille)

