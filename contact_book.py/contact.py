import json
try:
    with open("contacts.json","r") as file:
        data=json.load(file)
except FileNotFoundError:
    data = {"contacts":[]}
print("---| Contact Book Program |---")
while True:
    print("1.View all contacts\n2.Add new contact\n3.Remove contact\n4.exit")
    while True:
        try:
            choice = int(input("Enter your choice:"))
            while choice not in[1,2,3,4]:
                print("Enter correct choice!")
                choice = int(input("Enter your choice:"))
            break
        except ValueError:
            print("Enter numbers only!")
    if choice==1:
        for contact in data["contacts"]:
            print(f"Name:{contact['first_name']} {contact['last_name']} | Phone:{contact['phone']} | Email:{contact['email']}")
    elif choice==2:
        print("Enter information of new contact as described below!")
        f_name = input("Enter first name:")
        l_name = input("Enter last name:")
        phone = input("Enter phone number:")
        mail=input("Enter gmail account:")
        n_user={"first_name":f_name,"last_name":l_name,"phone":phone,"email":mail}
        data["contacts"].append(n_user)
        print(f"Contact:\nName:{f_name} {l_name} | Phone number:{phone} | Gmail account:{mail}\nSaved successfully in contact book\n")
        print("---New contact book---")
        for contact in data["contacts"]:
            print(f"Name:{contact['first_name']} {contact['last_name']} | Phone:{contact['phone']} | Email:{contact['email']}")
    elif choice == 3:
        f_name=input("Enter first name of contact:")
        l_name=input("Enter last name of contact:")
        for contact in data["contacts"]:
            if f_name.lower()==contact["first_name"].lower() and l_name.lower()==contact["last_name"].lower():
                data["contacts"].remove(contact)
                print("Contact removed successfully!")
                break
        else:
            print("Contact not found!")
    else:
        break
    c = input("Would you like to perform another operation(yes/no):").lower()
    while c not in["yes","no"]:
        c = input("Only yes/no:")
    if c=="no":
        print("Contact book closed!")
        break
with open("contacts.json","w") as file:
    json.dump(data,file,indent=4)