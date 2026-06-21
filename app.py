import streamlit as st
import pickle
from preprocess import cleanResume, cat_name

#loading models

lg = pickle.load(open('lg.pkl','rb'))
tfidf = pickle.load(open('tfidf.pkl','rb'))

#web app
def main():
    st.title("Resume Screening App")
    upload_file = st.file_uploader('Upload Resume',type=['txt','pdf'])
    if upload_file is not None:
        try:
            resume_byte = upload_file.read()
            resume_text = resume_byte.decode('utf-8')
        except UnicodeDecodeError:
            #if utf-8 decoding fails, try decoding with 'latin-1'
            resume_text = resume_byte.decode('latin-1')

        cleaned_resume = cleanResume(resume_text)

        input_features = tfidf.transform([cleaned_resume])

        prediction_id = lg.predict(input_features)[0]
        st.write("Category Name :",cat_name(prediction_id))





#python main
if __name__ == "__main__":
    main()