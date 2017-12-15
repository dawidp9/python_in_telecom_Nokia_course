import paramiko

# host = "example.com"
# transport = paramiko.Transport(host)
# user = "user"
# password = "password"
# transport.connect(user, password)
# client = paramiko.SFTPClient.from_transport(transport)
#
# remotepath = ""
# localpath = ""
#
# client.get(remotepath,localpath)

class SftpHandler:

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.transport = paramiko.Transport(self.host)
        self.transport.connect(self.user, self.password)

    def send(self, localpath, remotepath):
        client = paramiko.SFTPClient.from_transport(self.transport)
        try:
            client.put(remotepath, localpath)
        except IOError:
            print "file doesnt exist"
        finally:
            client.close()

    def recive(self, localpath, remotepath):
        client = paramiko.SFTPClient.from_transport(self.transport)
        client.get(remotepath, localpath)
        client.close()


SftpHandler("example.com", "user1", "password1").send("home/file.txt", "/dir/")