FROM python:3.10-alpine
ADD server.py .
RUN ls -l
#dobbiamo installare flask
RUN pip install flask
#manca l'html
RUN mkdir templates
ADD ./templates/index.html ./templates
#manca il mapping tra le porte
CMD ["python","./server.py"]