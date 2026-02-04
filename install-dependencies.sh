#install stuff
sudo pacman -S hyprpaper kitty waybar wob wofi yazi hyprpolkitagent nemo nautilus vscode fastfetch pavucontrol hyprshot hyprlock
#install yay
sudo pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si
#install AUR stuff
yay -S eww hyprwat walker elephant maplemono-ttf zen-browser-bin python-pulsectl