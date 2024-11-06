# Transportation Problem Solver

This project provides a set of Python functions and methods to solve the **Transportation Problem** using various allocation methods. It includes functions to print the transportation problem in a tabular format and solutions for the problem using the **Northwest Corner Method**, **Vogel’s Approximation Method (VAM)**, and **Russell’s Approximation Method**. Additionally, it calculates the total transportation cost based on the solution.

## Features

- **Transportation Table Printing**: Formats and displays the transportation costs, supply, and demand in a readable table.
- **Balance Checker**: Ensures that the total supply equals total demand, required for feasible solutions.
- **Allocation Methods**:
  - **Northwest Corner Method**: A basic method to allocate supply and demand in a top-left to bottom-right approach.
  - **Vogel's Approximation Method (VAM)**: A heuristic method that aims to minimize cost by reducing the penalty in allocation.
  - **Russell's Approximation Method**: Another heuristic method that uses row and column maxima to allocate supplies and demands.
- **Total Cost Calculation**: Computes the total cost of transportation based on the final allocation.

## Example Input

```plaintext
Enter coefficients of supply in one line separated by spaces:
75 125 100

Enter costs for each source separated by spaces:
464 513 654 867
352 416 690 791
995 682 388 685

Enter coefficients of demand in one line separated by spaces:
80 65 70 85

## Example Output

The program will display:

1. The **transportation problem table**, showing supply, demand, and costs.
2. A **balance check** message indicating whether the problem is balanced.
3. Solutions using **Northwest Corner**, **Vogel’s Approximation**, and **Russell’s Approximation** methods.
4. The **total cost** for each method's solution.

## Functions

- **`print_transportation_table(costs, supply, demand)`**: Prints a formatted table displaying the transportation problem.
- **`is_balanced(supply, demand)`**: Checks if total supply equals total demand.
- **`northwest_corner(supply, demand)`**: Solves the problem using the Northwest Corner Method.
- **`vogel_approximation(costs, supply, demand)`**: Solves the problem using Vogel's Approximation Method.
- **`russell_approximation(costs, supply, demand)`**: Solves the problem using Russell’s Approximation Method.
- **`calculate_total_cost(solution, costs)`**: Calculates the total cost of transportation for a given solution.
