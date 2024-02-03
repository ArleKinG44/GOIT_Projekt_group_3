FROM python:3.10
ENV ASSISTANT /Users/anastasia/Desktop/Projects/GOIT_Projekt_group_3-1
WORKDIR /Users/anastasia/Desktop/Projects/GOIT_Projekt_group_3-1
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python", "main.py"]