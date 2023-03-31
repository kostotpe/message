data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0: # %是求餘數的意思 例子是跟1000求餘數 就是除
            print(len(data))


wc = {} # words_count
for d in data:
    words = d.split(' ')
    for word in words:
        if word in wc:
            wc[word] += 1 # 已經遇過的字，統計數量加1
        else:
            wc[word] = 1 # 新增新的key進字典


for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])


while True:
    word = input('輸入你想查詢的字: ')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為: ', wc[word])
    else:
        print('無查詢到您輸入的字')


