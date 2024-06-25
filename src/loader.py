# prompt: load multiple documents by loading directory here using its path

from pathlib import Path
def load_documents():
  # Define the directory path containing the documents
  directory_path = "/petofy/data"

  # Get a list of all files in the directory
  files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

  # Load each document and add it to a list
  documents = []
  for file in files:
    with open(os.path.join(directory_path, file), "r") as f:
      document_content = f.read()
      documents.append({"id": file, "text": document_content})
  return documents

load_documents()