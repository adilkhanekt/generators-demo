

def gen_file_parts(path: str):
    with open(path, "rb") as f:
        data = f.read()
        current_position = 0
        while current_position < len(data):
            yield data[current_position : (current_position + 8)]
            current_position += 8


def gen_crypt(file_parts_iter):
    for chunk in file_parts_iter:
        yield int.to_bytes(int.from_bytes(chunk, byteorder="little") ^ 0xfe, length=8, byteorder="little")


def write_encrypted(result_path, encrypted_parts_iter):
    with open(result_path, "wb") as f:
        for chunk in encrypted_parts_iter:
            f.write(chunk)        


file_parts_gen = gen_file_parts("Bruno Mars - Treasure.mp3")
crypt_gen = gen_crypt(file_parts_gen)
write_encrypted("Bruno Mars - Treasure.mp3.encrypted", crypt_gen)


print("Encryption completed")