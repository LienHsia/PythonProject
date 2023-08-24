freq = {}   # frequency of words in text
print("请输入：")
line = input()
for word in line.split():
    freq[word] = freq.get(word,0)+1
words = sorted(freq.keys())  #按key值对字典排序
 
for w in words:
    print ("%s:%d" % (w,freq[w]))