FROM python:3
ARG URL
ARG TAGS
ENV ENV_URL=$URL
ENV ENV_TAGS=$TAGS
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "./extractTextFromTags.py"]
#CMD ["-u", ENV_URL, "-t", ENV_TAGS]
#CMD ["${URL}", "${TAGS}"]