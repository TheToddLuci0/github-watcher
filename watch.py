import requests
import json
from settings import *
from github import Github
import os

if os.environ.get('GITHUB_TOKEN') is not None:
    GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
g = Github(GITHUB_TOKEN)

def invoke_action(repo):
    branch = g.get_repo(repo['options']['repo']).get_branch(repo['options']['branch'])
    flow = g.get_repo(repo["options"]['repo']).get_workflow(repo['options']["name"])
    print(flow)
    #flow.create_dispatch(branch)

if __name__ == '__main__':
    with open(REPOS_JSON, 'r') as f:
        repos = json.loads(f.read())
    _repos = {"repos": []}
    for i in repos['repos']:
        if g.get_repo(i['repo']).get_branch(i['branch']).commit.sha == i['latest_commit']:
            _repos['repos'].append(i)
            continue
        i['latest_commit'] = g.get_repo(i['repo']).get_branch(i['branch']).commit.sha
        if i['action'].lower() == 'invoke_workflow':
            invoke_action(i)
        _repos['repos'].append(i)

    with open(REPOS_JSON, 'w') as f:
        f.write(json.dumps(_repos))
    
    if DEBUG:
        print("[+] Finished")