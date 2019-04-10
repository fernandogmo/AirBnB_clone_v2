#!/usr/bin/env bash
# Sets up your web servers for the deployment of `web_static`
apt update -y
apt upgrade -y
apt install nginx -y
mkdir -p '/data/web_static/shared/'
mkdir -p '/data/web_static/releases/test/'
echo '<html><head></head><body>Hello Holberton!</body></html>' > '/data/web_static/releases/test/index.html'
ln -sf 'releases/test/' '/data/web_static/current'
chown -R ubuntu:ubuntu '/data/'
FILE=/etc/nginx/sites-available/default
printf %s "server {
 	add_header X-Served-By $HOSTNAME;
	listen 80 default_server;
	listen [::]:80 default_server ipv6only=on;

	root /usr/share/nginx/html;
	index index.html index.htm;

	# Make site accessible from http://localhost/
	# server_name localhost;

	location /hbnb_static {
		alias /data/web_static/current;
		index index.html index.htm;
	}

	location /redirect_me {
		return 301 https://www.fernando.ai;
	}

	location / {
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		#try_files $uri $uri/ =404;
		# Uncomment to enable naxsi on this location
		# include /etc/nginx/naxsi.rules
	}

	error_page 404 /404.html;

	# redirect server error pages to the static page /50x.html
	#
	#error_page 500 502 503 504 /50x.html;
	#location = /50x.html {
	#	root /usr/share/nginx/html;
	#}
}" > $FILE
service nginx restart
