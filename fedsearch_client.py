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
Format options: 
Format examples:
# {email} {password}
# {email}+{password} | {ip} {database}
# {count}: {email} ___ {hash}

Format => """)
#thanks a lot man. I usually code in java I've only recently started using python for smaller things like this
format_options = ['{email}', '{password}', '{hash}', '{ip}', '{token}', '{database}', '{count}']
if not any(x in out_format for x in format_options):
    print("Non valid Format: Make sure to use at least 1 of the options")
    print("The program will now exit..")
    exit(0)


while True:
    out = []
    query = input("Query => ")
    response = requests.post('https://fedsearch.cf/API/search_api.php',data={'search': query, 'submit': '', 'key': key, }).json()

    print()
    c = 0
    if 'No Results Found' in str(response):
        print(f'No Results Found! Query: {query}\n')
        continue

    for result in response:
        c += 1
        email, password, ip, token, database = result['email'], result['password'], result['ip'], result['token'], result['database']
        opp = out_format.replace('{email}', email)\
                        .replace('{password}', password)\
                        .replace('{ip}', ip)\
                        .replace('{token}', token)\
                        .replace('{database}', database)\
                        .replace('{count}', str(c))\
                        .replace('{hash}',password)
        print(opp)
        out.append(opp)
    print()
    print("Writing to logfile..")
    fn = datetime.datetime.now().strftime("%H_%M_%S-%d_%m_%y")+'.txt'
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),fn),'w') as f:
        f.write('\n'.join(out).replace('\ufffd','') + '\n')
    print(f"Output saved to: \'{fn}\'")
    print()
