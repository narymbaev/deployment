import subprocess

def get_current_branch():
    result = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stdout=subprocess.PIPE)
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

# print(get_current_branch())
print(get_last_commit())
# print(git_push())
# print(git_pull())
# print(git_merge('feature-branch'))
# print(git_checkout('feature-branch'))
