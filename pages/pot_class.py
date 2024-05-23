import streamlit as st
import requests
import json.decoder

def main():
    st.title(":green[Potato Disease Detection]:potato:")

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    st.write("Diseases potato plants may suffer from are:\n Early Blight and Late Blight")
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
                                                                                                                        
        if st.button("Run Model"):
            trigger_url = "https://us-central1-striped-torus-403117.cloudfunctions.net/predict"
            files = {"file": ("image.jpg", uploaded_file.read(), "image/jpeg")}
            
            try:
                response = requests.post(trigger_url, files=files)
                response = response.json()
                
                st.subheader("Results:")
                if response["confidence"] < 89:
                    st.warning("The provided picture is not of the plant")

                if response["class"] == "Healthy":
                    st.success("The Plant is Healthy!")
                else:
                    st.warning("The Plant has the {} disease.".format(response["class"]))

                st.text("We are {:.1f}% confident".format(response["confidence"]))

            except json.decoder.JSONDecodeError:
                st.warning("The given image is either incorrect or in a wrong format. Either way, the model is incapable of passing inference on this image.")

if __name__ == "__main__":
    main()
