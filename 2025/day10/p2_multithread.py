import sys
import multiprocessing
from concurrent.futures import ProcessPoolExecutor, as_completed

# Increase recursion limit for the potentially deep BFS calls, 
# especially important when using multiprocessing.
sys.setrecursionlimit(2000) 

# --- Data Loading (Kept the same) ---
input_ = []

with open("test.txt") as file:
    for line in file:
        l = line.strip().split(' ')
        joltages_str = l[-1][1:-1]
        buttons_list = []
        joltages = []
        # Ensure only non-empty strings are converted to int
        for j in joltages_str.split(','):
            if j:
                joltages.append(int(j))

        for buttons in l[1:-1]:
            curr = []
            # Ensure only non-empty strings are converted to int
            for b in buttons[1:-1].split(','):
                if b:
                    curr.append(int(b))
            buttons_list.append(curr)

        # Store goal_state as a tuple for immutability when used in sets/memos later
        input_.append( (tuple(joltages), buttons_list ))


# --- Core Logic Functions (Kept the same) ---

def increase_joltage(curr_joltage, button, goal_state):
    next_ = list(curr_joltage)
    for idx in button:
        next_[idx]+=1
    return tuple(next_)


def bfs(states, curr_count, buttons, goal_state, memo):

    next_states = set()
    for curr_state in states:
        
        for b in buttons:
            # goal_state is not used in increase_joltage, keeping the original signature
            next_state = increase_joltage(curr_state, b, goal_state) 

            if next_state == goal_state:
                return curr_count
            else:
                for i in range(len(next_state)):
                    if next_state[i] > goal_state[i]:
                        break
                else:
                    if next_state not in memo:
                        next_states.add( next_state )
                        memo.add(next_state)

    curr_count+=1

    if len(next_states) > 0:
        return bfs(next_states, curr_count, buttons, goal_state, memo)
    # Return None if no more states to check and goal not reached
    return None 

# --- Parallel Processing Setup ---

# This function encapsulates the original loop body for a single input line (l)
def process_single_line(l):
    """Calculates the minimum button presses for a single input line."""
    goal_state , buttons = l
    
    # Starting state is a tuple of zeros
    starting = tuple([0]*len(goal_state))
    
    # Initialize BFS data structures
    start = set()
    start.add(starting)
    memo = set()
    memo.add(starting)
    
    # Run the BFS
    min_presses = bfs( start, 1, buttons, goal_state, memo)
    
    # Return the result (or 0 if min_presses is None/unreachable)
    return min_presses if min_presses is not None else 0

# --- Main Execution Block using ProcessPoolExecutor ---

if __name__ == '__main__':
    
    # Determine the number of processes to use (e.g., the number of CPU cores)
    # Using 'multiprocessing.cpu_count()' is generally a good default for CPU-bound tasks
    max_workers = multiprocessing.cpu_count() 
    
    print(f"Starting parallel execution of {len(input_)} tasks using up to {max_workers} processes...")
    
    total_result = 0
    results_count = 0
    
    # Use ProcessPoolExecutor to manage the worker processes
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        
        # Submit all tasks (each line of input_) to the executor
        # We use map to submit the input list to the process_single_line function
        # executor.map returns results in the order the tasks were submitted
        
        # Use submit/as_completed for progress tracking
        futures = {executor.submit(process_single_line, line): i for i, line in enumerate(input_)}

        for future in as_completed(futures):
            line_index = futures[future]
            try:
                result = future.result()
                if result is not None:
                    total_result += result
                    
                results_count += 1
                
                # Print progress update
                progress = f"[{results_count}/{len(input_)}]"
                print(f"\r{progress} Processed line {line_index + 1}. Current Total: {total_result}", end='', flush=True)

            except Exception as e:
                print(f"\nError processing line {line_index + 1}: {e}")
                
    
    print('\n' + '-'*100)
    print("RESULT:", total_result)