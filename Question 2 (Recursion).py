def power(x, n):
    if n == 0:  # base case
        return 1
    else:
        return x * power(x, n - 1)

# Contoh
print("Power:", power(2, 4))