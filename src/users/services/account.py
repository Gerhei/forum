from django.core.exceptions import ObjectDoesNotExist

from src.common.exceptions.domain_exceptions import EntityNotFound
from src.users.models import Account


class AccountService:
    @classmethod
    def get_account(cls, slug: str) -> Account:
        try:
            account = Account.objects.get(slug=slug)
        except ObjectDoesNotExist:
            raise EntityNotFound('Account not found.')
        return account

    @classmethod
    def update_account(cls, account: Account, description: str) -> Account:
        account.description = description
        account.save()
        return account
