#!/bin/bash

# Create the "notebooks" folder if it doesn't exist
mkdir -p notebooks

# Move all .ipynb files in the current directory (not in subdirectories) to the "notebooks" folder
find . -maxdepth 1 -type f -name "*.ipynb" -exec mv {} notebooks/ \;