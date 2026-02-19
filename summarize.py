from gemini_client import call_gemini
from chroma_db import search


def summarize(query):

    docs = search(query)

    context = "\n\n".join(docs)

    answer = call_gemini(context, query)

    return answer
