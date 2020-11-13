#!/usr/bin/python3


import banner
import sys, getopt
import json


def evaluate(build_number, kbList):
    try:
        db = json.loads("db.json")
        print(db.dumps(db))
    except json.decoder.JSONDecodeError as error:
        print(error)


def main():
    SUPPORTED_VERSIONS = { 10240, "1507", 
                        10586, "1511",
                        14393, "1607",
                        15063, "1703",
                        16299, "1709",
                        17134, "1803",
                        17763, "1809",
                        18362, "1903",
                        18363, "1909",
                        19041, "2004"}
    try:
        opts, ___ = getopt.getopt(sys.argv[1:],"hb:k:w:",["help","build-number=","kb=","windows-version="])
    except getopt.GetoptError:
      #usage()
      sys.exit(1)
    
    buildNumber = None
    windowsVersion = None
    kbList = []
    print (opts)
    for o, a in opts:
        if o in ("-b", "--build-number"):
            if a.isnumeric():
                if int(a) not in SUPPORTED_VERSIONS:
                    print ("Unsupported build number")
                else:
                    print(" [!] Windows version not supported")
                    print(a)
                    buildNumber = int(a)
        elif o in ("-h", "--help"):
            #usage()
            sys.exit(1)
        elif o in ("-w", "--windows-version"):
            windowsVersion = a

        elif o in ("-k", "--kb"):
            for kb in a.split(','):
                kbList.append(int(kb))
            print(kbList)
        else:
            assert False, "unhandled option"

    if (buildNumber == None and windowsVersion == None):
        print(" [!] You need to provide at least either the Windows Version or the Build Number")
        #usage()
        sys.exit(1)

    #banner.printLogo()
    evaluate(buildNumber, kbList)

main()