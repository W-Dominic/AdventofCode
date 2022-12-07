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

def adjust_size(node, size):
    if node.parent == "":
        return
    node.parent.size += size
    adjust_size(node.parent, size)

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
            else: # we have a file, increase current_dir size and adjust its parents size
                current_dir.increase_size(int(line[0]))
                adjust_size(current_dir, int(line[0]))

    #bfs traversal of directories
    global sizes
    sizes = []
    def dfs(node):
        if len(node.children) == 0:
            return
        for i in node.children:
            sizes.append(i.size)
            dfs(i)
    
    dfs(root)
    space_still_needed = 30000000 - (70000000 - root.size)
    potential = [i for i in sizes if i >= space_still_needed]
    print(min(potential))

    

