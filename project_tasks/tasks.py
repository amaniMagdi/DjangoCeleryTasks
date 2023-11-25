#import celery instance
from project.celery import app


#task decorator used for scheduled tasks
@app.task
def send_scheduled_emails():
    pass
    

