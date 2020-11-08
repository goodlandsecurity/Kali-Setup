#!/usr/bin/env python3

from modules.common.automation import *

class InstallerTemplate:

    
    def check(self, config):
        return True

    def install(self, config):
        print_status("Building BloodHound GUI", 1)
        run_command("npm install -g electron-packager")
        run_command("cd /opt/adaptivethreat_BloodHound-git")
        run_command("npm install")
        run_command("npm run linuxbuild")
        print_success("Done building BloodHound GUI!", 1)

