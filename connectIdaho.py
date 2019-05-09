import os
import subprocess

ip = 0

while ip not in range(201, 210):
    print("Enter a valid number ")
    ip = int(input("Which server? [201-210]: "))


def connectToByui(ip):
    print("Connecting to BYUi... ")
    server = " wurby@157.201.194."
    subprocess.call(f"ssh {server}{ip} -p 215", shell=True)


def tunnelToByui(ip):
    print("Tunneling to BYUi... ")
    server = "-L 1024:157.201.194.254:80 wurby@157.201.194."
    subprocess.call(f"sudo ssh {server}{ip} -p 215", shell=True)


answer = input("tunnel or ssh? ")

if answer[0].lower() == "t":
    tunnelToByui(ip)
else:
    connectToByui(ip)
