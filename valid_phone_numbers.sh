# Read from the file file.txt and output all valid phone numbers to stdout.

# You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt
