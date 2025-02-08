def count_unique_substrings():
    num_cases = int(input().strip())
    results = []
    
    for case_index in range(num_cases):
        while True:
            input_line = input().strip()
            if input_line:
                break
        
        N, NC = map(int, input_line.split())
        text = input().strip()
        
        unique_substrings = set()
        for i in range(len(text) - N + 1):
            unique_substrings.add(text[i:i+N])
        
        results.append(str(len(unique_substrings)))
        
    print("\n\n".join(results))

count_unique_substrings()