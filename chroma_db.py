import chromadb

client = chromadb.Client()

collection = client.get_or_create_collection("incident_collection")


def add_data(text):
    collection.add(
        documents=[text],
        ids=[str(hash(text))]
    )


def search(query):
    results = collection.query(
        query_texts=[query],
        n_results=3
    )
    return results["documents"][0]
