import os
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
import whoosh.qparser as qparser
import codecs
from hazm import *
from parsivar import Normalizer as pNormalizer
from parsivar import Tokenizer
from parsivar import FindStems


class SearchEngine:
    def __init__(self, documents_adress, index_adress):
        self.documents_adress = documents_adress
        self.index_adress = index_adress
        schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
        self.ix = create_in(index_adress, schema)
        self.writer = self.ix.writer()

    def Create_Index(self, preprocess):
        lemmatizer = Lemmatizer()
        preprocess_order = preprocess.split(",")
        files = os.listdir(self.documents_adress)
        print(len(files))
        for i in range(len(files)):
            file = files[i]
            if i%100 == 0:
                print(float(i)/len(files))
            file = self.documents_adress+"/"+file
            with codecs.open(file, 'r', "utf-8") as f:
                file_content = (f.read().replace('\n', ' '))
                if "N" in preprocess_order:
                    if "H" in preprocess_order:
                    #print("normalize")
                        normalizer = Normalizer()
                        file_content = normalizer.normalize(file_content)
                    else:
                        my_normalizer = pNormalizer()
                        file_content = my_normalizer.normalize(file_content)

                if "T"  in preprocess_order:
                    if "H" in preprocess_order:
                        #print("tokenize")
                        file_content = word_tokenize(file_content)
                    else:
                        my_tokenizer =  Tokenizer()
                        file_content = my_tokenizer.tokenize_words(file_content)
                if "S" in preprocess_order:
                    stemmer = Stemmer()
                    stem_output = []
                    for word in file_content:
                        stem_output.append(stemmer.stem(word))
                    stem_output = " ".join(stem_output)
                    file_content = stem_output
                if "L" in preprocess_order:
                    if "H" in preprocess_order:
                        lem_output = []
                        for word in file_content:
                            lem_output.append(lemmatizer.lemmatize(word))
                        lem_output = " ".join(lem_output)
                        
                        #print(lem_output)
                        file_content = lem_output
                    else:
                        my_stemmer = FindStems()
                        lem_output = []
                        for word in file_content:
                            lem_output.append(my_stemmer.convert_to_stem(word))
                        lem_output = " ".join(lem_output)
                        #print(lem_output)
                        file_content = lem_output



                self.writer.add_document(title=("filename: " +file), path =("path_to_file: "+file),content=file_content)
        self.writer.commit()
        print("indexing has been finished")

    def Search(self,this_query):
        searcher = self.ix.searcher()
        #og = qparser.OrGroup.factory(0.9)
        og = qparser.OrGroup
        #print("this_query")
        #print(this_query)
        #print(this_query)

        query = QueryParser("content", self.ix.schema, group = og).parse(this_query)
        #print(query)
        #raise(False)
        #print("query")
        #print(query)

        results = searcher.search(query, limit = 10)
        print(results)
        list_of_results_files = []
        for result in results:
            filename = result["path"]
            filename = filename.split('/')[-1]
            list_of_results_files.append(filename)
        return(list_of_results_files)
            




