name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"


handle = open(name)

counts = dict()

for line in handle: 
	if line.startswith('From '):
		time = line.split()
		totaltime = time[5]
		hours = totaltime.split(':')
		hour = hours[0]
		counts[hour] = counts.get(hour,0) +1 


lst = list()

for key, val in counts.items():
	lst.append( (key, val))

lst.sort()

for key, val in lst:
	print key, val



