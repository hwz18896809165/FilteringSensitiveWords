dictionaryTree = [None, 0]
def create_thesaurus(root, words, start):
    if (start+1 == len(words)):
        if(len(root)==2):
            root.append([words[start],1])
        else:
            flag = True
            for i in range(2,len(root)):
                if(root[i][0] == words[start]):
                    root[i][1] = 1
                    flag = False
                    break
                else:
                    continue
            if(flag == True):
                root.append([words[start], 1])
    else:
        if (len(root) == 2):
            root.append([words[start], 0])
            newroot = root[len(root) - 1]
        else:
            flag = True
            for i in range(2,len(root)):
                if(root[i][0] == words[start]):
                    newroot = root[i]
                    flag = False
                    break
                else:
                    continue
            if(flag == True):
                root.append([words[start], 0])
                newroot = root[len(root)-1]
        create_thesaurus(newroot,words,start+1)


def search_sensitive_words(dictionaryTree,words):
    sensitive_words = []
    str=""
    now_test = []
    for i in words:
        if(now_test == []):
            for j in range(2,len(dictionaryTree)):
                if(dictionaryTree[j][0] == i):
                    str += dictionaryTree[j][0]
                    now_test = dictionaryTree[j]
                    if(dictionaryTree[j][1] == 1):
                        sensitive_words.append(str)
                        str = ""
                        now_test = []

        else:
            flag = False
            for j in range(2,len(now_test)):
                if(now_test[j][0] == i):
                    flag = True
                    str += now_test[j][0]
                    if(now_test[j][1] == 1):
                        sensitive_words.append(str)
                        str = ""
                        now_test = []
                    else:
                        now_test = now_test[j]
                    break
                else:
                    continue
            if(flag == False):
                str = ''
                now_test = []
    return sensitive_words


def replace_sensitive_words(key_word,sensitive_words,start):
    if sensitive_words==[]:
        return key_word
    new_key_word = key_word.replace(sensitive_words[start], '*' * len(sensitive_words[start]))
    if(start+1 == len(sensitive_words)):
        return new_key_word
    else:
        new_key_word = replace_sensitive_words(new_key_word, sensitive_words, start + 1)
        return new_key_word



def start_search(key_word):
    result = search_sensitive_words(dictionaryTree,key_word)
    new_word = replace_sensitive_words(key_word,result,0)
    return result,new_word
def start_create_dictionaryTree():
    file_in = open("sensitivewords.txt", 'r',encoding='utf-8')
    list = []
    while(True):
        key_word =  file_in.readline()
        if(key_word == ''):
            break
        key_word = key_word.replace("\n","")
        list.append(key_word)
    for i in list:
        if(i == ''):
            list.remove(i)
    for i in list:
        create_thesaurus(dictionaryTree,i,0)
