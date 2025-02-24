def most_frequent_prefix(s):
    prefix_count = {}
    max_count = 0
    best_prefix = ""

    for i in range(1, len(s) + 1):
        prefix = s[:i]
        count = s.count(prefix)
        prefix_count[prefix] = count

        if count > max_count or (count == max_count and len(prefix) > len(best_prefix)):
            max_count = count
            best_prefix = prefix

    return f"{best_prefix}-{max_count}"

if __name__ == "__main__":
    s = input().strip()
    print(most_frequent_prefix(s))
