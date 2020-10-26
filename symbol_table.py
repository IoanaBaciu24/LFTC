
GLOBAL_ID = 0
BOOLEANS = [True, False]
class Node:
    def __init__(self, val, id: int):
        self.value = val
        self.id = id
        self.left = None
        self.right = None

    def __str__(self):
        return "node: " + str(self.value) + ", id: " + str(self.id)
        

class SymbolTable:
    def __init__(self, kind: str):
        self.root = None 
        self.kind = kind

    def add_value(self, value) -> Node:
        global GLOBAL_ID
        if self.root == None:
            self.root = Node(value, GLOBAL_ID)
            GLOBAL_ID+=1
            return self.root
        else:
            prev = None
            l,r = False, False
            current = self.root
            while current!=None:
                if current.value == value:
                    return current
                elif current.value > value:
                    l,r = True, False
                    prev = current
                    current = current.left
                else:
                    l,r = False, True
                    prev = current
                    current = current.right
            if l:
                prev.left = Node(value, GLOBAL_ID)
                GLOBAL_ID+=1
                return prev.left
            if r:
                prev.right = Node(value, GLOBAL_ID)
                GLOBAL_ID+=1
                return prev.right


    def search_for_value(self, value: str):
        
        current = self.root
        while current!=None:
            if current.value == value:
                return current.id 
            elif current.value> value:
                current = current.left
            else:
                current = current.right
        
        return -1

    def __preorder_get_string(self, node: Node):
        string = ""
        if node!=None:
            string += str(node) + ': ' 
            string+= 'left: ' + str(node.left) + ' '
            string+= 'right: ' + str(node.right) + ' '
            string+='\n'
            string+= self.__preorder_get_string(node.left)
            string+= self.__preorder_get_string(node.right)
        return string

    def __str__(self):
        return self.__preorder_get_string(self.root)



tbl = SymbolTable("identifiers")

tbl.add_value("c")
tbl.add_value("a")
tbl.add_value("b")
tbl.add_value("e")
tbl.add_value("d")

print(tbl.search_for_value("a"))
print(tbl.search_for_value("e"))
print(tbl.search_for_value("c"))
print(tbl.search_for_value("s"))

print(tbl)




