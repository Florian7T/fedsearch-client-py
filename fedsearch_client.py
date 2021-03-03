import os,requests,datetime

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')


print("Welcome to fedsearch!")
key = input("Key => ")
if len(requests.post('https://fedsearch.cf/API/search_api.php',data={'search': 'monkey', 'submit': '', 'key': key, }).json()) == 2: # using this until proper method is available
    print("Invalid key! The program will now exit..")
    exit(0)
else:
    print("Valid key!")

out_format = input("""
Format options: {email}, {password} or {hash}, {ip}, {token}, {database}, {count}
Format examples:
# {email} {password}
# {email}+{password} | {ip} {database}
# {count}: {email} ___ {hash}

Format => """)

if out_format.find('{email}') ==-1 and out_format.find('{password}') ==-1 and out_format.find('{email}') ==-1 and out_format.find('{token}') ==-1 and out_format.find('{ip}') ==-1  and out_format.find('{database}') ==-1 and out_format.find('{hash}') ==-1 and out_format.find('{count}') ==-1:
    print("Non valid Format: Make sure to use at least 1 of the options")
    print("The program will now exit..")
    exit(0)


while True:
    out = []
    response = requests.post('https://fedsearch.cf/API/search_api.php',data={'search': input("Query => "), 'submit': '', 'key': key, }).json()

    print()
    c = 0
    if 'No Results Found' in str(response):
        print('No Results Found!\n')
        continue

    for result in response:
        c += 1
        email, password, ip, token, database = result ['email'], result ['password'], result ['ip'], result ['token'], result ['database']
        opp = out_format.replace('{email}', email).replace('{password}', password).replace('{ip}', ip).replace('{token}', token).replace('{database}', database).replace('{count}', str(c)).replace('{hash}',password)
        print(opp)
        out.append(opp)
    print()
    print("Writing to logfile..")
    fn = str(datetime.datetime.now().strftime("%S_%M_%H-%d_%m_%y"))+'.txt'
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),fn),'w+') as f:
        for out_ in out:
            f.write(out_.replace('\ufffd','')+"\n")
        f.close()
    print(f"Output saved to: \'{fn}\'")
    print()
