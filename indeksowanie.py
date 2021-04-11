import string
docs = []
docs.append("YouR!! care set up, do not pluck my care down.")
docs.append("My cAre is loss of,, care? with old care done.")
docs.append("Your care is Gain of !care when new care is won.") 
docs_index  = dict()
for doc in docs:
    translate_table= doc.maketrans(string.punctuation, ''.join([' ' for s in string.punctuation]))
    doc_clean= doc.translate(translate_table).lower().split()
    print(doc_clean)



