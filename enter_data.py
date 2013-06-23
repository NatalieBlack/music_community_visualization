import json

def get_src():
    src_name = raw_input("source:")
    return DATA['nodes'].index({"name":src_name,"group":1})

def get_tar():
    tar_name = raw_input("target:")
    return DATA['nodes'].index({"name":tar_name,"group":1})

def enter_node():
    name = raw_input("name:")
    DATA['nodes'].append({"name":name, "group":1})

def finish():
    FILECONTENT.seek(0)
    FILECONTENT.write(json.dumps(DATA))
    FILECONTENT.truncate()
    FILECONTENT.close()


FILECONTENT = open('data.json', 'r+')
DATA = json.load(FILECONTENT)

option = None 

while option not in ("n", "l", "g", "x"):

    option = raw_input("""Options:
    n - enter new node
    l - enter new link
    g - enter set of links with common source
    x - exit
    """)

    if option == "n":
        enter_node()
        option = None #reset

    elif option == "g":
        try:
            src = get_src()
        except ValueError:
            print "Source name does not match any nodes"
            option = None #reset
            continue

        tar_name = None
        print "Press enter when finished with group"
        while tar_name != None:
            try:
                tar = get_tar()
            except ValueError:
                print "Target name does not match any nodes"
                option = None #reset

            val = raw_input("value:")
            DATA['links'].append({"source":src, "target":tar, "value":val})

        option = None #reset

    elif option == "l":

        try:
            src = get_src()
        except ValueError:
            print "Source name does not match any nodes"
            option = None #reset
            continue

        try:
            tar = get_tar()
        except ValueError:
            print "Source name does not match any nodes"
            option = None #reset
            continue

        val = raw_input("value:")
        DATA['links'].append({"source":src, "target":tar, "value":val})

        option = None #reset

    elif option == "x":
        finish()