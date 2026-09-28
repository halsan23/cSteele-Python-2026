# Clear Screen
import subprocess
import os

subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


inventory = {"croissant": 19, "bagel": 4, "muffin": 8, "cake": 1}
print("original list | {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}")


print('\n\nMake a copy of inventory and save it to a variable called "stock_list"')
stock_list = {}
stock_list.update(inventory)
print(f"stock_list | {stock_list}")


print('\n\nadd the value 18 to stock_list under the key "cookie"')
stock_list.update({"cookie": 18})
print(f"stock_list | {stock_list}")


print("\n\nremove 'cake' from 'stock_list' USE A DICTIONARY METHOD")
stock_list.pop("cake", "Key Not Found")
print(f"stock_list | {stock_list}")


print()
print()
print("- - End of Line - -")
