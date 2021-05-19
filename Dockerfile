FROM priiiiyo/priiiiyo-mirror-bot:ubuntu

WORKDIR /usr/src/app
COPY . .

CMD ["bash","start.sh"]

