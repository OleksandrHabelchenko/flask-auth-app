from werkzeug.security import generate_password_hash, check_password_hash

hash = generate_password_hash("qwerty123")
print("Password hash : ", hash)

result1 = check_password_hash(hash, "qwerty123")
print("Correct password: ", result1)

result2 = check_password_hash(hash, "wrongpass")
print("Incorrect password: ", result2)