import json
import os

import newspaper
from src.lucy.core.console import ConsoleManager as cm

class NewsGenerator:
    MIN_WORDS=3
    def __init__(self):
        self.console=cm
        self.final_article_list=[]
        self.news_sites=['https://timesofindia.indiatimes.com/india','https://www.ndtv.com/latest?pfrom=home-topnavigation/']
    def extract_urls(self,URL):
        paper = newspaper.build(URL, language='en')
        url_list=paper.category_urls()
        return url_list
    def get_artilcle(self,URL):
        article = newspaper.Article(URL, language='en')  # Chinese
        article.download()
        while article.download_state == 0:
            cm.console_output("Downloading news.....", refresh_console=True)
        article.parse()
        article.nlp()
        return article

    def fetchNews(self, ):
          for URL  in self.news_sites:
              url_list= self.extract_urls(URL)
              for url in url_list:
                    print("url is:"+url)
                    article=self.get_artilcle(url)
                    if(article is None or article.title.count(" ")<NewsGenerator.MIN_WORDS or article.summary.count(" ") < NewsGenerator.MIN_WORDS): continue
                    print("title:"+ article.title)
                    print("Text :"+ article.summary)
                    print("------------\n")
                    self.final_article_list.append({
                        "id":article.url,
                        "title":article.title,
                        "author":article.authors,
                        "summary":article.summary,

                    })

          json_object = json.dumps(self.final_article_list, indent=4)
          with open("../files/news.json", "w") as outfile:
              outfile.write(json_object)
    @staticmethod
    def get_news():
        news_text = ""
        utils_dir = os.path.dirname(__file__)
        new_file = os.path.join(utils_dir, '..', 'files', 'news.json')

        with open(new_file, "r") as outfile:
            articles_object = json.load(outfile)

        for article in articles_object:
            news_text+=article['title'] +' : '+article['summary'] + '║'

        return news_text
if __name__ =='__main__':
  print(NewsGenerator().get_news())
