from faker import Faker
import shortuuid
import pandas as pd


def create_fake_dataframe(n: int):
    datas = [create_fake_user() for _ in range(n)]

    df = pd.DataFrame(datas)

    return df

def create_fake_user():
    key_list = ['name', 'ssn', 'job', 'residence', 'blood_group', 'sex', 'birthdate']
    fake = Faker("ko_KR")
    data = fake.profile()

    data_dict = dict()

    for key in key_list:
        
        data_dict[key] = data[key]

        if key == "birthdate": 
            data_dict[key] = data[key].strftime("%Y%m%d")
    
    data_dict['uuid'] = shortuuid.uuid()

    return data_dict