# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")

try: 
	fh = open(fname)
except:
	print 'File cannot be opened:', fname 
	exit()

count = 0
total = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    elif line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        atpos = line.find('0')
        num = line[atpos - 1:26]
        num = float(num)
        total = total + num
        print num, total, count
print "Average spam confidence: " + str(total/count)