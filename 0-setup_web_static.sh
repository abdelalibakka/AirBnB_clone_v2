#!/usr/bin/env bash

# Install Nginx if not already installed
if ! command -v nginx &>/dev/null; then
    apt-get -y update
    apt-get -y install nginx
fi

# Create necessary directories
mkdir -p /data/web_static/{releases/test,shared}

# Create a fake HTML file
echo "Fake content for testing" > /data/web_static/releases/test/index.html

# Create or recreate a symbolic link
rm -f /data/web_static/current
ln -s /data/web_static/releases/test /data/web_static/current

# Give ownership to the ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_file="/etc/nginx/sites-available/default"
if [[ -f $config_file ]]; then
    sed -i "/location \/hbnb_static/ {s/\(alias.*\)/\1 \/data\/web_static\/current\/;/}" "$config_file"
fi

# Restart Nginx
service nginx restart
