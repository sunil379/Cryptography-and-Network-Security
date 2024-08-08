import numpy as np

def get_key_matrix():
    key = input("Enter key matrix: ")
    sq = int(np.sqrt(len(key)))
    if sq * sq != len(key):
        raise ValueError("Cannot form a square matrix")
    
    key_matrix = np.zeros((sq, sq), dtype=int)
    k = 0
    for i in range(sq):
        for j in range(sq):
            key_matrix[i][j] = ord(key[k]) - 97
            k += 1
    return key_matrix

def is_valid_matrix(key_matrix):
    det = int(np.linalg.det(key_matrix)) % 26
    if det == 0:
        raise ValueError("Det equals to zero, invalid key matrix!")

def is_valid_reverse_matrix(key_matrix, reverse_matrix):
    product = np.dot(key_matrix, reverse_matrix) % 26
    if not np.array_equal(product, np.eye(2, dtype=int)):
        raise ValueError("Invalid reverse matrix found!")

def reverse_matrix(key_matrix):
    det = int(np.linalg.det(key_matrix))
    det_mod26 = det % 26
    factor = pow(det_mod26, -1, 26)
    
    adjugate = np.array([[key_matrix[1][1], -key_matrix[0][1]],
                         [-key_matrix[1][0], key_matrix[0][0]]])
    reverse_matrix = (factor * adjugate) % 26
    reverse_matrix = np.mod(reverse_matrix, 26)
    return reverse_matrix

def echo_result(label, adder, phrase):
    result = ''.join(chr(c + (64 + adder)) for c in phrase)
    print(f"{label} {result}")

def encrypt(phrase, alpha_zero):
    adder = 1 if alpha_zero else 0
    phrase = ''.join(filter(str.isalpha, phrase)).upper()
    
    if len(phrase) % 2 == 1:
        phrase += 'Q'
    
    key_matrix = get_key_matrix()
    is_valid_matrix(key_matrix)
    
    phrase_to_num = [(ord(c) - (64 + adder)) for c in phrase]
    phrase_encoded = []
    
    for i in range(0, len(phrase_to_num), 2):
        x = (key_matrix[0][0] * phrase_to_num[i] + key_matrix[0][1] * phrase_to_num[i + 1]) % 26
        y = (key_matrix[1][0] * phrase_to_num[i] + key_matrix[1][1] * phrase_to_num[i + 1]) % 26
        phrase_encoded.extend([x, y])
    
    echo_result("Encoded phrase:", adder, phrase_encoded)

def decrypt(phrase, alpha_zero):
    adder = 1 if alpha_zero else 0
    phrase = ''.join(filter(str.isalpha, phrase)).upper()
    
    key_matrix = get_key_matrix()
    is_valid_matrix(key_matrix)
    
    phrase_to_num = [(ord(c) - (64 + adder)) for c in phrase]
    rev_key_matrix = reverse_matrix(key_matrix)
    is_valid_reverse_matrix(key_matrix, rev_key_matrix)
    
    phrase_decoded = []
    for i in range(0, len(phrase_to_num), 2):
        x = (rev_key_matrix[0][0] * phrase_to_num[i] + rev_key_matrix[0][1] * phrase_to_num[i + 1]) % 26
        y = (rev_key_matrix[1][0] * phrase_to_num[i] + rev_key_matrix[1][1] * phrase_to_num[i + 1]) % 26
        phrase_decoded.extend([x, y])
    
    echo_result("Decoded phrase:", adder, phrase_decoded)

def main():
    print("Hill Cipher Implementation (2x2)")
    print("-------------------------")
    print("1. Encrypt text (A=0,B=1,...Z=25)")
    print("2. Decrypt text (A=0,B=1,...Z=25)")
    print("3. Encrypt text (A=1,B=2,...Z=26)")
    print("4. Decrypt text (A=1,B=2,...Z=26)")
    print()
    print("Type any other character to exit")
    print()

    opt = input("Select your choice: ")
    if opt in {'1', '2', '3', '4'}:
        phrase = input("Enter phrase: ")
        if opt == '1':
            encrypt(phrase, True)
        elif opt == '2':
            decrypt(phrase, True)
        elif opt == '3':
            encrypt(phrase, False)
        elif opt == '4':
            decrypt(phrase, False)

if __name__ == "__main__":
    main()
