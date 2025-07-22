import re

email_regex = re.compile(r'^\w+(?:[.\-+!%]\w+)*@\w+(?:[.\-]\w+)+$')

def is_valid_email(email):
    return bool(email_regex.match(email))
