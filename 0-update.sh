 #!/bin/sh

#docker pull jekyll/jekyll

docker tag jekyll/jekyll jekyll:update
docker run --rm -v /home/erika/thecarboncaudex:/srv/jekyll -p 4000:4000 -it jekyll:update jekyll serve
