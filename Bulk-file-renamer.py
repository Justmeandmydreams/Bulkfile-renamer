import os

def bulk_rename_files():
	directory = input("Enter the directory path: ")
	prefix = input("Enter the prefix for the new file names: ")
	start_number = int(input("Enter the starting number for the new file names: "))
	for i, filename in enumerate(os.listdir(directory), start_number):
		old_path = os.path.join(directory, filename)
		new_filename = f"{prefix}_{i:04d}{os.path.splitext(filename)[1]}"
		new_path = os.path.join(directory, new_filename)
		os.rename(old_path, new_path)

if _name_ == "_main_":
	bulk_rename_files()
