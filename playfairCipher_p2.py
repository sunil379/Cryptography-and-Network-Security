class Playfair:
    def __init__(self, key, plain_text):
        self.key = key.lower()
        self.plain_text = plain_text.lower()
        self.matrix = [['' for _ in range(5)] for _ in range(5)]

    def clean_playfair_key(self):
        new_key = ''
        for char in self.key:
            if char not in new_key:
                new_key += char
        self.key = new_key

    def generate_cipher_key(self):
        key_set = set(self.key.replace('j', 'i'))
        temp_key = self.key
        for i in range(26):
            ch = chr(i + 97)
            if ch == 'j':
                continue
            if ch not in key_set:
                temp_key += ch

        idx = 0
        for i in range(5):
            for j in range(5):
                self.matrix[i][j] = temp_key[idx]
                idx += 1

        print("Playfair Cipher Key Matrix:")
        for row in self.matrix:
            print(row)

    def format_plain_text(self):
        message = self.plain_text.replace('j', 'i')
        i = 0
        while i < len(message) - 1:
            if message[i] == message[i + 1]:
                message = message[:i + 1] + 'x' + message[i + 1:]
            i += 2
        if len(message) % 2 == 1:
            message += 'x'
        return message

    def form_pairs(self, message):
        return [message[i:i+2] for i in range(0, len(message), 2)]

    def get_char_pos(self, ch):
        for i in range(5):
            for j in range(5):
                if self.matrix[i][j] == ch:
                    return [i, j]
        return [-1, -1]

    def encrypt_message(self):
        message = self.format_plain_text()
        msg_pairs = self.form_pairs(message)
        enc_text = ""
        for pair in msg_pairs:
            ch1, ch2 = pair[0], pair[1]
            ch1_pos = self.get_char_pos(ch1)
            ch2_pos = self.get_char_pos(ch2)

            if ch1_pos[0] == ch2_pos[0]:
                ch1_pos[1] = (ch1_pos[1] + 1) % 5
                ch2_pos[1] = (ch2_pos[1] + 1) % 5
            elif ch1_pos[1] == ch2_pos[1]:
                ch1_pos[0] = (ch1_pos[0] + 1) % 5
                ch2_pos[0] = (ch2_pos[0] + 1) % 5
            else:
                ch1_pos[1], ch2_pos[1] = ch2_pos[1], ch1_pos[1]

            enc_text += self.matrix[ch1_pos[0]][ch1_pos[1]] + self.matrix[ch2_pos[0]][ch2_pos[1]]

        return enc_text

def main():
    print("Example-1\n")
    key1 = input("Enter the key: ")
    plain_text1 = input("Enter the plain text: ")
    print(f"Key: {key1}")
    print(f"PlainText: {plain_text1}")
    pfc1 = Playfair(key1, plain_text1)
    pfc1.clean_playfair_key()
    pfc1.generate_cipher_key()
    enc_text1 = pfc1.encrypt_message()
    print(f"Cipher Text is: {enc_text1}")

    print("\nExample-2\n")
    key2 = input("Enter the key: ")
    plain_text2 = input("Enter the plain text: ")
    print(f"Key: {key2}")
    print(f"PlainText: {plain_text2}")
    pfc2 = Playfair(key2, plain_text2)
    pfc2.clean_playfair_key()
    pfc2.generate_cipher_key()
    enc_text2 = pfc2.encrypt_message()
    print(f"Cipher Text is: {enc_text2}")

if __name__ == "__main__":
    main()
