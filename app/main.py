from langchain.document_loaders.unstructured import UnstructuredFileLoader 

loader = UnstructuredFileLoader('document.txt')

documents = loader.load()