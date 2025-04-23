import streamlit as st
import webbrowser as wb

#import cp
#import spam
option = st.sidebar.selectbox('Select Project', ["None","Color Picker","Spam Classifier", "IPL API"])


if option == "None" :
    st.title("..MY PROJECT SPACE 🚀..")
    st.subheader('''Hi user I have tailored this webpage to show my different projects which I make out of curiosity..''')
    st.markdown('''### Here you will find interesting projects related to: 
- Machine Learning
- Data Science 
- Data Analytcs 
- Data Visualization ''')
    st.write('''and many more thinigs..''')
    st.write("if you want to check code of these projects you can visit my GitHub repo's")
    st.link_button('GitHub', url='https://github.com/lubaid-01')

if option == "Color Picker" :
    #cp.project()
    st.write("Color Picker")

if option == "Spam Classifier":
    #spam.project()
    st.write("Spam Classifier")
if option == "IPL API":
   wb.open_new_tab("https://ipl-api-ogdg.onrender.com")