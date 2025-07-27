from models import sentiment, summarizer, keywords


def route_task(task: str, text: str):
    task = task.lower()
    if task == "summarize":
        return {"summary": summarizer.predict(text)}
    elif task == "sentiment":
        return {"sentiment": sentiment.predict(text)}
    elif task == "keywords":
        return {"keywords": keywords.predict(text)}
    else:
        return {"error": f"Unknown task: {task}"} 