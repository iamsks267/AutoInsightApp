import sys
import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from datetime import datetime
import os

# Set page title and description
st.set_page_config(page_title="AutoInsight: Automated EDA", layout="wide")

# Title and description
st.title("AutoInsight - Automated EDA Tool")
st.write("Upload your CSV file to perform an automated exploratory data analysis.")

# Add circular LinkedIn photo using HTML and CSS
linkedin_image_url = "https://media.licdn.com/dms/image/v2/D4D03AQGgpAx6pUJCXw/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1696796667460?e=1731542400&v=beta&t=9dVlSMnDqqYTdAcBM69zTx12apE66b1OxWGrcXBMH4A"

# Web App Title
st.markdown('''      
**Technology Used:** App build in `Python` + `Streamlit` using **ydata-profiling** library

''')

# Display LinkedIn link followed by circular image
st.markdown(
    f'''
    <div style="display: flex; align-items: center;">
        <span>Created by <a href="https://www.linkedin.com/in/sanjeev-kumar-singh-sks-b7b612ba/" target="_blank">Sanjeev Kumar Singh</a></span>
        <img src="{linkedin_image_url}" style="border-radius: 50%; width: 30px; height: 30px; object-fit: cover; margin-left: 10px;">
    </div>
    
    ---
    ''',
    unsafe_allow_html=True
)

# Upload CSV Data
with st.sidebar.header('Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your CSV input file")

# Function to generate profile report as HTML string
def generate_report_as_html(dataframe):
    pr = ProfileReport(dataframe, explorative=True)
    return pr.to_html()  # Return HTML string

# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache_data
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv

    df = load_csv()
    report_html = generate_report_as_html(df)  # Generate report as HTML string

    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(ProfileReport(df, explorative=True))

    # Add button to save the report as HTML
    st.download_button(
        label="Download Report as HTML",
        data=report_html,
        file_name=f"data_profiling_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html",
        mime="text/html"
    )

else:
    st.info("Awaiting CSV file to be uploaded")
