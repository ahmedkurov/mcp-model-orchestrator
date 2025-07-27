def predict(text: str) -> str:
    text = text.lower()
    if any(word in text for word in ["good", "great", "excellent", "happy", "love"]):
        return "positive"
    elif any(word in text for word in ["bad", "terrible", "sad", "hate", "awful"]):
        return "negative"
    else:
        return "neutral" 