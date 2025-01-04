from .bootstrap import gh

class Repositories:
    def __self__(self):
        pass

    def print_all_user_repos(self):
        print("Getting user repositories...")
        user_repositories = []

        for repo in gh.get_user().get_repos():
            user_repositories.append(repo.name)
        gh.close()

        print(user_repositories)
        return user_repositories

