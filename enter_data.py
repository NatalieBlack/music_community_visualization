import json
from operator import itemgetter

def get_node_by_name(name):
    return DATA['nodes'].index({"name":name,"group":1})

def get_link_node(prompt):
    node_name = raw_input(prompt + ":")
    return get_node_by_name(node_name)

def enter_node():
    name = raw_input("name:")

    if {"name":name,"group":1} in DATA['nodes']:
        print "Node already exists"
    else:
        DATA['nodes'].append({"name":name, "group":1})

def del_node(data, name1):
    nodes = data['nodes']
    for n in xrange(len(nodes)):
        if(nodes[n]["name"] == name1):
            del nodes[n]
            data['nodes'] = nodes
            return data

    print "That node is not in the list"
    return data

def del_link(data, name1, name2):
    name1_index = get_node_by_name(name1)
    name2_index = get_node_by_name(name2)

    links = data['links']
    for i in xrange(len(links)):
        if(((links[i]['target'] == name1_index) and (links[i]['source'] == name2_index)) or 
           ((links[i]['target'] == name2_index) and (links[i]['source'] == name1_index))):
            del links[i]
            data['links'] = links
            return data

    print "That link is not in the list"
    return data

def finish(f, data):
    f.seek(0)
    f.write(json.dumps(data))
    f.truncate()
    f.close()


FILECONTENT = open('data.json', 'r+')
DATA = json.load(FILECONTENT)

option = None 

while option not in ("n", "l", "g", "d", "b", "x"):

    option = raw_input("""Options:
    n - enter new node
    l - enter new link
    g - enter set of links with common source
    d - delete node
    b - break link
    x - exit
    """)

    if option == "n":
        enter_node()
        option = None #reset

    elif option == "g":
        try:
            src = get_link_node("source")
        except ValueError:
            print "Source name does not match any nodes"
            option = None #reset
            continue

        tar_name = None
        print "Press enter when finished with group"
        while tar_name != "":
            try:
                tar_name = raw_input("target:")
                tar = DATA['nodes'].index({"name":tar_name,"group":1})
            except ValueError:
                print "Target name does not match any nodes"
                continue

            val = raw_input("value:")
            link = {"source":src, "target":tar, "value":val}

            if link in DATA['links']:
                print "link already exists"
            else:
                DATA['links'].append(link)

                option = None #reset

    elif option == "l":

        try:
            src = get_link_node("source")
        except ValueError:
            print "Source name does not match any nodes"
            option = None #reset
            continue

        try:
            tar = get_link_node("target")
        except ValueError:
            print "Target name does not match any nodes"
            option = None #reset
            continue

        val = raw_input("value:")
        link = {"source":src, "target":tar, "value":val}

        if link in DATA['links']:
            print "link already exists"
        else:
            DATA['links'].append(link)

        option = None #reset

    elif option == "d":
        #n = raw_input("Enter the name of the node you want to remove: ")
        #DATA = del_node(DATA, n)
        print "This option is broken"
        option = None #reset
    elif option == "b":
        n1 = raw_input("Enter the name of the source of the link you want to remove: ")
        n2 = raw_input("Enter the name of the target of the link you want to remove: ")
        DATA = del_link(DATA, n1, n2)
        option = None #reset
    elif option == "x":
        finish(FILECONTENT, DATA)
