# Reads two bits and prints the output of AND, OR and XOR gates.
bit_a=int(input("Enter A:"))
bit_b=int(input("Enter B:"))
if (bit_a!=0 and bit_a!=1) or (bit_b!=0 and bit_b!=1):
    print("Bits must be 0 or 1")
else:
    if bit_a==1 and bit_b==1:
        and_out=1
    else:
        and_out=0

    if bit_a==1 or bit_b==1:
        or_out=1
    else:
        or_out=0

    if bit_a!=bit_b:
        xor_out=1
    else:
        xor_out=0
    print("AND =",and_out)
    print("OR =",or_out)
    print("XOR =",xor_out)
