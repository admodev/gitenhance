from github.bootstrap import Octokit

# Prueba
print(Octokit.repos.list_for_org(org='octokit', type='public'))

