import re

def isValidOAB(numberOAB):
    return bool(re.fullmatch(r"\d+\.\d+", numberOAB))

def isValidJsonStructure(jsonData, requiredKeys):
    if not isinstance(jsonData, list):
        return False
    for entry in jsonData:
        if not all(key in entry for key in requiredKeys):
            return False
    return True
