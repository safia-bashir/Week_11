import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

# Add and resize an image to the top of the app
img_fuel = Image.open("../img/fuel_efficiency.png")
st.image(img_fuel, width=700)

st.markdown("<h1 style='text-align: center; color: black;'>Fuel Efficiency</h1>", unsafe_allow_html=True)

# Import train dataset to DataFrame
train_df = pd.read_csv("train.csv")
model_results_df = pd.read_csv("model_results.csv")

# Create sidebar for user selection
with st.sidebar:
    # Add FB logo
    st.image("https://user-images.githubusercontent.com/37101144/161836199-fdb0219d-0361-4988-bf26-48b0fad160a3.png" )    

    # Available models for selection
 
    # YOUR CODE GOES HERE!
    models = ["DNN", "TPOT"]

    # Add model select boxes
    model1_select = st.selectbox(
        "Choose Model 1:",
        (models)
    )
    
    # Remove selected model 1 from model list
    # App refreshes with every selection change.
    models.remove(model1_select)
    
    model2_select = st.selectbox(
        "Choose Model 2:",
        (models)
    )

# Create tabs for separation of tasks
tab1, tab2, tab3 = st.tabs(["🗃 Data", "🔎 Model Results", "🤓 Model Explainability"])

with tab1:    
    # Data Section Header
    st.header("Raw Data")

    # Display first 100 samples of the dateframe
    st.dataframe(train_df.head(100))

    st.header("Correlations")

    # Heatmap
    corr = train_df.corr()
    fig = px.imshow(corr)
    st.write(fig)

with tab2:    
    
    # YOUR CODE GOES HERE!

    # Columns for side-by-side model comparison
    col1, col2 = st.columns(2)

    # Build the confusion matrix for the first model.
    with col1:
        st.header(model1_select)
        model1_results = model_results_df[model_results_df["model"] == model1_select]
        cm1  = model1_results[cols].to_numpy()[0].reshape(2,2).tolist()

        x1 = ["0", "1"]
        y1 = ["1", "0"]
        z1 = cm1
        z_text1 = [[str(y) for y in x] for x in z1]

        # YOUR CODE GOES HERE!
        st.header(model1_select)

        fig1 = px.imshow(z1, text_auto=True)
        
        # add custom x-axis title
        fig1.add_annotation(dict(font=dict(color="black",size=14),
                                x=0.5,
                                y=-0.00005,
                                showarrow=False,
                                text="Predicted value",
                                xref="paper",
                                yref="paper"))

        # add custom y-axis title
        fig1.add_annotation(dict(font=dict(color="black",size=14),
                                x=-0.25,
                                y=0.5,
                                showarrow=False,
                                text="True value",
                                textangle=-90,
                                xref="paper",
                                yref="paper"))


        # Write plotly chart and fit to the container width.
        st.plotly_chart(fig1, use_container_width=True)

    # Build confusion matrix for second model
    with col2:
        st.header(model2_select)
          model2_results = model_results_df[model_results_df["model"] == model2_select]
        cm2  = model2_results[cols].to_numpy()[0].reshape(2,2).tolist()

        x2 = ["0", "1"]
        y2 = ["1", "0"]
        z2 = cm2
        z_text2 = [[str(y) for y in x] for x in z2]

        st.header(model2_select)

        fig2 = px.imshow(z2, text_auto=True)
        
        # add custom x-axis title
        fig2.add_annotation(dict(font=dict(color="black",size=14),
                                x=0.5,
                                y=-0.00005,
                                showarrow=False,
                                text="Predicted value",
                                xref="paper",
                                yref="paper"))

        # add custom y-axis title
        fig2.add_annotation(dict(font=dict(color="black",size=14),
                                x=-0.25,
                                y=0.5,
                                showarrow=False,
                                text="True value",
                                textangle=-90,
                                xref="paper",
                                yref="paper"))



        
        # Write plotly chart and fit to the container width.
        st.plotly_chart(fig2, use_container_width=True)
        # YOUR CODE GOES HERE!


with tab3: 
    # YOUR CODE GOES HERE!
        # Use columns to separate visualizations for models
        # Include plots for local and global explanability!
     
    st.header(model1_select)

    
    
    st.header(model2_select)

    
