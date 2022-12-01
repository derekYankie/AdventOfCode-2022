# Get data
def readFile(path):
    with open(path) as f:
        contents = f.read()
        return contents

# Find the Elf carrying the most Calories.
# How many TOTAL calories is that Elf carrying?
def findMostCalories():
    elves_data = readFile("./puzzle-input")
    elves_data = str(elves_data).split("\n\n")
    sum_data = []
    for i in elves_data:
        new_data = i.split("\n")
        sum_data.append(sum([int(calories) for calories in new_data]))
    total = max(sum_data)
    print("Total most calories carried by an elf:",total)  
    return total

# Find the Top Three Elves carrying the MOST calories.
# How many calories are those Elves carrying in TOTAL?
def getTopThreeElves(n=3):
    elves_data = readFile("./puzzle-input")
    elves_data = str(elves_data).split("\n\n")
    sum_data = []
    for i in elves_data:
        new_data = i.split("\n")
        sum_data.append(sum([int(calories) for calories in new_data]))
    sum_data.sort(reverse=True)  
    sum_top_3 = sum(sum_data[0:n])
    print("Sum of calories from the top 3 elves:",sum_top_3)  
    return sum_top_3

# Display results
def main():
    """ Main program """
    findMostCalories()
    getTopThreeElves(3)

if __name__ == "__main__":
    main()