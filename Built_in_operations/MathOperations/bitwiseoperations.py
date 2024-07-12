# 1. Bitwise AND (&)
# The bitwise AND operation takes two binary representations and performs the AND operation on each pair of corresponding bits.

a = 5  # 0b0101
b = 3  # 0b0011
result = a & b  # 0b0001 which is 1 in decimal
print(result)  # Output: 1


# 2. Bitwise OR (|)
# The bitwise OR operation takes two binary representations and performs the OR operation on each pair of corresponding bits.

a = 5  # 0b0101
b = 3  # 0b0011
result = a | b  # 0b0111 which is 7 in decimal
print(result)  # Output: 7


# 3. Bitwise XOR (^)
# The bitwise XOR operation takes two binary representations and performs the XOR operation on each pair of corresponding bits.

a = 5  # 0b0101
b = 3  # 0b0011
result = a ^ b  # 0b0110 which is 6 in decimal
print(result)  # Output: 6


# 4. Bitwise NOT (~)
# The bitwise NOT operation takes one binary representation and inverts all the bits.

a = 5  # 0b0101
result = ~a  # 0b1010 which is -6 in decimal (two's complement representation)
print(result)  # Output: -6


# 5. Bitwise Left Shift (<<)
# The left shift operation shifts the bits of the first operand left by the number of positions specified by the second operand.

a = 5  # 0b0101
result = a << 1  # 0b1010 which is 10 in decimal
print(result)  # Output: 10


# 6. Bitwise Right Shift (>>)
# The right shift operation shifts the bits of the first operand right by the number of positions specified by the second operand.

a = 5  # 0b0101
result = a >> 1  # 0b0010 which is 2 in decimal
print(result)  # Output: 2


# Combining Bitwise Operations
# You can also combine these operations to perform more complex bitwise manipulations.

a = 5  # 0b0101
b = 3  # 0b0011

# Combining AND and OR
result = (a & b) | (a ^ b)  # (0b0001) | (0b0110) = 0b0111 which is 7 in decimal
print(result)  # Output: 7