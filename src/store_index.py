
from src.helper import load_pdf_file, text_split,download_hugging_face_embeddings
from pinecone.grpc import PineconeGRPC as pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeSparseVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

pinecone_api_key = os.environ.get("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"] = api_key

extracted_data = load_pdf_file(data ="dataset/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()
