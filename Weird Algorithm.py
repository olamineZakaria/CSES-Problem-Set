n = int(input())

sequence = []

while n!=1:
    sequence.append(n)
    if n % 2 ==0:
        n = n // 2
    else:
        n = n * 3 + 1

sequence.append(1)

print(' '.join(map(str,sequence)))