data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0: # %是求餘數的意思 例子是跟1000求餘數 就是除
            print(len(data))

print('檔案讀取完了，總共有', len(data), '筆資料')

sum_len = 0 # 算留言平均長度 總長/總筆數
for d in data:
    sum_len = sum_len + len(d)
print('每筆留言的平均長度為: ', sum_len/len(data))

new = [] # 對清單做篩選
for d in data:
    if len(d) < 100:
        new.append(d)
print('共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])

good = [] # 篩選所有有提到good的連言
for d in data:
    if 'good' in d:
        good.append(d) # a in 'abc' -> True , b in 'abc' -> false
print('共有', len(good), '筆留言提到good')
print(good[0])

# 搜尋good快寫法
# output = [(number - 1) for number in referencr if number % 2 == 0]
# (number - 1) 運算
# number 變數
# referencr 清單
# number % 2 == 0 篩選條件
good = [d for d in data if 'good' in d]
print('have', len(good), 'good')
# 練習取bad
bad = [d for d in data if 'bad' in d]
print('have', len(bad), 'bad')
# 再進階
# 'bad' in bad是否有在清單內，True or false
bad = ['bad' in d for d in data]
print(bad)
# '再進階'原始寫法
bad = []
for d in data:
    bad.append('bad' in d)
