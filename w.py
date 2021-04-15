с = input()
l = len(с)
l = l//2
for i in range(l):
    if с[i] != с[-1-i]:
        print("итс нот э паледроме")
        quit()
print("итс э паледроме")
c = input()