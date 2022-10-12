import numpy as np
import pandas as pd
import streamlit as st
import datetime
from datetime import timedelta
# import matplotlib.pyplot as plt

st.header(" SALES INCOME ESTIMATION  ")
st.subheader("(Data: Salevali_Samdata )")

st.image("Total_Sales_Revenue_Predition/flooring.jpg",width=600, caption="Could you guess the Total Sales?")
st.subheader(" What could be the  sales income in next days, weeks and months?")

st.image("Total_Sales_Revenue_Predition/luckyfloorsbc_LOGO.JPG",width=200)
datetime.datetime.now()


st.success("For estimation Please choose one of the options below")

if st.checkbox("Month by month prediction"):
    test_=pd.read_csv("ARIMA_test_monthly_all.csv").set_index("Unnamed: 0") 
    test_.index = pd.to_datetime(test_.index)

    st.warning("From the beginning monthly sales income,  the next 6 months future prediction")
    st.line_chart(test_)  # grafik çizer
    
    result=test_["predicted"][-6]
    result_avg=test_["predicted"][-6:].mean()

    st.info("Next month's estimation: €{}".format(int(result)))
    st.info("Next 6 months'  average: €{}".format(int(result_avg)))
    
    test_ = test_.resample('M').sum().astype('int')        # to prevent the floating numbers after dot (.)
    test_.index = pd.to_datetime(test_.index).date         # only to show the date not date&time
    
    st.table(test_[-8:])                                        # tablo halinde listeler

if st.checkbox("Week by week prediction"):
    test_=pd.read_csv("ARIMA_test_weekly_all.csv").set_index("Unnamed: 0") 
    test_.index = pd.to_datetime(test_.index)

    st.warning("The Last year's weekly sales income,  next 3 months future prediction")
    st.line_chart(test_) 
    st.warning("The Last 1 year weekly Sales, Total in Euro,  next 2 months future prediction")
    st.line_chart(test_[-64:-4]) 
    st.warning("The Last 6 months weekly Sales, Total in Euro,  next month future prediction")
    st.line_chart(test_[-38:-9]) 

    # Total predicted record number for 3 months =13 weeks=13 records in ARIMA_test_weekly_all
    result=test_["predicted"][-13]
    result_avg=test_["predicted"][-13:-9].mean()
    st.info("Next week's estimation  : €{}".format(int(result)))
    st.info("Next 4 weeks' mean: €{}".format(int(result_avg)))

    test_ = test_.resample('W').sum().astype('int')        # to prevent the floating numbers after dot (.)
    test_.index = pd.to_datetime(test_.index).date         # only to show the date not date&time
    st.table(test_[-15:-9])                                        # tablo halinde listeler

if st.checkbox("Day by day prediction"):
    test_=pd.read_csv("ARIMA_test_daily_all.csv").set_index("Unnamed: 0") 
    test_.index = pd.to_datetime(test_.index)


    prn=-93
    # Total predicted record number(prn) for 3 months =13 weeks=93 days records in ARIMA_test_daily_all
    last_record=prn-1


    st.warning('All years daily Sales, Total in Euro,  next month future prediction')
    st.line_chart(test_) 
    st.warning('The last 3 months daily Sales, Total in Euro,  next  two weeks  future prediction')
    st.line_chart(test_[last_record-120:last_record+14]) 
    st.warning('The last months daily Sales, Total in Euro,  next  7 days future prediction')
    st.line_chart(test_[last_record-30:last_record+7]) 


    result=test_["predicted"][prn]
    result_avg=test_["predicted"][prn:prn+7].mean()

    st.info("Next day's estimation : €{}".format(int(result)))
    st.info("Next week's daily mean: €{}".format(int(result_avg)))

    test_ = test_.resample('D').sum().astype('int')  # to prevent the floating numbers after dot (.)
    test_.index = pd.to_datetime(test_.index).date  # only to show the date not date&time

    st.table(test_[prn-2:prn+7])    # tablo halinde listeler

  
