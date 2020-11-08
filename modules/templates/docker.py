#!/usr/bin/env python3

from modules.common.automation import *

class InstallerTemplate:

    def check(self, config):
        return True

    def install(self, config):
        print_status("Configuring Docker", 1)
        run_command("apt update")
        apt_install("docker.io")
        run_command("systemctl enable --now docker")
        run_command("usermod -aG docker {0}".format(get_user()))
        print_success("Docker configuration complete!", 1)
        
