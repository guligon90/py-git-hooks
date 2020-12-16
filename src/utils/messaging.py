from enum import Enum

from utils.text import Text


class HookType(Enum):
    COMMIT_MSG = "commit-msg"
    POST_COMMIT = "post-commit"
    PRE_COMMIT = "pre-commit"


class MessageType(Enum):
    ERROR = "error"
    INFO = "info"
    WARN = "warn"


def set_message_type_color(message_type: MessageType) -> str:
    text = message_type.value

    type_switcher = {
        'error': Text.red,
        'warn': Text.yellow,
        'info': Text.light_blue,
    }

    color_function = type_switcher.get(text)

    if color_function is not None:
        return color_function(text)

    return text


def message_from_hook(
    hook_type: HookType,
    message: str,
    message_type: MessageType
) -> str:
    hook_type_text = Text.bold(hook_type.value)
    message_type_text = Text.bold(set_message_type_color(message_type))

    return f"[{hook_type_text}][{message_type_text}] {message}"


class BasicHookLogger:
    def __init__(self, hook_type: HookType) -> None:
        self.hook_type = hook_type

    def info(self, message: str) -> None:
        formatted_info = message_from_hook(
            self.hook_type,
            message,
            MessageType.INFO
        )
        print(formatted_info)

    def warn(self, message: str) -> None:
        formatted_warn = message_from_hook(
            self.hook_type,
            message,
            MessageType.WARN
        )
        print(formatted_warn)

    def error(self, message: str) -> None:
        formatted_error = message_from_hook(
            self.hook_type,
            message,
            MessageType.ERROR
        )
        print(formatted_error)


class CommitMessageHookLogger(BasicHookLogger):
    def __init__(self, hook_type: HookType = HookType.COMMIT_MSG) -> None:
        super().__init__(hook_type)


class PreCommitHookLogger(BasicHookLogger):
    def __init__(self, hook_type: HookType = HookType.PRE_COMMIT) -> None:
        super().__init__(hook_type)


class PostCommitHookLogger(BasicHookLogger):
    def __init__(self, hook_type: HookType = HookType.POST_COMMIT) -> None:
        super().__init__(hook_type)
