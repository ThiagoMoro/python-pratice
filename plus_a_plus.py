# Simple demo to show differences between r+ and a+ files modes.

def prepare_file(path, content):
  """Create or overwrite a file with given content (used to prepare r+ demo)."""
  with open(path, "w") as f:
    f.write(content)

def demo_r_plus(path):
  """
  r+ : open for reading and cursor starts at beginning.
  - File must exist (otherwise FileNotFoundError).
  - Writing at current cursor may overwrite existing bytes.
  """
  print("\n -- DEMO r+ --")
  try:
    with open(path, "r+") as f:
      print("Initial content (read):")
      print(repr(f.read()))           # read moves cursor to end
      f.seek(0)                       # move cursor back to start
      print("After seek(0), telling position:", f.tell())
      f.write("R+")                   # writes at start (overwrites first 2 chars)
      f.flush()                       # ensure it's written to disk
      f.seek(0)
      print("Content after writing 'R+':")
      print(repr(f.read()))
  except FileNotFoundError:
    print(f"File '{path}' not found. r+ requires existing file.")

def demo_a_plus(path):
  """
  a+ : open for reading and writing, cursor for writing is at the end.
  - If file does not exist, it's created.
  - write() appends to end; seeking before write usually does not change append behavior.
  """
  print("\n--- DEMO a+ ---")
  with open(path, 'a+') as f:
    print("File opened in a+.")
    f.seek(0)
    print("Initial content (read from start):")
    print(repr(f.read()))
    print("Current cursor (after read):", f.tell())
    # Try moving cursor to beginning and writing (note: append mode still writes at end)
    f.seek(0)
    f.write("A+")          # in append mode, this will be appended to the end
    f.flush()
    # Read full content to show new data present
    f.seek(0)
    print("Content after write('A+') in a+:")
    print(repr(f.read()))

if __name__ == "__main__":
    # Prepare a file for the r+ demo (must exist)
    sample_r = 'sample_r_plus.txt'
    sample_a = 'sample_a_plus.txt'

    # Create or reset sample_r file with known content
    prepare_file(sample_r, "HelloWorld")

    # Ensure sample_a has some content for demonstration (optional)
    prepare_file(sample_a, "Start")

    # Run demos
    demo_r_plus(sample_r)
    demo_a_plus(sample_a)

    print("\n--- End of demo ---")
    print("Check the files 'sample_r_plus.txt' and 'sample_a_plus.txt' to inspect results.")