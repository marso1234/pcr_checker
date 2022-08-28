from character_pool import character_pool

filename = 'team_list.txt'
outputname = 'output.txt'

#Empty
with open(outputname, 'w',encoding="utf-8") as output_file:
    output_file.write('')

with open(filename, 'r',encoding="utf-8") as input_file:
    lines = input_file.readlines()
    lines = [i.strip() for i in lines]
    lack_characters = lines[0].split(':')[1].split(',')
    lines = lines[4:]
    for i in range(len(lines)):
        for j in range(5):
            if lines[i][j] in lack_characters:
                lines[i][j] = lines[i][j] + '*'

success_cp = []

for l1 in lines:
    for l2 in lines:
        if l1 == l2:
            break
        for l3 in lines:
            if l2 == l3 or l1 == l3:
                break
            cp = character_pool(l1,l2,l3)
            if cp.check_valid():
                success_cp.append(cp)
                

success_cp.sort(key=lambda x: x.score_delt(),reverse=True)
for cp in success_cp:
    cp.save_combination(outputname)

