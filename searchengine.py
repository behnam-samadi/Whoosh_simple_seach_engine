import os
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
import whoosh.qparser as qparser
import codecs
from hazm import *

class SearchEngine:
    def __init__(self, documents_adress, index_adress):
        self.documents_adress = documents_adress
        self.index_adress = index_adress
        schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
        self.ix = create_in(index_adress, schema)
        self.writer = self.ix.writer()

    def Create_Index(self, preprocess):
        preprocess_order = preprocess.split(",")
        files = os.listdir(self.documents_adress)
        print(len(files))
        for i in range(len(files)):
            file = files[i]
            if i%100 == 0:
                print(float(i)/len(files))
            file = self.documents_adress+"/"+file
            with codecs.open(file, 'r', "utf-8") as f:
                file_content = unicode(f.read().replace('\n', ' '))
                if "N" in preprocess_order:
                    #print("normalize")
                    normalizer = Normalizer()
                    file_content = normalizer.normalize(file_content)
                if "T"  in preprocess_order:
                    #print("tokenize")
                    file_content = word_tokenize(file_content)
                if "R" in preprocess_order:
                    stopwords = []
                    with codecs.open("Stopwords/Stopwords.txt", 'r', "utf-8") as f:
                        lines = f.readlines()
                    for line in lines:
                        stopwords.append(line.split('\n')[0])
                    #print("Remove StopWords")
                    file_content_temp = []
                    for word in file_content:
                        if not word in stopwords:
                            file_content_temp.append(word)
                    #print(file_content)
                    #print("chaged to")
                    #print(file_content_temp)
                    file_content = file_content_temp





                self.writer.add_document(title=unicode("filename: " +file), path =unicode("path_to_file: "+file),content=file_content)
        self.writer.commit()
        print("indexing has been finished")

    def Search(self,this_query):
        searcher = self.ix.searcher()
        og = qparser.OrGroup.factory(0.3)
        #print("this_query")
        #print(this_query)
        query = QueryParser("content", self.ix.schema, group = og).parse(this_query)
        #print("query")
        #print(query)

        results = searcher.search(query, limit = 10)
        print(results)
        list_of_results_files = []
        for result in results:
            filename = result["path"]
            filename = filename.split('/')[-1]
            list_of_results_files.append(filename.encode("utf-8"))
        return(list_of_results_files)
            



