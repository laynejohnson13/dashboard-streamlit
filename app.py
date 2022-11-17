import pandas as pd
import streamlit as st
import numpy as np 

##importing data
slp = pd.read_csv("data/slp_small.csv")
slp

pollution = pd.read_csv('data/pollution_by_region.csv')
pollution

##creating title
st.title('Job Satisfaction of SLPs & Global Pollution')

#creating caption
st.caption('collected via Qualtrics Survey & Kaggle')

if st.checkbox('SLP Survey Responses'):
    st.dataframe(slp)

##barchart
st.subheader('Length of Employment as a SLP')
employment_length = slp['How_long_have_you_been_working_as_a_Speech_Language_Pathologist_'].value_counts()
st.bar_chart(employment_length)
st.caption('This visual gives us an idea as to length of employment per survey response')


##linechart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['region_id', 'country_name', 'gdp'])
st.line_chart(chart_data)


##histogram
#st.subheader('Organic Waste Percent by Region')
#waste_percentage = pollution['composition_food_organic_waste_percent]
