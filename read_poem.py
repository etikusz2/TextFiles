jabber = open('Jabberwocky.txt', 'r')

for line in jabber:
    print(line.strip())

jabber.close()