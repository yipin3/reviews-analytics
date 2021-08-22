data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
	print('讀完了，總共有', len(data), '筆資料')

sum = 0
for i in range(len(data)):
	sum = sum + len(data[i])

print('每筆平均留言長度:', sum / len(data))