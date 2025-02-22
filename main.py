import streamlit as st
import time

from scrape import scrape_website, split_dom_content, clean_body_content, extract_body_content

st.title("AI Multi Website Scraper")
st.subheader("By Ahmad Fauzan")

url = st.text_input("Masukkan URL Website: ")

if st.button("Mulai Scraping"):
    st.write("Sedang mengambil data website...")
    time.sleep(0.3)

    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)

    # print(result)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Data apa yang ingin anda ambil dari website ini?")

    if st.button("Mulai Parsing"):
        if parse_description:
            st.write("Sedang melakukan parsing data pada website...")

            dom_chunks = split_dom_content(st.session_state.dom_content)



