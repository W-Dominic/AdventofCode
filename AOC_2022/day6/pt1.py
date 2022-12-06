if __name__ == "__main__":
    f = open("input.txt").read().splitlines()
    data = []
    for i in f:  
        data.append(i)

    buff = data[0]

    view = []
    visited = {} #letter : freq
    count = 0
    for c in buff:
        if c in visited:
            visited[c] += 1
        else:
            visited[c] = 1
        view.append(c)
        if len(view) == 5:
            visited[view[0]] -= 1
            if visited[view[0]] == 0: # remove entry
                visited.pop(view[0])
            view.pop(0)
        print(view)
        count += 1

        if len(visited) == 4:
            print(count)
            break
        
        

