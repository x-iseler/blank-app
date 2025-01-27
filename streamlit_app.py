import streamlit as st
import pandas as pd
import numpy as np

#listA = [0,1,2,3,4,5,6,7,0,1,2,3]
#listB = [10,11,12,13,14,15,16,17,10,11,12,13]
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
    #'A':listA,
    #'B':listB,
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

#listA = ['All'] + list(sorted(set(listA)))
#listB = ['All'] + list(sorted(set(listB)))
listYear = ['All'] + list(sorted(set(listYear)))
listBrand = ['All'] + list(sorted(set(listBrand)))
listCommName = ['All'] + list(sorted(set(listCommName)))
listModel = ['All'] + list(sorted(set(listModel)))
list4gUSA = ['All'] + list(sorted(set(list4gUSA)))
listpSim = ['All'] + list(sorted(set(listpSim)))
listeSim = ['All'] + list(sorted(set(listeSim)))
listVoLTEFR = ['All'] + list(sorted(set(listVoLTEFR)))
listVoLTERoaming = ['All'] + list(sorted(set(listVoLTERoaming)))
listVoWifi = ['All'] + list(sorted(set(listVoWifi)))
listEVS = ['All'] + list(sorted(set(listEVS)))
listLTEInterband = ['All'] + list(sorted(set(listLTEInterband)))
listLTEUL = ['All'] + list(sorted(set(listLTEUL)))
listWifi = ['All'] + list(sorted(set(listWifi)))
listNRCA = ['All'] + list(sorted(set(listNRCA)))
listNRCASA = ['All'] + list(sorted(set(listNRCASA)))
list5gSA = ['All'] + list(sorted(set(list5gSA)))
listVoNR = ['All'] + list(sorted(set(listVoNR)))
listmmWave = ['All'] + list(sorted(set(listmmWave)))
listSMSoIMS = ['All'] + list(sorted(set(listSMSoIMS)))
listVVMnative = ['All'] + list(sorted(set(listVVMnative)))
listComment = ['All'] + list(sorted(set(listComment)))


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

with st.container(border=True):
    selectedDataFrame = st.dataframe(df,
                    use_container_width=False,
                    key="data",
                    hide_index=True,
                    on_select="rerun",
                    selection_mode="single-row",
                    )





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

#listA[0] = "";
#listB[0] = "";
listYear[0] = "";
listBrand[0] = "";
listCommName[0] = "";
listModel[0] = "";
list4gUSA[0] = "";
listpSim[0] = "";
listeSim[0] = "";
listVoLTEFR[0] = "";
listVoLTERoaming[0] = "";
listVoWifi[0] = "";
listEVS[0] = "";
listLTEInterband[0] = "";
listLTEUL[0] = "";
listWifi[0] = "";
listNRCA[0] = "";
listNRCASA[0] = "";
list5gSA[0] = "";
listVoNR[0] = "";
listmmWave[0] = "";
listSMSoIMS[0] = "";
listVVMnative[0] = "";
listComment[0] = "";

selectedRowsIndex = 0
#if len(filteredDf) > 0 :
#    selectedRowsIndex = selectedRows[0]+1

#selectedARowsIndex = 0
#if len(filteredDf) > 0 :
#    i = 0
#    for x in listA :
#        if listA[i] == list(filteredDf['A'])[0] :
#            selectedARowsIndex = i
#        i = i + 1

#selectedBRowsIndex = 0
#if len(filteredDf) > 0 :
#    i = 0
#    for x in listB :
#        if listB[i] == list(filteredDf['B'])[0] :
#            selectedBRowsIndex = i
#        i = i + 1

selectedYearRowsIndex = 0
if len(filteredDf) > 0 :
    i = 0
    for x in (listYear) :
        if listYear[i] == str(list(filteredDf['year'])[0]) :
            selectedYearRowsIndex = i
        i = i + 1

selectedBrandRowsIndex = 0
if len(filteredDf) > 0 :
    i = 0
    for x in (listBrand) :
        if listBrand[i] == str(list(filteredDf['Brand'])[0]) :
            selectedBrandRowsIndex = i
        i = i + 1

selectedCommNameRowsIndex = 0
if len(filteredDf) > 0 :
    i = 0
    for x in (listCommName) :
        if listCommName[i] == str(list(filteredDf['Commercial Name'])[0]) :
            selectedCommNameRowsIndex = i
        i = i + 1

