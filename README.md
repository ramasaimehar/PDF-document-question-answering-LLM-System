# PDF-document-question-answering-LLM-System
This project is a Streamlit app  using LangChain and OpenAI. Users enter queries to get answers from pdf's that are uploaded. It loads documents, splits them, generates embeddings, and indexes them with Pinecone. The app then performs similarity searches and provides answers using a QA chain and OpenAI's GPT-3.5-turbo model.

To use this project:

1. Clone the repository.
2. Open a terminal in the working directory.
3. Run the following command to install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Set the `OPENAI_API_KEY` (replace `-------API KEY--------` with your actual API key):
    ```
   OPENAI_API_KEY="-------API KEY--------"
    ```
5. The `main.py` file contains the Streamlit application.
6. Run the script with the following command:
    ```
    python3 streamlit run main.py
    ```
