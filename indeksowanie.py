import string

# def check_word_frequency():
#     docs= []
#     # number of documents input
#     n =int(input())
#     # appending documents to docs array
#     for i in range(n):
#         docs.append(str(input()))
#     # indexing and cleanup    
#     docs_dict  = dict()    
#     for doc_index, doc in enumerate(docs):
#         translate_table= doc.maketrans(string.punctuation, ''.join([' ' for s in string.punctuation]))
#         doc_clean= doc.translate(translate_table).lower().split()
#     for word in doc_clean:
#         if word not in docs_dict:
#             docs_dict[word]=dict()
#         if doc_index not in docs_dict[word]:
#             docs_dict[word][doc_index]= 0
#         docs_dict[word][doc_index]+=1
#     # number of word queries
#     m = int(input())
#     # query check
#     queries=[]
#     for i in range(m):
#         query=str(input())
#         queries.append(query)
#     for q in queries:      
#         if q not in docs_dict:
#             print([])
#         else:
#             word_array = docs_dict[q]
#             sorted_array=sorted(list(word_array.items()), reverse=True, key= lambda x:x[1])
#             print([i[0] for i in sorted_array])
# check_word_frequency()
        



docs = []
queries = ['care','is']
docs.append("YouR!! care set up, do not pluck my care down.")
docs.append("My cAre is loss of,, care? with old care done.")
docs.append("Your care is Gain of !care when new care is won.") 
docs_dict  = dict()
for doc_index, doc in enumerate(docs):
    translate_table= doc.maketrans(string.punctuation, ''.join([' ' for s in string.punctuation]))
    doc_clean= doc.translate(translate_table).lower().split()
    #print(doc_clean)
    for word in doc_clean:
        if word not in docs_dict:
            docs_dict[word]=dict()
        if doc_index not in docs_dict[word]:
            docs_dict[word][doc_index]= 0
        docs_dict[word][doc_index]+=1
for q in queries:
    if q not in docs_dict:
        print(q,[])
    else:
        word_array = docs_dict[q]
        sorted_table=sorted(list(word_array.items()), reverse=True, key= lambda x:x[1])
        print([i[0] for i in sorted_table])







