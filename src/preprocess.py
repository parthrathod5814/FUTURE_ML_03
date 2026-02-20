import spacy

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    text = str(text)
    doc = nlp(text.lower())

    tokens = [
        token.lemma_
        for token in doc
        if not token.is_stop
        and not token.is_punct
        and token.is_alpha
    ]

    return " ".join(tokens)
