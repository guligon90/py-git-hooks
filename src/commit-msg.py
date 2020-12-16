#!/usr/bin/python3
# pylint: disable=broad-except
# pylint: disable=invalid-name

import re
import sys
from typing import Tuple

from utils.constants import (
    COMMIT_MSG_MIN_LEN,
    COMMIT_MSG_MAX_LEN,
    COMMIT_MSG_PATTERN
)
from utils.exceptions import CommitMessageHookError
from utils.messaging import CommitMessageHookLogger


logger = CommitMessageHookLogger()


def get_commit_text() -> str:
    # The message is stored in ./git/COMMIT_EDITMSG
    commit_msg_file = open(sys.argv[1])
    commit_msg = commit_msg_file.read().strip()

    return commit_msg


def check_incoming_commit_text(line: str) -> None:
    regex = re.compile(COMMIT_MSG_PATTERN)
    match = regex.match(line)

    if match is None:
        raise CommitMessageHookError("Your commit message has an invalid format.")

    if not COMMIT_MSG_MIN_LEN <= len(match.group()) <= COMMIT_MSG_MAX_LEN:
        raise CommitMessageHookError(
            f"Your commit message must have between {COMMIT_MSG_MIN_LEN} and {COMMIT_MSG_MAX_LEN} characters."
        )

    logger.info("Commit message is valid!")


def main(args=None) -> None:
    logger.info("Running hook...")
    commit_text = get_commit_text()
    check_incoming_commit_text(commit_text)
    logger.info('Done!')
    

if __name__ == '__main__':
    try:
        main()
        sys.exit(0)
    except CommitMessageHookError as cm_exc:
        print(cm_exc)
        sys.exit(1)
    except Exception as exc:
        logger.error(f"{exc.__class__.__name__} :: {exc}")
        sys.exit(1)
