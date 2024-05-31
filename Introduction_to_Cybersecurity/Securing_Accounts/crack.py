from string import ascii_letters, digits, punctuation

key = ascii_letters + digits + punctuation

for i in key:
    for j in key:
        for k in key:
            for l in key:
                print(i, j, k, l)