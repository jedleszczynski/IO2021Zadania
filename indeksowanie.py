import string
docs = []
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
print(docs_dict['care'])        
print(docs_dict['gain'])     





