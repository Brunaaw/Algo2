from collections import defaultdict

def find_second_smallest_cow():
    cows = ["Bessie", "Elsie", "Daisy", "Gertie", "Annabelle", "Maggie", "Henrietta"]
    milk_production = defaultdict(int)
    
    n = int(input())
    entries = [input() for _ in range(n)]
    
    for entry in entries:
        name, milk = entry.split()
        milk_production[name] += int(milk)
    
    for cow in cows:
        milk_production.setdefault(cow, 0)
    
    unique_milk_values = sorted(set(milk_production.values()))
    if len(unique_milk_values) < 2:
        print("Tie")
        return
    
    second_smallest_value = unique_milk_values[1]
    second_smallest_cows = [cow for cow, milk in milk_production.items() if milk == second_smallest_value]
    
    print(second_smallest_cows[0] if len(second_smallest_cows) == 1 else "Tie")

find_second_smallest_cow()