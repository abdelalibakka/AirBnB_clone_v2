#!/usr/bin/env bash

# Set the web_static_dir variable
web_static_dir="/data/web_static"

# Update and install Nginx if not already installed
if ! command -v nginx &>/dev/null; then
    apt-get update
    apt-get -y install nginx
fi

# Create directories if they don't exist
web_static_releases="$web_static_dir/releases/test"
web_static_shared="$web_static_dir/shared"

mkdir -p "$web_static_releases"
mkdir -p "$web_static_shared"

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > "$web_static_releases/index.html"

# Create or recreate a symbolic link
if [ -L "$web_static_dir/current" ]; then
    rm -f "$web_static_dir/current"
fi

ln -s "$web_static_releases" "$web_static_dir/current"

# Give ownership to the www-data user and group recursively
chown -R www-data:www-data "$web_static_dir"

# Update Nginx configuration to serve the content
config_file="/etc/nginx/sites-available/default"
if [[ -f "$config_file" ]]; then
    sed -i "s#\(alias.*\)#\1 $web_static_dir/current/#;" "$config_file"
fi

# Restart Nginx
service nginx restart
