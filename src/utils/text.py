# Displaying colors
class TextColors:
    BLUE = '\033[94m'
    DEFAULT = '\033[39m'
    GREEN = '\033[92m'
    YELLOW = '\033[33m'
    RED = '\033[91m'
    LIGHT_BLUE = "\033[94m"


class TextFormats:
    BOLD = '\033[1m'
    HEADER = '\033[95m'
    UNDERLINE = '\033[4m'


class Text:
    END = '\033[0m'

    @staticmethod
    def blue(text: str) -> str:
        return TextColors.BLUE + text + Text.END

    @staticmethod
    def green(text: str) -> str:
        return TextColors.GREEN + text + Text.END

    @staticmethod
    def red(text: str) -> str:
        return TextColors.RED + text + Text.END

    @staticmethod
    def light_blue(text: str) -> str:
        return TextColors.LIGHT_BLUE + text + Text.END

    @staticmethod
    def yellow(text: str) -> str:
        return TextColors.YELLOW + text + Text.END

    @staticmethod
    def bold(text: str) -> str:
        return TextFormats.BOLD + text + Text.END

    @staticmethod
    def header(text: str) -> str:
        return TextFormats.HEADER + text + Text.END

    @staticmethod
    def underline(text: str) -> str:
        return TextFormats.UNDERLINE + text + Text.END
