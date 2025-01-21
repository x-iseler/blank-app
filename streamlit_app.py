import streamlit as st
import pandas as pd
import numpy as np

listA = [0,1,2,3,4,5,6,7,8,9]
listB = [10,11,12,13,14,15,16,17,18,19]
listYear = ['->2022','2023','->2022','2023','2024','2025','2024','2025','2024','2025']

df = pd.DataFrame({
    'A':listA,
    'B':listB,
    'year':listYear
    })

st.title("Visualisation")

listA = ['All'] + list(sorted(set(listA)))
listB = ['All'] + list(sorted(set(listB)))
listYear = ['All'] + list(sorted(set(listYear)))

st.dataframe(df)

firstExpander = st.sidebar.expander('test 1')
firstExpander.selectbox("Year",
                        listYear
                        )
firstExpander.selectbox("A",
                        listA
                        )
firstExpander.button("Filter", "2", None, None, None,None)
firstExpander.selectbox("B",
                        listB
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

