FROM debian:latest
RUN apt-get update && apt-get install curl -y 
WORKDIR /partyou
VOLUME /partyou
ENV SITE_TESTE https://partyou.com.br/
CMD sh -c "curl -Lk $SITE_TESTE > /partyou/site" 