selectedModelRowsIndex = 0
if len(filteredDf) > 0 :
    i = 0
    for x in (listModel) :
        if listModel[i] == str(list(filteredDf['Model'])[0]) :
            selectedModelRowsIndex = i
        i = i + 1

selected4gUSARowsIndex = 0
if len(filteredDf) > 0 :
    i = 0
    for x in (list4gUSA) :
        if list4gUSA[i] == str(list(filteredDf['4G USA'])[0]) :
            selected4gUSARowsIndex = i
        i = i + 1

selectedpSimRowsIndex = 0
if len(filteredDf) > 0 :
    i = 0
    for x in (listpSim) :
        if listpSim[i] == str(list(filteredDf['nb pSIM'])[0]) :
            selectedpSimRowsIndex = i
        i = i + 1

selectedeSimRowsIndex = 0
if len(filteredDf) > 0 :
    i = 0
    for x in (listeSim) :
        if listeSim[i] == str(list(filteredDf['nb eSIM'])[0]) :
            selectedeSimRowsIndex = i
        i = i + 1

selectedVoLTEFRRowsIndex = 0
if len(filteredDf) > 0 :
    i = 0
    for x in (listVoLTEFR) :
        if listVoLTEFR[i] == str(list(filteredDf['VoLTE FR'])[0]) :
            selectedVoLTEFRRowsIndex = i
        i = i + 1

selectedVoLTERoamingRowsIndex = 0
if len(filteredDf) > 0 :
    i = 0
    for x in (listVoLTERoaming) :
        if listVoLTERoaming[i] == str(list(filteredDf['VoLTE Roaming'])[0]) :
            selectedVoLTERoamingRowsIndex = i
        i = i + 1

selectedVoWifiRowsIndex = 0
if len(filteredDf) > 0 :
    i = 0
    for x in (listVoWifi) :
        if listVoWifi[i] == str(list(filteredDf['VoWifi'])[0]) :
            selectedVoWifiRowsIndex = i
        i = i + 1

selectedEVSRowsIndex = 0
if len(filteredDf) > 0 :
    i = 0
    for x in (listEVS) :
        if listEVS[i] == str(list(filteredDf['EVS'])[0]) :
            selectedEVSRowsIndex = i
        i = i + 1

selectedLTEInterbandRowsIndex = 0
if len(filteredDf) > 0 :
    i = 0
    for x in (listLTEInterband) :
        if listLTEInterband[i] == str(list(filteredDf['LTE INTERBAND UPLINK CA'])[0]) :
            selectedLTEInterbandRowsIndex = i
        i = i + 1

selectedLTEULRowsIndex = 0
if len(filteredDf) > 0 :
    i = 0
    for x in (listLTEUL) :
        if listLTEUL[i] == str(list(filteredDf['LTE UL 256 QAM (Without NR)'])[0]) :
            selectedLTEULRowsIndex = i
        i = i + 1

selectedWifiRowsIndex = 0
if len(filteredDf) > 0 :
    i = 0
    for x in (listWifi) :
        if listWifi[i] == str(list(filteredDf['Wifi'])[0]) :
            selectedWifiRowsIndex = i
        i = i + 1

selectedNRCARowsIndex = 0
if len(filteredDf) > 0 :
    i = 0
    for x in (listNRCA) :
        if listNRCA[i] == str(list(filteredDf['NR CA N78 + N28'])[0]) :
            selectedNRCARowsIndex = i
        i = i + 1

selectedNRCASARowsIndex = 0
if len(filteredDf) > 0 :
    i = 0
    for x in (listNRCASA) :
        if listNRCASA[i] == str(list(filteredDf['NR CA in SA 78 + 28'])[0]) :
            selectedNRCASARowsIndex = i
        i = i + 1

selected5gSARowsIndex = 0
if len(filteredDf) > 0 :
    i = 0
    for x in (list5gSA) :
        if list5gSA[i] == str(list(filteredDf['5G SA'])[0]) :
            selected5gSARowsIndex = i
        i = i + 1

selectedVoNRRowsIndex = 0
if len(filteredDf) > 0 :
    i = 0
    for x in (listVoNR) :
        if listVoNR[i] == str(list(filteredDf['VoNR'])[0]) :
            selectedVoNRRowsIndex = i
        i = i + 1

