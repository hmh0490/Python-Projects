import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg") # width=600

with col2:
    st.title("Hoang Minh Hanh")
    content = """
    Hi, I am Hanh!
     
    I am an accomplished finance professional with a diverse international background in banking and finance. 
    I have gained extensive experience in various roles, allowing me to develop a comprehensive understanding of 
    financial markets and strategies. Notably, I have also successfully passed the rigorous examination for the 
    Chartered Financial Analyst (CFA) certificate, highlighting my commitment to professional excellence.
    
    Throughout my career, I have developed a strong passion for programming and have acquired valuable skills in this
    area. I also proactively pursued programming skills to complement my finance expertise. Through self-study and 
    practical application, I have acquired a strong foundation in programming languages relevant to the finance sector.
    
    I am now driven to combine my profound knowledge of finance with my programming capabilities, aiming to leverage
    technology to optimize financial processes, automate tasks, and develop sophisticated models for data analysis 
    and forecasting, and deliver innovative solutions.
    """
    # st.write(content)
    st.info(content)

content2 = """
Below you find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

