import string

def trans(s):
    p=s.maketrans(string.punctuation+string.ascii_uppercase," "*len(string.punctuation)+string.ascii_lowercase)
    return s.translate(p)

while True:
    s=input()
    if s=='DONE':
        break
    else:
        s=trans(s)
        l=s.split(" ")
        s="".join(l)
        if s==s[::-1]:
            print("You won't be eaten!")
        else:
            print('Uh oh..')
