def create_maze():
    return [
        ['P', '.', '.', '#', '#'],
        ['#', '#', '.', '#', '#'],
        ['#', '.', '.', '.', '#'],
        ['#', '.', '#', '#', '#'],
        ['#', '.', '.', '.', 'E']
    ]

def print_maze(maze):
    print()
    for row in maze:
        print(" ".join(row))
    print()

def play_game():
    maze = create_maze()
    p_row, p_col = 0, 0
    moves = 0

    print("\n--- MAZE ESCAPE GAME ---")
    print("Controls: W (Up), A (Left), S (Down), D (Right) | Q (Quit to Menu)")
    print_maze(maze)

    while True:
        move = input("Enter move (W/A/S/D): ").strip().upper()

        if move == 'Q':
            break

        # 1. Calculate next position
        if move == 'W':
            new_row, new_col = p_row - 1, p_col
        elif move == 'S':
            new_row, new_col = p_row + 1, p_col
        elif move == 'A':
            new_row, new_col = p_row, p_col - 1
        elif move == 'D':
            new_row, new_col = p_row, p_col + 1
        else:
            print(f"Invalid key '{move}'. Use W, A, S or D only.")
            print(f"Moves counted: {moves}")
            continue

        # 2. Check Boundary
        if new_row < 0 or new_row >= 5 or new_col < 0 or new_col >= 5:
            print(f"Cannot move outside the maze. Player stays at ({p_row}, {p_col}) | Moves: {moves}")
            continue

        # 3. Check Wall
        if maze[new_row][new_col] == '#':
            print(f"Wall ahead. Move blocked. Player stays at ({p_row}, {p_col}) | Moves: {moves}")
            continue

        # 4. Valid Move
        moves += 1
        reached_exit = (maze[new_row][new_col] == 'E')

        maze[p_row][p_col] = '.'
        maze[new_row][new_col] = 'P'
        p_row, p_col = new_row, new_col

        print_maze(maze)

        if reached_exit:
            print(f"You escaped the maze! Total moves: {moves}")
            break
        else:
            print(f"Player moved to (row {p_row}, col {p_col}) | Moves: {moves}")

def find_shortest_path():
    maze = create_maze()
    queue = [(0, 0, 0)]  # (row, col, steps)
    visited = [(0, 0)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while len(queue) > 0:
        r, c, steps = queue.pop(0)

        if maze[r][c] == 'E':
            print(f"\nShortest path length: {steps} steps")
            return

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 5 and 0 <= nc < 5:
                if maze[nr][nc] != '#' and (nr, nc) not in visited:
                    visited.append((nr, nc))
                    queue.append((nr, nc, steps + 1))

# Main Menu
while True:
    print("\n=== MAIN MENU ===")
    print("1. Play Maze Escape Game")
    print("2. Find Shortest Path (BFS)")
    print("3. Exit")
    choice = input("Choose an option (1/2/3): ").strip()

    if choice == '1':
        play_game()
    elif choice == '2':
        find_shortest_path()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")