def predict(text: str) -> str:
    sentences = text.split('.')
    if sentences:
        return sentences[0].strip() + '.' if sentences[0].strip() else text
    return text 