import r2pipe
import os
import subprocess


class R2_cmd:

    dex_file = ""

    cmd = ""

    r2 = None

    def __init__(self, dex_file):

        self.r2 = r2pipe.open(dex_file)
        self.dex_file = dex_file

    def run_command(self, cmd):

        # analyze only function
        self.r2.cmd("aac")

        return self.r2.cmd(cmd)

    def getFunctionCall(self):

        for line in self.run_command("afl").splitlines():
            len_num = len(line.split()) - 1
            print(line.split()[len_num])

    def getString(self):

        os.system("rabin2 -zqq" + " " + self.dex_file)


def main():
    pass


if __name__ == '__main__':
    main()
