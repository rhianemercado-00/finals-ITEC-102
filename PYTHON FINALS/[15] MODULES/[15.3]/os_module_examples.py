# OS Module Examples

import os

# Example 1: Getting current working directory
print("Example 1: Current Working Directory")
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# Example 2: Listing directory contents
print("\nExample 2: Directory Contents")
files = os.listdir(current_dir)
print(f"Files in current directory: {files[:5]}...")  # Show first 5 items

# Example 3: Creating and removing directories
print("\nExample 3: Directory Operations")
new_dir = "temp_folder"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"Created directory: {new_dir}")
    
# Check if it exists
if os.path.exists(new_dir):
    print(f"Directory {new_dir} exists")
    os.rmdir(new_dir)
    print(f"Removed directory: {new_dir}")

# Example 4: Environment variables
print("\nExample 4: Environment Variables")
path_var = os.environ.get('PATH', 'Not found')
print(f"PATH environment variable (first 100 chars): {path_var[:100]}...")

# Example 5: File path operations
print("\nExample 5: Path Operations")
file_path = os.path.join("folder", "subfolder", "file.txt")
print(f"Constructed path: {file_path}")
print(f"Base name: {os.path.basename(file_path)}")
print(f"Directory name: {os.path.dirname(file_path)}")
print(f"Is absolute path: {os.path.isabs(file_path)}")

# Example 6: File information
print("\nExample 6: File Information")
script_path = __file__  # Current script file
stat_info = os.stat(script_path)
print(f"Size of this script: {stat_info.st_size} bytes")

# Example 7: Running system commands
print("\nExample 7: System Commands")
try:
    result = os.system("echo Hello from OS command")
    print(f"Command executed with result: {result}")
except Exception as e:
    print(f"Could not execute command: {e}")

# Example 8: Walking through directory tree
print("\nExample 8: Directory Tree Walk")
print("Walking current directory (first 3 levels only):")
for root, dirs, files in os.walk("."):
    level = root.replace('.', '').count(os.sep)
    if level < 3:  # Only show first 3 levels
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)/}")
        subindent = ' ' * 2 * (level + 1)
        for file in files[:3]:  # Show first 3 files only
            print(f"{subindent}{file}")