def update_tail(H, T):
    # DETERMINE IF TAIL SHOULD MOVE, THEN RETURN NEW TAIL POSITION
    dif_r = H[0] - T[0]
    dif_c = H[1] - T[1]
    new_tail = T
    if dif_r > 1:
        new_tail = (H[0]-1, H[1])
    elif dif_r < -1: 
        new_tail = (H[0]+1, H[1])
    elif dif_c > 1: 
        new_tail = (H[0], H[1]-1)
    elif dif_c < -1: 
        new_tail = (H[0], H[1]+1)
    return new_tail
    

if __name__ == "__main__":
    f = open("input.txt").read().splitlines()
    data = []
    for i in f:  
        data.append(i)

    commands = []

    for i in data:
        commands.append(i.split(" "))
    print(commands)

    matrix = []
    H = (0,0)
    T = (0,0)
    visited = set()
    visited.add((0,0))
    for c in commands:
        print(H, T, len(visited))
        direction = c[0]
        val = c[1]
        if direction == 'R':
            for i in range(int(val)):
                H = (H[0], H[1]+1)
                T = update_tail(H,T)
                if not T in visited:
                    visited.add(T)
        elif direction == 'L':
            for i in range(int(val)):
                H = (H[0], H[1]-1)
                T = update_tail(H,T)
                if not T in visited:
                    visited.add(T)
        elif direction == 'U':
            for i in range(int(val)):
                H = (H[0]+1, H[1])
                T = update_tail(H,T)
                if not T in visited:
                    visited.add(T)
        elif direction == 'D':
             for i in range(int(val)):
                 H = (H[0]-1, H[1])
                 T = update_tail(H,T)
                 if not T in visited:
                    visited.add(T)
    print(len(visited))


        
