import streamlit as st
from sklearn import datasets
import pandas as pd

# Load the iris dataset
iris = datasets.load_iris()

# Create a DataFrame from the data
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Add the target variable to the DataFrame
df['target'] = iris.target

# Create the tabs
st.sidebar.title("Tabs")
app_mode = st.sidebar.radio("Choose tab", ["Overview", "Data", "About"])

if app_mode == "Overview":
    st.title("Overview")
    st.markdown("This is the overview tab.")
elif app_mode == "Data":
    st.title("Data")
    st.table(df)
elif app_mode == "About":
    st.title("About")
    st.markdown("This is the about tab.")