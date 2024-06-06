import os
from langchain import PromptTemplate
from constants import openai_key
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain.llms import openai
from langchain.embeddings.openai import OpenAIEmbeddings

import pinecone
from langchain.vectorstores import Pinecone

os.environ["OPENAI_API_KEY"] = openai_key
directory = 'data'# PUT YOUR DATA DIRECTORY NAME

def load_docs(directory):
    loader = DirectoryLoader(directory)
    documents = loader.load()
    return documents

documents = load_docs(directory)
print(len(documents))

def split_docs(documents, chunk_size=800, chunk_overlap=20):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(documents)
    return docs

docs = split_docs(documents)
print(len(docs))


embeddings = OpenAIEmbeddings()

query_result = embeddings.embed_query("Hello world")
print(len(query_result))

pinecone.init(
    api_key="YOUR PINECONE API KEY",
    environment="YOUR PINECONE ENVIRONMENT NAME"
)

index_name = "YOUR PINECONE INDEX NAME"

index = Pinecone.from_documents(docs, embeddings, index_name=index_name)

def get_similiar_docs(query,k=2,score=False):
  if score:
    similar_docs = index.similarity_search_with_score(query,k=k)
  else:
    similar_docs = index.similarity_search(query,k=k)
  return similar_docs


from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
model_name = "gpt-3.5-turbo"
temperature = 0.1
# Set the temperature value
llm = ChatOpenAI(model_name=model_name, temperature=temperature)



from langchain.chains.question_answering import load_qa_chain

chain = load_qa_chain(llm, chain_type="stuff")

def get_answer(query):
  similar_docs = get_similiar_docs(query)
  answer = chain.run(input_documents=similar_docs, question=query)
  return answer



import streamlit as st

st.title('PDF Document Question Answering:books:')
input_text = st.text_input("Ask me a question!")

template = '''
          
Client: I want to focus on strength training. What exercises should I include in my workout program?

Bot: For strength training, I recommend incorporating compound exercises like squats, deadlifts, bench presses, and overhead presses into your workout program. These exercises target multiple muscle groups and are highly effective for building overall strength. Additionally, include exercises such as pull-ups, rows, and lunges to further enhance your muscle development. Remember to start with lighter weights and gradually increase the intensity as you progress. Don't forget to prioritize proper form and technique to avoid injuries.
          {context}
          Client: {human_input}
          Bot:'''



prompt = PromptTemplate(input_variables=["context", "human_input"], template=template)
if input_text:
    documents = load_docs('--YOUR DATA DIRECTORY NAME--')
    docs = split_docs(documents)
    embeddings = OpenAIEmbeddings()
    index_name = "----YOUR--INDEX--NAME-----"
    index = Pinecone.from_documents(docs, embeddings, index_name=index_name)
    llm = OpenAI(model_name='gpt-3.5-turbo')
    

    chain = load_qa_chain(llm=llm, chain_type="stuff")
    with st.spinner('Searching for the answer...'):
        response = get_answer(input_text)
    st.write(response)
    
