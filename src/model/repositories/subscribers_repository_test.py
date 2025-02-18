import pytest
from .subscribers_repository import SubscribersRepository

@pytest.mark.skip("Insert in DB")
def test_insert():
    subscribers_info = {
        "name" : "meuNome222",
        "email" : "email222@email.com",
        "evento_id" : 2
    }
    subs_repo = SubscribersRepository()
    subs_repo.insert(subscribers_info)
 
@pytest.mark.skip("Select in DB")   
def test_select():
    email ="email@email.com"
    evento_id = 444
    subs_repo = SubscribersRepository()
    res = subs_repo.select_subscriber(email, evento_id)
    print(res.nome)