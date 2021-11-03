for i in range(1, 11):
    print(i, end=" ")


print("")


def send_email(recipient):
    print(f"sending to '{recipient}'")


emails = ["john@test.com", "james@test.com", "adam@test.com", "loen@test.com"]

for email in emails:
    send_email(email)
