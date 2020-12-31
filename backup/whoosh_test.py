import os
from whoosh.index import create_in
from whoosh.fields import *

schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
ix = create_in("index_whoosh", schema)
writer = ix.writer()
files = os.listdir("./Poems")
for file in files:
	file = "./Poems/"+file
	with open(file) as f:
		writer.add_document(title="filenam: " +file, path="path_to_file: "+file,content=f.readlines())
writer.commit()
from whoosh.qparser import QueryParser
with ix.searcher() as searcher:
	query = QueryParser("content", ix.schema).parse("salam".encode('utf-8'))
	results = searcher.search(query)


