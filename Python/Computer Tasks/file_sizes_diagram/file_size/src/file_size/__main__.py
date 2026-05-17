import os

import plotly.express as px
import pandas as pd
import Adonis

import cli

def convert_size(size: int) -> str:

    if size < 1024:
        return f"{size}b"
    if size < 1024 * 1024:
        return f"{size / 1024}kb"
    if size < 1024 * 1024 * 1024:
        return f"{size / 1024 / 1024}mb"
    if size < 1024 * 1024 * 1024 * 1024:
        return f"{size / 1024 / 1024 / 1024}gb"

    return ""

def main():
    ROOTS,FILES, SIZES = [], [], []
    try:
        TERMINAL_WIDTH = os.get_terminal_size()[0]
    except:
        TERMINAL_WIDTH = 80
        
    PREV_LENGTH = TERMINAL_WIDTH

    flags = cli.cli()

    Adonis.PrintInfo(f"Been asked to ignore: {flags.ignore}")

    for root, _, list_of_files in os.walk("."):

        for file in list_of_files:
            full_file_path = os.path.join(root, file)

            if any (file in flags.ignore for file in full_file_path.split(os.sep)):
                message = f"Ignoring: {full_file_path}"
                current_length = len(message)
                Adonis.PrintWarning(message + (" " * abs((current_length - PREV_LENGTH))), end="\r")
                PREV_LENGTH = len(f"Ignoring: {full_file_path}")
                continue

            FILES.append(file)
            ROOTS.append(root)

            try:
                # print(f"Looking at {full_file_path}", end="\r")        
                SIZES.append(os.path.getsize(full_file_path))
                # real_size.append(convert_size(os.path.getsize(full_file_path)))
            except Exception as e:
                Adonis.PrintError(f"[ERROR]: {e}")
                FILES.pop(-1)
                ROOTS.pop(-1)

    df = pd.DataFrame(
        dict(ROOTS=ROOTS,FILES=FILES, SIZES=SIZES)
    )
    df["all"] = "all" # in order to have a single root node
    fig = px.treemap(df, path=['all', 'ROOTS', 'FILES'], values='SIZES')
    fig.update_traces(root_color="lightgrey")
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    fig.show()

if __name__ == "__main__":
    main()