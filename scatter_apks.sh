#!/bin/bash

# Define the directory containing the organized APK files
ORGANIZED_DIR="./Downloads/gochat"

# Define the directory to move the APK files back to
DOWNLOADS_DIR="./Downloads"

# Find all APK files under the organized directory, and move them back to the downloads directory
find "$ORGANIZED_DIR" -type f -name '*.apk' -print0 | xargs -0 -I {} mv {} "$DOWNLOADS_DIR"

#I should add a code to remove the created directories but i'm way too lazy rn 😴
