import streamlit as st
import requests

st.set_page_config(
    page_title="Text classification model",
    initial_sidebar_state="expanded"
)


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


# HUGGING FACE API CONNECTION
API_KEY = st.secrets["API_KEY"]
API_URL = "https://api-inference.huggingface.co/models/valhalla/distilbart-mnli-12-3"
headers = {"Authorization": f"Bearer {API_KEY}"}

with st.form(key="my_form"):
    labels = st.multiselect('Choose your labels', ["refund", "legal", "faq", "food", "sports"])
    text_input = st.text_area("Enter some text for classification 👇")
    run_model = st.form_submit_button("Run classification model")
    output = query({
        "inputs": f"{text_input}",
        "parameters": {"candidate_labels": labels},
    })

if run_model:
    st.write("This is the result")
    output


# Hi, I recently bought a device from your company but it is not working as advertised and I would like to get reimbursed!
# Hi, I would like to buy a new computer. How does your store work?