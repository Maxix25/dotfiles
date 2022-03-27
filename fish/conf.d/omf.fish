set fish_greeting
alias ls='ls --color=auto'
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
alias gs='git status'
alias gp='git push'
alias gpp='git pull --ff'
alias gd='git diff'
alias gc='git commit -m'
alias ga='git add'
alias rm='rm -f'
alias blackarch='pacman -Sgg | grep blackarch | cut -d " " -f2 | sort -u | grep '
alias dot='cp -r ~/.config/qtile/ ~/.config/i3/ ~/.Xresources ~/.bashrc ~/.config/nvim ~/.config/qutebrowser/ ~/dotfiles'
alias font='sudo mv *.ttf /usr/share/fonts'
alias pbcopy='xsel --clipboard --input'
alias pbpaste='xsel --clipboard --output'
alias generic_send_tcp='spike-fuzzer-generic-send_tcp'
alias pattern_create='/opt/metasploit/.tools/exploit/pattern_create.rb'
alias maxicentos='ssh -l root maxicentos.com'
alias maxikali='ssh -l root maxikali.com'
alias qemucreatedisk='qemu-img create -f qcow2 -o preallocation=off'
alias vim='nvim'
alias verseletdb="mysql -h bscwdxvrlgpqghiwem5u-mysql.services.clever-cloud.com -P 3306 -u uqy97dkloyexzhhn -p bscwdxvrlgpqghiwem5u"
alias ..='cd ..'
alias emacs="emacsclient -c -a 'emacs'"
alias doom="~/.emacs.d/bin/doom"
alias macchanger="sudo macchanger -r enp0s25"
alias monitor="pactl load-module module-loopback latency_msec=1"
alias monitor-unload="pactl unload-module module-loopback"
export PATH="$HOME/.local/bin:$PATH"
function __user_host
  set fqdn (hostname -f)
  set -l content 
  if [ (id -u) = "0" ];
    echo -n (set_color --bold yellow)\((set_color --bold red)$USER(set_color --bold yellow)💀(set_color --bold red)$fqdn(set_color --bold yellow)\) (set color normal)
  else
    echo -n (set_color --bold blue)\((set_color --bold 33C8FF)$USER(set_color --bold 33C8FF)@MAXI-PC(set_color --bold 33C8FF)\) (set color normal)
  end
end

function __current_path
  if [ (id -u) = "0" ];
    echo -n (set_color --bold yellow)-[(set_color --bold white)(prompt_pwd)(set_color --bold yellow)] (set_color normal)
  else
    echo -n (set_color --bold blue)-[(set_color --bold white)(prompt_pwd)(set_color --bold blue)] (set_color normal) 
  end
end

function _git_branch_name
  echo (command git symbolic-ref HEAD 2> /dev/null | sed -e 's|^refs/heads/||')
end

function _git_is_dirty
  echo (command git status -s --ignore-submodules=dirty 2> /dev/null)
end

function __git_status
  if [ (_git_branch_name) ]
    set -l git_branch (_git_branch_name)

    if [ (_git_is_dirty) ]
      set git_info '<'$git_branch"*"'>'
    else
      set git_info '<'$git_branch'>'
    end

    echo -n (set_color yellow) $git_info (set_color normal) 
  end
end

function fish_prompt
  if [ (id -u) = "0" ];
    echo -n (set_color --bold yellow)"╭─"(set_color normal)
  else
    echo -n (set_color --bold blue)"╭─"(set_color normal)
  end
  __user_host
  __current_path
  __git_status
  echo -e ''
  if [ (id -u) = "0" ];
    echo (set_color --bold yellow)"╰─""# "(set_color normal)
  else
    echo (set_color --bold blue)"╰─""\$ "(set_color normal)
  end
end

function fish_right_prompt
  set -l st $status

  if [ $st != 0 ];
    echo (set_color red) ↵ $st  (set_color normal)
  end
  set_color -o 666
  date '+ %T'
  set_color normal
end
set fish_color_command normal
set fish_color_error FF0000
set fish_color_cancel normal
neofetch
