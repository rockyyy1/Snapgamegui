import os

def remove_underscores(folder_path):
  """Removes all underscores from the filenames in the specified folder.

  Args:
    folder_path: The path to the folder containing the images.
  """
  for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Remove the underscore.
    new_filename = filename.replace("king", "King")

    # Rename the file.
    os.rename(file_path, os.path.join(folder_path, new_filename))


if __name__ == "__main__":
  folder_path = "c:\\Users\\Rocky\\Desktop\\test\\Graphics\\Vector Playing Cards"
  remove_underscores(folder_path)