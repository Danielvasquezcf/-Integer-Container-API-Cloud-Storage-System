class CloudStorageSystem:
    def __init__(self):
        self.users = {}
        self.files = {}

    def add_user(self, user_id, capacity):
        if user_id in self.users:
            return "false"
        self.users[user_id] = int(capacity)
        return "true"

    def add_file_by_user(self, user_id, name, size):
        if user_id not in self.users:
            return ""
        capacity = self.users[user_id]
        if user_id == "admin" or size <= capacity:
            if name not in self.files:
                self.files[name] = size
                self.users[user_id] -= size
                return str(self.users[user_id])
        return ""

    def update_capacity(self, user_id, capacity):
        if user_id not in self.users:
            return ""
        new_capacity = int(capacity)
        current_capacity = self.users[user_id]
        removed_files = 0

        if new_capacity < current_capacity:
            files_sorted = sorted(self.files.items(), key=lambda x: (x[1], x[0]))

            while current_capacity > new_capacity:
                if not files_sorted:
                    break

                file_name, file_size = files_sorted.pop()

                if file_name.startswith("/"):
                    owner_id = file_name.split("/")[1]
                    if owner_id == user_id:
                        del self.files[file_name]
                        current_capacity -= file_size
                        removed_files += 1

        self.users[user_id] = new_capacity
        return str(removed_files)

    def add_file(self, name, size):
        if name not in self.files:
            self.files[name] = size
            return "true"
        return "false"

    def copy_file(self, name_from, name_to):
        if name_from not in self.files or name_to in self.files:
            return "false"
        self.files[name_to] = self.files[name_from]
        return "true"

    def find_files(self, prefix, suffix):
        matching_files = []
        for name in self.files:
            if name.startswith(prefix) and name.endswith(suffix):
                matching_files.append((name, self.files[name]))

        matching_files.sort(key=lambda x: (-x[1], x[0]))

        if matching_files:
            formatted_files = ", ".join(f"{name}({size})" for name, size in matching_files)
            return formatted_files
        else:
            return ""

    def get_file_size(self, name):
        return str(self.files.get(name, -1))


def solution(queries):
    storage_system = CloudStorageSystem()
    results = []

    for query in queries:
        operation = query[0]
        if operation == "ADD_USER":
            user_id = query[1]
            capacity = query[2]
            result = storage_system.add_user(user_id, capacity)
        elif operation == "ADD_FILE_BY":
            user_id = query[1]
            name = query[2]
            size = int(query[3])
            result = storage_system.add_file_by_user(user_id, name, size)
        elif operation == "UPDATE_CAPACITY":
            user_id = query[1]
            capacity = query[2]
            result = storage_system.update_capacity(user_id, capacity)
        elif operation == "ADD_FILE":
            name = query[1]
            size = int(query[2])
            result = storage_system.add_file(name, size)
        elif operation == "COPY_FILE":
            name_from = query[1]
            name_to = query[2]
            result = storage_system.copy_file(name_from, name_to)
        elif operation == "FIND_FILES":
            prefix = query[1]
            suffix = query[2]
            result = storage_system.find_files(prefix, suffix)
        elif operation == "GET_FILE_SIZE":
            name = query[1]
            result = storage_system.get_file_size(name)
        else:
            result = "Invalid operation"
        results.append(result)

    return results


# Pruebas
queries = [
    ["ADD_FILE", "/dir/file.txt", "10"],
    ["GET_FILE_SIZE", "/dir/file.txt"]
]

results = solution(queries)
print(results)

queries = [
    ["ADD_FILE", "/dir/file1.mov", "20"],
    ["GET_FILE_SIZE", "/dir/file1.mov"],
    ["ADD_FILE", "/dir/file1.mov", "70"],
    ["ADD_FILE", "/dir/file1.mov", "90"],
    ["GET_FILE_SIZE", "/dir/file1.mov"],
    ["ADD_FILE", "/dir2/file1.mov", "11"]
]

results = solution(queries)
print(results)

queries = [
    ["GET_FILE_SIZE", "/dir/non-existing-file.gif"],
    ["ADD_FILE", "/dir/non-existing-file.gif", "34"],
    ["GET_FILE_SIZE", "/non-existing-file.gif"],
    ["ADD_FILE", "/non-existing-file.gif", "100000"],
    ["GET_FILE_SIZE", "/non-existing-file.gif"]
]

results = solution(queries)
print(results)

queries = [
    ["COPY_FILE", "/from/file", "/to/file"],
    ["GET_FILE_SIZE", "/to/file"],
    ["ADD_FILE", "/from/file", "68"],
    ["COPY_FILE", "/to/file", "/file"],
    ["ADD_FILE", "/to/file", "11"],
    ["COPY_FILE", "/from/file", "/to/file"],
    ["COPY_FILE", "/from/file", "/file"]
]

results = solution(queries)
print(results)

queries = [
    ["ADD_FILE", "/file/file.txt", "50"],
    ["ADD_FILE", "/file.png", "880"],
    ["GET_FILE_SIZE", "/file/file.txt50"],
    ["GET_FILE_SIZE", "/file/file"],
    ["GET_FILE_SIZE", "/fil"],
    ["GET_FILE_SIZE", "/file/file.txt"],
    ["COPY_FILE", "/file.png", "/file.png880"],
    ["ADD_FILE", "/file.png8", "80"],
    ["COPY_FILE", "/file/file.txt", "/file.pn"],
    ["GET_FILE_SIZE", "/file.pn"],
    ["GET_FILE_SIZE", "/file.png"],
    ["GET_FILE_SIZE", "/file.png8"],
    ["GET_FILE_SIZE", "/file.png880"]
]

results = solution(queries)
print(results)
