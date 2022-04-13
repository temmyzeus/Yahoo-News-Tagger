from urllib import response

import requests
import streamlit as st
import streamlit.components.v1 as components
from bs4 import BeautifulSoup


st.title("Yahoo News Tagger")
# Enter link to yahoo news url
news_url = st.text_input(label="Enter link to news on yahoo news")
# Check new link, if not from yahoo.com, throw error
render_yahoo_news = st.checkbox(label="Render Yahoo News")

if news_url:
    response = requests.get(url=news_url)
    html = response.content.decode()
    # with open("index.html", mode="w") as f:
    #     f.write(html)
    # st.markdown(html, unsafe_allow_html=True)
    soup = BeautifulSoup(response.text, "html.parser")

    def get_title():
        return soup.title.string

    def get_plain_text() -> list:
        """Get paragraphs in plain text"""
        content_soup = soup.find("div", class_="caas-body")
        return [p.text for p in content_soup.find_all("p") if not p.ul]

    title:str = get_title()
    content_paragraphs:list = get_plain_text()

    if render_yahoo_news:
        components.html(html, width=1000, height=3000)
    else:
        st.title(title)
        for paragraph in content_paragraphs:
            st.markdown(paragraph)
            st.markdown("\n")

