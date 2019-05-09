import hashlib
import time
from filehandler import unfile

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

    def to_rov_line(self):
        s = "\t".join([self.sig, self.id, self.unfile, self.get_digest()])
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

