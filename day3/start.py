from datetime import datetime, timedelta, timezone
import click, time
from pipeline import controller
from fake_data.insert import insert_data

@click.command
@click.option('-d', '--custom-batch-date', type=click.STRING, default='', help='배치작업연월일')
def start_batch(custom_batch_date):
    
    for _ in range(10):
        print("START BATCH")
        insert_data()
        
        if custom_batch_date:
            batch_date = custom_batch_date
        else:
            batch_date = (datetime.now(timezone(timedelta(hours=9))) - timedelta(days = 1)).strftime('%Y%m%d')
            
        controller.main(batch_date)
        time.sleep(5)
        
if __name__ == "__main__":
    
    start_batch()