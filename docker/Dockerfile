FROM pandoc/latex:2.11.4

RUN apk add --no-cache \
            --update \
            --repository=http://dl-cdn.alpinelinux.org/alpine/edge/community \
            inkscape=1.0-r1 \
            python3=3.8.5-r1 \
            py3-pip=20.1.1-r0 \
            git=2.26.2-r0

RUN tlmgr update --self && tlmgr install standalone

RUN pip install git+https://github.com/kacperkan/drawio2pdf/

WORKDIR "/app"

ENTRYPOINT ["drawio2pdf"]
CMD ["--help"]
