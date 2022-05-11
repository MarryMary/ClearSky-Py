import sys
from Exposure.index import index
from Core.Elena.Tools.VTools import array_key_exists

if(sys.argv[1]):
    command = sys.argv[1].split(':')
    if(len(command) == 2):
        if(command[0].lower() == "system"):
            if(command[1].lower() == "start"):
                port = 8000
                if(array_key_exists(2, sys.argv) and sys.argv[2].isdigit):
                    port = int(sys.argv[2])
                index.SystemStartTrigger(port)
        elif(command[0].lower() == "controller"):
            if(command[1].lower() == "create"):
                if(sys.argv[2]):
                    pass
                else:
                    print("Err! controller name undefined.")