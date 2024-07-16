import telnetlib

# HOST = "185.84.160.58"
# user = "xver"
# password = "Ra%N46@*QYcN1aZE"

HOST = "192.168.122.3"
user = "mild-honey"
password = "Honey155@Mild-R"

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode("ascii") + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii") + b"\n")

tn.write(b"ls -la\n")
tn.write(b"exit\n")

print(tn.read_all().decode("ascii"))

tn.close()
