#!/usr/bin/python3
# pylint: disable=broad-except
# pylint: disable=invalid-name

import re
import sys

from utils.git import get_branch_name
from utils.constants import BRANCH_NAME_PATTERN, FORBIDDEN_BRANCHES
from utils.messaging import PreCommitHookLogger
from utils.exceptions import PreCommitHookError


logger = PreCommitHookLogger()


def check_current_branch(branch_name: str) -> None:
    regex = re.compile(BRANCH_NAME_PATTERN)
    matches = regex.search(branch_name)    

    if branch_name in FORBIDDEN_BRANCHES:
        raise PreCommitHookError(f"You can't commit directly into the {branch_name} branch.",)

    if matches is None:
        raise PreCommitHookError("Your branch name has an invalid format.")

    logger.info('Current branch is valid!')
    

def main() -> None:
    logger.info("Running hook...")
    branch_name = get_branch_name()
    check_current_branch(branch_name)
    logger.info('Done!')


if __name__ == '__main__':
    try:
        main()
        sys.exit(0)
    except PreCommitHookError as hook_exc:
        print(hook_exc)
        sys.exit(1)
    except Exception as exc:
        logger.error(f"{exc.__class__.__name__} :: {exc}")
        sys.exit(1)
