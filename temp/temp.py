# Clear Screen
import subprocess
import os

subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


this_dictionary = dict(key1=1, key2=2, key3="value3", key4=True)


print(this_dictionary)
print()
print(this_dictionary.keys())
print()
print(this_dictionary.values())
print()

print("Keys:")
for key, value in this_dictionary.items():
    print(f"{key}")

print("\nValues:")
for key, value in this_dictionary.items():
    print(f"{value}")

print("\nBoth:")
for key, value in this_dictionary.items():
    print(f"{key}: {value}")

if "garbage" not in this_dictionary:
    print(False)


print()
print()
print("- - End of Line - -")
