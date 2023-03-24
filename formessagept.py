data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0: # %是求餘數的意思 例子是跟1000求餘數 除的意思
            print(len(data))
print(data[0])
print('-----------------')
print(data[1])