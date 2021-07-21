import regex as regex
from django.core.exceptions import ValidationError


class Validators:
    """
    Check Validation of the All the Input Values
    """

    __phone_pattern = r"^(09)([0-9]{9})$"
    __email_pattern = r"^([\w\.\_\-]+)[@]([\w\.\_\-]*\w)[.]([A-Za-z]{2,3})$"
    __password_pattern = r"^([^ ]{8,})$"

    @classmethod
    def check_phone(cls, phone_number: str):
        """
        Check Validation of Phone Number and Return Boolean Value
        Example Valid Number: 09123456789(Start with 09 length 11)
        """
        if not bool(regex.search(cls.__phone_pattern, phone_number)):
            raise ValidationError

    @classmethod
    def check_email(cls, email_address: str):
        """
        Check Validation of Email Address and Return Boolean Value
        Example Valid Address: Username@domain.com
        """
        if not bool(regex.search(cls.__email_pattern, email_address)):
            raise ValidationError

    @classmethod
    def check_password(cls, password: str):
        """
        Check Validation of Password and Return Boolean Value
        Example Password: abcd1234...(minimum length 8 without space)
        """

        if not bool(regex.search(cls.__password_pattern, password)):
            raise ValidationError
