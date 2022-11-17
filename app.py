import pandas as pd
import streamlit as st

##importing data
slp = pd.read_csv("data/slp_small.csv")
slp

##creating title
st.title('Job Satisfaction of Speech Language Pathologists ')

#creating caption
st.caption('collected via Qualtrics Survey')

if st.checkbox('Survey Responses'):
    st.dataframe(slp)

##barchart
st.subheader('Length of Employment as a SLP')
employment_length = slp['How_long_have_you_been_working_as_a_Speech_Language_Pathologist_'].value_counts()
st.bar_chart(employment_length)
st.caption('This visual gives us an idea as to length of employment per survey response')