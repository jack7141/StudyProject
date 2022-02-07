new_id = "123_.def"
deleteOfExecpt = "~!@#$%^&*()=+[{]}:?,<>/"
replace = ['...','..']
genesis_id = new_id
# 1
new_id = new_id.lower()
# 2
for i in deleteOfExecpt:
    new_id = new_id.replace(i,'')
# 3
for i in replace:
    new_id = new_id.replace(i,'.')
# 4
if new_id[0] == '.':
    new_id = new_id[1:]
elif new_id[-1] == '.':
    new_id = new_id[:-1]
# 5
if new_id == '':
    new_id = 'a'*len(genesis_id)
# 6
new_id = new_id[:15]
if new_id[-1] == '.':
    new_id = new_id[:-1]

for i in new_id:
    if i == ' ':
        new_id = new_id.replace(' ','')
while len(new_id) <= 2:
    new_id += new_id[-1]

print(new_id)
