FROM python:3
ARG URL
ARG TAGS
ENV URL=$URL
ENV TAGS=$TAGS
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "./extractTextFromTags.py" ]
#CMD ["python", "extractFromHTMLTags.py", "${URL}", "${TAGS}"]