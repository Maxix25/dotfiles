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
alias dot='cp -r ~/.config/qtile/ ~/.config/i3/ ~/.Xresources ~/.bashrc ~/dotfiles'
parse_git_branch() {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}
export PS1="\[\e[34m\]\u@\[\e[34m\]\h \[\e[37m\]\w \[\e[35m\]\$(parse_git_branch)\[\e[00m\]$ "
neofetch
