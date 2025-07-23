from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text, max_length=500, min_length=100):
    return summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']
