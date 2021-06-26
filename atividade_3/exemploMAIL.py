fname = input('Enter a file name: ')
if len(fname) < 1: fname = "mbox-short.txt"

try:
    fhandle = open(fname)
except:
    print('Error opening file.')
    exit()

address = dict()
for line in fhandle:
    line = line.rstrip()
    
    if len(line) == 0 or 'From ' not in line: continue
    wrds = line.split()
    
    # the second term of the line is the e-mail address
    address[wrds[1]] = address.get(wrds[1], 0) + 1

# print(address)

lst = list()
for key, val in address.items():
    lst.append( (val, key) )

lst.sort(reverse=True)

count, email = lst[0]
print(email, count)
