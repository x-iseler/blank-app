import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'A':[0,1,2,3,4,5,6,7,8,9],
    'B':[10,11,12,13,14,15,16,17,18,19],
    'year':['->2022','2023','->2022','2023','2024','2025','2024','2025','2024','2025']
    })

st.title("Visualisation")


st.dataframe(df)

