from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator


class Business(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=600, null=True, blank=False)
    '''
   
    email = fields.CharField(max_length=600, null=True)
    company_name = fields.CharField(max_length=600, null=True)

    address_street_line_number_one = fields.CharField(max_length=600, null=True)
    address_street_line_number_two = fields.CharField(max_length=600, null=True)

    beneficiary_main_language = fields.CharField(max_length=600, null=True)

    client_region = fields.CharField(max_length=600, null=True)
    client_city = fields.CharField(max_length=600, null=True)
    client_country = fields.CharField(max_length=600, null=True)
    client_postcode = fields.CharField(max_length=600, null=True)
    is_approved = fields.BooleanField(default=False, null=True)

    client_owner_first_name = fields.CharField(max_length=600, null=True)
    client_owner_last_name = fields.CharField(max_length=600, null=True)

    business_email = fields.CharField(max_length=200, null=True)
     '''

    class Meta:
        table = "business_management_business"  # django table name


Businesses_pydantic = pydantic_model_creator(Business, name="Business")
