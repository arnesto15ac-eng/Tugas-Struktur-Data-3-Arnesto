def decimal_to_binary(n):
    if n == 0:  # base case
        return 0
    else:
        return n % 2 + 10 * decimal_to_binary(n // 2)

# Contoh
print("Binary:", decimal_to_binary(10))