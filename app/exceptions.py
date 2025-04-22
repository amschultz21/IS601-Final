# app/exceptions.py

class DuplicateEmailException(Exception):
    def __init__(self, email: str):
        self.email = email
