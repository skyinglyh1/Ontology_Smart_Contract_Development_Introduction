OntCversion = '2.0.0'
"""
Contract Record
"""
from ontology.interop.System.Storage import GetContext, Get, Put
from ontology.interop.System.Runtime import CheckWitness, Notify
from ontology.interop.Ontology.Runtime import Base58ToAddress

# set the owner address to your base58 address (starting with a captical A)
Owner = Base58ToAddress('AQf4Mzu1YJrhz9f3aRkkwSm9n3qhXGSh4p')

def Main(operation, args):
    if operation == "putRecord":
        assert (len(args) == 2)
        key = args[0]
        value = args[1]
        return putRecord(key, value)
    if operation == "getRecord":
        assert (len(args) == 1)
        key = args[0]
        return getRecord(key)
    return False


def putRecord(key, value):
    assert (_isOwner())
    Put(GetContext(), key, value)
    Notify(["putRecord", key, value])
    return True

def getRecord(key):
    return Get(GetContext(), key)

def _isOwner():
    return CheckWitness(Owner)