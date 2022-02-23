

import os
from time import sleep
os.system('cls' if os.name == 'nt' else 'clear')

"""
Simple RSA Encryption Program in Python 3.9!!!
@Author Brian Cusack
"""


def sending():
    for i in range(3):
        print('. ', end='')
        sleep(1)


def getValues():
    """ Get values p,q and e from user or default values"""
    p = int(input("Enter the value of 'p' (as Integer) or enter for default: ") or 11)
    print(f'p = {p}')
    q = int(input("Enter the value of 'q' (as Integer) or enter for default: ") or 17)
    print(f'q = {q}')
    e = int(input("Enter the value of 'e' (as Integer) or enter for default: ") or 7)
    print(f'e = {e}')
    return p, q, e


def message(n):
    """ Get message from user safely"""
    while True:
        # Input Message
        m = int(input("\nEnter the value of Message 'm' (as Integer): "))
        if m < n:
            break
        else:
            print(f"\n 😝 The value of 'm' {m} must be less than n' {n}"), sleep(1)
    return m


def generateKeys(p, q, e):
    """Generate RSA key pairs"""
    n = p*q  # Key parameter "n"
    print(f"\nThe value of 'n' is p*q: {n} "), sleep(1)
    phi_n = (p-1) * (q-1)  # Function Phi(n)
    print(f"The value of 'Phi(n)' is (p-1) * (q-1): {phi_n}"), sleep(1)
    print(f"The Public-Key (n,e): ({n}, {e})"), sleep(1)
    # Private Key parameter "d" - e inverse mod of phi(n)
    d = pow(e, -1, phi_n)
    print(f"The value of 'd' is e inverse Phi(n): {d}"), sleep(1)
    print(f"The Private-Key (n,d): ({n}, {d})"), sleep(1)
    return n,  d


def main():
    """Run the main program 🏃 """
    p, q, e = getValues()
    n,  d = generateKeys(p, q, e)
    m = message(n)
    C = pow(m, e, n)  # Encrypted Message
    print(f"\n🥳 The Ciphertext 'C' is m^e mod n: {C}"), sleep(1)
    M = pow(C, d, n)		# Decrypted Message
    print(f"🏸 The Decryphering Ciphertext with Private key d")
    sending()
    print(f'\n😎 Plaintext is: {M}')


if __name__ == "__main__":
    main()
