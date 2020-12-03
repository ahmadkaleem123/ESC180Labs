import os
import random
os.chdir(r'C:\Users\Ahmad\Desktop\UofT EngSci Year 1\ESC180 (Introduction to Computer Programming)\Lab 9')
#1 a
f = open("prejudice.txt", encoding="latin-1").read().split()#open("text.txt", encoding="latin-1").read().split()

word_counts = {}

for word in f:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
#print(word_counts)

#1 b
x = []
for i in range(100):
    x.append(random.randint(1,101))
#print(x)
def top10(L):
    k = sorted(L)
    return k[90:]
#print(top10(x))

#1c

inv_freq = {6: "the", 12: "a", 1:"hi"}
print(sorted(inv_freq.items()))
#print(word_counts.items())

words = list(word_counts.items())

words.sort(key=lambda x :x[1])
a = words[-10:]
for i in range(len(a)-1,-1,-1):
    print(a[i][0])


#print(words[-10:])
#Problem 2 in html

#Problem 3  
import urllib.request
f = urllib.request.urlopen("http://www.cs.toronto.edu/~guerzhoy/180/draft/draft.html")
page = f.read().decode("utf-8")
f.close()
#print(page)

def num_results(w):
    w = w.replace(" ", "+")
    #print(w)
    f = urllib.request.urlopen("https://ca.search.yahoo.com/search;_ylt=Av3YHOEya_QRKgRTD8kMWgst17V_?p="+ w +"&amp;toggle=1&amp;cop=mss&amp;ei=UTF-8&amp;fr=yfp-t-715&amp;fp=1")
    page = f.read().decode("utf-8")
    #results</span>
    b = page.split()
    s = "results</span></div></div></li></ol></div></div><div"
    f.close()
    
    s2 = b[b.index(s)-1]
    return s2[s2.index("span")+5:]

#print(num_results("google"))

def choose_variant(variants):
    max_s = []
    max_results = 0
    for elem in variants:
        n = int(num_results(elem).replace(",", ""))
        if n > max_results:
            max_results = n
            max_s = [elem]
        
        elif n == num_results(elem):
            max_s.append(elem)
    return max_s

variants = ["top ranked school uoft", "top ranked school ryerson"]
print(choose_variant(variants))