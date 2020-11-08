#!/usr/bin/env python3

from modules.common.automation import *

class InstallerTemplate:

    _PACKAGES = {
            "I2P Dependencies": ['libecj-java', 'libgetopt-java', 'libservlet3.1-java', 'i2p', 'i2p-router', 'libjbigi-jni'],
            "I2P Packages": ['i2p-keyring', 'secure-delete', 'tor']
    }

    def check(self, config):
        return True

    def install(self, config):
        print_status("Configuring anonsurf", 1)
        file_write("etc/apt/sources.list.d/i2p.list", "deb http://deb.i2p2.no/ unstable main")
        print_status("Adding new I2P repository", 1)
        run_command("wget -O - https://geti2p.net/_static/i2p-debian-repo.key.asc | sudo apt-key add -")
        print_status("Updating repos before starting installs", 1)
        run_command("apt update")
        print_status("Installing packages/dependencies", 1)
        apt_install("libservlet3.1-java")
        file_download("http://ftp.us.debian.org/debian/pool/main/j/jetty9/libjetty9-java_9.4.33-1_all.deb", "/tmp/libjetty9.deb")
        run_command("dpkg -i /tmp/libjetty9.deb")
        for title,pkgs in self._PACKAGES.items():
            print_status("Installing {0}...".format(title), 2)
            apt_install(pkgs)
            print_success("Done!", 2)
        print_success("Done installing packages/dependencies", 1)
        print_status("Configuring and installing kali-anonsurf.deb", 1)
        github_clone_option(option='', repo='Und3rf10w/kali-anonsurf', dest_folder='/tmp/kali-anonsurf')
        run_command('cd /tmp/kali-anonsurf')
        run_command('dpkg-deb -b kali-anonsurf-deb-src/ kali-anonsurf.deb')
        run_command('dpkg -i kali-anonsurf.deb')
        print_success("Done installing kali-anonsurf.deb", 1)

