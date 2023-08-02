from manager import Manager
m=Manager()
m.generate_password("google","gman",9)
m.generate_password("youtube","gman",10)
m.save()
print(m.load())


