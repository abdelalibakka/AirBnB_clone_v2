#!/usr/bin/env bash
# Set up web servers for deployment of web_static

# Install Nginx if it(s not already installed
if ! dpkg -l nginx >/dev/null 2>&1;
then
	sudo apt-get update
	sudo apt-get -y install nginx
fi

# Create directories if don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create HTML file for testing
echo "<html><body>Hello, this is a test page.</body></html>" > /data/web_static/releases/test/index.html

# create symbolic or recreate symbolic link
if [ -L /data/web_static/current ];
then
	sudo rm -rf /data/web_static/current
fi

sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Set ownership recursively to ubuntu user and group
sudo chown -hR ubuntu:ubuntu /data

# Update Nginx configuration using alias
config="location /hbnb_static/ {\n   alias /data/web_static/current/;\n}\n"
sudo sed -i "/server_name _;/a $config" /etc/nginx/sites-available/default


# Create symbolic link for Nginx configuration
sudo ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'

# Restart Nginx to apply the changes
sudo service nginx restart

# Provide feedback
echo "Web server setup complete."
