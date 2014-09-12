a = ['This is the beginning of the story']

for i in range(0, 3):
    print a[i]
    nextLine = raw_input()
    a.append(nextLine)

print "\n"
print "\n".join(a)
