def check(s):
    if s==s[::-1]:
       return True


while True:
    try:
        s=input()
        unique=(set(s))
        for i in range(0,len(s)):
            for j in range(i+1,len(s)):
                if check(s[i:j+1]):
                    unique.add(s[i:j+1])
        print("The string '{}' contains {} palindromes.".format(s,len(unique)))
    except:
           break
