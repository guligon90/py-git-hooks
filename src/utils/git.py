from typing import List, Optional

from utils.commands import get_text_output_from_command


def get_branch_name() -> Optional[str]:
    return get_text_output_from_command(
        "git rev-parse --abbrev-ref HEAD"
    )


def get_last_commit_info() -> Optional[List[str]]:
    output = get_text_output_from_command(
        "git show -s --format='%h %s'"
    )

    if output is not None:
        return output.split(" ")

    return output
