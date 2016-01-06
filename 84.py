fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()

allword = []

for line in fh:
	stripped = line.rstrip()
	split = stripped.split()
	for i in split:
	 	if i not in allword:
	 		allword.append(i)
print sorted(allword)


