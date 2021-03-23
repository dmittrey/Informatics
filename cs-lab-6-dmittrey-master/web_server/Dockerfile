FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install apache2 -y

RUN mkdir -p /var/www/html
WORKDIR /var/www/html
RUN printf "<html>\n<head>\n\t<title> I love Docker! </title>\n</head>\n<body>\n\t<p> Hello world! I'm Dmitry Zubakhin and I study at ITMO University! </p>\n</body>\n</html>" > index.html


EXPOSE 80
