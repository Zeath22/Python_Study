# The "with" statement uses a context manager,
# which is an object that defines the methods __enter__() and __exit__()
# to handle the setup and cleanup of resources.
try:
    with open('test.txt', 'r') as file:         # we can open multiple files
        content = file.read()
        print(content)

    # At this point, the file is automatically closed
except RuntimeError:
    print("error")
