# Python Naming and Style Guide

# Variables and Functions

# Use snake_case (lowercase with underscores)
# Be descriptive but concise

# Correct examples:
email_address = "bob@example.com"
def calculate_discount_price():
    pass

# Incorrect examples:
# EmailAddress = "bob@example.com"  # PascalCase is for classes
# def calcDP():  # too short and unclear
#     pass

# Constants

# Use UPPER_CASE_WITH_UNDERSCORES

# Correct examples:
MAX_USERS = 250
TIMEOUT_LIMIT = 120

# Incorrect example:
# TimeoutLimit = 120  # Not all caps and contains mixed case


# Classes


# Use PascalCase (Each word starts with a capital letter)

# Correct example:
class PaymentGateway:
    pass

# Incorrect example:
# class payment_gateway:  # should use PascalCase
#     pass

# Methods (inside classes)

# Use snake_case, just like functions

# Correct example:
class BankAccount:
    def check_balance(self):
        pass

# Incorrect example:
# def CheckBalance(self):  # too Java-like
#     pass

# Private Variables and Methods

# Prefix with a single underscore _ for internal use
# Use double underscore __ for name mangling (rarely needed)

# Correct examples:
_temp_cache = {}
__api_key = "secret123"  # name-mangled

# Modules and Packages

# Use short, lowercase names
# Avoid capital letters and underscores

# Correct import:
# import log_reader

# Incorrect import:
# import LogReader

# Booleans

# Use prefixes like is_, has_, or can_ for clarity

# Correct examples:
is_enabled = True
has_access = False

# Incorrect example:
# enabled = True  # not descriptive enough

# Exceptions

# Use PascalCase and end with Error

# Correct example:
class AccessDeniedError(Exception):
    pass

# Incorrect example:
# class accessdenied(Exception):
#     pass

# Type Hints

# Use type hints for clarity and maintainability

# Correct example:
def multiply(a: int, b: int) -> int:
    return a * b
