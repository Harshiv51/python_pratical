Test_Case = int(input()) 
for i in range(Test_Case): 
    word = input() 
    l = len(word) 
    if l % 2 == 0: 
        b, c = word[:l//2], word[l//2:] 
    else: b, c = word[:l//2], word[l//2+1:] 
    if sorted(b) == sorted(c): print("YES") 
    else: print("NO")