from newsapi.newsapi_client import NewsApiClient

newsapi = NewsApiClient(api_key = "12cf0c6d785d4158a9e3e053ba3791e7")

def search(q, category):
  top_headlines = newsapi.get_top_headlines(q = q, category = category)
  return top_headlines