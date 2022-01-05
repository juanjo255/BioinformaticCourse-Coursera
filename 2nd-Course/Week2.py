# function to solve Eulerian cycle path on direct graph

def parseList ():
    file = open ("file2.txt")
    ware = dict()
    
    for i in file.readlines():
        i = i.split("->")
        if len (i[1].strip()) > 1:
            nums = i[1].strip()
            for j in nums.split(","):
                if not (i[0] in ware):
                    ware [i[0]] = j
                else:
                    ware [i[0]] = ware [i[0]] + "," + j
        else:
            ware [i[0]] = i[1].strip()
    print (ware)
    # [(2,6)(2,1)]
    return

parseList()








