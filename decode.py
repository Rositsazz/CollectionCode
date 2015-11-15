def reverse_dict(dictionary):
    new_dictionary = {}
    for key in dictionary:
        value = dictionary[key]
        new_dictionary[value] = key

    return new_dictionary


def decode_word(encrypted_word, cipher):
    decrypt = reverse_dict(cipher)
    decode = ""
    for char in encrypted_word:
        decode += decrypt[char]

    return decode


def main():
    print(decode_word("mjriew",{'h': 'i', 'y': 'j', 'o': 'e', 't': 'r', 'n': 'w', 'p': 'm'}))
    print(decode_word("wfhsftzzuys", {'r': 'f', 'o': 'h', 'i': 'u', 'm': 'z', 'g': 's', 'a': 't', 'p': 'w', 'n': 'y'}))


if __name__ == '__main__':
    main()
