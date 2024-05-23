word = input().upper()
s_word = list(set(word))
count_word = []
for k in s_word:
    count_word.append(word.count(k))
if count_word.count(max(count_word)) > 1:
    print("?")
else:
    index = count_word.index(max(count_word))
    print(s_word[index])