
file = open("/Internal storage/Python/wordlist.txt")

for password in file:
    try:
        with pikepdf.open("/Internal storage/Python/1.pdf",password.strip()) as pdf:
            print(colored("password Found: {}".format(password),'green'))
            break
    except:
        print(colored("Trying Password: {}".format(password),'red'))
        continue