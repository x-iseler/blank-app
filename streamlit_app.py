from turtle import onclick
import streamlit as st
import pandas as pd
import pandas as pdAll

df = pd.DataFrame({
    'A':[0,1,2,3,4,5,6,7,8,9],
    'B':[10,11,12,13,14,15,16,17,18,19],
    'year':['->2022','2023','->2022','2023','2024','2025','2024','2025','2024','2025']
    })

dfAll = pdAll.DataFrame({
    'A':['All'],
    'B':['All'],
    'year':['All']
    })


st.title("Visualisation")

st.dataframe(df)

firstExpander = st.sidebar.expander('test 1')

firstExpander.selectbox("Year",
                        df['year'].unique()
                        )
firstExpander.selectbox("A",
                        df['A'].unique()
                        )
firstExpander.button("Filter", "2", None, None, None,None)
firstExpander.selectbox("B",
                        df['B'].unique()
                        )
firstExpander.button("Filter", "3", None, None, None,None)

secondExpander = st.sidebar.expander('test 2')

secondExpanderForm = secondExpander.form('Form2')

secondExpanderForm.selectbox("A",
                        df['A'].unique()
                        )
secondExpanderForm.selectbox("B",
                        df['B'].unique()
                        )
secondExpanderForm.selectbox("Year",
                        df['year'].unique()
                        )
secondExpanderForm.form_submit_button("Submit", None, None, None, None)

