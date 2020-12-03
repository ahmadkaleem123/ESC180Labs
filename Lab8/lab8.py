import os
#Problem 1
os.chdir(r'C:\Users\Ahmad\Desktop\UofT EngSci Year 1\ESC180 (Introduction to Computer Programming)\Lab 8')
f = open("data2.txt","r")
#text = f.read()
lines = f.readlines()
for line in lines:
    if line.lower().find("lol") == -1:
        continue
    else:
        print(line)

#print(lines[3].lower().find('lol'))
f.close()
# Problem 2
def dict_to_str(d):
    
    """Return a str containing each key and value in dict d. Keys andvalues are separated by a comma. Key-value pairs are separatedby a newline character from each other.For example, dict_to_str({1:2, 5:6}) should return "1, 2\n5, 6".(the order of the key-value pairs doesn’t matter and can be differentevery time)."""
    string = ""
    c = list(d.items())
    for i in range(len(c)):
        if i == len(c) - 1:
            string += str(c[i][0]) + ", " +  str(c[i][1])
        else:
            string += str(c[i][0]) + ", " + str(c[i][1]) + "\n"
    return string

    
'''
d = {1: 2, 5: 6}
c = list(d.items())
print(c[0][1])
'''
d = {5: 6, 1: 2, 3:6, 19:20}
#print(sorted(d.items()))
#print(dict_to_str(d))
# Problem 3
def dict_to_str_sorted(d):
    
    """Return a str containing each key and value in dict d. Keys andvalues are separated by a comma. Key-value pairs are separatedby a newline character from each other.For example, dict_to_str({1:2, 5:6}) should return "1, 2\n5, 6".(the order of the key-value pairs doesn’t matter and can be differentevery time)."""
    string = ""
    c = list(sorted(d.items()))
    for i in range(len(c)):
        if i == len(c) - 1:
            string += str(c[i][0]) + ", " +  str(c[i][1])
        else:
            string += str(c[i][0]) + ", " + str(c[i][1]) + "\n"
    return string
#print(dict_to_str_sorted(d))

# Problem 4a 

f = open("cmudict-0.7b.txt", "r")
lines = f.readlines()
dic = {}
for l in lines:
    n = l.find(" ")
    key = l[0:n]
    lnew = l[n+1: len(l)]
    value = lnew.split()
    dic[key] = value
#print(dic)

#Problem 4b
phones = open("cmudict-0.7b.phones.txt", "r")

phone_dic = {}
lines2 = phones.readlines()
for l2 in lines2:
    n = l2.find("\t")
    key = l2[0:n]
    value = l2[n+1: len(l2)-1]
    phone_dic[key] = value
#print(phone_dic)
# Problem 4c
def numvowels(w):
    vowel = 0
    s = w.upper()
    phones = dic[s]
    for phone in phones:
        if phone[-1].isdigit():
            if phone_dic[phone[0:len(phone)-1]] == "vowel":
                vowel += 1
                
        else:
            if phone_dic[phone] == "vowel":
                vowel += 1
    return vowel
#print(numvowels(""))

#Problem 4d
def numsyllables(w):
    syllable = 0
    s = w.upper()
    prev_vowel = False
    phones = dic[s]
    for phone in phones:
        if phone[-1].isdigit():
            if phone_dic[phone[0:len(phone)-1]] == "vowel" and prev_vowel == False:
                syllable += 1
                prev_vowel = True
            else:
                prev_vowel = False
        else:
            if phone_dic[phone] == "vowel" and prev_vowel == False:
                syllable += 1
                prev_vowel = True
            else:
                prev_vowel = False
    return syllable
#print(numsyllables("niihau"))

#Problem 5
news = open("news.txt", "r")
article = news.read()
story = open("mobydick.txt", "r")
moby = story.read()

def fleschkincaid(t):
    words = 0
    sentences = 0
    for i in range(len(t)):
        
        if(t[i] == " " or t[i] == "\t" or t[i] == "\n"):
            words+= 1
            #t[i].replace(" ")
            
        elif(t[i] == "." or t[i] == "!" or t[i] == "?"):
            sentences += 1
           
       # elif t[i] == "," or t[i] == ":" or t[i] == ";" or t[i] == '"' or t[i] == "(" or t[i] == ")" or t[i] == "[" or t[i] == "]" or t[i] == "{" or t[i] == "}" or t[i] == "-":
            #t[i] = " "
      #  elif t[i].isdigit():
         #   t[i] = " "
    t = t.replace("\t", " ")
    t = t.replace("\n", " ")
    t = t.replace(".", " ")
    t = t.replace("!", " ")
    t = t.replace("?", " ")
    t = t.replace(",", " ")
    t = t.replace(":", " ")
    t = t.replace(";", " ")
    t = t.replace('"', " ")
    t = t.replace("(", " ")
    t = t.replace(")", " ")
    t = t.replace("[", " ")
    t = t.replace("{", " ")
    t = t.replace("]", " ")
    t = t.replace("}", " ")
    t = t.replace("%", " ")
    t = t.replace("$", " ")
    t = t.replace("-", " ")
    t = t.replace("0", " ")
    t = t.replace("1", " ")
    t = t.replace("2", " ")
    t = t.replace("3", " ")
    t = t.replace("4", " ")
    t = t.replace("5", " ")
    t = t.replace("6", " ")
    t = t.replace("7", " ")
    t = t.replace("8", " ")
    t = t.replace("9", " ")
    #print(t)
    wordlist = t.split() 
    syl = 0
    
    for word in wordlist:
        #syl += numsyllables(word)
        
        try:
            syl += numsyllables(word)
        except:
            syl += 1.66 # Average number of syllables in a word
        
    score = 0.39 * (words/sentences) + 11.8 *(syl/words) - 15.59
    return score
    
print(fleschkincaid(article))
print(fleschkincaid(moby))