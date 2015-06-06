import subprocess
from caprice.common.core.logging import log


def command(arguments):
    log._shell(" ".join(arguments))
    return subprocess.check_call(arguments)


def command_can_fail(arguments):
    log._shell(" ".join(arguments))
    return subprocess.call(arguments)
