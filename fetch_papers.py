import arxiv

def fetch_arxiv_papers(query, max_results=10):
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )
    papers = []
    for result in search.results():
        papers.append({
            'title': result.title,
            'summary': result.summary,
            'url': result.pdf_url
        })
    return papers
