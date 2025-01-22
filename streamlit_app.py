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

listA = ['All'] + list(sorted(set(listA)))
listB = ['All'] + list(sorted(set(listB)))
listYear = ['All'] + list(sorted(set(listYear)))

st.title("Visualisation")

#listDataFrame = st.dataframe(df)

firstExpander = st.sidebar.expander('Filters')
yearFilterValue = firstExpander.selectbox("Year",
                        listYear
                        )
if yearFilterValue != "All":
    df = df[df['year']==yearFilterValue]
#if yearFilterValue == "All":
#    df = df[df['year']]

#listDataFrame = st.dataframe(df)

aFilterValue = firstExpander.selectbox("A",
                        listA
                        )
if aFilterValue != "All":
    df = df[df['A']==aFilterValue]


bFilterValue = firstExpander.selectbox("B",
                        listB
                        )
if bFilterValue != "All":
    df = df[df['B']==bFilterValue]

selectedDataFrame = st.dataframe(df,
                    key="data",
                    hide_index=True,
                    on_select="rerun",
                    selection_mode="single-row")


selectedRows = selectedDataFrame.selection.rows
filteredDf = df.iloc[selectedRows]

#st.dataframe(filteredDf)

if len(filteredDf) > 0 :
    expanderLabel = "Edit"
else :
    expanderLabel = "Add"

secondExpander = st.sidebar.expander(expanderLabel,
                    expanded=True)

#def formAdd() :
#    df['A'][0] = '5'

if len(filteredDf) > 0 :
    secondExpanderForm = secondExpander.form('Form2');
    secondExpanderForm.selectbox("A",
                            filteredDf['A'].unique()
                            );
    secondExpanderForm.selectbox("B",
                            filteredDf['B'].unique()
                            );
    secondExpanderForm.selectbox("Year",
                            filteredDf['year'].unique()
                            );                    
    secondExpanderForm.form_submit_button("Submit", None, None, None, None)
else:
    secondExpanderForm = secondExpander.form('Form2');
    listA[0] = "";
    secondExpanderForm.selectbox("A", listA);
    listB[0] = "";
    secondExpanderForm.selectbox("B", listB);
    listYear[0] = "";
    secondExpanderForm.selectbox("Year", listYear);                    
    secondExpanderForm.form_submit_button("Submit", None, None)

