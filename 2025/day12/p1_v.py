import copy
from functools import cache
import os
import time

# --- CONFIGURATION ---
# Adjust this value (in seconds) to speed up or slow down the visualization.
# 0.05 is a good starting point. Use 0.0 for max speed.
VISUALIZATION_DELAY = 0.01
# --- END CONFIGURATION ---


# --- COLOR SETUP (ANSI ESCAPE CODES) ---
# Note: These colors may not work perfectly in all terminals (e.g., PowerShell without proper setup).
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    # Background colors for the grid cells
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    
    # 256-color codes for more options
    BG_ORANGE = '\033[48;5;208m' 
    BG_PURPLE = '\033[48;5;129m' 
    BG_GRAY = '\033[48;5;250m' 
    BG_BRIGHT_YELLOW = '\033[48;5;226m' 
    
    # Empty space is black
    BG_BLACK = '\033[40m' 

# Map shape index (0-9) to a background color
COLOR_MAP = {
    '0': Colors.BG_RED,
    '1': Colors.BG_GREEN,
    '2': Colors.BG_YELLOW,
    '3': Colors.BG_BLUE,
    '4': Colors.BG_MAGENTA,
    '5': Colors.BG_CYAN,
    '6': Colors.BG_ORANGE,
    '7': Colors.BG_PURPLE,
    '8': Colors.BG_GRAY,
    '9': Colors.BG_BRIGHT_YELLOW,
    '.': Colors.BG_BLACK
}

GRID_SEP = '|'
# --- END COLOR SETUP ---


# --- CURSOR CONTROL FUNCTIONS ---
def clear_screen():
    """Clears the terminal screen."""
    # Use 'cls' for Windows, 'clear' for Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')

def move_cursor_to_top():
    """Moves the terminal cursor to the top-left corner (row 1, column 1)."""
    # ANSI code for cursor positioning
    print('\033[1;1H', end='', flush=True)
# --- END CURSOR CONTROL FUNCTIONS ---


# --- FILE LOADING & SHAPE PROCESSING (Original Code) ---

lines = []

with open("test.txt") as file:
    lines=[]
    for l in file:
        lines.append(l.rstrip())
 
def spin(shape):
    new = []
    for i in range(3):
        new_l = ''
        for j in range(2,-1,-1):
            new_l+=shape[j][i]
        new.append(new_l)
    return new

def mirror(shape):
    new = []
    for i in range(2,-1,-1):
        new_l = ''
        for j in range(2,-1,-1):
            new_l+=shape[j][i]
        new.append(new_l)
    return new

def check_shapes_equal(s1,s2):
    for i in range(3):
        for j in range(3):
            if s1[i][j] != s2[i][j]:
                return False
    return True

shapes=[]
idx = 0

for i in range(1,27,5):
    curr_shapes = []
    curr_shape = []
    for l in lines[i:i+3]:
        curr_shape.append(l.replace('#',str(idx)))

    curr_shapes.append(curr_shape)
    for _ in range(3):
        next_ = spin(curr_shape)
        next_flipped = mirror(next_)
        
        # Check if the spun shape is new
        is_new = True
        for s in curr_shapes:
            if check_shapes_equal(next_,s):
                is_new = False
                break
        if is_new:
            curr_shapes.append(next_)
        
        curr_shape=next_
    

    idx+=1
    shapes.append(curr_shapes)

print("--- Loaded Shapes ---")
for s_list in shapes:
    print('-'*30)
    for s in s_list:
        for l in s:
            print(l)

print('-'*30)
print("--- Loaded Regions ---")

regions = []

for l in lines[30:]:
    
    area, quantities_str = l.split(':')
    width, height = area.split('x')
    
    quantities = []
    # Assuming quantities are space separated after a single space following ':'
    for q in quantities_str.strip().split(' '): 
        if q:
            quantities.append(int(q))

    region = (int(width), int(height), quantities)
    regions.append(region)
    print(region)

print('-'*30)

row_range = None
col_range = None


# --- HELPER FUNCTIONS (Original Code) ---

def get_starting_region(width, height):
    region = []
    for _ in range(height):
        line = []
        for _ in range(width):
            line.append('.')
        region.append(line)
    return region

