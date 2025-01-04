from github_utils.bootstrap import gh

class Repositories:
    def __init__(self):
        pass

    def print_all_user_repos():
        print("Getting user repositories...")
        
        for repo in gh.get_user().get_repos():
            print(repo.name)
        gh.close()

