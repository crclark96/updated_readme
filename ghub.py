import json
import github

with open("credentials.json","r") as file:
    creds = json.load(file)

g = github.Github(creds["api_key"])

for repo in g.get_repos():
    print repo
