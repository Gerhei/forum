from django.core.exceptions import ObjectDoesNotExist

from src.common.exceptions.domain_exceptions import EntityNotFound, AccessError
from src.users.models import Account


class AccountService:
    def get_account(self, slug: str) -> Account:
        try:
            account = Account.objects.get(slug=slug)
        except ObjectDoesNotExist:
            raise EntityNotFound('Account not found.')
        return account

    def update_account(self, slug: str, description: str, user) -> Account:
        try:
            account = Account.objects.get(slug=slug)
        except ObjectDoesNotExist:
            raise EntityNotFound('Account not found.')
        if not account.user == user:
            raise AccessError('This account can\'t be edited because you are not it is owner.')
        account.description = description
        account.save()
        return account
