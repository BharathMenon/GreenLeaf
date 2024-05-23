import streamlit as st
import requests

def main():
    st.title(":green[Tea Disease Detection]:tea:")


    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    st.write("Diseases tea plants may suffer from are:\n Anthracnose, algal leaf, bird eye spot, brown blight, gray light, red leaf spot and white spot")
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)

        if st.button("Run Model"):

            trigger_url = "https://us-central1-shaped-infusion-403004.cloudfunctions.net/predict_tea"
            files = {"file": ("image.jpg", uploaded_file.read(), "image/jpeg")}
            response = requests.post(trigger_url, files=files)

            response = response.json()
            st.subheader("Results:")
            if response["confidence"]<89:
                st.warning("The provided picture is not of the plant")
            if response["class"] == "Healthy":
                st.success("The Plant is Healthy!")
            else:
                st.warning("The Plant has the {} disease.".format(response["class"]))

            st.text("We are {:.1f}% confident".format(response["confidence"]))

if __name__ == "__main__":
    main()