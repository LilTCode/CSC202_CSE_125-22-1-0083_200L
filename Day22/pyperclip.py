import pyperclip

class PyperClip:
    def __init__(self):
        self.clipboard = pyperclip

    def copy(self, text):
        """Copy text to the clipboard"""
        self.clipboard.copy(text)

    def paste(self):
        """Paste text from the clipboard"""
        return self.clipboard.paste()

    def password(self, password_length=12):
        """Generate a random password of a given length"""
        import secrets
        import string

        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for _ in range(password_length))
        self.copy(password)
        return password

# Example usage:
clip = PyperClip()
clip.copy("Hello, World!")
print(clip.paste())  # Output: Hello, World!

new_password = clip.password(16)
print(new_password)  # Output: a randomly generated password of length 16