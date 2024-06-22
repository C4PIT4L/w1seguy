import string

def decode_flag(hex_encoded, key):
    bytes_encoded = bytes.fromhex(hex_encoded)

    decoded_chars = []
    for i in range(len(bytes_encoded)):
        decoded_chars.append(chr(bytes_encoded[i] ^ ord(key[i % len(key)])))

    decoded_flag = ''.join(decoded_chars)
    return decoded_flag


def try_variants(hex_encoded, base_key):
    charset = string.ascii_letters + string.digits
    key_variants = []

    # Generate all variants by replacing 'a' in base_key with each character in charset
    for char in charset:
        variant_key = base_key.replace('a', char)
        decoded_flag = decode_flag(hex_encoded, variant_key)
        key_variants.append((variant_key, decoded_flag))

    return key_variants


if __name__ == '__main__':
    hex_encoded = input("Enter the hex encoded flag: ").strip()

    base_key = "iDFka"

    key_variants = try_variants(hex_encoded, base_key)

    for key, decoded_flag in key_variants:
        print(f"Key: {key}")
        print(f"Decoded Flag: {decoded_flag}")
        print("-" * 20)
