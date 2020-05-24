FROM joyzoursky/python-chromedriver:3.7

COPY docker-python-chromedriver/data/Liste_mails_retargeting.xlsx ./Liste_mails_retargeting.xlsx

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python","docker-python-chromedriver/start_insta_scraping.py"]

