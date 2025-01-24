import streamlit as st
import pandas as pd
import numpy as np

listA = [0,1,2,3,4,5,6,7,0,1,2,3]
listB = [10,11,12,13,14,15,16,17,10,11,12,13]
listYear =          ['->2022','2023','->2022','2023','2024','2025','2024','2025', '2023','2024','2025','2024']
listBrand =         ['Nokia', 'Nokia', 'Nokia', 'Nokia', 'Microsoft', 'Microsoft', 'Microsoft', 'Microsoft', 'BlackBerry', 'BlackBerry', 'BlackBerry', 'BlackBerry']
listCommName =      ['3210', '3310', '3310 plus', '3310 max', 'MS 3210', 'MS 3310', 'MS 3310 plus', 'MS 3310 max', 'BB 3210', 'BB 3310', 'BB 3310 plus', 'BB 3310 max']
listModel =         ['3210B', '3310B', '3310P', '3310M', 'MS32B', 'MS33B', 'MS33P', 'MS33M', 'BB32B', 'BB33B', 'BB33P', 'BB33M']
list4gUSA =         ['NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES']
listpSim =          ['1', '1', '1', '2', '1', '1', '1', '2', '1', '1', '1', '2']
listeSim =          ['0', '0', '1', '1', '0', '0', '1', '1', '0', '0', '1', '1']
listVoLTEFR =       ['NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES']
listVoLTERoaming =  ['NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES']
listVoWifi =        ['NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES']
listEVS =           ['NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES']
listLTEInterband =  ['NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES']
listLTEUL =         ['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A']
listWifi =          ['N/A', '5', '6', '7', 'N/A', '5', '6', '7', 'N/A', '5', '6', '7']
listNRCA =          ['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A']
listNRCASA =        ['', '', '', '', '', '', '', '', '', '', '', '']
list5gSA =          ['UPD', 'UPD', 'UPD', 'UPD', 'UPD', 'UPD', 'UPD', 'UPD', 'N/A', 'N/A', 'N/A', 'N/A']
listVoNR =          ['NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES']
listmmWave =        ['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A']
listSMSoIMS =       ['NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES']
listVVMnative =     ['NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES', 'NO', 'YES']
listComment =       ['comm2', 'comm3', 'comm4', 'comm5', 'commmentaire ...', 'commmentaire ...', 'commmentaire ...', 'commmentaire ...', 'commmentaire ...', 'commmentaire ...', 'commmentaire ...', 'Full option total max']


df = pd.DataFrame({
    'A':listA,
    'B':listB,
    'year':listYear,
    'Brand':listBrand,
    'Commercial Name':listCommName,
    'Model':listModel,
    '4G USA':list4gUSA,
    'nb pSIM':listpSim,
    'nb eSIM':listeSim,
    'VoLTE FR':listVoLTEFR,
    'VoLTE Roaming':listVoLTERoaming,
    'VoWifi':listVoWifi,
    'EVS':listEVS,
    'LTE INTERBAND UPLINK CA':listLTEInterband,
    'LTE UL 256 QAM (Without NR)':listLTEUL,
    'Wifi':listWifi,
    'NR CA N78 + N28':listNRCA,
    'NR CA in SA 78 + 28':listNRCASA,
    '5G SA':list5gSA,
    'VoNR':listVoNR,
    'mmWave':listmmWave,
    'SMSoIMS':listSMSoIMS,
    'VVM Native':listVVMnative,
    'Comment':listComment
    })

listA = ['All'] + list(sorted(set(listA)))
listB = ['All'] + list(sorted(set(listB)))
listYear = ['All'] + list(sorted(set(listYear)))
listBrand = ['All'] + list(sorted(set(listBrand)))
listCommName = ['All'] + list(sorted(set(listCommName)))
listModel = ['All'] + list(sorted(set(listModel)))

st.title("Visualisation")

#listDataFrame = st.dataframe(df)

firstExpander = st.sidebar.expander('Filters')

yearFilterValue = firstExpander.selectbox("Year",
                        listYear
                        )
if yearFilterValue != "All":
    df = df[df['year']==yearFilterValue]

brandFilterValue = firstExpander.selectbox("Brand",
                        listBrand
                        )
if brandFilterValue != "All":
    df = df[df['Brand']==brandFilterValue]

modelFilterValue = firstExpander.selectbox("Model",
                        listModel
                        )
if modelFilterValue != "All":
    df = df[df['Model']==modelFilterValue]

#if yearFilterValue == "All":
#    df = df[df['year']]

#listDataFrame = st.dataframe(df)

#aFilterValue = firstExpander.selectbox("A",
#                        listA
#                        )
#if aFilterValue != "All":
#    df = df[df['A']==aFilterValue]

#bFilterValue = firstExpander.selectbox("B",
#                        listB
#                        )
#if bFilterValue != "All":
#    df = df[df['B']==bFilterValue]

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
listYear = [""] + listYear;
listBrand = [""] + listBrand
listCommName = [""] + listCommName
listModel = [""] + listModel
list4gUSA = [""] + list4gUSA
listpSim = [""] + listpSim
listeSim = [""] + listeSim
listVoLTEFR = [""] + listVoLTEFR
listVoLTERoaming = [""] + listVoLTERoaming
listVoWifi = [""] + listVoWifi
listEVS = [""] + listEVS
listLTEInterband = [""] + listLTEInterband
listLTEUL = [""] + listLTEUL
listWifi = [""] + listWifi
listNRCA = [""] + listNRCA
listNRCASA = [""] + listNRCASA
list5gSA = [""] + list5gSA
listVoNR = [""] + listVoNR
listmmWave = [""] + listmmWave
listSMSoIMS = [""] + listSMSoIMS
listVVMnative = [""] + listVVMnative
listComment = [""] + listComment

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


def formSubmitButtonClicked() :
    #selectedRows = selectedDataFrame.selection.rows
    #filteredDf = df.iloc[selectedRows]
    #filteredDf
    #selectedA
    #selectedB
    #selectedYear
    if len(selectedRows) > 0 :
        filteredDf['A'] = "15"
        filteredDf['B'] = selectedB;
        filteredDf['Year'] = selectedYear;
        #df.iloc[selectedRows] = filteredDf
        #df
        
        #selectedDataFrame.update(selection=filteredDf)
        #df.update(df)
        #df.iloc[selectedRows] = [{'':selectedRows, 'A':selectedA, 'B':selectedB, 'year':selectedYear}]
        #['A':selectedA, 'B':selectedB, 'year':selectedYear]


secondExpanderForm = secondExpander.form('Form2');
selectedA = secondExpanderForm.selectbox("A", listA, index=selectedARowsIndex);
selectedB = secondExpanderForm.selectbox("B", listB, index=selectedBRowsIndex);
selectedYear = secondExpanderForm.selectbox("Year", listYear, index=selectedYearRowsIndex);                    
secondExpanderForm.form_submit_button("Submit", None, on_click=formSubmitButtonClicked)

