# removeUnnecessary.py
# Guanying Deng (dguany@bu.edu)
# Zujing Zhao (zujingkl@bu.edu)
# Jingwen Guan (jwguan@bu.edu)
# This program performs some modifications to dataset, and
# write the modified dataset to a new file.

# open files
infile=open('test1.csv', 'r')
outfile=open('gg00.csv','w')

# use comma to split between attributes
for line in infile:
    line=line[:-1]
    fields=line.split(',')

    # transforms sizes ending with Mb to kb (also transform nominal to numeric)
    if fields[4][-1]=='M':
        fields[4]=fields[4][:-1]+'000'
    if fields[4][-1]=='k':
        fields[4]=fields[4][:-1]

    # removes "+" at the end of installs
    if fields[12][-1]=='+':
        fields[12]=fields[12][:-1]

    # Devide installs into 3 groups
    if fields[12] == '':
        continue
    if int(fields[12])<30000:
        fields[12]='1'
    elif 30000<=int(fields[12])<750000:
        fields[12]='2'
    else:
        fields[12]='3'

    # removes data for rows with missing values and writes to new file
    if fields[2]!='NaN' and fields[4]!='Varies with device' and fields[7]!='Unrated:
        print(fields[0]+','+fields[1]+','+fields[2]+','+fields[3]+','+fields[4]+','+fields[5]+','+fields[6]+','+fields[7]+','+fields[8]+','+fields[9]+','+fields[10]+','+fields[11]+','+fields[12],file=outfile)

infile.close()
outfile.close()
