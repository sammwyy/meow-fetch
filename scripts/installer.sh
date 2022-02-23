#!/bin/bash
# Check if script is running as root or not.
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

# Check if installer is running from a cloned repo or not.
AUX_FILE=.gitignore
if test -f "$AUX_FILE"; then
    cd ..
else
    git clone https://github.com/sammwyy/meow-fetch
    cd meow-fetch
fi

# Install python dependencies.
pip install -r requirements.txt > /dev/null

# Move source files to /usr/share.
sudo mkdir /usr/share/meow-fetch
sudo cp ./src/* /usr/share/meow-fetch

# Create bin under /usr/bin.
echo "#!/bin/bash" > /usr/bin/meow-fetch
echo "python /usr/share/meow-fetch/main.py" >> /usr/bin/meow-fetch

sudo chmod 755 /usr/bin/meow-fetch

# Copy default config
mkdir "/home/$SUDO_USER/.config/meow-fetch"
cp -r ./default_config/* "/home/$SUDO_USER/.config/meow-fetch"
echo "Installed"