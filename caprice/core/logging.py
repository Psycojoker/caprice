import sys


class Logger(object):
    DEFAULT = "\033[0m"
    OK = "\033[0;32m"
    QUESTION = "\033[0;36m"
    ACTION = "\033[1;36m"
    SHELL = "\033[1;37m"


    def _shell(self, message):
        sys.stdout.write(self.SHELL)
        sys.stdout.write("Shell: ")
        sys.stdout.write(self.DEFAULT)
        sys.stdout.write(message)
        sys.stdout.write("\n")

    def action(self, message):
        sys.stdout.write(self.ACTION)
        sys.stdout.write(message.lstrip())
        sys.stdout.write(self.DEFAULT)
        sys.stdout.write("\n")

    def question(self, message):
        sys.stdout.write(self.QUESTION)
        sys.stdout.write(message.lstrip())
        sys.stdout.write(self.DEFAULT)
        sys.stdout.write("\n")

    def ok(self, message):
        sys.stdout.write(self.OK)
        sys.stdout.write(message.lstrip())
        sys.stdout.write(self.DEFAULT)
        sys.stdout.write("\n")

    def info(self, message):
        sys.stdout.write(message.lstrip())
        sys.stdout.write("\n")


log = Logger()
