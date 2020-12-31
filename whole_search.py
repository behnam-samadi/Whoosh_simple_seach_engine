from  searchengine import *
from pre_rec import precision_recall
import codecs

SE = SearchEngine("./Poems","index_whoosh")
SE.Create_Index("N,T")

#results = SE.Search(query)
with open("RelevanceAssesment/RelevanceAssesment.txt") as f:
    lines = f.readlines()
test_file_names = lines[0::3]
Relevantdocs = lines[1::3]

for i in range(len(test_file_names)):
    print("processing file "+str(i))
    file = test_file_names[i]
    with codecs.open("Queries/"+file.split("\n")[0], 'r', "utf-8") as f:
        query = f.read().replace("\n", " ")
    results = SE.Search(query)
    print(precision_recall(results, Relevantdocs[i].split("\n")[0].split(" ")))
