import paramiko

hostname = "192.168.122.3"
port = 22
user = "mild-honey"
passwd = "Honey155@Mild-R"

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port=port, username=user, password=passwd)

    while True:
        try:
            cmd = input("Command: ")
            stdin, stdout, stderr = client.exec_command(cmd)
            print(stdout.read().decode())
        except KeyboardInterrupt:
            break

    client.close()
except Exception as e:
    print(e)
