from langchain_community.document_loaders import CSVLoader

# Load CSV file
loader = CSVLoader(file_path='batting_summary.csv')
docs = loader.load()

print(len(docs))
print(docs[1 ].page_content[:100])  # Print the first 100 characters of the first document
