from langchain_huggingface import HuggingFaceEndpoint
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.agents import AgentType
import streamlit as st
import os


os.environ["HUGGINGFACEHUB_API_TOKEN"]="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"
API="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"

st.set_page_config(
    page_title="Large Language Model - ChatBot",
    page_icon="💻",
    layout="centered"
)

st.title("Large Language Model 💻🔗 Text-Generation")

if "chat_history" not in st.session_state:
  st.session_state.chat_history=[]

for message in st.session_state.chat_history:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

user_prompt=st.chat_input("Ask Large Language Model")

if user_prompt:
  st.chat_message("user").markdown(user_prompt)
  st.session_state.chat_history.append({"role":"user","content":user_prompt})
  LargeLanguageModel=HuggingFaceEndpoint(repo_id="mistralai/Mistral-7B-Instruct-v0.3",max_length=200,temperature=0.3,token=API)

  response=LargeLanguageModel.invoke(user_prompt)

  st.session_state.chat_history.append({"role":"assistant","content":response})

  with st.chat_message("assistant"):
    st.markdown(response)
