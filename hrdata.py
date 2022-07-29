import streamlit as st
import pandas as pd
from tabulate import tabulate
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Gender Pay Gap
This app predicts the Pay!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
  Sex = st.sidebar.slider('Sex', M, F)
  Termd = st.sidebar.slider('Termd', 0, 1)
   data = {'Sex': Sex,
            'Termd': Termd}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('Sex')
st.write(df)

Termd = pd.read_csv('https://raw.githubusercontent.com/cheryllim1/hrdata7/main/HRDataset_v14.csv')
X = Termd.drop('termd',axis = 1)
Y = Sex['Sex']

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Sex and Termd')
st.write(pay)
