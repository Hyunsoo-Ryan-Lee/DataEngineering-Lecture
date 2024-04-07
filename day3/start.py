import click, random, time
from controller import main
from datetime import datetime, timedelta
from fakedata.create import create_fakedataframe
from fakedata.insert import insert_fakedataframe

@click.command()
@click.option('-s', '--batch_date', default="")
def start_pipeline(batch_date: str) -> None:
    
    if not batch_date: # batch_date 값이 들어옴
        _date = datetime.now() - timedelta(days=1)
        batch_date = _date.strftime("%Y%m%d")
    
    for _ in range(30):
        count = random.randint(5,15)
        print(f"========={count}개의 row가 삽입됩니다.=========")
        ### fake data에 대한 dataframe 생성 ###
        fake_df = create_fakedataframe(count) 
        
        ### fake dataframe -> postgresql 저장
        insert_fakedataframe(fake_df)
        
        main(batch_date)
        
        time.sleep(3)
    
    
if __name__ == "__main__":
    start_pipeline()