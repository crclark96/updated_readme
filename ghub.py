from subprocess import call
import json
import github

with open("credentials.json","r") as file:
    creds = json.load(file)

g = github.Github(creds["api_key"])
user = g.get_user()
all_repos = g.get_repos()

forks = []

forks.append(user.create_fork(all_repos[0]))

call(["git", "clone", forks[0].html_url])

call(["rm", "-rf", forks[0].name])

forks[0].delete()

