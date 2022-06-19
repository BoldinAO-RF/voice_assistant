from jira import JIRA
import configparser

config = configparser.RawConfigParser()
config.read('Config.properties')

project = "there project number"

jr = JIRA(config.get('jira', 'server.url'),  token_auth=config.get('jira', 'server.api_key'))


jql = 'project = {} and assignee = currentUser()'.format(project)
issues_list = jr.search_issues(jql)

print(issues_list)