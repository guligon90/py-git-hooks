import subprocess
from typing import Optional


def get_status_from_command(command: str) -> int:
    status = subprocess.call(command, shell=True)

    return status


def get_text_output_from_command(command: str) -> Optional[str]:
    sub_process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE
    )

    if sub_process and sub_process.stdout:
        # Get subprocess output in bytes
        branch_name = sub_process.stdout.read()
        # Convert to UTF-8 string
        return branch_name.decode("utf-8").strip()

    return None
