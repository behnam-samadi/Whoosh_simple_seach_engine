#Experiment: SE0
from  searchengine import *
from pre_rec import precision_recall
import codecs
from hazm import *

experiment = ""
SE = SearchEngine("./Poems","index_whoosh")
SE.Create_Index(experiment)


with open("RelevanceAssesment/RelevanceAssesment.txt") as f:
    lines = f.readlines()
test_file_names = lines[0::3]
Relevantdocs = lines[1::3]


sum_precision = 0
sum_recall = 0

for i in range(len(test_file_names)):
    print("processing file "+str(i))
    file = test_file_names[i]
    with codecs.open("Queries/"+file.split("\n")[0], 'r', "utf-8") as f:
        query = f.read().replace("\n", " ")
        if "N" in experiment:
                #print("normalize")
            normalizer = Normalizer()
            query = normalizer.normalize(query)
        #if "T"  in experiment:
            #print("tokenize")
            #query = word_tokenize(query)
            #query = " ".join(query)
        if "R" in experiment:
            stopwords = []
            with codecs.open("Stopwords/Stopwords.txt", 'r', "utf-8") as f:
                lines = f.readlines()
            for line in lines:
                stopwords.append(line.split('\n')[0])
            #print("Remove StopWords")
            query = query.split(" ")
            #stopwords = stopwords.split(" ")
            query_temp = []
            for word in query:
                if not word in stopwords:
                    query_temp.append(word)
                else:
                    print("word",word)
            print(len(query))
            print("chaged to")
            print(len(query_temp))
            query = query_temp
            query = " ".join(query)
    
    results = SE.Search(query)
    pre,rec = precision_recall(results, Relevantdocs[i].split("\n")[0].split(" "))
    sum_precision += pre
    sum_recall += rec
experiment_precision = sum_precision / len(test_file_names)
experiment_recall = sum_recall / len(test_file_names)