from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

# ===== GLOB PATTERN METHODS =====
# '*.pdf'              - Loads all PDF files in the specified directory (non-recursive)
# '**/*.pdf'           - Loads all PDF files recursively from all subdirectories
# '*.{pdf,txt}'        - Loads multiple file types (PDF and TXT files)
# '*.csv'              - Loads all CSV files
# '*.json'             - Loads all JSON files
# '*.md'               - Loads all Markdown files
# '*.docx'             - Loads all Word documents
# '*'                  - Loads all files of all types
# 'doc_*.pdf'          - Loads PDF files that start with 'doc_'
# '*/reports/*.pdf'    - Loads PDF files from 'reports' subdirectory
# 'Q[1-4]/*.pdf'       - Loads PDF files from Q1, Q2, Q3, Q4 directories

loader = DirectoryLoader(path = 'docs',
                         glob = '*.pdf',
                         loader_cls = PyPDFLoader)

#docs = loader.load()
docs = loader.lazy_load()

"""print(len(docs), type(docs))
print(docs[0].page_content[:500])  # Print the first 500 characters of the first document's content
print(docs[0].metadata)  # Print metadata of the first document
"""
for document in docs:
    print(document.metadata)