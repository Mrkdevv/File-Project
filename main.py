import os


print("WELCOME TO FILTER YOUR PC PROGRAM".upper())
print("Choose what filtration you want in your disk C:\n")

print("1. Filter by file extension (e.g. .txt, .jpg, .pdf)")
print("2. Filter by file size (e.g. files greater than 1MB)")
print("3. Filter by folder or file name")
print("4. Show all files and folders")
print("5. Exit")

try:
    User_choice = int(input("\nEnter your variant: "))
except ValueError:
    print("Please enter number!")
except Exception as e:
    print(f"Error! {e}")



def choice_one():
    extension = input("Enter extension (e.g. .txt): ")
    print(f"Filtering by {extension}...")

    for root,dirs,files in os.walk("C:\\"):
        for file in files:
            if file.endswith(extension):
                print(os.path.join(root,file))

def choice_two():
    try:
        size = int(input("Min size in bytes (e.g. 1000000 for 1MB): "))
        print(f"Filtering files > {size} bytes...")

        for root,dirs,files in os.walk("C:\\"):
            for file in files:
                try:
                    path = os.path.join(root,file)
                    if os.path.getsize(path) > size:
                        print(path)
                except Exception as e:
                    print(f"Unknown error {e}")
    except ValueError:
        print("Error enter a number")

def choice_three():
    name = input("Enter a name of the file | folder: ")
    print(f"Filtering by name containing '{name}'...")
    for root,dirs,files in os.walk("C:\\"):
        for item in files + dirs:
            if name in item:
                print(os.path.join(root,item))

def choice_four():
    print("Showing all files in C:\\ ...")
    for root,dirs,files in os.walk("C:\\"):
        for name in files + dirs:
                print(os.path.join(root,name))
def choice_five():
    print("Exiting...")

if User_choice == 1:
    choice_one()
elif User_choice == 2:
    choice_two()
elif User_choice == 3:
    choice_three()
elif User_choice == 4:
    choice_four()
elif User_choice == 5:
    choice_five()
else:
    print("Invalid choice!")










