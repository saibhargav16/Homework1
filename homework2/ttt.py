 count_frequency(wl):
    for word in wl:
        if word in wordDict.key():
            wordDict[word] += 1
        else:
            pass
        return wordDict

mylist = ['one','two','eleven','one','three','two','eleven','three','seven','eleven']
print(count_frequency(mylist))