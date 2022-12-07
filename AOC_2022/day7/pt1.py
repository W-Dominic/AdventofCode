class Directory:
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.children = []
        self.parent = ""
    def increase_size(self, sz):
        self.size += sz
    def add_child(self, dir):
        self.children.append(dir)
    def set_parent(self, dir):
        self.parent = dir

def adjust_size(node): # given a node, recurse through parents updating their size
    if(node.parent != ""):
        node.parent.increase_size(node.size)
        adjust_size(node.parent)
    return

if __name__ == "__main__":
    f = open("input.txt").read().splitlines()
    data = []
    for i in f:  
        data.append(i)

    root = Directory("/")
    current_dir = root
    for d in data:
        line = d.split(" ")
        if line[0] == "$": #command
            if line[1] == "cd":
                if line[2] == "..":
                    current_dir = current_dir.parent
                else:
                    for dir in current_dir.children:
                        if dir.name == line[2]:
                            current_dir = dir
                            break
        else: #output, means we just executed an ls
            if line[0] == "dir": # means we need to add child
                child = Directory(line[1])
                child.parent = current_dir
                current_dir.add_child(child)
            else: # we have a file
                current_dir.increase_size(int(line[0]))

    #bfs traversal of directories
    global total
    total = 0
    def dfs(root, should_print):
        global total
        if len(root.children) == 0:
            if not should_print: adjust_size(root)
            return
        for i in root.children:
            if should_print: 
                if i.size < 100000:
                    total += i.size
                #print(i.name, i.size, i.parent.name)
            dfs(i, should_print)
    dfs(root, False)
    dfs(root, True)
    print(total)
            