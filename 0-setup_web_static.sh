#!/usr/bin/env bash
# Config Server
sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install -y nginx
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared
echo "<h1>Holberton School</h1>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown unubtu:ubuntu -hR /data/
sudo service nginx restart
