#from asyncio.windows_events import NULL
import streamlit as st
import pandas as pd
#from tqdm import tqdm

df_counted = []
df_expected = []
#st.set_page_config(initial_sidebar_state="collapsed")
rad =st.sidebar.radio("Menu",["Fuente de Datos","Analisis","Proceso","Acerca del EJ3"])
st.sidebar.info(
        "Esta aplicacion fue diseñada para resolver el **ejercicio 3** de "
        "la ultima clase "
        "[reclamos](https://galarzavictor-mojix-bootcamp-v2-discrepancy-fmi9qv.streamlitapp.com/) o "
        "el codigo fuente [source code](https://galarzavictor-mojix-bootcamp-v2-finance01-mrasnr.streamlitapp.com/). "
    )
if rad == "Fuente de Datos":
    st.title("Captura - Fuente de Datos")
    st.markdown('''
    ## Diariamente debe obtener un respaldo de los siguientes archivos...
    [Download Expected](https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Expected.csv)

    [Download Counted](https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Counted.csv)
    ''', unsafe_allow_html=True)

if rad == "Analisis":
    if df_expected == []:
        df_expected = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Expected.csv", encoding="latin-1")
        #df_expected = pd.read_csv("..\..\Streamlit\stock_inventory\Expected.csv", encoding="latin-1") # df_ICC
    if df_counted == []:
        df_counted = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Counted.csv", encoding="latin-1")
        #df_counted = pd.read_csv("..\..\Streamlit\stock_inventory\Counted.csv", encoding="latin-1") # df_SOH
        #st.session_state["df_counted"] = df_counted
        #df_counted = st.session_state["df_counted"]
    st.markdown("<h2 style='text-align: center; color: blue;'>Tabla Expected</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: left; color: blue;'>Filtro:</h3>", unsafe_allow_html=True)
    st.markdown("""---""")
    Level1Name = st.selectbox("Elija Retail_Product_Level1Name:",options=df_expected["Retail_Product_Level1Name"].unique(),index = 0)
    ProductColor = st.selectbox("Elija Retail_Product_Color:",options=df_expected["Retail_Product_Color"].unique(),index = 0)
    ProductStyle = st.selectbox("Elija Retail_Product_Style:",options=df_expected["Retail_Product_Style"].unique(),index = 0)
    st.markdown("""---""")
    
    df_selection = df_expected.query("Retail_Product_Level1Name == @Level1Name & Retail_Product_Color == @ProductColor & Retail_Product_Style == @ProductStyle")
    st.dataframe(df_selection)

if rad == "Proceso":
    if df_expected == []:
        #df_expected = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Expected.csv", encoding="latin-1")
        df_expected = pd.read_csv("..\..\Streamlit\stock_inventory\Expected.csv", encoding="latin-1") # df_ICC
    if df_counted == []:
        #df_counted = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Counted.csv", encoding="latin-1")
        df_counted = pd.read_csv("..\..\Streamlit\stock_inventory\Counted.csv", encoding="latin-1") # df_SOH
        #st.session_state["df_counted"] = df_counted
        #df_counted = st.session_state["df_counted"]

    df_expected["Retail_Product_SKU"].nunique() # Cuenta el numero de elementos diferentes

    st.markdown("### SOBRANTES / FALTANTES E INVENTARIO")

    df_counted = df_counted.drop_duplicates("RFID")
    #st.write(df_counted.sample(5))
    #st.write('df_counted 01',df_counted.shape) # Cuenta numero de filas y columnas

    df_A0 = df_counted.groupby("Retail_Product_SKU").count()[["RFID"]].reset_index().rename(columns={"RFID":"Retail_CCQTY"})
    #st.write(df_A0)   # Se nota que Retail_Product_SKU es tomado como numero
    #df_B = df_counted[["RFID","Retail_Product_Level1Name","Retail_Product_SKU"]].groupby(["Retail_Product_Level1Name","Retail_Product_SKU"]).count()[["RFID"]].reset_index().rename(columns={"RFID":"Retail_CCQTY"})
    df_B = df_counted.groupby("Retail_Product_SKU").count()[["RFID"]].reset_index().rename(columns={"RFID":"Retail_CCQTY"})
    #st.write(df_B)   # Se nota que Retail_Product_SKU es tomado como numero

    #df_B.sample(10)

    my_cols_selected = ["Retail_Product_Color",
    "Retail_Product_Level1",
    "Retail_Product_Level1Name",
    "Retail_Product_Level2Name",
    "Retail_Product_Level3Name",
    "Retail_Product_Level4Name",
    "Retail_Product_Name",
    "Retail_Product_SKU",
    "Retail_Product_Size",
    "Retail_Product_Style",
    "Retail_SOHQTY"]
    df_A = df_expected[my_cols_selected]
    #df_A.sample(5)

    #st.write(df_A.head().T)

    # Fusionamos las Discrepancias
    df_discrepancy = pd.merge(df_A, df_B, how="outer", left_on="Retail_Product_SKU", right_on="Retail_Product_SKU", indicator=True)
    #st.write(df_discrepancy.head(30))
    #st.write(df_discrepancy.head().T)
    #st.write(df_discrepancy[['Retail_Product_SKU','Retail_CCQTY',"Retail_SOHQTY"]])    # Osea hay valores del tipo NaN

    # Eliminando valores del tipo NaN
    df_discrepancy['Retail_CCQTY'] = df_discrepancy['Retail_CCQTY'].fillna(0)
    #df_discrepancy['Retail_CCQTY'].sample(25)

    df_discrepancy["Retail_CCQTY"] = df_discrepancy["Retail_CCQTY"].astype(int)
    #df_discrepancy['Retail_CCQTY'].sample(25)

    #df_discrepancy.head()

    #st.write(df_discrepancy.dtypes)

    df_discrepancy["Retail_SOHQTY"] = df_discrepancy["Retail_SOHQTY"].fillna(0).astype(int)
    #st.write(df_discrepancy["Retail_SOHQTY"])

    #st.write(df_discrepancy.dtypes)

    # Enriquecemos la Discrepancia
    df_discrepancy["Diff"] = df_discrepancy["Retail_CCQTY"] - df_discrepancy["Retail_SOHQTY"]
    #st.write(df_discrepancy.head(10))

    # Buscamos Existencias, Faltantes, Sobrantes (Match, Unders, Covers)
    df_discrepancy.loc[df_discrepancy["Diff"]<0, "Unders"] = df_discrepancy["Diff"] * (-1)
    df_discrepancy["Unders"] = df_discrepancy["Unders"].fillna(0).astype(int)
    #st.write(df_discrepancy.sample(10))
    #st.write(df_discrepancy.sample(2).T)
    # 
    #st.write(df_discrepancy.groupby("Retail_Product_Level1Name").sum())

    #st.write(df_discrepancy.describe())
    #df_discrepancy.shape
    #df_discrepancy[df_discrepancy["Diff"].isnull()]
    st.write(df_discrepancy.groupby("Retail_Product_Level1Name").sum())
    #st.write(df_discrepancy.groupby("Retail_Product_SKU").sum())
    #st.write(df_discrepancy.groupby(["Retail_Product_Level1Name","Retail_Product_SKU"]).sum())

if rad == "Acerca del EJ3":
    st.write('Graficas de un DataFrame con sidebar')
    st.balloons()
    st.error("Error")
    st.success("Show Success")
    st.info("Information")
    st.exception(RuntimeError("this is an error"))
    st.warning("this is a warning")

# HIDE STREAMLIT STYLE
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)