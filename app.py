from flask import Flask, render_template, request
from fetch_papers import fetch_arxiv_papers
from embedder import embed_texts
from summarizer import summarize_text
from search_engine import PaperSearchEngine
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            papers = fetch_arxiv_papers(query, max_results=20)
            summaries = [paper['summary'] for paper in papers]
            embeddings = embed_texts(summaries)
            engine = PaperSearchEngine(np.array(embeddings), papers)
            query_embedding = embed_texts([query])
            top_results = engine.search(query_embedding, top_k=5)

            for paper in top_results:
                summary = summarize_text(paper['summary'])
                results.append({
                    'title': paper['title'],
                    'url': paper['url'],
                    'summary': summary
                })

    return render_template("index.html", results=results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
