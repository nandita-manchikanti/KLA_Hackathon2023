input=open("Format_Source.txt",'r')
inputlist=input.readlines()
length=len(inputlist)

#Header
header=[]
for i in range(8):
    header.append(inputlist[i])
print(header)

#Points
i=8
pointlist=[]
while i<(length-3):
    pointlist.append(inputlist[i:i+5])
    i=i+5
print(pointlist)

#Footer
footer=[]
i=length-2
while i<(length):
    footer.append(inputlist[i])
    i=i+1
print(footer)

#write inputfile into output file
out=open("milestone1out.txt","w")
for item in header:
    out.write("%s" % item)

for i in range(2):
    for j in pointlist[i]:
        out.write("%s" % j)

for item in footer:
    out.write("%s" % item)

out.close()