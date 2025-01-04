from github import Github

from github import Auth

import os

token_path = "~/gitenhance_github_token"
token_file = os.open(token_path, os.O_RDONLY)
token = os.read(token_file)
auth = Auth.Token(token)
os.close(token_file)

gh = Github(auth=auth)

