import os
import argparse

def main():
    seen = {}
    wasted_space = 0
    for root, _, files in os.walk("."):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                with open(file_path, "rb") as rb:
                    hashed = hash(rb.read())
                
                if hashed in seen.keys():
                    print(f"Duplicate file: {file_path} = {seen[hashed]}")
                    wasted_space += os.path.getsize(file_path)
                else:
                    seen[hashed] = file_path
                    
            except Exception as e:
                # print(f"Could not hash/read {file_path} because {e}")
                pass

    print(f"Duplicate files found: {len(seen.keys())}")
    print(f"Size wasted: {wasted_space}")

if __name__ == "__main__":

    flags = argparse.ArgumentParser()
    flags.add_argument("--dir", required=True, help="Choose the directory to run this on")
    args = flags.parse_args()

    if not os.path.exists(args.dir) or not os.path.isdir(args.dir):
        print(f"Can not find the directory: {args.dir}")
        exit(1)

    os.chdir(args.dir)
    main()