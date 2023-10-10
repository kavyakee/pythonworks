tweets="What a game , hats off to both teams. Well done @benstokes @patcummies2 you have bought test cricket back to life. Love test cricket @TheBarmyArmy @CricketAus @ECB_cricket"
words=tweets.split(" ")              # to split the words
for w in words:
    if w.startswith("@"):            # endswith() - to check the last letter.
        print(w)

# to sort a word
text="cabbage"
srt_word=sorted(text)       #sorted()- to sort a text
print(srt_word)
print(len(text))            # to print the length of a text.

# anagram - to have another word from a text with the same no of characters,misplaced.eg; care-race,bread-beard not beards
text="wow"
out="won"
if(sorted(text)==sorted(out)):     #sorted(text)=oww   sorted(out)=onw  !=
    print("Anagram") 
else:
    print("not")  

#palindrome or not
text="kadak"
count=len(text)-1               
p_str=""
for i in range(count,-1,-1):
    p_str+=text[i]
print("palindrome " if text==p_str else "not palindrome")


