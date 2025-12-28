import os
import time
from dotenv import load_dotenv # <--- Add this
from pinecone import Pinecone, ServerlessSpec
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load environment variables from .env file
load_dotenv()

# Explicitly set them for the libraries to see (standard practice)
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["PINECONE_API_KEY"] = os.getenv("PINECONE_API_KEY")

def ingest_pdfs(folder_path, index_name):
    pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

    # Check and Create Index (768 dimensions for Gemini)
    if index_name not in pc.list_indexes().names():
        print(f"Creating index '{index_name}'...")
        pc.create_index(
            name=index_name,
            dimension=768, 
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )
        while not pc.describe_index(index_name).status['ready']:
            time.sleep(1)

    # Use the loaded keys for embeddings and storage
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

    print(f"Reading PDFs from {folder_path}...")
    loader = DirectoryLoader(folder_path, glob="./*.pdf", loader_cls=PyPDFLoader)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_documents(docs)

    print(f"Uploading {len(chunks)} chunks...")
    vector_store = PineconeVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings,
        index_name=index_name
    )
    print("Success! Data is now in Pinecone.")

if __name__ == "__main__":
    ingest_pdfs(folder_path="./my_pdfs", index_name="hackx")