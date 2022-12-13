import pandas as pd
import streamlit as st
import plotly.express as px
from application_formula import pca_maker


st.set_page_config(layout='wide')
scatter_column, settings_column = st.columns((4,1))

scatter_column.title('Multi-Dimensional Analysis')
settings_column.title('Settings')

uploaded_file = settings_column.file_uploader("Choose File")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    pca_data, cat_cols, pca_cols = pca_maker(df)

    categorical_variables = settings_column.selectbox('Variable Select', options=cat_cols)
    categorical_variables_2 = settings_column.selectbox('Second Variable Select', options=cat_cols)

    pca_1 = settings_column.selectbox('First Principal Component',options=pca_cols, index=0)
    pca_cols.remove(pca_1)
    pca_2 = settings_column.selectbox('Second Principal Component', options=pca_cols)
    scatter_column.plotly_chart(px.scatter(data_frame=pca_data, x=pca_1, y='PCA_2', color=categorical_variables,template='simple_white', height=800, hover_data=[categorical_variables_2]), use_container_width=True)



else :
    scatter_column.header('Please Choose File')


