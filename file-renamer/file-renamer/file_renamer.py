import os

folder = input("Folder path: ")
prefix = input("Filename prefix: ")

files = os.listdir(folder)

for i, name in enumerate(files):
    old_path = os.path.join(folder, name)
    if os.path.isfile(old_path):
        new_name = f"{prefix}_{i}.txt"
        new_path = os.path.join(folder, new_name)
        os.rename(old_path, new_path)

print("Done")
