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

listA[0] = "";
listB[0] = "";
listYear[0] = "";

selectedRowsIndex = 0
#if len(filteredDf) > 0 :
#    selectedRowsIndex = selectedRows[0]+1

selectedARowsIndex = 0
if len(filteredDf) > 0 :
    i = 0
    for x in listA :
        if listA[i] == list(filteredDf['A'])[0] :
            selectedARowsIndex = i
        i = i + 1

selectedBRowsIndex = 0
if len(filteredDf) > 0 :
    i = 0
    for x in listB :
        if listB[i] == list(filteredDf['B'])[0] :
            selectedBRowsIndex = i
        i = i + 1

selectedYearRowsIndex = 0
if len(filteredDf) > 0 :
    i = 0
    for x in (listYear) :
        if listYear[i] == str(list(filteredDf['year'])[0]) :
            selectedYearRowsIndex = i
        i = i + 1


#if len(filteredDf) > 0 :
#    secondExpanderForm = secondExpander.form('Form2');
#    secondExpanderForm.selectbox("A",
#                            filteredDf['A'].unique()
#                            );
#    secondExpanderForm.selectbox("B",
#                            filteredDf['B'].unique()
#                            );
#    secondExpanderForm.selectbox("Year",
#                            filteredDf['year'].unique()
#                            );                    
#    secondExpanderForm.form_submit_button("Submit", None, None, None, None)
#else:
secondExpanderForm = secondExpander.form('Form2');
secondExpanderForm.selectbox("A", listA, index=selectedARowsIndex);
secondExpanderForm.selectbox("B", listB, index=selectedBRowsIndex);
secondExpanderForm.selectbox("Year", listYear, index=selectedYearRowsIndex);                    
secondExpanderForm.form_submit_button("Submit", None, None)

