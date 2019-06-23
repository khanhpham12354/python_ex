__author__ = "khanh pham"
# Alice and Bob
name = input("What is your name?")

while(name != "Alice" and name != "Bob"):
    name = input("What is your name?\n")
print(f"Hello {name}")
