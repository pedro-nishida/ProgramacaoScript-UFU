N = int(input())

if (((N % 2 == 0) and (N > 10)) or ((N % 2 != 0) and (N < 50))):
    print("SIM")
else:
    print("NÃO")