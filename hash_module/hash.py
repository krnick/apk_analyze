import subprocess


class HASH():

    apk_file = ""

    def __init__(self, apk_file):

        self.apk_file = apk_file

    def getAPKHASH(self):

        output = subprocess.check_output(
            "md5sum " + self.apk_file + "  |awk '{print $1}'",
            shell=True).strip()
        output = str(output, encoding="utf-8")

        return output
