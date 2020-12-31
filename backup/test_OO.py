from  searchengine import *
SE = SearchEngine("./Poems","index_whoosh")
SE.Create_Index()
with open("persianQuery.txt") as f:
    query = f.read()
print(query.encode("utf-8"))
exit()
results = SE.Search(query)
result[0]
results[1]
