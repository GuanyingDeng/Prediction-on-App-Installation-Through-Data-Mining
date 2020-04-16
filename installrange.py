infile=open('googleplaystore0022.csv', 'r')
outfile=open('gg00.csv','w')

# use comma to split between attributes
for line in infile:
    line=line[:-1]
    fields=line.split(',')

    # Devide installs into 3 groups
    if fields[12] == '':
        continue
    if int(fields[12])<30000:
        fields[12]='1'
    elif 30000<=int(fields[12])<750000:
        fields[12]='2'
    else:
        fields[12]='3'

    print(fields[0]+','+fields[1]+','+fields[2]+','+fields[3]+','+fields[4]+','+fields[5]+','+fields[6]+','+fields[7]+','+fields[8]+','+fields[9]+','+fields[10]+','+fields[11]+','+fields[12],file=outfile)

infile.close()
outfile.close()
