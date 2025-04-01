 #Variables and Functions
Use snake_case (lowercase with underscores)
Be descriptive but concise

✅ email_address = "bob@example.com"
✅ calculate_discount_price()
❌ EmailAddress = "bob@example.com" (PascalCase is for classes)
❌ calcDP() (too short and unclear)

#Constants
Use UPPER_CASE_WITH_UNDERSCORES

✅ MAX_USERS = 250
✅ TIMEOUT_LIMIT = 120
❌ TimeoutLimit = 120

#Classes
Use PascalCase (Each word starts with a capital letter)

✅ class PaymentGateway:
❌ class payment_gateway: (wrong, should be PascalCase)

Methods (inside classes)
Use snake_case, just like functions

✅ def check_balance(self):
❌ def CheckBalance(self): (too Java-like)

#Private Variables and Methods
Prefix with a single underscore _ for internal use
Use double underscore __ for name mangling (rarely needed)

✅ _temp_cache = {}
✅ __api_key = "secret123" (name-mangled)

#Modules and Packages
Use short, lowercase names
Avoid capital letters and underscores

✅ import log_reader
❌ import LogReader
 
#Booleans
Use prefixes like is_, has_, or can_ for clarity

✅ is_enabled = True
✅ has_access = False
❌ enabled = True (not descriptive enough)

#Exceptions
Use PascalCase and end with Error

✅ class AccessDeniedError(Exception):
❌ class accessdenied(Exception):

#Type Hints
Use type hints for clarity and maintainability

✅ def multiply(a: int, b: int) -> int:




            








