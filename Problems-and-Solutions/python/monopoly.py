import sys
import json 

def Monopoly():
    with open(sys.argv[1]) as json_data:
        d = json.load(json_data)
        print d


if __name__ == "__main__":
    Monopoly()
