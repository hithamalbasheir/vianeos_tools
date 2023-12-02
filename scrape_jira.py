from jira import JIRA
import getpass
username = input("Enter your jira username: ")
password = getpass.getpass("Enter your jira pass: ")
# Connect to Jira
jira = JIRA('replace_with_jira_url', auth=(username, password))

# Define your JQL query based on the project and sprint, you can just check the quey that shows within search
jql_query = 'project = '

# Execute the JQL query
issues = jira.search_issues(jql_query)

# Define a separator
separator = '\n\n\n' + '='*100 + '\n\n\n'

# Open the README file for writing
with open('filename.txt', 'w') as file:
    # Iterate over the issues and write the descriptions to the file
    for issue in issues:
        # Write the issue description followed by a separator to the file
        file.write(issue.fields.summary)
        file.write("\n"+"-"*90+"\n")
        if issue.fields.description:
            file.write(issue.fields.description + separator)