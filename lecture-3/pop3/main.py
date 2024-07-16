import poplib

server = "192.168.122.3"
user = "mild-honey"
passwd = "Honey155@Mild-R"

server = poplib.POP3(server)
server.user(user)
server.pass_(passwd)

msgNum = len(server.list()[1])

for i in range(msgNum):
    for msg in server.retr(i + 1)[1]:
        print(msg.decode())