selectedmmWaveRowsIndex = 0
if len(filteredDf) > 0 :
    i = 0
    for x in (listmmWave) :
        if listmmWave[i] == str(list(filteredDf['mmWave'])[0]) :
            selectedmmWaveRowsIndex = i
        i = i + 1

selectedSMSoIMSRowsIndex = 0
if len(filteredDf) > 0 :
    i = 0
    for x in (listSMSoIMS) :
        if listSMSoIMS[i] == str(list(filteredDf['SMSoIMS'])[0]) :
            selectedSMSoIMSRowsIndex = i
        i = i + 1

selectedVVMnativeRowsIndex = 0
if len(filteredDf) > 0 :
    i = 0
    for x in (listVVMnative) :
        if listVVMnative[i] == str(list(filteredDf['VVM Native'])[0]) :
            selectedVVMnativeRowsIndex = i
        i = i + 1

selectedCommentRowsIndex = 0
if len(filteredDf) > 0 :
    i = 0
    for x in (listComment) :
        if listComment[i] == str(list(filteredDf['Comment'])[0]) :
            selectedCommentRowsIndex = i
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
#selectedA = secondExpanderForm.selectbox("A", listA, index=selectedARowsIndex);
#selectedB = secondExpanderForm.selectbox("B", listB, index=selectedBRowsIndex);
selectedYear = secondExpanderForm.selectbox("Year", listYear, index=selectedYearRowsIndex);
selectedBrand = secondExpanderForm.selectbox("Brand", listBrand, index=selectedBrandRowsIndex);
selectedCommName = secondExpanderForm.selectbox("Commercial Name", listCommName, index=selectedCommNameRowsIndex);
selectedModel = secondExpanderForm.selectbox("Model", listModel, index=selectedModelRowsIndex);
selected4gUSA = secondExpanderForm.selectbox("4G USA", list4gUSA, index=selected4gUSARowsIndex);
selectedpSim = secondExpanderForm.selectbox("nb pSIM", listpSim, index=selectedpSimRowsIndex);
selectedeSim = secondExpanderForm.selectbox("nb eSIM", listeSim, index=selectedeSimRowsIndex);
selectedVoLTEFR = secondExpanderForm.selectbox("VoLTE FR", listVoLTEFR, index=selectedVoLTEFRRowsIndex);
selectedVoLTERoaming = secondExpanderForm.selectbox("VoLTE Roaming", listVoLTERoaming, index=selectedVoLTERoamingRowsIndex);
selectedVoWifi = secondExpanderForm.selectbox("VoWifi", listVoWifi, index=selectedVoWifiRowsIndex);
selectedEVS = secondExpanderForm.selectbox("EVS", listEVS, index=selectedEVSRowsIndex);
selectedLTEInterband = secondExpanderForm.selectbox("LTE INTERBAND UPLINK CA", listLTEInterband, index=selectedLTEInterbandRowsIndex);
selectedLTEUL = secondExpanderForm.selectbox("LTE UL 256 QAM (Without NR)", listLTEUL, index=selectedLTEULRowsIndex);
selectedWifi = secondExpanderForm.selectbox("Wifi", listWifi, index=selectedWifiRowsIndex);
selectedNRCA = secondExpanderForm.selectbox("NR CA N78 + N28", listNRCA, index=selectedNRCARowsIndex);
selectedNRCASA = secondExpanderForm.selectbox("NR CA in SA 78 + 28", listNRCASA, index=selectedNRCASARowsIndex);
selected5gSA = secondExpanderForm.selectbox("5G SA", list5gSA, index=selected5gSARowsIndex);
selectedVoNR = secondExpanderForm.selectbox("VoNR", listVoNR, index=selectedVoNRRowsIndex);
selectedmmWave = secondExpanderForm.selectbox("mmWave", listmmWave, index=selectedmmWaveRowsIndex);
selectedSMSoIMS = secondExpanderForm.selectbox("SMSoIMS", listSMSoIMS, index=selectedSMSoIMSRowsIndex);
selectedVVMnative = secondExpanderForm.selectbox("VVM Native", listVVMnative, index=selectedVVMnativeRowsIndex);
selectedComment = secondExpanderForm.selectbox("Comment", listComment, index=selectedCommentRowsIndex);                    
secondExpanderForm.form_submit_button("Submit", None, on_click=formSubmitButtonClicked)

