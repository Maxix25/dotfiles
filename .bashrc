
export LS_OPTIONS='--color=auto'
eval "$(dircolors -b)"
alias ls='ls $LS_OPTIONS'
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
alias gs='git status'
alias gp='git push'
alias gpp='git pull'
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
parse_git_branch() {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}
export PS1="\[\e[34m\]\u@\[\e[34m\]\h \[\e[32m\]\w \[\e[35m\]\$(parse_git_branch)\[\e[00m\]$ "

neofetch
