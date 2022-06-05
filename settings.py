from os.path import exists


# Github Personal Access Token
GITHUB_TOKEN = "NOT A REAL TOKEN"

REPOS_JSON = "./repos.json"

DEBUG = False

if exists("local_settings.py"):
    from local_settings import *
