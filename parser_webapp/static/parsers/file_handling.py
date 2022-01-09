fname = input("Enter file name: ")
fh = open(fname,'r')
c=0
s=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    c+=1
    s+=float(line[19:].strip())
print("Average spam confidence:",str(s/c))
