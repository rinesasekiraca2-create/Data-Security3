def encrypt_file():

    process("Encrypt")

def decrypt_file():

    process("Decrypt")

def process(mode):

    if not validate_inputs():

        return

