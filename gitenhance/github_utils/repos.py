from .bootstrap import gh
from utils.notifications import TerminalNotification

class Repositories:
    def __self__(self):
        pass

    def print_all_user_repos(self):
        notification = TerminalNotification()
        
        try:
            print("Getting user repositories...")
            user_repositories = []

            for repo in gh.get_user().get_repos():
                user_repositories.append(repo.name)
            gh.close()

            print(user_repositories)
            notification.notify_success()
            return user_repositories
        except Exception as e:
            print(f"An unexpected error has occured: {e}")
            notification.notify_error()

