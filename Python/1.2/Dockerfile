FROM python:3

ARG URL
ARG TAGS

ENV URL=$URL
ENV TAGS=$TAGS

WORKDIR /usr/src/app

COPY extractFromHTMLTags.py .

RUN pip install BeautifulSoup4 requests
CMD ["python", "extractFromHTMLTags.py", "${URL}", "${TAGS}"]