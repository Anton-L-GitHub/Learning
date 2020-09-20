from sys import argv
assert len(argv) == 4
txt = argv[3]
with open(argv[1], 'r') as f1, open(argv[2], 'w') as f2:
    for r in f1:
        if r.find(txt) >= 0:
            f2.write(r)