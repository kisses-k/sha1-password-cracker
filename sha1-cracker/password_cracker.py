import hashlib

def crack_sha1_hash(hash_to_crack, use_salts=False):
    # Load passwords from the file into a list
    passwords_arr = []
    with open("top-10000-passwords.txt", "r") as f:
        # Read lines and strip newline characters
        passwords_arr = [line.strip() for line in f]

    # Load salts if needed
    salts_arr = []
    if use_salts:
        with open("known-salts.txt", "r") as f:
            salts_arr = [line.strip() for line in f]

    # Iterate through each password in the database
    for password in passwords_arr:
        if use_salts:
            # If using salts, we must check every combination of salt + password
            for salt in salts_arr:
                # Check Prepend: Salt + Password
                term_prepend = salt + password
                hash_prepend = hashlib.sha1(term_prepend.encode()).hexdigest()
                
                if hash_prepend == hash_to_crack:
                    return password

                # Check Append: Password + Salt
                term_append = password + salt
                hash_append = hashlib.sha1(term_append.encode()).hexdigest()

                if hash_append == hash_to_crack:
                    return password
        else:
            # Standard check without salts
            # Encode string to bytes, hash it, then convert to hex string
            hashed_pass = hashlib.sha1(password.encode()).hexdigest()
            
            if hashed_pass == hash_to_crack:
                return password

    # If the loop finishes without returning, the password wasn't found
    return "PASSWORD NOT IN DATABASE"