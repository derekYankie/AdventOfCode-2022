'''
The first start-of-packet marker is complete after...
bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5
nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11
'''

file = open("puzzle-input-06", "r", encoding="utf-8")

data = file.read()


def find_start_of_packet(datastream, unique_char):
    """Returns how many characters needs to be processed before the first
    start-of-message marked is detected with the given unique_char"""
    pk_start = 0
    pk_end = len(datastream)

    while pk_start < pk_end:
        word = ""

        if pk_start + unique_char > pk_end:
            return -1  # NOT FOUND

        for index in range(pk_start, pk_start + unique_char):
            word += datastream[index]

        pk_start += 1

        if len(set(word)) == unique_char:
            return pk_start + (unique_char - 1)


# Display results 
print(f"Packages required for processing with 4 distinct characters:\n {find_start_of_packet(data, 4)}")
print(f"Packages required for processing with 4 distinct characters:\n {find_start_of_packet(data, 14)}")

# Test
file_string = "day06_test.py"

with open(file_string, "r") as input_string:
    buffer = input_string.read()
    print( "PART 1:", [len(set(buffer[subroutine:subroutine+4])) for subroutine in range(0, len(buffer)-4)].index(4)+4 )