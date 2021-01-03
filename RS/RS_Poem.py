import os

with open("../Stopwords/Stopwords.txt") as f:
	Swords = f.readlines()

new_sword = []
for sword in Swords:
	new_sword.append(sword.split("\n")[0])




documents_adress = "../Poems"
files = os.listdir(documents_adress)




for i in range(len(files)):
	print(i)
	file = files[i]
	adress = documents_adress + "/" + file

	with open(adress) as f:
		lines = f.readlines()
	lines = " ".join(lines)
	print(lines)
	words = lines.split(" ")
	result = []
	for word in words:
		if not word in new_sword:
			result.append(word)

	result_str = " ".join(result)

	with open("../Poems_Remove/"+file, 'w')  as f:
	   f.write(result_str)




