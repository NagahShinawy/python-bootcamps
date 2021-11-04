# string formatting, f string, string concatenate

info = "username: {username}\nnationalID: {nid}\ndate of birth: {dob}"

username = "James"
nationalid = "1234567890"
date_of_birth = "1990-01-01"


print(info.format(username=username, nid=nationalid, dob=date_of_birth))


user = {
    "username": username,
    "nid": nationalid,
    "dob": date_of_birth,
}


print("#" * 100)

print(info.format(**user))


book = "title: {0}\nprice: {1}\npages: {2}"

print(book.format("Clean code", 700, 10))

print("#" * 50)


HOST = "localhost"
PORT = 5432
DB = "centers"

server = f"host: {DB}\nport: {PORT}\ndb: {DB}"

print(server)