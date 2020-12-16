#!/usr/bin/python3
# pylint: disable=broad-except
# pylint: disable=invalid-name

import re
import sys
from os import getcwd
from typing import Dict, Optional, Callable

from utils.git import (
    get_branch_name,
    get_last_commit_info
)
from utils.constants import SEMANTIC_VERSION_PATTERN
from utils.exceptions import PostCommitHookError
from utils.messaging import PostCommitHookLogger
from utils.commands import get_status_from_command, get_text_output_from_command

logger = PostCommitHookLogger()


def get_version_from_tag(branch_name: str) -> Optional[Dict]:
    version_info = None

    version_text = get_text_output_from_command(
        "git tag  -l --sort='-*authordate' | head -n1"
    )

    regex = re.compile(SEMANTIC_VERSION_PATTERN)
    match = regex.search(version_text)

    if match is not None:
        version_info = match.groupdict()

    return version_info


def calculate_version(prefix: str, version_info: Dict, increment: int = 1) -> Optional[str]:
    major = int(version_info.get("major", 0))
    minor = int(version_info.get("minor", 0))
    patch = int(version_info.get("patch", 0))
    pre_release = version_info.get("prerelease")
    build_metadata = version_info.get("buildmetadata")

    prefix_switcher = {
        "feat:": lambda _increment:
            f"{str(major + _increment)}.{minor}.{patch}-{pre_release}+{build_metadata}",
        "fix:": lambda _increment:
            f"{major}.{minor}.{str(patch + _increment)}-{pre_release}+{build_metadata}",
    }

    switcher_item = prefix_switcher.get(prefix)

    return switcher_item(increment) if isinstance(switcher_item, Callable) else None


def update_commit_tag(commit_hash: str, commit_prefix: str, version_info: Dict) -> None:
    if commit_hash and commit_prefix and version_info:
        commit_tag = calculate_version(commit_prefix, version_info)

        if commit_tag is not None:
            status = get_status_from_command(
                f"git tag -a -f {commit_tag} {commit_hash} -m \"tagged with v{commit_tag}\"",
            )

            if status != 0:
                raise PostCommitHookError(f"Error while tagging commit with version. Status {status}")

            logger.info(f"Commit tagged with version {commit_tag}.")
    else:
        logger.warn("Tagging not performed. Current version maintained.")



def main() -> None:
    logger.info('Running hook...')
    branch_name = get_branch_name()
    commit_hash, commit_prefix, _ = get_last_commit_info()
    version_info = get_version_from_tag(branch_name)
    update_commit_tag(commit_hash, commit_prefix, version_info)
    logger.info('Done!')


if __name__ == '__main__':
    try:
        main()
        sys.exit(0)
    except PostCommitHookError as pc_exc:
        print(pc_exc)
        sys.exit(1)
    except Exception as exc:
        logger.error(f"{exc.__class__.__name__} :: {exc}")
        sys.exit(1)
