#!/usr/bin/env bash

# Colors
GREEN="\033[1;32m"
CYAN="\033[1;36m"
YELLOW="\033[1;33m"
MAGENTA="\033[1;35m"
RESET="\033[0m"

clear
echo ""
echo ""
echo ""
# Box design
cols=$(tput cols)
box_width=$((cols - 4))
top_border=$(printf '╔'; for ((i=0; i<$box_width; i++)); do printf '═'; done; printf '╗')
bottom_border=$(printf '╚'; for ((i=0; i<$box_width; i++)); do printf '═'; done; printf '╝')

# Banner text (DownVid logo)
banner=(
"       ██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗   ██╗██╗██████╗ "
"       ██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║   ██║██║██╔══██╗"
"       ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║   ██║██║██║  ██║"
"       ██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║   ██║██║██║  ██║"
"       ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║╚██████╔╝██║██████╔╝"
"       ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═════╝"
)

# Print top border
echo -e "${CYAN}${top_border}${RESET}"

# Blank padding line
printf "${CYAN}║%$((box_width))s${CYAN}║\n" " "

# Animated printing (slow-motion)
for line in "${banner[@]}"; do
    printf "${CYAN}║  "
    for ((i=0; i<${#line}; i++)); do
        printf "${GREEN}${line:$i:1}${RESET}"
        sleep 0.0015
    done
    printf "%$((box_width - ${#line} - 2))s${CYAN}║\n" " "
done

# Spacer
printf "║%$((box_width))s║\n" " "

# Info Section
printf "${CYAN}║  🚀 ${GREEN}DownVid${RESET} v1.0 — Download like a smart !                     %$((box_width-64))s${CYAN}║\n" " "
printf "${CYAN}║  👨‍💻 Author: ${YELLOW}Bittu Yadav          ${RESET}%$((box_width-36))s${CYAN}║\n" " "
printf "${CYAN}║  🔗 GitHub: ${GREEN}https://github.com/bittuyadav0214        ${RESET}%$((box_width-54))s${CYAN}║\n" " "
printf "${CYAN}║  📸 Instagram: ${MAGENTA}https://instagram.com/bittu.yadav0214  ${RESET}%$((box_width-55))s${CYAN}║\n" " "

# Bottom padding
printf "${CYAN}║%$((box_width))s${CYAN}║\n" " "

# Bottom border
echo -e "${CYAN}${bottom_border}${RESET}"

echo ""
echo ""

