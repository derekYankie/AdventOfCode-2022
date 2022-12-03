# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

from pathlib import Path

def common_items(list):
    supplies = []
    for rucksack in list:
        comp_a, comp_b = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        for same_type in set(comp_a):
            if same_type in comp_b:
                supplies.append(same_type)
    return supplies

# The priorities of each item types
def get_priority(char):
    if ord(char) >= 96 and ord(char) <= 122:
        return ord(char) - 96
    if ord(char) >= 65 and ord(char) <= 90:
        return ord(char) - 38

# The sum of the priorities of supply items 
# in both compartments of each rucksack
p = Path(__file__).with_name("puzzle-input-03")
supplies = open(p).read().splitlines()
part_one = sum([get_priority(item) for item in common_items(supplies)])
print("Total supply in both compartments of each rucksack:", part_one)

# The sum of the priorities of supply items 
# that corresponds to the badges of each three-Elf group
elven_groups = [supplies[i:i + 3] for i in range(0, len(supplies), 3)]
badges = ["".join(set(a) & set(b) & set(c)) for a,b,c in elven_groups]
part_two = sum([get_priority(badge) for badge in badges])
print("Total supply items that corresponds to the badges of each three-Elf group:", part_two)