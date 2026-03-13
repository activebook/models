#!/bin/bash

# Configuration
MODELS_DIR="models"
LIST_FILE="list.json"
RAW_FILE="raw_models.json"

echo "Synthesizing changes and synchronizing with remote repository..."

# Ensure we are in a git repository
if ! git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
    echo "Error: Not a git repository."
    exit 1
fi

# Stage relevant files
git add "$MODELS_DIR" "$LIST_FILE" "$RAW_FILE"

# Check if there are changes to commit
if git diff --cached --quiet; then
    echo "No modifications detected in the registry. Synchronization aborted."
    exit 0
fi

# Commit changes with a standardized message
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
git commit -m "chore: synchronized model registry at $TIMESTAMP"

# Push to the remote repository
echo "Pushing changes to remote (main branch)..."
if git push origin main; then
    echo "Successfully synchronized registry with remote repository."
else
    echo "Error: Failed to push changes to remote repository."
    exit 1
fi
