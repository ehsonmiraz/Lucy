from googlesearch import search,get_page

query = "studytonight"

for i in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(get_page(i).)
