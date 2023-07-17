class IntegerContainer:
    def __init__(self):
        self.container = set()
    
    def add(self, value):
        self.container.add(int(value))
        return ""
        
    def exists(self, value):
        return "true" if int(value) in self.container else "false"
        
def solution(queries):
    container = IntegerContainer()
    results = []
    
    for query in queries:
        operation, value = query
        if operation == 'ADD':
            result = container.add(value)
        elif operation == "EXISTS":
            result = container.exists(value)
        else:
            result = "Invalid operation"
            
        results.append(result)
        
    return results

queries = [
    ["ADD", "1"],
    ["ADD", "2"],
    ["ADD", "5"],
    ["ADD", "2"],
    ["EXISTS", "2"],
    ["EXISTS", "5"],
    ["EXISTS", "1"],
    ["EXISTS", "4"],
    ["EXISTS", "3"],
    ["EXISTS", "0"],
]

results = solution(queries)
print(results)
