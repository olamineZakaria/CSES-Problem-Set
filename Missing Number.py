n = int(input())
numbers = list(map(int,input().split()))

n_sum = sum(range(n+1))
n_one_sum = sum(numbers)

print(abs(n_one_sum  - n_sum))