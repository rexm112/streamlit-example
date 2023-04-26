from langchain.document_loaders import PyPDFLoader
import streamlit as st
from tempfile import NamedTemporaryFile
import os


st.title = "LangChain File Uploader"
st.header = "Upload a file to get started"

TEMP_DIRECTORY = "tempDir"


def save_uploaded_file(uploadedfile):
    st.write(uploadedfile.name)
    with open(os.path.join(TEMP_DIRECTORY, uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())
        st.write(uploadedfile.name)
    return st.success("Saved File: {} to tempDir".format(uploadedfile.name))


source_file = st.file_uploader("Upload a file", type=["pdf", "txt"])
st.write(source_file)

upload_button = st.button("Upload")

if source_file is not None: 
    if upload_button:
        save_uploaded_file(source_file)
        st.write("File {} uploaded succeessfully to {}".format(source_file.name, TEMP_DIRECTORY))
        st.write("File Name: {}".format(source_file.name))

        loader = PyPDFLoader("{}/{}".format(TEMP_DIRECTORY, source_file.name))
        pages = loader.load_and_split()

        st.write(pages[0])




    