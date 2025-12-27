from password_cracker import crack_sha1_hash

print("--- Testing without Salts ---")
# Should return "sammy123"
print(f"Cracking 'b305...': {crack_sha1_hash('b305921a3723cd5d70a375cd21a61e60aabb84ec')}")

# Should return "abacab"
print(f"Cracking 'c7ab...': {crack_sha1_hash('c7ab388a5ebefbf4d550652f1eb4d833e5316e3e')}")

# Should return "password"
print(f"Cracking '5baa...': {crack_sha1_hash('5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8')}")

print("\n--- Testing WITH Salts ---")
# Should return "superman"
print(f"Cracking '53d8...': {crack_sha1_hash('53d8b3dc9d39f0184144674e310185e41a87ffd5', use_salts=True)}")

# Should return "q1w2e3r4t5"
print(f"Cracking 'da5a...': {crack_sha1_hash('da5a4e8cf89539e66097acd2f8af128acae2f8ae', use_salts=True)}")

# Should return "bubbles1"
print(f"Cracking 'ea3f...': {crack_sha1_hash('ea3f62d498e3b98557f9f9cd0d905028b3b019e1', use_salts=True)}")

# Should return "PASSWORD NOT IN DATABASE"
print(f"Cracking 'missing...': {crack_sha1_hash('0000000000000000000000000000000000000000', use_salts=True)}")