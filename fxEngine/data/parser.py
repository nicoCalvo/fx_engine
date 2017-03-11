import pdb
fdest = open('pair_list.json', 'w')

with open('pairs_lists.json') as f:
    content = f.readlines()
    for line in content:
        pdb.set_trace()
        if 'name' in line:
            fdest.write(content)
