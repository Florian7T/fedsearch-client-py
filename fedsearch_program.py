import os
import fedsearch

api = fedsearch.api()
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

def check_if_any(x:str)-> bool:
    if x.find('{email}') !=-1 or x.find('{password}') !=-1 or x.find('{email}') !=-1 or x.find('{token}') !=-1 or x.find('{ip}') !=-1 or x.find('{database}') !=-1:
        return True
    return False

print("Welcome to fedsearch.cf!")
key = input("Key => ")
if len(api.search(key,'monkey')) == 2: # cba reading & filtering the html
    print("Invalid key! The program will now exit..")
    exit(0)
else:
    print("Valid key!")

out_format = input("""
Format options: {email}, {password}, {ip}, {token}, {database}, {num}
Format examples:
# {email} {password}
# {email}+{password} | {ip} {database}

Format => """)

if not check_if_any(out_format):
    print("Non valid Format: Make sure to use at least 1 of the options")
    print("The program will now exit..")
    exit(0)

while True:
    response = api.search(key, input("Query => "))
    c=0
    print()
    for result in response:
        c+=1
        try:
            email, password, ip, token, database = result ['email'], result ['password'], result ['ip'], result ['token'], result ['database']
            print(out_format.replace('{email}',email).replace('{password}',password).replace('{ip}',ip).replace('{token}',token).replace('{database}',database).replace('{num}',str(c)))
        except TypeError:
            print("# 0 results for this Query")
            break
    print()