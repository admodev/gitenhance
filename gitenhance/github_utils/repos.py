from .bootstrap import gh
from utils.notifications import TerminalNotification

class Repositories:
    def __self__(self):
        pass

    def print_all_user_repos(self):
        print("Getting user repositories...")
        notification = TerminalNotification()
        user_repositories = []

        for repo in gh.get_user().get_repos():
            user_repositories.append(repo.name)
        gh.close()

        print(user_repositories)
        notification.notify_success()
        return user_repositories

