#Experiment: SE0
from  searchengine import *
from pre_rec import precision_recall
import codecs
from hazm import *

experiment = "R,N,T"




if "R" in experiment.split(","):
    SE = SearchEngine("./Poems_Remove","index_whoosh")
else:
    SE = SearchEngine("./Poems","index_whoosh")
SE.Create_Index(experiment)


with open("RelevanceAssesment/RelevanceAssesment.txt") as f:
    lines = f.readlines()
test_file_names = lines[0::3]
Relevantdocs = lines[1::3]


sum_precision = 0
sum_recall = 0
if "R" in experiment:
    Queries_adress = "Queries_Remove/"
else:
    Queries_adress = "Queries/"
for i in range(len(test_file_names)):
    print("processing file "+str(i))
    file = test_file_names[i]

    with codecs.open(Queries_adress+file.split("\n")[0], 'r', "utf-8") as f:
        query = f.read().replace("\n", " ")
        if "N" in experiment:
                #print("normalize")
            normalizer = Normalizer()
            query = normalizer.normalize(query)
        if "S" in experiment:
            stemmer = Stemmer()
            stem_output = []
            for word in query.split(" "):
                stem_output.append(stemmer.stem(word))
            stem_output = " ".join(stem_output)
            query = stem_output
        if "L" in experiment:
            lemmatizer = Lemmatizer()
            lem_output = []
            for word in query:
                lem_output.append(lemmatizer.lemmatize(word))
            lem_output = " ".join(lem_output)
            query = lem_output
                    

            #if "T"  in experiment:
            #print("tokenize")
            #query = word_tokenize(query)
            #query = " ".join(query)
    
    results = SE.Search(query)
    pre,rec = precision_recall(results, Relevantdocs[i].split("\n")[0].split(" "))
    sum_precision += pre
    sum_recall += rec
experiment_precision = sum_precision / len(test_file_names)
experiment_recall = sum_recall / len(test_file_names)
