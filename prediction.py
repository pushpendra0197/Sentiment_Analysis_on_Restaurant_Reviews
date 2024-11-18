import numpy as np 
import pandas as pd 
import nltk
import spacy
import re 
import seaborn as sns
import string
from nltk.corpus import stopwords
stop=stopwords.words("english")
from nltk.stem import PorterStemmer
pos_stem=PorterStemmer()
import joblib
import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import  CountVectorizer



model=joblib.load(r"H:\reviews\review_prediction_model")
fitdata=joblib.load(r"H:\reviews\fit_data")
cv=CountVectorizer(max_features=1500)
x=cv.fit(fitdata)

def clean(text):
    review=text.lower()
    review=re.sub('[^a-zA-z]',' ',review)
    review=review.split()    
    review=[ i for i in review if i not in string.punctuation]
    review=[pos_stem.stem(word) for word in review]
    review=" ".join(review)
    
    return review



st.title("Sentiment Anlysis On Restaurant Reviews")
input=st.text_input("enter your comment >>")
button=st.button("Predict")
if button:
    input_vec=cv.transform([input])
    prediction=model.predict(input_vec)
    header=st.subheader(prediction)   

