from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Load PDF
loader = PyPDFLoader("sample.pdf")
documents = loader.load()

# Convert to embeddings
embeddings = OpenAIEmbeddings()

# Store in FAISS
db = FAISS.from_documents(documents, embeddings)

# Create retriever
retriever = db.as_retriever()

# QA Chain
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    retriever=retriever
)

# Ask question
query = "What is the main idea of this paper?"
result = qa.run(query)

print(result)