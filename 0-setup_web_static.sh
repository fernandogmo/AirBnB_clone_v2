#!/usr/bin/env bash
# Sets up your web servers for the deployment of `web_static`
apt update -y
apt upgrade -y
apt install nginx -y
mkdir -p './data/web_static/shared/'
mkdir -p './data/web_static/releases/test/'
echo '<html><head></head><body>Hello Holberton!</body></html>' > './data/web_static/releases/test/index.html'
ln -sf 'releases/test/' './data/web_static/current'
chown -R ubuntu:ubuntu './data/'
# TODO Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static)
FILE=/etc/nginx/sites-available/default
STATIC_SITE="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}"
sed -i "/^\tserver_name localhost;/a\ $STATIC_SITE" $FILE
service nginx restart

