import os

# Paths
photos_folder = r"C:\ahmad\Programming\Python\projects\photoSplitProgram\photos"
cropped_folder = r"C:\ahmad\Programming\Python\projects\photoSplitProgram\cropped"
aligned_folder = r"C:\ahmad\Programming\Python\projects\photoSplitProgram\aligned"
final_folder = r"C:\ahmad\Programming\Python\projects\photoSplitProgram\final"

# Toggles
SAVE_CROPPED = False
SAVE_ALIGNED = False

# Create folders if not exist
for folder in [cropped_folder, aligned_folder, final_folder]:
    os.makedirs(folder, exist_ok=True)
