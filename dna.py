import csv
import sys


def main():

    if len(sys.argv) != 3:  # Check for command-line usage
        print("Usage Error")
        exit(1)

    database_file = sys.argv[1]

    dna_file = sys.argv[2]

    profile_data = []  # Read database file into a variable
    with open(database_file, 'r') as file:
        reader = csv.DictReader(file)
        str_names = reader.fieldnames[1:]
        for row in reader:
            profile_data.append(row)

    with open(dna_file, 'r', encoding="utf-8") as f:  # Read DNA sequence file into a variable
        sequence = f.read()

    longest_run = {}  # Find longest match of each STR in DNA sequence

    for str_name in str_names:
        longest_run[str_name] = longest_match(sequence, str_name)

    for profile in profile_data:  # Check database for matching profiles
        match = True
        for str_name in str_names:
            if int(profile[str_name]) != longest_run[str_name]:
                match = False
                break
        if match == True:
            print(profile['name'])
            return

    print("No Match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
