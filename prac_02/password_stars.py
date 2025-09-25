"""Practical 02"""
MIN_PW_LENGTH = 5

def main():
    """Password Check with Functions"""

def get_password(min_len: int) -> str:
    while True:
        password = input(f"Password (minimum of {min_len} characters): ")
        if len(password) >= min_len:
            return password
        print(f"Too few characters. Try again.")

password = get_password(MIN_PW_LENGTH)
print ('*' * len(password))

if __name__ == '__main__':
    main()