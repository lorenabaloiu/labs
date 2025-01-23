def inverted_index(documents):
    index = {}
    for doc_id, doc in enumerate(documents):
        words = doc.split()
        for word in words:
            if word not in index:
                index[word] = set()
            index[word].add(doc_id)
    return index

num_docs = int(input("Enter the number of documents: "))
documents = []
for i in range(num_docs):
    doc = input(f"Enter document {i + 1}: ")
    documents.append(doc)
result = inverted_index(documents)
print("Inverted Index:", result)
