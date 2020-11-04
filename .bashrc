[[ $- != *i* ]] && return
export LS_OPTIONS='--color=auto'
eval "$(dircolors -b)"
alias ls='ls $LS_OPTIONS'
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
parse_git_branch() {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}
export PS1="\[\e[32m\]\u@\[\e[32m\]\h \[\e[34m\]\w \[\e[91m\]\$(parse_git_branch)\[\e[00m\]$ "
neofetch
