#!/usr/bin/env bash
#Prepare web servers for deployment

sudo apt-get update

sudo apt-get install -y nginx

sudo mkdir -p /data/web_static/releases/test/

sudo mkdir -p /data/web_static/shared/

sudo touch /data/web_static/releases/test/index.html

cat > /data/web_static/releases/test/index.html << EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

sudo rm -f /data/web_static/current

sudo ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu: /data/

#echo "
#server {
#	location /hbnb_static/ {
#		alias /data/web_static/current/;
#	}
#}" >> /etc/nginx/sites-available/default

sudo service nginx reload
