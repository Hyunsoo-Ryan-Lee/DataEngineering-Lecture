# 함수 형태로 생성

from faker import Faker
import shortuuid


def create_fake_user():
    
    key_list = ['name', 'job', 'residence', 'blood_group', 'sex', 'birthdate']
    fake = Faker("ko_KR")
    user_data = dict()

    for key in key_list:
        user_data[key] = fake.profile()[key]
        
        if key == 'birthdate':
            user_data[key] = str(fake.profile()[key].year) + str(fake.profile()[key].month).zfill(2) + str(fake.profile()[key].day).zfill(2)

    user_data['uuid'] = shortuuid.uuid()
    
    return user_data