def can_place_shape(curr_region, shape, row, col):
    for shape_c, c in enumerate(range(col,col+3)):
        for shape_r, r in enumerate(range(row,row+3)):
            # Check bounds
            if r not in row_range or c not in col_range:
                return False
            # Check collision: if target cell is not '.' AND shape cell is not '.', it's a collision
            if curr_region[r][c] !='.' and shape[shape_r][shape_c] != '.':
                return False
    return True

def place_shape(curr_region, shape, row, col):
    # NOTE: The calling function (dfs) must ensure can_place_shape is True
    # before calling this, but we'll re-check defensively.
    if can_place_shape(curr_region, shape, row, col):
        for shape_c, c in enumerate(range(col,col+3)):
            for shape_r, r in enumerate(range(row,row+3)):
                if shape[shape_r][shape_c] != '.':
                    curr_region[r][c] = shape[shape_r][shape_c]
        return True
    return False


# --- MODIFIED print_matrix FUNCTION ---

def print_matrix(m, delay=VISUALIZATION_DELAY):
    """Prints the matrix using ANSI colors, without surrounding borders."""
    
    for row in m:
        line_str = GRID_SEP
        for cell in row:
            # Get the color code, default to black background if number > 9 or unknown char
            color = COLOR_MAP.get(cell, Colors.BG_BLACK)
            
            # Print the colored cell: [COLOR] [BOLD] [CELL_VALUE] [RESET_COLOR]
            # Use space padding to make cells look square
            line_str += f"{color}{Colors.BOLD} {cell} {Colors.RESET}{GRID_SEP}"
        
        print(line_str)
    
    # Add a short delay to make the changes visible
    time.sleep(delay)


# --- MODIFIED dfs FUNCTION FOR VISUALIZATION ---

def dfs(curr_region, quantities, start_time=None):
    """
    Depth-First Search to find a solution, with live visualization.
    """
    # Initialize start_time on the first call
    if start_time is None:
        start_time = time.time()
        clear_screen() # Clear the screen once at the start

    # --- VISUALIZATION BLOCK ---
    move_cursor_to_top()
    print("--- 🧩 Tiling Solver ---")
    print(f"Time Elapsed: {time.time() - start_time:.2f}s | Current Quants: {quantities}")
    print('=' * (len(curr_region[0]) * 4 + 1)) # Top border
    print_matrix(curr_region) # Draws the matrix
    print('=' * (len(curr_region[0]) * 4 + 1)) # Bottom border
    # --- END VISUALIZATION BLOCK ---

    # Base Case: Check if all quantities are zero
    res = False
    for q in quantities:
        if q > 0:
            break
    else:
        # Solution found! Hold the final solution on screen.
        print("\n*** SOLUTION FOUND! ***")
        time.sleep(5) 
        return True

    # Recursive Step: Try placing shapes
    for i, q in enumerate(quantities):
        if q > 0:
            # Iterate through all possible starting positions
            for r in row_range:
                for c in col_range:
                    # Iterate through all rotations/flips of the shape 'i'
                    for shape in shapes[i]:
                        if can_place_shape(curr_region, shape, r, c):
                            # Create new state for the next recursion
                            next_region = copy.deepcopy(curr_region)
                            
                            if place_shape(next_region, shape, r, c):
                                next_quantities = quantities.copy()
                                next_quantities[i] -= 1
                                
                                # Recursive call, passing the start_time
                                res = dfs(next_region, next_quantities, start_time)
                                
                                if res:
                                    return True
    
    # If the function returns False (backtracks), the visualization will show the state
    # right before it was abandoned, then update to the parent state on return.
    return res

# --- MAIN EXECUTION LOOP ---

output = 0

print("Starting Tiling Solver...")

for r in regions:
    width, height, quants = r
    print(f"\nProcessing Region {width}x{height} with Quants: {quants}")
    
    # Set the global range variables for the current region
    row_range = range(height)
    col_range = range(width)

    # Get the initial empty grid
    curr = get_starting_region(width,height)

    # Start the DFS solver with visualization
    if dfs(curr, quants):
        output+=1
        
    print(f"\n--- Region Processed ---")
    print(f"Region {width}x{height} Solved: {'Yes' if output > 0 else 'No'}")
    print(f"Total Regions Solved: {output}")
    print('-'*50)

print(f"\nFinal Total Regions Solved: {output}")