from datetime import datetime
from help import commanddescription


class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.down = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def insertEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            p = self.head
            while (p.next is not None):
                p = p.next
            p.next = newNode

    def insertDown(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        p = self.head
        while (p.down is not None):
            p = p.down
        p.down = newNode

    def removeAtPos(self, foldername):
        if self.head is None:
            return
        if self.head.next is None:
            self.head == None
        p = self.head
        pp = self.head
        while p.next is not None or p.data is not foldername:
            pp = p
            p = p.next
        pp.next = p.next

    def displayFolders(self):
        p = self.head
        while p is not None:
            print(p.data, end="  ")
            p = p.next
        print()

    def displayFiles(self, p):
        p = p.down
        while p is not None:
            print(p.data, end="  ")
            p = p.down
        print()

    def searchFolder(self, s):
        ptr = self.head
        while ptr.next is not None:
            if ptr.data == s:
                return ptr
            ptr = ptr.next
        return ptr


    def CdSearch(self, s):
        ptr = self.head
        global path
        while (ptr.next != None and ptr.data != s):
            ptr = ptr.next
        path = f"root/{ptr.data}> "


def linearSearch(p, f):
    for i in f:
        if i == p:
            return True
    return False



commands = ["exit", "mkdir", "ls", "rmdir", "date", "echo", "mk", "rm", "find", "findfile", "dispfolders", "cd", "pwd", "--help"]
folders = []
files = []
folder = Linkedlist()

print()
print("Welcome to the \033[94mNIE Terminal v1.0.0\033[0m")
print("For instructions on how to use, enter --help")
print()

path = "root> "

while True:

    x = input(path)

    if x.split(" ")[0] not in commands:
        print("ERROR: INVALID COMMAND")
    else:
        if x == "exit":
            print("for source code, visit \033[92mhttps://github.com/sonikaratok/unix-terminal-simulator\033[0m")
            print("ciao")
            break

        if x == "--help":
            print("Try the following commands to use the terminal")
            for k, v in commanddescription.items():
                print(f"{k} --> {v}")
            print()
            print("For any queries, mail to \033[91m2021ec_sonikar_b@nie.ac.in\033[0m")
            print()

        if x.split(' ')[0] == "mkdir" and len(x.split(' ')) == 2:
            folders.append(x.split(' ')[1])
            folder.insertEnd(x.split(' ')[1])
        elif x.split(' ')[0] == "mkdir" and len(x.split(' ')) != 2:
            if len(x.split(' ')) == 1:
                print("ERROR: MISSING ARGUMENT(S) FOR mkdir")
            else:
                print("ERROR: TOO MANY ARGUMENT(S) FOR mkdir")

        if x == "ls":
            print("Folders:")
            for i in folders:
                print(i, end="  ")
            print()
            print("Files:")
            for i in files:
                print(i, end="  ")
            print()

        if x.split(' ')[0] == "rmdir":
            if x.split(' ')[1] in folders:
                folders.remove(x.split(' ')[1])
            else:
                print("ERROR: FOLDER DOESN'T EXIST")
            folder.removeAtPos(x.split(' ')[1])

        if x == "date":
            print(datetime.now())

        if x.split(" ")[0] == "echo" and len(x.split(' ')) == 2:
            print(x.split(" ")[1])
        elif x.split(' ')[0] == "echo" and len(x.split(' ')) != 2:
            if len(x.split(' ')) == 1:
                print("ERROR: MISSING ARGUMENT(S) FOR echo")
            else:
                print("ERROR: TOO MANY ARGUMENT(S) FOR echo")









        if x.split(' ')[0] == "mk" and len(x.split(' ')) == 2:
            if x.split(' ')[1] not in files:
                files.append(x.split(' ')[1])
                pathtofolder = path.split("/")[-1][:-2]
                if pathtofolder != "root":
                    xyz = folder.searchFolder(pathtofolder)
                    downnode = Node(x.split(' ')[1])
                    if xyz.down == None:
                        xyz.down = downnode
                    else:
                        downnode.down = xyz.down
                        xyz.down = downnode

                    folder.displayFiles(xyz)
            else:
                print("ERROR: FILE ALREADY EXISTS")


        elif x.split(' ')[0] == "mk" and len(x.split(' ')) != 2:
            if len(x.split(' ')) == 1:
                print("ERROR: MISSING ARGUMENT(S) FOR mk")
            else:
                print("ERROR: TOO MANY ARGUMENT(S) FOR mk")











        if x.split(' ')[0] == "rm" and len(x.split(' ')) == 2:
            if x.split(' ')[1] in files:
                files.remove(x.split(' ')[1])
            else:
                print("ERROR: FILE DOESN'T EXIST")











        if x.split(' ')[0] == "find" and len(x.split(' ')) == 2:
            if linearSearch(x.split(' ')[1], folders):
                print(f"{x.split(' ')[1]} exists")
            else:
                print(f"{x.split(' ')[1]} doesn't exist")

        elif x.split(' ')[0] == "find" and len(x.split(' ')) != 2:
            if len(x.split(' ')) == 1:
                print("ERROR: MISSING ARGUMENT(S) FOR find")
            else:
                print("ERROR: TOO MANY ARGUMENT(S) FOR find")

        if x.split(' ')[0] == "findfile" and len(x.split(' ')) == 2:
            if linearSearch(x.split(' ')[1], files):
                print(f"{x.split(' ')[1]} exists")
            else:
                print(f"{x.split(' ')[1]} doesn't exist")

        elif x.split(' ')[0] == "findfile" and len(x.split(' ')) != 2:
            if len(x.split(' ')) == 1:
                print("ERROR: MISSING ARGUMENT(S) FOR findfile")
            else:
                print("ERROR: TOO MANY ARGUMENT(S) FOR findfile")

        if x == "dispfolders":
            folder.displayFolders()

        if x.split(' ')[0] == "cd" and len(x.split(' ')) == 2:
            if x.split(' ')[1] == ".." and len(path.split('/')) > 1:
                path = "root> "
            elif x.split(' ')[1] == ".." and len(path.split('/')) == 1:
                print("YOU ARE ALREADY IN THE root DIRECTORY")
            else:
                if x.split(' ')[1] not in folders:
                    print("ERROR: NO SUCH DIRECTORY")
                    continue
                folder.CdSearch(x.split(' ')[1])

        elif x.split(' ')[0] == "cd" and len(x.split(' ')) != 2:
            if len(x.split(' ')) == 1:
                print("ERROR: MISSING ARGUMENT(S) FOR cd")
            else:
                print("ERROR: TOO MANY ARGUMENT(S) FOR cd")

        if x.split(' ')[0] == "pwd" and len(x.split(' ')) == 1:
            print(path[:-2])
