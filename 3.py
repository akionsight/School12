def find_nth_root(n, r):
    return n**(1/r)

base = int(input("Enter Base: "))
radix = int(input("Enter Radix: "))

print(f"The {radix}th root of {base} is {round(find_nth_root(base, radix), 3)}")