#!/bin/bash
# Check if script is running as root or not.
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

# Delete files.
sudo rm -rf /usr/share/meow-fetch

# Delete binary.
sudo rm -rf /usr/bin/meow-fetch

# Delete config.
sudo rm -rf /home/$SUDO_USER/.config/meow-fetch