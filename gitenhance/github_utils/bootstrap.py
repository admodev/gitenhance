from github import Github

from github import Auth

import os

token_path = os.path.expanduser("~/gitenhance_github_token")
token_file_bytes_size = 50

try:
    token_file = os.open(token_path, os.O_RDONLY)
    token = os.read(token_file, token_file_bytes_size).decode('utf-8').strip()
    
    os.close(token_file)
    
    auth = Auth.Token(token)
except FileNotFoundError:
    print(f"Error: GitHub token file not found at {token_path}")
    raise
except Exception as e:
    print(f"An unexpected error occured: {e}")
    raise

gh = Github(auth=auth)

