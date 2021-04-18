import string
def check_word_frequency():
    docs =[] # n - numbers of docs/documents
    queries=[] # m - number of queries
    n =int(input()) 
    # appending documents to docs array
    for i in range(n): 
        docs.append(str(input()))
    # indexing and cleanup of inputed documents
    docs_dict  = dict()
    for doc_index, doc in enumerate(docs):
        translate_table= doc.maketrans(string.punctuation, ''.join([' ' for s in string.punctuation]))
        doc_clean= doc.translate(translate_table).lower().split()
        for word in doc_clean:
            if word not in docs_dict:
                docs_dict[word]=dict()
            if doc_index not in docs_dict[word]:
                docs_dict[word][doc_index]= 0
            docs_dict[word][doc_index]+=1
    # end of indexing and cleanup    
    queries=[] # m - number of queries
    m =int(input()) 
    for i in range(m):
        query=str(input())
        queries.append(query)
    # resolution of queries based on doc_dict created and indexed beforehand
    for q in queries:
        if q not in docs_dict:
            print(q,[])
        else:
            word_array = docs_dict[q]
            sorted_table=sorted(list(word_array.items()), reverse=True, key= lambda x:x[1])
            print([i[0] for i in sorted_table])
check_word_frequency()            






