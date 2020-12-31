import os
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
import codecs

class SearchEngine:
    def __init__(self, documents_adress, index_adress):
        self.documents_adress = documents_adress
        self.index_adress = index_adress
        schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
        self.ix = create_in(index_adress, schema)
        self.writer = self.ix.writer()

    def Create_Index(self):
        files = os.listdir(self.documents_adress)
        print(len(files))
        for i in range(len(files)):
            file = files[i]
            print(float(i)/len(files))
            file = self.documents_adress+"/"+file
            with codecs.open(file,'r', "utf-8") as f:
                self.writer.add_document(title=unicode("filename: " +file),content=f.read().replace('\n', ' '))
        self.writer.commit()
        print("indexing has been finished")

    def Search(self,this_query):
        with self.ix.searcher() as searcher:
            query = QueryParser("content", self.ix.schema).parse(this_query)
            results = searcher.search(query)
            print(results)
            print(results[0])
            print(results[1])
            return results
            





