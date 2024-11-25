def solve_map_coloring(variables, domains, constraintbs):
    def is_safe(assignment, var, value):
        return all(assignment.get(neighbor) != value for neighbor in constraints[var])
    def backtrack(assignment):
        if len(assignment) == len(variables):
            return assignment
        var = next((v for v in variables if v not in assignment), None)
        if var is None:
            return None
        for value in domains[var]:
            if is_safe(assignment, var, value):
                assignment[var] = value
                result = backtrack(assignment)
                if result:
                    return result
                del assignment[var]
        return None
    return backtrack({})
# Example usage
variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
domains = {var: ['Red', 'Green', 'Blue'] for var in variables}
constraints = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'Q', 'SA'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}
solution = solve_map_coloring(variables, domains, constraints)
if solution:
    print("Solution found:")
    for var in solution:
        print(f"{var}: {solution[var]}")
else:
    print("No solution found.")
