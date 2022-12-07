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

if __name__ == "__main__":
    f = open("test_data.txt").read().splitlines()
    data = []
    for i in f:  
        data.append(i)

    root = Directory("/")
    current_dir = root
    total_size = 0
    for d in data:
        line = d.split(" ")
        if line[0] == "$": #command
            if line[1] == "cd":
                if line[2] == "..":
                    current_dir = current_dir.parent
                    print("changing directory to", current_dir.name)
                else:
                    for dir in current_dir.children:
                        if dir.name == line[2]:
                            current_dir = dir
                            print("changing directory to", current_dir.name)
                            break
        else: #output, means we just executed an ls
            if (current_dir.size == 0):
                if line[0] == "dir": # means we need to add child
                    child = Directory(line[1])
                    child.parent = current_dir
                    current_dir.add_child(child)
                else: # we have a file
                    current_dir.increase_size(int(line[0]))
                    total_size += int(line[0])

    #bfs traversal of directories
    global needs_adjust
    needs_adjust = []
    def dfs(curr):
        global needs_adjust
        if len(curr.children) == 0:
            needs_adjust.append(curr)
            return
        for i in curr.children:
            dfs(i)
    dfs(root)

    q = needs_adjust
    sizes = []
    while(len(q) > 0):
        curr = needs_adjust.pop(0)
        sizes.append(curr.size)
        if curr.parent != "":
            curr.parent.increase_size(curr.size)
            if not curr.parent in q:
                q.append(curr.parent)

    print(sizes)
    print(root.size, total_size)
    space_still_needed = 30000000 - (70000000 - total_size)
    potential = [i for i in sizes if i >= space_still_needed]

    print(min(potential))
    

