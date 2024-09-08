from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_core.documents import Document

import tempfile

def load_from_pdf(file_bytes) -> Document:
    with tempfile.NamedTemporaryFile(suffix=f'.pdf', delete=False) as temp_file:
        temp_path = temp_file.name
        temp_file.write(file_bytes)

    loader = PyPDFLoader(temp_path)
    document = loader.load()
    return document


def load_from_docx(file_bytes):
    pass
    
    
def split_text(document: Document) -> list[Document]:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500, 
        chunk_overlap=500, 
        separators=[''],
        add_start_index=True
    )
    
    chunks = text_splitter.split_documents(document)
    
    return chunks
    