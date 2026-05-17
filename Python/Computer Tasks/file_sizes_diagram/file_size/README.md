# file_size

I use `file_size` to turn a folder of files into a treemap that makes large files easier to spot.

## What It Does

- walks a directory tree
- collects file sizes
- renders a treemap with `plotly`
- skips files that cannot be read instead of stopping the whole scan

## Example

![Example treemap](./docs/images/example.png)

## How To Run It

```bash
python ./src/file_size/__main__.py
```

If I want to install the package locally first, I use:

```bash
python -m pip install -r ./requirements.txt
```

## Why I Kept It

I built this as a quick visual reporting tool for everyday file housekeeping. It is useful when I want a clear picture of which folders or files are consuming the most space without digging through a manual listing.
