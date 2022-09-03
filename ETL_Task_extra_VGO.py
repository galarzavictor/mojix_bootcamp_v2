#from asyncio.windows_events import NULL
import streamlit as st
#!pip install "pymongo[srv]"
import pymongo
from pymongo import UpdateOne
import pandas as pd

def getDataFromMongo(db_name, collection, query):
  db = client.get_database(db_name)
  cursor = db[collection].find(query)

  data = [doc for doc in cursor]
  df = pd.json_normalize(data)
  
  return df

def write_mongo_bulk_upsert(db_name, collection, df):
  db = client.get_database(db_name)
  collect_name = db["%s" % (collection)]

  dictionary = df.to_dict(orient="records")

  upserts = [UpdateOne({'_id':x['_id']}, {"$set": x} , upsert=True) for x in dictionary]
  response = collect_name.bulk_write(upserts)

  print(response)

def drop_mongo_collection (db_name, collection):
  db = client.get_database(db_name)
  collect_name = db["%s" % (collection)]  
  collect_name.drop()

df_discrepancy = []
#st.set_page_config(initial_sidebar_state="collapsed")
rad =st.sidebar.radio("Menu",["Fuente de Datos","Analisis","Acerca de ELT/ETL"])
st.sidebar.info(
        "Esta aplicacion fue diseñada para resolver mostrar resultados del **Task 2** de "
        "el Modulo ETL/ELT "
        "[reclamos](https://galarzavictor-mojix-bootcamp-v2-discrepancy-fmi9qv.streamlitapp.com/) o "
        "el codigo fuente [source code](https://galarzavictor-mojix-bootcamp-v2-finance01-mrasnr.streamlitapp.com/). "
    )

if rad == "Fuente de Datos":
    st.title("Verificacion de la Fuente de Datos")
    st.markdown('''
    ## Diariamente se ejecutan los consumidores de datos en las siguientes direcciones...
    [Data Expected](https://colab.research.google.com/drive/1jvKgLFnZK1PdI9UEFjh9SWRnGvpAFepL?usp=sharing)

    [Data Counted](https://colab.research.google.com/drive/1X3iBf1YQjzxM1UxadhiUaFBUj3kKyhUr?usp=sharing)

    [Data Batch](https://colab.research.google.com/drive/1X3iBf1YQjzxM1UxadhiUaFBUj3kKyhUr?usp=sharing)
    ''', unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center; color: yellow;'>Documento discrepancy-VGO en MongoDB</h2>", unsafe_allow_html=True)
    if df_discrepancy == []:
        client = pymongo.MongoClient("mongodb+srv://bootcamp:MjrSCGYPhfmbxc68@cluster0.w7ren.mongodb.net/admin")
        # print the expected inventory from Mongo
        query = {}
        df_discrepancy = getDataFromMongo(db_name="bootcamp", collection="discrepancy_VGO", query=query)
        st.dataframe(df_discrepancy)

if rad == "Analisis":
    if df_discrepancy == []:
        client = pymongo.MongoClient("mongodb+srv://bootcamp:MjrSCGYPhfmbxc68@cluster0.w7ren.mongodb.net/admin")
        # print the expected inventory from Mongo
        query = {}
        df_discrepancy = getDataFromMongo(db_name="bootcamp", collection="discrepancy_VGO", query=query)

    st.markdown("<h2 style='text-align: center; color: yellow;'>Resultados del Inventario</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: left; color: yellow;'>Filtros:</h3>", unsafe_allow_html=True)
    st.markdown("""---""")
    ProductSKU = st.selectbox("Elija Retail_Product_SKU:",options=df_discrepancy["Retail_Product_SKU"].unique(),index = 0)
    st.markdown("""---""")
    df_discrepancy = df_discrepancy.query("Retail_Product_SKU == @ProductSKU")
    st.dataframe(df_discrepancy.loc[:,['Retail_Product_SKU',"Retail_StoreNumber",'Retail_Product_Level1Name','Retail_SOHQTY','Retail_CCQTY','_merge','Diff','Unders','Match','Overs']])

if rad == "Acerca de ELT/ETL":
    st.write('ELT/ETL')
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