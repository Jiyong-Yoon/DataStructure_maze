
#미로를 보기 편하게 수정
def printMaze(stdscr,maze):
    stdscr.clear()
    for row in maze:
        visual_row = " ".join("■" if cell == "1" else "·" if cell == "0" else ' ' if cell == ' ' else "☆" if cell == "2" else cell for cell in row)
        stdscr.addstr(visual_row + "\n")
    stdscr.refresh()


def isValidPos(x, y,maze, MAZE_SIZE):
    if x < 0 or x >= MAZE_SIZE or y < 0 or y >= MAZE_SIZE:
        return False
    if maze[x][y] in ('1', ' '):
        return False
    else:
        return True


def wall(x, y,maze, MAZE_SIZE):
    if x < 0 or x >= MAZE_SIZE or y < 0 or y >= MAZE_SIZE:
        return False
    if maze[x][y] in ('0', ' ','e','x','2','+'):
        return False
    else:
<<<<<<< HEAD
        return True
    
# 파일에서 미로 데이터 읽어오기
def load_maze(filename):
    with open(filename, 'r') as file:
        content = file.read()
        
        # Python 코드 형식으로 된 파일 내용 파싱
        exec_locals = {}
        exec(content, {}, exec_locals)
        
        # m과 MAZE_SIZE 값 추출
        return exec_locals['m'], exec_locals['MAZE_SIZE']
    
# 시작점과 도착점의 좌표를 찾는 함수
def find_points_queue(maze):
    start_pos = None
    end_pos = None
    
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'e':
                start_pos = (i, j, None)
            elif maze[i][j] == 'x':
                end_pos = (i, j, None)
                
            # 시작점과 도착점을 모두 찾았으면 반환
            if start_pos and end_pos:
                return start_pos, end_pos

def find_points_stack(maze):
    start_pos = None
    end_pos = None
    
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'e':
                start_pos = (i, j)
            elif maze[i][j] == 'x':
                end_pos = (i, j)
                
            # 시작점과 도착점을 모두 찾았으면 반환
            if start_pos and end_pos:
                return start_pos, end_pos
=======
        return True
>>>>>>> 63ddf4d3c9e677b35329c5e19e94f850eaa85981
