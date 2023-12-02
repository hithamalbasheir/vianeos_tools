# vianeos_tools
A set of scripts that I wrote during my tenure at vianeos to help me with some mundane tasks, hope you find it helpful :)

# Team Utility Tools Repository

## Introduction
This repository contains a collection of automation and utility scripts designed to streamline and enhance our team's workflow. These tools cover a range of functionalities from issue tracking, file organization, to generating test data.

## Tools Overview

### 1. Batch Clone Jira (`batch_clone_jira.py`)
- **Purpose**: Facilitates the cloning of a large number of JIRA issues, particularly useful for setting up new sprints.
- **Usage**:
  - Specify the sprint for which issues need to be cloned.
  - Optionally, set issues to be skipped.
  - Run the script to clone the specified number of issues.

### 2. Scrape Jira (`scrape_jira.py`)
- **Purpose**: Gathers all issues related to a particular sprint or epic link into a single file for easy analysis and summarization.
- **Usage**:
  - Input the sprint or epic link details.
  - Run the script to extract the issues.
  - Use the output file for analysis or feed into an LLM for summarization.

### 3. Organize APKs (`organize_apks.sh`)
- **Purpose**: Organizes APK files based on specific criteria, sorting them into folders by sprint, stage (stag/prod), and platform (Huawei/Android).
- **Usage**:
  - Define the organizing formula and destination folders.
  - Run the script to automatically sort APK files.

### 4. Scatter APKs (`scatter_apks.sh`)
- **Purpose**: Reverses the organization of APK files done by `organize_apks.sh`.
- **Usage**: Run the script to move APK files back to their original location.

### 5. Mouse Movement Simulator (`mouse.py`)
- **Stay online all the time with this** 🌝
- **Purpose**: Simulates mouse movements to mimic user activity.
- **Usage**: Run the script when needed to maintain an active status on your computer.

### 6. Generate Contacts (`generate_contacts.py`)
- **Purpose**: Generates a specified number of valid UAE contact numbers and exports them as a VCF file. Useful for testing purposes.
- **Usage**:
  - Set the desired number of contacts to be generated.
  - Run the script to generate and export the contacts.

## Getting Started
- Clone this repository: `git clone [repository-url]`
- Ensure you have the necessary dependencies installed for each script.
- Follow the usage instructions for each tool as needed.

## Contributing
Feedback and contributions to improve these tools are welcome. Please follow the standard Git workflow - fork, create a feature branch, commit your changes, and submit a pull request.
