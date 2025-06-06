import streamlit as st
import  pickle
import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import stopwords
import string
import contractions
import re

nltk.download("stopwords")
nltk.download("punkt_tab")
nltk.download("wordnet")
nltk.download("averaged_perceptron_tagger_eng")

def project():
    lemmatizer= WordNetLemmatizer()

    def lemmatize_words(text):
        lemma = None
        tag = pos_tag([text])[0][1]
        if tag.startswith('NN'):
          lemma = lemmatizer.lemmatize(text, pos='n')
        elif tag.startswith('VB'):
          lemma = lemmatizer.lemmatize(text, pos='v')
        elif tag.startswith('JJ'):
          lemma = lemmatizer.lemmatize(text, pos='a')
        elif tag.startswith('RB'):
          lemma = lemmatizer.lemmatize(text, pos='r')
        else:
          lemma = lemmatizer.lemmatize(text)
        return lemma
    stpwords = stopwords.words("english")
    def transform(li):
      y = []
      for i in li:
        if i.isalnum() and i not in string.punctuation and i not in stpwords :
              y.append(lemmatize_words(i))

      return " ".join(y)
    tf = pickle.load(open("SpamVectorizer.pkl","rb"))
    model = pickle.load(open("SpamModel.pkl","rb"))

    st.title("EMAIL/SMS Sapm Classifier")
    st.write( "<p style= 'color : #cd0e0e';> Caution: This is a basic spam classifier. It may not be 100% accurate. Always exercise caution and verify results before taking action.",unsafe_allow_html=True)
    inp_msg = st.text_area("Enter message")


    #preprocess
    if st.button("Predict"):
        inp_msg = nltk.word_tokenize(contractions.fix(re.sub(re.compile(r"https?://\S+|www\.\S+"),"",inp_msg).lower()))
        inp_msg = transform(inp_msg)

        in_vector = tf.transform([inp_msg]).toarray()
        result = model.predict(in_vector)[0]
        if result :
          st.header("Spam")
        else:
          st.header("Not Spam")
