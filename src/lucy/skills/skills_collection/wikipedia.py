import wikipedia
class Wikipedia:
    def search(subject):
        result=wikipedia.summary(subject,sentences=1)
        return result