# dotfiles
# i3 Setup
- First clone the repo using ```git clone https://github.com/Maxix25/dotfiles.git```
- Change directory into the repo folder using ```cd dotfiles/```
- Copy the directory into the corresponding folder ```cp -r i3/ ~/.config/```
### i3 Dependencies:
- ### Font Awesome
  - You need to install <a href="https://github.com/FortAwesome/Font-Awesome/archive/v4.4.0.zip">Font Awesome</a> for having the icons for the workspaces
  - Go to your Downloads folder using ```cd ~/Downloads```
  - Unzip the file that you've just downloaded using ```unzip Font-Awesome-4.4.0.zip```
  - Then navigate into the fonts folder using ```cd Font-Awesome-4.4.0/fonts```
  - Make a directory for the ttf file that we are going to copy using ```mkdir ~/.fonts```
  - You can either copy or move the ttf using ```cp fontawesome-webfont.ttf ~/.fonts``` to copy it or you can use ```mv fontawesome-webfont.ttf ~/.fonts``` to move it
- ### Rofi
  - For Ubuntu use ```sudo apt-get install rofi```
  - For Arch Linux use ```sudo pacman -S rofi```
  
### Screenshot
![i3Screenshot](https://github.com/Maxix25/dotfiles/blob/master/screenshots/i3.png)
# Neovim Setup
- Clone the repo using ```git clone https://github.com/Maxix25/dotfiles.git```
- Change directory into the repo folder using ```cd dotfiles/```
- Copy the neovim directory to the corresponding folder ```cp -r nvim/ ~/.config/```
- Download vim-plug using ```curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim```
- You're ready to use neovim just open it and run ```:PlugInstall``` and all the plugins will install
- ### Plugins (Optional)
  - To install some useful plugins use ```:CocInstall coc-emmet coc-explorer coc-python coc-discord-neovim coc-tsserver```
### Screenshot
![NeovimScreenshot](https://github.com/Maxix25/dotfiles/blob/master/screenshots/neovim.png)
# Qtile Setup
- Clone the repo using ```git clone https://github.com/Maxix25/dotfiles.git```
- Change directory into the repo folder using ```cd dotfiles/```
- Copy the qtile config into the .config folder using ```cp -r qtile/ ~/.config```
### Screenshot
![QtileScreenshot](https://github.com/Maxix25/dotfiles/blob/master/screenshots/qtile.jpeg)
