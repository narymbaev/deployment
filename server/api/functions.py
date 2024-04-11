import subprocess

def get_current_branch():
    result = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8').strip()

def get_last_commit_id():
    result = subprocess.run(['git', 'log', '--format="%H"', '-n', '1'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8').strip()

def get_last_commit():
    result = subprocess.run(['git', 'log', '-1'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8').strip()


def git_push():
    result = subprocess.run(['git', 'push'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8').strip()


def git_merge(branch_name):
    result = subprocess.run(['git', 'merge', branch_name], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8').strip()


def git_checkout(branch_name):
    result = subprocess.run(['git', 'checkout', branch_name], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8').strip()


def git_pull():
    result = subprocess.run(['git', 'pull'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8').strip()

print("THe current branch: ", get_current_branch())
print("The last commit: ", get_last_commit_id())
# print("Details of last commit: ", get_last_commit())
# print("Merged: ", git_merge('ft/bug'))
print("Pushed", git_push())
# print(git_pull())
# print(git_checkout('feature-branch'))

print("NEW FEATURE FROM ANOTHER BRANCH")
