# right.py
print("Hello from right.py")
count = 20

def get_count():
    import left
    return count + left.count

print("Goodbye from right.py")
