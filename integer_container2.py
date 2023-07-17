"""
Scenario
The next step is to support removal from the container:

REMOVE <value> should remove a single occurrence of the specified value from the container. If the value has multiple occurrences, only one of them should be removed.
Previous level functionality should remain the same. To pass to the next level you have to pass all tests at this level.

Given a list of queries, return the list of answers for these queries.

Environment
To customize the editor settings and see the editor hotkeys, check out the IDE Settings tab  in the lower left corner of the page.

For debugging purposes, you can:
Run just a single test case by clicking the "Run single" button  to the right of each test case
Setting up and executing a set of custom tests at "Custom Tests" tab
For more information, check out the Readme tab  on the left.
Partial credit will be granted for each test passed, so press Submit often to run tests and receive partial credits for passed tests. Please check tests for requirements and argument types.

Example

For
queries = [
    ["ADD", "1"],
    ["ADD", "2"],
    ["ADD", "2"],
    ["ADD", "3"],
    ["EXISTS", "1"],
    ["EXISTS", "2"],
    ["EXISTS", "3"],
    ["REMOVE", "2"],
    ["REMOVE", "1"],
    ["EXISTS", "2"],
    ["EXISTS", "1"]
]
the output should be solution(queries) = ["", "", "", "", "true", "true", "true", "true", "true", "true", "false"].

Explanation:

Add 1, 2, 2, 3 -> [1, 2, 2, 3]
Numbers 1, 2, 3 exist in the container
Remove 2, 1 -> [2, 3]
Number 2 exists in the container, number 1 doesn't exist
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.string queries

An array of queries. It is guaranteed that all queries consist only of operations described 
in the description, and these operations satisfy the format described in the description.
All integers represented as strings are from range [-100, 100].

Guaranteed constraints:
1 ≤ queries.length ≤ 100.

[output] array.string

Array consisting of operation results.

[Python 3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name
"""

class IntegerContainer:
    def __init__(self):
        self.container = set()

    def add(self, value):
        self.container.add(int(value))
        return ""

    def exists(self, value):
        return "true" if int(value) in self.container else "false"

    def remove(self, value):
        value = int(value)
        if value in self.container:
            self.container.remove(value)
            return "true"
        else:
            return "false"

    def get_next(self, value):
        value = int(value)
        next_value = float('inf')
        for num in self.container:
            if num > value and num < next_value:
                next_value = num
        return str(next_value) if next_value != float('inf') else ""

def solution(queries):
    container = IntegerContainer()
    results = []

    for query in queries:
        operation, value = query
        if operation == 'ADD':
            result = container.add(value)
        elif operation == 'EXISTS':
            result = container.exists(value)
        elif operation == 'REMOVE':
            result = container.remove(value)
        elif operation == 'GET_NEXT':
            result = container.get_next(value)
        else:
            result = "Invalid operation"

        results.append(result)

    return results

# Ejemplo de prueba
queries = [
    ["ADD", "1"],
    ["ADD", "2"],
    ["ADD", "2"],
    ["ADD", "4"],
    ["GET_NEXT", "1"],
    ["GET_NEXT", "2"],
    ["GET_NEXT", "3"],
    ["GET_NEXT", "4"],
    ["REMOVE", "2"],
    ["GET_NEXT", "1"],
    ["GET_NEXT", "2"],
    ["GET_NEXT", "3"],
    ["GET_NEXT", "4"]
]

results = solution(queries)
print(results)
