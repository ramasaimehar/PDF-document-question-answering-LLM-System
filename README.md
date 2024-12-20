Here's the enhanced README with emojis and details about setting up the AssemblyAI and Pinecone API keys:

---

# 📄 PDF Document Question Answering LLM System

**This project is a Streamlit app** that uses LangChain and OpenAI to enable users to query and retrieve answers from PDF documents. It uses **Pinecone** for vector storage and **GPT-3.5-turbo** for intelligent answers.

---

## 🚀 Features

- 📂 **Document Loading**: Upload and process PDF documents.  
- ✂️ **Text Splitting**: Automatically splits large texts into manageable chunks.  
- 🧠 **Embeddings**: Generates embeddings using OpenAI for similarity search.  
- 🔎 **Similarity Search**: Uses Pinecone for vector-based similarity searches.  
- 💬 **Interactive Q&A**: Get intelligent responses using LangChain's QA chain and GPT-3.5-turbo.

---

## 🛠️ Setup and Usage

Follow these steps to set up and run the project:

### 1️⃣ Clone the Repository  
   ```bash
   git clone https://github.com/ramasaimehar/PDF-document-question-answering-LLM-System.git
   cd PDF-document-question-answering-LLM-System
   ```

### 2️⃣ Install Dependencies  
   ```bash
   pip install -r requirements.txt
   ```

### 3️⃣ Set API Keys  
- **OpenAI API Key**:  
   1. Get your OpenAI API key by signing up [here](https://platform.openai.com/signup).  
   2. Replace `-------API KEY--------` with your API key in the `constants.py` file or use an environment variable:  
      ```python
      openai_key = "-------YOUR API KEY--------"
      ```
      
- **Pinecone API Key**:  
   1. Sign up at [Pinecone](https://www.pinecone.io/) and create a project.  
   2. Add the following to your script:
      ```python
      api_key = "YOUR PINECONE API KEY"
      environment = "YOUR PINECONE ENVIRONMENT NAME"
      index_name = "YOUR PINECONE INDEX NAME"
      ```

---

### 4️⃣ Run the Application  
   Start the Streamlit app using the following command:  
   ```bash
   streamlit run main.py
   ```

---

## 📋 Workflow

1. Upload your PDF documents to the `data` folder.
2. The app loads, splits, and indexes the documents using **LangChain** and **Pinecone**.  
3. Enter a question in the input field, and the app retrieves similar chunks from the documents.  
4. The QA chain uses GPT-3.5-turbo to provide a detailed response.

---

## 🖼️ App Interface  

- **Sidebar**: Upload PDFs and configure parameters.  
- **Main Section**: Input your query and view the results, including extracted context and generated answers.  

---

## 🔗 Useful Links  
- [OpenAI Signup](https://platform.openai.com/signup)  
- [Pinecone Signup](https://www.pinecone.io/)  

