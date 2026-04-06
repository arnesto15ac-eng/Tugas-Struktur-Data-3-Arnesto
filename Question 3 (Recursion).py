def gcd(a, b):
    if b == 0:  # base case
        return a
    else:
        return gcd(b, a % b)

# Contoh
print("GCD:", gcd(48, 18))