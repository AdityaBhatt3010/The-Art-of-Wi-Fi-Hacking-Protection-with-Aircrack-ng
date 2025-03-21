import itertools
import string

def generate_password_list(length, charset):
    # Generate all possible password combinations based on given length and charset.
    return [''.join(p) for p in itertools.product(charset, repeat=length)]

def main():
    print("Brute Force Password List Generator")
    length = int(input("Enter password length: "))
    
    charset = ""
    
    if input("Include lowercase letters? (yes/no): ").strip().lower() == "yes":
        charset += string.ascii_lowercase
    if input("Include uppercase letters? (yes/no): ").strip().lower() == "yes":
        charset += string.ascii_uppercase
    if input("Include numbers? (yes/no): ").strip().lower() == "yes":
        charset += string.digits
    if input("Include special characters? (yes/no): ").strip().lower() == "yes":
        charset += string.punctuation
    
    if not charset:
        print("No character set selected. Defaulting to lowercase letters.")
        charset = string.ascii_lowercase
    
    passwords = generate_password_list(length, charset)
    
    output_file = "password_list.txt"
    with open(output_file, "w") as file:
        file.write("\n".join(passwords))
    
    print(f"Password list generated and saved to {output_file}.")

if __name__ == "__main__":
    main()
