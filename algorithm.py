def print_transportation_table(costs, supply, demand):
    """
    Print the transportation problem in a formatted table
    
    Example:
            Costs
    Source  Destinations
            D1   D2   D3   D4    Supply
    S1      464  513  654  867    75
    S2      352  416  690  791   125
    S3      995  682  388  685   100
    Demand  80   65   70   85
    """
    m = len(costs)
    n = len(costs[0])
    
    print("\nTransportation Problem Table:")
    print("     ", end="")
    for j in range(n):
        print(f"D{j+1:2d}   ", end="")
    print("Supply")
    
    for i in range(m):
        print(f"S{i+1:d}  ", end="")
        for j in range(n):
            print(f"{costs[i][j]:4d}  ", end="")
        print(f"  {supply[i]:3d}")
    
    print("Demand ", end="")
    for j in range(n):
        print(f"{demand[j]:4d}  ", end="")
    print()

def is_balanced(supply, demand):
    """Check if total supply equals total demand"""
    return sum(supply) == sum(demand)

def northwest_corner(supply, demand):
    """
    Implement Northwest Corner method
    Returns: Solution matrix with allocations
    """
    m = len(supply)
    n = len(demand)
    supply_copy = supply.copy()
    demand_copy = demand.copy()
    solution = [[0 for _ in range(n)] for _ in range(m)]
    
    i, j = 0, 0
    while i < m and j < n:
        quantity = min(supply_copy[i], demand_copy[j])
        solution[i][j] = quantity
        supply_copy[i] -= quantity
        demand_copy[j] -= quantity
        
        if supply_copy[i] == 0:
            i += 1
        if demand_copy[j] == 0:
            j += 1
            
    return solution

def vogel_approximation(costs, supply, demand):
    """
    Implement Vogel's Approximation Method (VAM)
    Returns: Solution matrix with allocations
    """
    m = len(supply)
    n = len(demand)
    supply_copy = supply.copy()
    demand_copy = demand.copy()
    solution = [[0 for _ in range(n)] for _ in range(m)]
    
    while sum(supply_copy) > 0:
        # Calculate row and column differences
        row_diffs = []
        col_diffs = []
        
        # Calculate row differences
        for i in range(m):
            if supply_copy[i] > 0:
                row_costs = [costs[i][j] for j in range(n) if demand_copy[j] > 0]
                if len(row_costs) >= 2:
                    sorted_costs = sorted(row_costs)
                    row_diffs.append((i, sorted_costs[1] - sorted_costs[0]))
                elif len(row_costs) == 1:
                    row_diffs.append((i, row_costs[0]))
        
        # Calculate column differences
        for j in range(n):
            if demand_copy[j] > 0:
                col_costs = [costs[i][j] for i in range(m) if supply_copy[i] > 0]
                if len(col_costs) >= 2:
                    sorted_costs = sorted(col_costs)
                    col_diffs.append((j, sorted_costs[1] - sorted_costs[0]))
                elif len(col_costs) == 1:
                    col_diffs.append((j, col_costs[0]))
        
        # Find maximum difference
        max_row_diff = max(row_diffs, key=lambda x: x[1]) if row_diffs else (0, -1)
        max_col_diff = max(col_diffs, key=lambda x: x[1]) if col_diffs else (0, -1)
        
        if max_row_diff[1] >= max_col_diff[1]:
            i = max_row_diff[0]
            # Find minimum cost in selected row
            valid_cols = [j for j in range(n) if demand_copy[j] > 0]
            j = min(valid_cols, key=lambda j: costs[i][j])
        else:
            j = max_col_diff[0]
            # Find minimum cost in selected column
            valid_rows = [i for i in range(m) if supply_copy[i] > 0]
            i = min(valid_rows, key=lambda i: costs[i][j])
        
        # Allocate
        quantity = min(supply_copy[i], demand_copy[j])
        solution[i][j] = quantity
        supply_copy[i] -= quantity
        demand_copy[j] -= quantity
    
    return solution

def russell_approximation(costs, supply, demand):
    """
    Implement Russell's Approximation Method
    Returns: Solution matrix with allocations
    """
    m = len(supply)
    n = len(demand)
    supply_copy = supply.copy()
    demand_copy = demand.copy()
    solution = [[0 for _ in range(n)] for _ in range(m)]
    
    while sum(supply_copy) > 0:
        # Calculate u_i and v_j
        u = [max(row) for row in costs]
        v = [max(costs[i][j] for i in range(m)) for j in range(n)]
        
        # Find cell with minimum delta
        min_delta = float('inf')
        min_i = min_j = 0
        
        for i in range(m):
            for j in range(n):
                if supply_copy[i] > 0 and demand_copy[j] > 0:
                    delta = costs[i][j] - u[i] - v[j]
                    if delta < min_delta:
                        min_delta = delta
                        min_i, min_j = i, j
        
        # Allocate
        quantity = min(supply_copy[min_i], demand_copy[min_j])
        solution[min_i][min_j] = quantity
        supply_copy[min_i] -= quantity
        demand_copy[min_j] -= quantity
    
    return solution

def calculate_total_cost(solution, costs):
    """Calculate total transportation cost"""
    total = 0
    for i in range(len(solution)):
        for j in range(len(solution[0])):
            total += solution[i][j] * costs[i][j]
    return total

# Example usage
if __name__ == "__main__":
    # Example problem from slides
    costs = [
        [464, 513, 654, 867],
        [352, 416, 690, 791],
        [995, 682, 388, 685]
    ]
    
    supply = [75, 125, 100]
    demand = [80, 65, 70, 85]
    
    # Print initial problem
    print("Transportation Problem")
    print_transportation_table(costs, supply, demand)
    
    # Check if problem is balanced
    if not is_balanced(supply, demand):
        print("Error: The problem is not balanced!")
        exit()
    
    # Solve using all three methods
    print("\n1. Northwest Corner Method")
    nw_solution = northwest_corner(supply, demand)
    print("Solution:")
    for row in nw_solution:
        print(row)
    print(f"Total Cost: {calculate_total_cost(nw_solution, costs)}")
    
    print("\n2. Vogel's Approximation Method")
    vogel_solution = vogel_approximation(costs, supply, demand)
    print("Solution:")
    for row in vogel_solution:
        print(row)
    print(f"Total Cost: {calculate_total_cost(vogel_solution, costs)}")
    
    print("\n3. Russell's Approximation Method")
    russell_solution = russell_approximation(costs, supply, demand)
    print("Solution:")
    for row in russell_solution:
        print(row)
    print(f"Total Cost: {calculate_total_cost(russell_solution, costs)}")
