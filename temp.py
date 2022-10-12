# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go

st.title('Information about stocks and a travel agency')


st.header("How stock prices changed over the years since 1965")
stocks = pd.read_csv(r"C:\Users\student\Desktop\Assignment2\indexData.csv")
if st.checkbox("View Data", help="Click this buttom to view the dataset"): 
    st.dataframe(stocks)
fig1=px.scatter(stocks, x='Date', y='High', color='Index')


st.plotly_chart(fig1)

date_buttons= [{'count':12, 'step':'month', 'stepmode':'todate', 'label':'1yearTD'},{'count':24, 'step':'month', 'stepmode':'todate', 'label':'2yearsTD'}, {'count':36, 'step':'month', 'stepmode':'todate', 'label':'3yearsTD'}, {'count':48, 'step':'month', 'stepmode':'todate', 'label':'4yearsTD'} ]
fig2=px.line(stocks, x='Date', y='High', color='Index', title='The daily change of a number of international stock prices over the years since 1965 up to 2021')
fig2.update_yaxes(title_text='Highest Stock Price during Trading Day')
fig2.update_layout(
{
    'xaxis':
    {
        'rangeselector':
        {'buttons': date_buttons}
    }
})
st.plotly_chart(fig2)
st.header("How a travel Agency succeeded to target its clients more effectively")
travel_agency= pd.read_csv(r"C:\Users\student\Desktop\Assignment2\Travel Agency - Copy.csv")

option = st.selectbox('Want to add another variable?', ('None', 'Gender','MaritalStatus'))

if option == 'None':
    occupation_chart=px.bar(travel_agency, x="Occupation", title="Number of cases for each occupation")
    st.plotly_chart(occupation_chart)
elif option == 'Gender':
    occupation_chart=px.bar(travel_agency, x="Occupation", title="Number of cases for each occupation", color="Gender")
    st.plotly_chart(occupation_chart)
else:
    occupation_chart=px.bar(travel_agency, x="Occupation", title="Number of cases for each occupation", color="MaritalStatus")
    st.plotly_chart(occupation_chart)



from plotly.subplots import make_subplots
fig3 = make_subplots(rows=2, cols=2, subplot_titles=['Type of Product Pitched', 'Gender Distribution', 'Marital Status', 'Designation'])
fig3.add_trace(
    go.Histogram(x=travel_agency["ProductPitched"], name="ProductPitched") ,row=1, col=1)
fig3.add_trace(
    go.Histogram(x=travel_agency["Gender"],name="Gender"),row=1, col=2)
fig3.add_trace(
    go.Histogram(x=travel_agency["MaritalStatus"],name="MaritalStatus"),row=2, col=2)
fig3.add_trace(
    go.Histogram(x=travel_agency["Designation"],name="Designation"), row=2, col=1)
fig3.update_layout({'title':{'text': 'Plots for Customer Demographics', 'x':0.5, 'y':0.9}})
st.plotly_chart(fig3)

stock_Slider=st.slider("Choose a range", max_value=18, min_value=61, step=1, value = [18, 61])
df_new = travel_agency.loc[(travel_agency["Age"] >= stock_Slider[0]) & (travel_agency["Age"] <= stock_Slider[1]) ]
fig4=px.scatter(df_new, x='Age', y='MonthlyIncome')
st.plotly_chart(fig4)


fig5 = px.box(travel_agency, x="ProdTaken", y="MonthlyIncome", points="all", log_y=True)
fig5.update_xaxes(title_text='Accepted to Purchase the product')
st.plotly_chart(fig5)


