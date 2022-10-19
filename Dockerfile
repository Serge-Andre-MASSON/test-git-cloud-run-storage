FROM python:3.9

EXPOSE 8501

WORKDIR /test-git-cloud-run-storage

RUN pip3 install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "Introduction.py", "--server.port=8501", "--server.address=0.0.0.0"]