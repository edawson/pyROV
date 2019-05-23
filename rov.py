import hashlib
import time
import socket
from unfile import unfile

"""
 A ROV objects defines a unit of computation which is composed of the 5 modular
 components of our compute system:
 - inputs
 - parameters
 - environment
 - execution
 - output

 We also define three other types:
 - a STATUS type that provides handling return codes and other items related to
   determining if a workflow was successful.
 - a FORK type to describe when an input is split into smaller parts and the
   command used to do so.
 - a JOIN type used to describe when multiple inputs are glued together to form
   a single file.
"""

def get_time():
    return time.time()

def get_hostname():
    return socket.gethostname()

def basename(s, ext=""):
    return s.split("/")[-1].strip(ext)

class INPUT:
    def __init__(self):
        self.sig = "I"
        self.id = None
        self.unfile = None
        self.location = None
        self.system = None
        self.digest = None

    def get_digest(self): 
        return self.unfile.digest()

    def digest_to_tag(self):
        return ":".join(["DIGEST", self.digest.algo, self.digest.digest])

    def system_to_tag(self):
        if self.system is not None:
            return ":".join(["SYS", "Z", self.system])
        else:
            raise Exception("System variable was not set for file " + self.location)

    def fill_from_local_file(self, filepath):
        uf = Unfile()
        uf.load_local(filepath)
        self.unfile = uf
        self.location = self.unfile.local_path
        self.system = get_hostname()
        self.digest = self.unfile.get_digest("md5")
        self.id = basename(self.unfile.chop_prefix(self.unfile.unpath))
        self.system = get_hostname()


    def to_rov_line(self):
        l = []
        l.append(self.sig)
        l.append(self.id)
        l.append(self.unfile.unpath)
        l.append(self.digest_to_tag())
        if self.system is not None:
            l.append(system_to_tag())
        s = "\t".join(l)
        return s

class PARAMETER:
    def __init__(self):
        self.sig = "P"
        self.id = None
        self.type = None
        self.value = None
        self.isFile = None
        self.digest = None

    def to_rov_line(self):
        return


class ENVIRONMENT:
    def __init__(self):
        self.sig = "E"
        self.id = None
        self.name = None
        self.image = None
        self.isPublic = None

    def to_rov_line(self):
        return


class EXECUTION:
    def __init__(self):
        self.sig = "X"
        self.id = None
        self.command = None

    def to_rov_line(self):
        return


class OUTPUT:
    def __init__(self):
        self.sig = "O"
        self.id = None
        self.location = None
        self.digest = None

    def to_rov_line(self):
        return


class STATUS:
    def __init__(self):
        self.sig = "S"
        self.id = None
        self.exec = None
        self.rc = None

class FORK:
    def __init__(self):
        self.sig = "F"

class JOIN:
    def __init__(self):
        self.sig = "J"
    

class ROV:
    def __init__(self):
        self.inputs = []
        self.parameters = []
        self.executions = []
        self.environment = None
        self.outputs = []
        self.statuses = []

    def to_string(self):
        
        i_lines = "\n".join(i.to_rov_line() for i in self.inputs)
        p_lines = "\n".join(p.to_rov_line() for p in self.parameters)
        ex_lines = "\n".join(e.to_rov_line() for e in self.parameters)
        env_lines = []
        o_lines = []

        s = "\n".join([i_lines, p_lines, ex_lines, env_lines, o_lines])
        return s

