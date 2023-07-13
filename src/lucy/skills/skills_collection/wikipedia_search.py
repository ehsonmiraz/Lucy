import wikipedia
class WikipediaSearch:
    def search(subject):
        result=wikipedia.summary(subject,sentences=1)
        return result