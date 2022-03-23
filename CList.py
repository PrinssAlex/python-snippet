
#18/3/2022: clist()
#==================

#this is a function that selects the first series of words before a comma from a list of strings
#E.g ['I love to eat banana, peanut, paw paw', 'I love fishing, hiking'...]
#will return ['I love to eat banana', 'I love fishing']

def clist(list_obj):
    bbag=[]
    for i in list_obj:
        val = ''
        for j in i:
            if j != ',':
                val = val+j
            else:
                break
        bbag.append(val)
    return bbag 