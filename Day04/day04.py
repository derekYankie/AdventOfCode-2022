# Within the first pair of Elves, the first Elf was assigned sections
# 2-4 (sections 2, 3, and 4), while the second Elf was assigned sections 6-8 (sections 6, 7, 8).
# The Elves in the second pair were each assigned two sections.
# The Elves in the third pair were each assigned three sections: one got
# sections 5, 6, and 7, while the other also got 7, plus 8 and 9.

with open('puzzle-input-04') as file:
    ranges = file.read().split('\n')

assignments = [assignment.split(',') for assignment in ranges]

full_overlap = 0
partial_overlap = 0
for assignment in assignments:
    assignment_list = [range.split('-') for range in assignment]
    assignment_list = [set(range(int(assignment[0]), int(
        assignment[1]) + 1)) for assignment in assignment_list]

    # Part 1
    if assignment_list[0] <= assignment_list[1] or assignment_list[0] >= assignment_list[1]:
        full_overlap += 1
    # print(full_overlap)

    # Part 2
    if assignment_list[0] & assignment_list[1]:
        partial_overlap += 1

# Display results 
print(f"Number of assignment pairs with overlapping sets:", full_overlap)
print(f"Partially overlapping sets: {partial_overlap}")
