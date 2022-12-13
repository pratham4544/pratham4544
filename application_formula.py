import pandas as pd
import streamlit as st
from sklearn.decomposition import PCA
import plotly.express as px
import numpy as np
from sklearn.preprocessing import StandardScaler


def pca_maker(df):
    num_col_list =[]
    cat_col_list = []

    for i in df.columns:
        if df[i].dtype == np.dtype('float64') or df[i].dtype == np.dtype('int64'):
            num_col_list.append(df[i])
        else:
            cat_col_list.append(df[i])

    num_data = pd.concat(num_col_list, axis=1)
    cat_data = pd.concat(cat_col_list,axis=1)
    num_data = num_data.apply(lambda x: x.fillna(np.mean(x)))


    scaler = StandardScaler()
    scaled_values = scaler.fit_transform(num_data)


    pca = PCA()
    pca_data = pca.fit_transform(scaled_values)
    pca_data = pd.DataFrame(pca_data)


    new_col_names = ['PCA_' + str(i) for i in range(1, len(pca_data.columns) + 1)]
    col_map= dict(zip(list(pca_data.columns),new_col_names))
    pca_data.rename(columns=col_map, inplace=True)
    output = pd.concat([df, pca_data],axis=1)

    return output, list(cat_data.columns), new_col_names