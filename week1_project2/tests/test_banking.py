import pytest
from src.services import Services
from src.account import Account

@pytest.fixture
def service():
    return Services()

@pytest.fixture
def account(service: Services):
    return service.create_account("Bunny", 29)

def test_withdrawal_not_allowed(service: Services, account: Account):
    service.deposit(account, 300)
    with pytest.raises(ValueError):
        service.withdrawal(account, 500)

@pytest.mark.parametrize(
        "amount", [0, -10]
)
def test_amount_check_validate(service: Services, account: Account, amount: int):
    with pytest.raises(ValueError):
        service.deposit(account, amount)

    service.deposit(account, 1000)
    with pytest.raises(ValueError):
        service.withdrawal(account, amount)

def test_withdrawal_limit(service: Services, account: Account):
    service.deposit(account, 10000)
    with pytest.raises(ValueError):
        service.withdrawal(account, 5500)

def test_age_validator(service: Services):
    with pytest.raises(ValueError):
        service.create_account("Bunny", 15)

def test_account_created_successfully(service: Services):
    account = service.create_account("Saitama", 23)
    assert account.name == "Saitama"

def test_withdrawal_check(service: Services, account: Account):
    service.deposit(account, 100)
    service.withdrawal(account, 50)
    assert account.balance == 50

def test_deposit_check(service: Services, account: Account):
    service.deposit(account, 100)
    assert account.balance == 100

def test_get_balance(service: Services, account: Account):
    service.deposit(account, 400)
    service.withdrawal(account, 150)
    assert account.balance == 250

def test_transaction_list(service: Services, account: Account):
    service.deposit(account, 400)
    service.deposit(account, 400)
    service.withdrawal(account, 150)
    service.deposit(account, 400)
    service.withdrawal(account, 150)
    service.withdrawal(account, 150)
    service.withdrawal(account, 150)
    service.deposit(account, 400)

    assert len(account.transactions) == 8