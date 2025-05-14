from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r'C:\Users\Legion\Desktop\LangChain models\RAG_components\document-loader\pdfs\Cohere Resume - Suril Purohit.pdf')

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)