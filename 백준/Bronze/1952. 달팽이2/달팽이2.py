M,N = map(int, input().split())

if M > N:
    print(2 *N - 1)
else:
    print((M-1)*2)