#!/bin/bash

# Define the directory containing the APK files
APK_DIR="./Downloads"

# Change to the directory containing the APK files
cd "$APK_DIR"

# Loop through each APK file in the directory
for apk in *.apk; do
    # Replace dashes with underscores for consistency
    normalized_apk=$(echo $apk | tr '-' '_')
    
    # Extract the app name from the APK file name
    app_name=$(echo $normalized_apk | awk -F'[_ ]' '{print $1}')
    
    # Determine whether the APK is for Huawei or Android
    if [[ $normalized_apk == *"huawei"* ]]; then
        platform="huawei"
    elif [[ $normalized_apk == *"prod"* ]] || [[ $normalized_apk == *"stag"* ]]; then
        platform="android"
    else
        platform="misc"
    fi
    
    # Determine whether the APK is a staging or production version
    if [[ $normalized_apk == *"prod"* ]]; then
        stage="prod"
    elif [[ $normalized_apk == *"stag"* ]]; then
        stage="staging"
    else
        stage="misc"
    fi
    
    # Try to extract the sprint number, if it exists
    if [[ $normalized_apk =~ .*_sprint([0-9]+)_.* ]]; then
        sprint=$(echo $normalized_apk | sed -E 's/.*_sprint([0-9]+)_.*\.apk/\1/')
    else
        sprint="misc"
    fi
    
    # Create the necessary directories
    mkdir -p "$app_name/$platform/sprint_$sprint/$stage"
    
    # Move the APK file to the appropriate directory
    mv "$apk" "$app_name/$platform/sprint_$sprint/$stage/"
done
