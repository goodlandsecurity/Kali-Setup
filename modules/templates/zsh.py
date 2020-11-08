#!/usr/bin/env python3

from modules.common.automation import *

class InstallerTemplate:

    def check(self, config):
        return True

    def install(self, config):
        print_status("Installing zsh", 1)
        apt_install('zsh')
        print_success("Done!", 1)

        print_status("Installing oh-my-zsh", 1)
        run_command('curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh | zsh')
        print_status("Installing PowerLevel10k theme for oh-my-zsh", 1)
        github_clone_option(option='--depth=1',
                            repo='romkatv/powerlevel10k',
                            dest_folder='{0}/.oh-my-zsh/custom/themes/powerlevel10k'.format(get_home_folder()))
        print_status("Installing zsh-syntax-highlighting", 1)
        github_clone_option(option='',
                            repo='zsh-users/zsh-syntax-highlighting',
                            dest_folder='{0}/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting'.format(get_home_folder()))
        file_append_once('{0}/.zshrc'.format(get_home_folder()), 'setopt interactivecomments', 'interactivecomments')
        file_append_once('{0}/.zshrc'.format(get_home_folder()), 'setopt ignoreeof', 'ignoreeof')
        file_append_once('{0}/.zshrc'.format(get_home_folder()), 'setopt correctall', 'correctall')
        file_append_once('{0}/.zshrc'.format(get_home_folder()), 'setopt globdots', 'globdots')
        file_append_once('{0}/.zshrc'.format(get_home_folder()), 'source $HOME/.aliases', '.aliases')
        if config.getboolean('general', '4k', fallback=False):
            file_append_once('{0}/.zshrc'.format(get_home_folder()), 'export GDK_SCALE=2')
        file_replace('{0}/.zshrc'.format(get_home_folder()), 'ZSH_THEME=.*', 'ZSH_THEME="powerlevel10k/powerlevel10k"')
        file_replace('{0}/.zshrc'.format(get_home_folder()),
                     'plugins=.*', 'plugins=(git git-extras tmux zsh-syntax-highlighting dirhistory python pip)')
        file_append_once('{0}/.zshrc'.format(get_home_folder()), 'source $HOME/.xinitrc')
        print_success("Done!", 1)
        print_status("Installing Meslo Nerd Font for Powerlevel10k!", 1)
        make_dir('{0}/.fonts'.format(get_home_folder()))

        font_list = ['MesloLGS NF Regular', 'MesloLGS NF Bold', 'MesloLGS NF Italic', 'MesloLGS NF Bold Italic']

        for i in font_list:
            url = 'https://github.com/romkatv/powerlevel10k-media/raw/master/{0}.ttf'.format(i)
            file_download(url, '{0}/.fonts/{1}.ttf'.format(get_home_folder(), i))
            
        run_command('fc-cache -fv')
        print_success("Done!", 1)
