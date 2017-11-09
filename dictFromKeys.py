list1 = list('123456')
list2 = list('abcd')
list3 = 123

def dictionaryFromKeys(k, v):
    try:
        res = dict.fromkeys(k, None)
        res.update(zip(k, v))
    except TypeError:
        res = 'TypeError'
    return res

result = dictionaryFromKeys(list1, list2)
result2 = dictionaryFromKeys(list1, list3)
result
result2

