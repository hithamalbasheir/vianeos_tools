from jira import JIRA
import getpass

username = input("Enter your jira username: ")
password = getpass.getpass("Enter your jira pass: ")
# Connect to Jira
jira = JIRA('replace_with_jira_url', auth=(username, password))

# Define the JQL query to get the issues you want to clone
jql_query = 'project = '

# Execute the JQL query
issues = jira.search_issues(jql_query)

# Iterate over the issues
for issue in issues:
    # Clone the issue

    # Check if customfield_10300 is not None before accessing its attributes
    customfield_10300 = {'id': issue.fields.customfield_10300.id, 'value': issue.fields.customfield_10300.value} if issue.fields.customfield_10300 else None
    
    # Create a list of component dictionaries from the original issue's components
    components = [{'id': component.id} for component in issue.fields.components]

    cloned_issue = jira.create_issue(project=issue.fields.project.key,
                                     assignee={'name': 'h.elbasheir'},
                                     summary=f'QA - {issue.fields.summary}',
                                     description=issue.fields.description,
                                     issuetype={'name': "Task"},
                                     components=components,
                                     priority={'id': issue.fields.priority.id},
                                     customfield_10300=customfield_10300, #Priority
                                     customfield_10106=issue.fields.customfield_10106, #story points
                                     customfield_10100= #Sprint
                                     )
    
    # Create a link from the original issue to the cloned issue with a link description of "Cloned By"
    jira.create_issue_link(type="clones", outwardIssue=cloned_issue.key, inwardIssue=issue.key)
