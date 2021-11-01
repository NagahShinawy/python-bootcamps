locations = ["Cairo", "Alex", "SSH", "Aswan", "Luxor"]

cairo = locations[0]
alex = locations[1]
ssh = locations[2]

print(cairo)
print(alex)
print(ssh)


cairo_ssh = locations[:3]

print(cairo_ssh)

# print(locations[10])  # IndexError: list index out of range

capitals = [
    {"name": "Cairo", "country": "Egypt"},
    {"name": "Riyad", "country": "KSA"},
    {"name": "Berlin", "country": "Germany"},
    {"name": "Paris", "country": "France"},
]

for capital in capitals:
    for name, country in capital.items():
        print(name, country)


print("#" * 100)

EGYPT = {"name": "Cairo", "country": "Egypt", "pop": "100M", "region": "Africa"}

for key, value in EGYPT.items():
    print(key, value)