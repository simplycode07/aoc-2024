with open("input.txt") as file:
    maze = [line.rstrip() for line in file]

# print(maze)

from heapq import heappop, heappush

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    
    pq = []
    heappush(pq, (0, start[0], start[1], 1))
    
    visited = {}
    
    while pq:
        score, x, y, dir = heappop(pq)
        
        if (x, y) == end:
            return score
        
        if (x, y, dir) in visited and visited[(x, y, dir)] <= score:
            continue

        visited[(x, y, dir)] = score
        
        nx, ny = x + dirs[dir][0], y + dirs[dir][1]
        if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '#':
            heappush(pq, (score + 1, nx, ny, dir))
        
        for turn in [-1, 1]:
            new_dir = (dir + turn) % 4
            nx, ny = x + dirs[new_dir][0], y + dirs[new_dir][1]
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '#':
                heappush(pq, (score + 1001, nx, ny, new_dir))
    
    return -1 

start = None
end = None
for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == 'S':
            start = (i, j)
        elif maze[i][j] == 'E':
            end = (i, j)


print(bfs(maze, start, end))
