#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import streamlit.components.v1 as components
import io
import time
import plotly.figure_factory as ff
import plotly.graph_objects as go
#import os 
#os.add_dll_directory("C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.2/bin")
#import tensorflow as tf
#import csv

st.set_page_config(layout="wide")

def clean_data(df):
    df = df.dropna()
    df.drop_duplicates(inplace=True)
    return df

def time_taken(df):
    df['application_date'] = pd.to_datetime(df['application_date'])
    df['approval_date'] = pd.to_datetime(df['approval_date'])

    df['Time Taken'] = df['approval_date']-df['application_date']
    df['Time Taken'] = df['Time Taken'].dt.days.astype('int64')
    df[df['Time Taken']>0]
    return df

def investment_insights(df):
    df.sort_values(by='application_date', inplace=True)
    df['Year'] = pd.to_datetime(df['application_date']).dt.year
    df_current = df.groupby(['Year']).sum()['investment']
#    st.header("Investment Insights")
    st.markdown(f"<h1 style='text-align: center;'>Investment Insights</h1>", unsafe_allow_html=True)
    st.write(df.describe())
    st.markdown('##')
    st.bar_chart(df_current)
        
def application_insights(df,select_type):
#    st.header("Application Insights")
    st.markdown(f"<h1 style='text-align: center;'>{select_type} Insights</h1>", unsafe_allow_html=True)
    select_type = select_type.lower()
    current_sectoral_time_taken = df.groupby(['sector']).median()
    st.markdown('##')
    st.bar_chart(current_sectoral_time_taken['Time Taken'])
    st.write(f'Median Investment, Employment and Time Taken in every {select_type}',current_sectoral_time_taken)

def sectoral_insights(df,select_type):
#    st.header(f"{select_type} Insights")
    st.markdown(f"<h1 style='text-align: center;'>{select_type} Insights</h1>", unsafe_allow_html=True)
    select_type = select_type.lower()
    current_state_sum = df.groupby([select_type]).sum()
    current_state_median = df.groupby([select_type]).median()
    st.write('Total Investment in every sector',current_state_sum)
    st.markdown('##')
    st.bar_chart(current_state_sum['investment'])
    st.markdown('##')
    st.write(f'Median Investment, Employment and Time Taken in every {select_type}',current_state_median)
    st.bar_chart(current_state_median['investment'])

def district_insights(df,select_type):
#    st.header(f"{select_type} Insights")
    st.markdown(f"<h1 style='text-align: center;'>{select_type} Insights</h1>", unsafe_allow_html=True)
    select_type = select_type.lower()
    df_current =df.groupby([select_type]).median().sort_values(by=['investment'])
    st.bar_chart(df.groupby([select_type]).median()['investment'])
#    st.bar_chart(df_current)
    st.write(f'Median Investment, Employment and Time Taken in every {select_type}',df_current)

def main(OPTIONS):
    st.title('Telangana Investment Data Analysis')
    uploaded_file = st.file_uploader('Upload all_time_data.csv')
    
    if uploaded_file:

        df = pd.read_csv(uploaded_file)
        st.sidebar.title('Dashboard Selector')
        option = st.sidebar.selectbox("",(OPTIONS),0)
        df = clean_data(df)
        df = time_taken(df)
        select_type = option.split()[0]
        
        if option == 'Telangana Investment Map':
            # embed streamlit docs in a streamlit app
            col1_left, col1_right = st.columns(2)
            col1_left.markdown('##')
            #components.iframe("https://www.google.com/maps/d/u/0/embed?mid=15PbXco8n_UAmg6XMnvwYX_paQy5g5BQ&ehbc=2E312F",width=700, height=580, scrolling=True)
            components.iframe("https://www.google.com/maps/d/u/0/embed?mid=15PbXco8n_UAmg6XMnvwYX_paQy5g5BQ&ehbc=2E312F",height=600)
        
        if option == 'Investment Insights':
            investment_insights(df)
            
        if option == 'Application Insights':
            application_insights(df,select_type)

        if option == 'Sector Insights':
            sectoral_insights(df,select_type)
            
        if option == 'District Insights':
            district_insights(df,select_type)


        if option == 'Data Statistics':
            
            col1_left, col1_right = st.columns(2)

            col1_left.header('Data Statistics')
            col1_left.write(df.describe())

            col1_right.header('Dataset Information')
            buffer = io.StringIO()
            df.info(buf=buffer)
            s = buffer.getvalue()
            col1_right.text(s)

        
        
        
#    data = pd.read_csv("D:\Linkedin Learning\PythonTraining\Time_Series_Analysis\TS_Civil_Shop_Transactions\shop_status_details_01-01-2018 to 31-12-2018.csv")
#    print(data.head())
if __name__ == "__main__":
    OPTIONS = ['Telangana Investment Map','Investment Insights', 'Application Insights', 'Sector Insights', 'District Insights','Data Statistics']
    main(OPTIONS)

