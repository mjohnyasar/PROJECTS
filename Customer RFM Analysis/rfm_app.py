import pandas as pd 
import plotly.express as px
import streamlit as st


st.set_page_config(page_title ="RFM Analysis",
                  page_icon= ":bar_chart:",
                  layout= "wide"
                  )

df= pd.read_excel(io='rfm.xlsx', engine='openpyxl',
                  skiprows=0, sheet_name= 'RFM',
                  usecols="A:J", nrows=2819)
df["customer_id"]=df["customer_id"].astype(str)

st.header("All Data:")
st.dataframe(df)

    
st.sidebar.header("Please type the Customer ID")
customers=df["customer_id"].drop_duplicates()
customer_id= st.sidebar.selectbox("Select the Customer",customers)

st.sidebar.header("Please select Segments")
segments=df["Segment"].drop_duplicates()
segments= st.sidebar.selectbox("Select Segments",segments)


df_selection = df.query(
    "customer_id == @customer_id")

st.header("Results of Customer Filter:")
st.write(df.loc[(df['customer_id']==customer_id)])
st.header("Results of Segment Filter:")
st.write(df.loc[(df['Segment']==segments)])