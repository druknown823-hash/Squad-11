# Email Validation 
import re
def is_valid_email(email):
    # Define a regex pattern for validating an Email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
    
    # Use re.match to check if the email matches the pattern
    if re.match(pattern, email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is a not valid email address.")
# Test the function
test_emails = "kushagra.khatri2007@gmail.com"
is_valid_email(test_emails)

