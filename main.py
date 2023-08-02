from manager import Manager
PIN=0000


def login():
    while True:
     p=input("enter pin:")
     if p== PIN:
        break
def menu():
    print("pick an option")
    print("1. Generate password")
    print("2. Update password")
    print("3. Delete password")
    print("4. Get password")
    print("5.Quit")
    choice=input("Enter option:")
    return choice
def generate_pass(m):
    site=input("Enter site name: ")
    usr=input("Enter username: ")
    length= input("password length: ")
    print("password: "+ m.generate_password(site,usr,length))
def get_pass(m):
    site=input("Enter site name: ")
    usr=input("Enter username: ")
    print("username: ",usr)
    print("password: ",m.getpassword(site,usr))
def delete(m):
    site=input("Enter site: ")
    usr=input("enter username: ")
    m.delete(site,usr)
def delete(m):
    site = input("Enter the site: ")
    usr = input("Enter username")
    m.delete(site, usr)

def update(m):
    site=input("Enter site")
    usr=input("Enter username: ")
    p = input("Enter password")
    m.update(site, usr, p)
    print("password update")

def main():
    login()
    m=Manager()
    m.load()
    while  True:
        choice=menu()
        if choice==1:
            update(m)
        elif choice==2:
            print("not ready")

        elif choice==3:
            delete(m)
        elif choice==4:
            get_pass(m)
        else:
            m.save()
            break

main()