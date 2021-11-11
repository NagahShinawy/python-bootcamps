# how to write python clean code
# https://dev.to/jerrynsh/how-to-write-clean-code-in-python-2pf3

# todo: 1. Name Things Properly

expired = True  # Don't
is_expired = True  # Do


# ########## ########## ########## #########

expire = "2021-04-17 03:25:37.403283"  # Don't

expiration_date = "2024-01-01"  # Do


"""
The reason why expired is a less ideal name is because expired on its own is ambiguous.
A new developer working on the project wouldn't know whether expired is a date or a boolean.
"""

# todo 2: For example if the existing project names a Response object as "res" already:

# Existing functions
# ^^^^^^^^^^^^^^^^^^


def existing_function(res, var):
    # Do something...
    pass


def another_existing_function(res, var):
    # Do something...
    pass


# Example 1
# ^^^^^^^^^
# Don't
def your_new_function(response, var):
    # Do something...
    pass


# Do
def your_new_function(res, var):
    # Do something...
    pass


# ########################################################

# todo: 3. Avoid Double Negatives


# Example to check if a user's membership is valid or not:

# Don't
is_invalid = False
if not is_invalid:
    print("User's membership is valid!")

# Do
is_valid = True
if not is_valid:
    print("User's membership is invalid!")

# ########################################################

# todo: 4. Write Self-Explanatory Code

# Don't write long conditionals
if (
    meeting
    and (current_time > meeting.start_time)
    and (user.permission == "admin" or user.permission == "moderator")
    and (not meeting.is_cancelled)
):
    print("# Do something...")

# Do capture them in many variables that reads like English
is_meeting_scheduled = meeting and not meeting.is_cancelled
has_meeting_started = current_time > meeting.start_time
has_user_permission = user.permission == "admin" or user.permission == "moderator"
if is_meeting_scheduled and has_meeting_started and has_user_permission:
    print("# Do something...")


# ########################################################

# todo: 5- Do not abuse comments
# Example of getting an email returned from a 3rd party API:

# Example 1
# ^^^^^^^^^
# Do
raw_string = get_user_info()
email = raw_string.split("|", maxsplit=2)[
    -1
]  # NOTE: raw_string e.g. "Magic Rock|jerry@example.com"


# ########################################################
