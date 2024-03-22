import click, time
from datetime import datetime, timedelta, timezone
from controller import main
from fake_user.insert import insert_fake_dataframe

@click.command()
@click.option('-s', '--custom_batch_date')
def start_pipeline(custom_batch_date):
    print("START PIPELINE!!!")
    
    if custom_batch_date:
        batch_date = custom_batch_date
    else:
        batch_date = (datetime.now(timezone(timedelta(hours=9))) - timedelta(days = 1)).strftime('%Y%m%d')

    main(batch_date)
    for _ in range(30):
        insert_fake_dataframe()
        main(batch_date)
        time.sleep(5)

if __name__ == "__main__":
    start_pipeline()