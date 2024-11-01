sentence = input("请输入一个句子: ")
word_frequency = {}
words = sentence.split()
for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1
print(word_frequency)