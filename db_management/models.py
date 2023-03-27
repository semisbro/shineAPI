from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator


class Business(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=600, null=True)

    logo = fields.CharField(max_length=600, null=True)
    business_preview_image = fields.CharField(max_length=255, null=True)

    public_description = fields.CharField(max_length=4000, null=True)
    longitude = fields.DecimalField(max_digits=9, decimal_places=6, null=True)
    latitude = fields.DecimalField(max_digits=9, decimal_places=6, null=True)

    amount_of_reviews = fields.IntField(default=0, null=True)

    category_name = fields.CharField(max_length=600, null=True)

    #business_user = fields.ForeignKeyField("models.BusinessUser", null=True, on_delete=fields.SET_NULL)

    used_languages = fields.CharField(max_length=600, null=True)

    avg_star_review_score = fields.FloatField(null=True)




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
