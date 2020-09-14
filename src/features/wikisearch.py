import wikipedia
import re


def wikisearch(query):
    query = query.replace(" en wikipedia", "").replace("busca", "").replace("quién es ", "")
    # Specify the title of the Wikipedia page
    wikipedia.set_lang("es")
    wiki = wikipedia.page(query)
    # Extract the plain text content of the page
    text = wiki.content
    text = re.sub(r'==.*?==+', '', text).split("\n")
    print(text[0])
    return text[0]
