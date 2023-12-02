from jira import JIRA
import getpass
#Some jira fields come with custom field id, and this code helps me check it, adjust as needed
username = input("Enter your jira username: ")
password = getpass.getpass("Enter your jira pass: ")
# Connect to Jira
jira = JIRA('replace_with_jira_url', auth=(username, password))

# Get all fields
fields = jira.fields()

# Initialize field IDs to None
severity_field_id = None
story_points_field_id = None

# Find the custom field IDs for Severity and Story Points
for field in fields:
    if field['name'].lower() == 'sprint':
        severity_field_id = field['id']
    elif field['name'].lower() == 'story points':
        story_points_field_id = field['id']

    # Break if both field IDs have been found
    if severity_field_id and story_points_field_id:
        break

# Output the field IDs
if severity_field_id:
    print(f'The field ID for sprint is: {severity_field_id}')
else:
    print('Severity field not found')

if story_points_field_id:
    print(f'The field ID for Story Points is: {story_points_field_id}')
else:
    print('Story Points field not found')
