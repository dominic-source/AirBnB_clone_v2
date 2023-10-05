#!/usr/bin/env bash
# Deploy code
if ! dpkg -l | grep -qE "^ii\s+nginx\s"
then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi
sudo mkdir -p "/data/web_static/releases/test/"
sudo mkdir -p "/data/web_static/shared/"
content="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
sudo touch "/data/web_static/releases/test/index.html"
sudo echo "$content" | sudo tee "/data/web_static/releases/test/index.html" > "/dev/null"
sudo ln -sf "/data/web_static/releases/test/" "/data/web_static/current"
sudo chown -R ubuntu:ubuntu "/data/"
sudo sed -i "47s|^|\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}|" "/etc/nginx/sites-available/default"
sudo service nginx restart
