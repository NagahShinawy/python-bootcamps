# string methods


# 1- join
DOMAIN = "www.example.com"

ENDPOINT = "api/v1/users"

PARAMS = "1"

URL = [DOMAIN, ENDPOINT, PARAMS]

print("/".join(URL))

cc = [
    "loen@test.com",
    "adam@test.com",
    "smith@test.com",
    "james@test.com",
    "john@test.com",
]

print(cc)
to = ";".join(cc)

print(to)

FAV_LANGS = ["Python", "Java", "PHP", "Ruby", "Swift", "Kotlin"]

print(" | ".join(FAV_LANGS))


# 2- replace

WELCOME = "Hello World"

WELCOME = WELCOME.replace("Hello", "Hi")

print(WELCOME)


# 3 - startswith

names = ["james", "john", "loen", "smith", "angela", "adam"]

startj = [name for name in names if name.startswith("j")]
starta = [name for name in names if name.startswith("a")]
endn = [name for name in names if name.endswith("n")]

print(startj)
print(starta)
print(endn)


lang = "python is cool"

print(lang)
print(lang.upper())  # PYTHON IS COOL
print(lang.title())  # Python Is Cool

print(lang.capitalize())  # Python is cool

web = "HTML CSS JS"

print(web.lower())

print(web.count("S"))  # 3
