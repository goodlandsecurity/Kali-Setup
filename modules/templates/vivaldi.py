#!/usr/bin/env python3

from modules.common.automation import *


class InstallerTemplate:

    def check(self, config):
        return True

    def install(self, config):
        print_status("Installing Vivaldi", 1)
        vivaldi_link = run_command_with_output('curl -s "https://vivaldi.com/download/" | '
                                               'grep -Eo \'href="[^\"]+"\' | '
                                               'grep -E amd | cut -d \'"\' -f 2',
                                               safe=True).strip()
        file_download(location=vivaldi_link, destination="/tmp/vivaldi.deb")
        run_command("dpkg -i /tmp/vivaldi.deb")
        file_append_no_new_line(filename="/opt/vivaldi/vivaldi", content="--user-data-dir --test-type --no-sandbox")
        print_success("Done!", 1)
