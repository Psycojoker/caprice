import pwd

from caprice.core.logging import log
from caprice.core.shell import command


def _user_exists(name):
    try:
        pwd.getpwnam(name)
        return True
    except KeyError:
        return False


def _create_user(name, password="!"):
    to_run = ["useradd", "--create-home", "-p", password]
    to_run.append(name)
    return command(to_run)


def user(name, password):
    log.question("check if user '%s' exists" % name)
    if not _user_exists(name):
        log.action("user doesn't exists, create it")
        _create_user(name, password=password)
    else:
        log.ok("user exists, continue")


def headless_user(name):
    "Create a user that isn't able to log by password"
    log.question("check if user '%s' exists" % name)
    if not _user_exists(name):
        log.action("user doesn't exists, create it")
        _create_user(name)
    else:
        log.ok("user exists, continue")
