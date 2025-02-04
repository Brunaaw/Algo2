def register_users(n, usernames):
    database = {}
    results = []
    
    for name in usernames:
        if name in database:
            database[name] += 1
            results.append(f"{name}{database[name]}")
        else:
            database[name] = 0
            results.append("OK")
    
    return results

n = int(input())
usernames = [input().strip() for _ in range(n)]

for response in register_users(n, usernames):
    print(response)