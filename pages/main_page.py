import streamlit as st

def main():
    st.title(':green[GreenCheck] :herb:')
    st.divider()
    st.write(":green[Welcome to GreenCheck! Identify the disease your plant may be having with the help of highly trained ML models!\n Select the species of plant from the sidebar and upload an image of the leaf.\n Run the model to get a prediction!\n]")
    st.write("\n\n\n All the models used have an accuracy above 90%. They have all been implemented using Convolutional Neural Networks in tensorflow.\nThey have been trained on annotated and verified datasets open-sourced on Kaggle.")
