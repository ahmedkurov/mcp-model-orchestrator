def predict(text: str) -> list:
    words = set(word.strip('.,!?').lower() for word in text.split())
    return [word for word in words if len(word) > 4] 