data = []
count = 0
#讀檔案，列出進度
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
	print('讀完了，總共有', len(data), '筆資料')


#平均留言長度
sum = 0
for i in range(len(data)):
	sum = sum + len(data[i])
print('每筆平均留言長度:', sum / len(data))

#列出留言小於100
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言小於100')
print(new[0])

#篩選留言裡含有'good'
# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
# print('一共有', len(good), '筆留言提到good')
good = [d for d in data if 'good' in d]
print(good[0])

bad = ['bad' in d for d in data]
print(bad)

# 文字計數
wc = {} # word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1  # 新增新的key進wc字典
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
print(len(wc))

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現的次數為: ', wc[word])
	else:
		print('這個字沒有出現過喔')
print('感謝使用查詢功能')



