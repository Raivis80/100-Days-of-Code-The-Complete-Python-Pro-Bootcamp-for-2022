# # Access Files and Directories
#
# # read file mode r, write mode w, append mode a, read and write mode r+
#
# # Or Open a file with using "with as" does not require to close the file
# with open('file.txt', 'w') as f:
#     f.write('write Hello World')
# with open('file.txt', 'r') as f:
#     print(f.read())
#
# # Write to a file create a new file if it does not exist
# with open('mew_file.txt', 'w') as f:
#     f.write('New write Hello World')
# with open('mew_file.txt', 'r') as f:
#     print(f.read())
#
# # Append to a file.
# with open('file.txt', 'a') as f:
#     f.write('\nappend Hello World')
# with open('file.txt', 'r') as f:
#     print(f.read())
#
# # Read and write to a file
# with open('file.txt', 'r+') as f:
#     f.write('read and write Hello World')
#     print(f.read())

# Read document from desktop using path
with open('\\Users\\rapet\\OneDrive\\Desktop\\file.txt', 'r') as f:
    print(f.read())

