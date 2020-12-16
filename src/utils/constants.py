# Branch related
BRANCH_NAME_PATTERN = r"(^(HEAD)|(^(KOP|KERP)(\-)([1-9]\d+)))"

# Commit related
COMMIT_EDIT_MSG_FILE = '.git/COMMIT_EDITMSG'
COMMIT_MSG_MIN_LEN = 15
COMMIT_MSG_MAX_LEN = 100
COMMIT_MSG_PATTERN = r"(((feat|fix|chore|refactor|style|test|docs)(((\w{0,15})))?))(:.\S.*)"
COMMIT_PREFIX_GROUP_PATTERN = r"(^(?<feature>feat)|(?<fix>fix))(:.\S.*)"


# List of branches that don't allow direct commit
FORBIDDEN_BRANCHES = ["master", "stage", "dev"]


# Semantic versioning related
SEMANTIC_VERSION_PATTERN = r"^(?P<major>0|[1-9]\d*)\." + \
    r"(?P<minor>0|[1-9]\d*)\." + \
    r"(?P<patch>0|[1-9]\d*)" + \
    r"(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))" + \
    r"?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
