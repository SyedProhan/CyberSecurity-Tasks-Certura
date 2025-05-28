
import hashlib
def input_password():
    while True:
        password = input("Enter a password: ")
        if not password:
            print("The password is Empty. Please enter a password.")
            continue

        confirm = input("Confirm password: ")
        if password != confirm:
            print("Passwords do not match. Try again.")
            continue

        return password

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest() #convert string to bytes and then to hexadecimal string

def store_hash(hash_password, filename="Passwords.txt"):
    with open(filename, "a") as file:
        file.write(hash_password + "\n")
    print(f"Password stored in '{filename}'")

def verify_password(filename="Passwords.txt", max_attempts=3):
    try:
        with open(filename, "r") as file:
            stored_hashes=[line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("Password not found. Please register a new password first.")
        return False

    for attempt in range(1,max_attempts+1):
        password = input(f"Attempt {attempt}/{max_attempts} Enter password for verification( or type 'exit' to exit): ")
        if password.lower()=='exit':
            print("Exiting...")
            return False

        hashed_input = hashlib.sha256(password.encode()).hexdigest()

        if hashed_input in stored_hashes:
            print("Password verified.")
            return True
        else:
            print("Password not verified.")

    print("Too many failed attempts. Access denied.")
    return False

user_password = input_password()
hash_password=hash_password(user_password)
print("The password entered is accepted.")
print("The hashed password is: ", hash_password)
store_hash(hash_password)
verify_password()




