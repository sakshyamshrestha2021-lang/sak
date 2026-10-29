import random as R
import time as T
print("=== NEURAL BREACH=== ")
for i in range(20):
    print("|",end="",flush =True)
    T.sleep(0.2)
U = input("\nenter a username : ").lower().strip()
T.sleep(0.5)
print(f"welcome to Neural Breach {U} i am vision your ai assistant for this game")
T.sleep(0.5)
print("vision >> selecting target web..")
T.sleep(0.5)
for i in range(20):
    print("|",end="",flush =True)
    T.sleep(0.2)
x = ["www.google.com","www.github.com","www.rajarshigurukul.edu.np","www.shutterstock.com","www.youtube.com","www.spotify.com","www.instagram.com",]
Y = R.choice(x)
print(f"target found \n= {Y} =")
print("vision.ai >> to find weak spots of the website we will be using 'dirb' .DIRB is a command-line web content scanner written in C."
      "\n It works like a web-based brute-forcer—it launches a dictionary attack against a web server to find hidden directories and files")
T.sleep(0.5)
print("vision >> the syntax for dirb is 'dirb <website name>. Type it in your console to run a scan")
while True:
    cmd = input(f"\n{U}@neural-breach:~$ ").strip().lower()
    if cmd == f"dirb {Y}":
        print(f"\n[*] Launching DIRB scan against {Y}...")
        T.sleep(1)
        wordlist = ["admin", "login", "secret", "backup.zip", "api", "dashboard", "config.bak", "robots.txt"]
        for word in wordlist:
            T.sleep(0.4)
            status_code = R.choice([200, 403, 404, 404])
            if status_code == 200:
                print(f"[+] FOUND: http://{Y}/{word} (CODE: 200)")
            elif status_code == 403:
                print(f"[!] FORBIDDEN: http://{Y}/{word} (CODE: 403)")
            else:
                print(f"[-] NOT FOUND: http://{Y}/{word} (CODE: 404)")
                print(f"[-] FOUND: http://{Y}/adm/")
        print("\n[+] Scan complete.")
        break
    else:
        print(f"vision >> Invalid syntax. Remember to type: dirb {Y}")
