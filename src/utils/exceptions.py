from utils.messaging import HookType, MessageType, message_from_hook


class BasicHookError(Exception):
    def __init__(self, message: str, hook_type: HookType) -> None:
        self.message = message_from_hook(
            hook_type,
            message,
            MessageType.ERROR
        )
        super().__init__(message)

    def __str__(self) -> str:
        return self.message


class CommitMessageHookError(BasicHookError):
    def __init__(
        self,
        message: str,
        hook_type: HookType = HookType.COMMIT_MSG
    ) -> None:
        super().__init__(message, hook_type)


class PreCommitHookError(BasicHookError):
    def __init__(
        self,
        message: str,
        hook_type: HookType = HookType.PRE_COMMIT
    ) -> None:
        super().__init__(message, hook_type)


class PostCommitHookError(BasicHookError):
    def __init__(
        self,
        message: str, hook_type: HookType = HookType.POST_COMMIT
    ) -> None:
        super().__init__(message, hook_type)
