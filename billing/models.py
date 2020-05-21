import stripe
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save

stripe.api_key = settings.STRIPE_API_KEY
User = get_user_model()


class BillingProfileManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter()


class BillingProfile(models.Model):
    class CountriesChoises(models.TextChoices):
        AF = 'AF', 'Afghanistan'
        AX = 'AX', 'Åland Islands'
        AL = 'AL', 'Albania'
        DZ = 'DZ', 'Algeria'
        AS = 'AS', 'American Samoa'
        AD = 'AD', 'Andorra'
        AO = 'AO', 'Angola'
        AI = 'AI', 'Anguilla'
        AQ = 'AQ', 'Antarctica'
        AG = 'AG', 'Antigua and Barbuda'
        AR = 'AR', 'Argentina'
        AM = 'AM', 'Armenia'
        AW = 'AW', 'Aruba'
        AU = 'AU', 'Australia'
        AT = 'AT', 'Austria'
        AZ = 'AZ', 'Azerbaijan'
        BS = 'BS', 'Bahamas'
        BH = 'BH', 'Bahrain'
        BD = 'BD', 'Bangladesh'
        BB = 'BB', 'Barbados'
        BY = 'BY', 'Belarus'
        BE = 'BE', 'Belgium'
        BZ = 'BZ', 'Belize'
        BJ = 'BJ', 'Benin'
        BM = 'BM', 'Bermuda'
        BT = 'BT', 'Bhutan'
        BO = 'BO', 'Bolivia (Plurinational State of)'
        BQ = 'BQ', 'Bonaire, Sint Eustatius and Saba'
        BA = 'BA', 'Bosnia and Herzegovina'
        BW = 'BW', 'Botswana'
        BV = 'BV', 'Bouvet Island'
        BR = 'BR', 'Brazil'
        IO = 'IO', 'British Indian Ocean Territory'
        UM = 'UM', 'United States Minor Outlying Islands'
        VG = 'VG', 'Virgin Islands (British)'
        VI = 'VI', 'Virgin Islands (U.S.)'
        BN = 'BN', 'Brunei Darussalam'
        BG = 'BG', 'Bulgaria'
        BF = 'BF', 'Burkina Faso'
        BI = 'BI', 'Burundi'
        KH = 'KH', 'Cambodia'
        CM = 'CM', 'Cameroon'
        CA = 'CA', 'Canada'
        CV = 'CV', 'Cabo Verde'
        KY = 'KY', 'Cayman Islands'
        CF = 'CF', 'Central African Republic'
        TD = 'TD', 'Chad'
        CL = 'CL', 'Chile'
        CN = 'CN', 'China'
        CX = 'CX', 'Christmas Island'
        CC = 'CC', 'Cocos (Keeling) Islands'
        CO = 'CO', 'Colombia'
        KM = 'KM', 'Comoros'
        CG = 'CG', 'Congo'
        CD = 'CD', 'Congo (Democratic Republic of the)'
        CK = 'CK', 'Cook Islands'
        CR = 'CR', 'Costa Rica'
        HR = 'HR', 'Croatia'
        CU = 'CU', 'Cuba'
        CW = 'CW', 'Curaçao'
        CY = 'CY', 'Cyprus'
        CZ = 'CZ', 'Czech Republic'
        DK = 'DK', 'Denmark'
        DJ = 'DJ', 'Djibouti'
        DM = 'DM', 'Dominica'
        DO = 'DO', 'Dominican Republic'
        EC = 'EC', 'Ecuador'
        EG = 'EG', 'Egypt'
        SV = 'SV', 'El Salvador'
        GQ = 'GQ', 'Equatorial Guinea'
        ER = 'ER', 'Eritrea'
        EE = 'EE', 'Estonia'
        ET = 'ET', 'Ethiopia'
        FK = 'FK', 'Falkland Islands (Malvinas)'
        FO = 'FO', 'Faroe Islands'
        FJ = 'FJ', 'Fiji'
        FI = 'FI', 'Finland'
        FR = 'FR', 'France'
        GF = 'GF', 'French Guiana'
        PF = 'PF', 'French Polynesia'
        TF = 'TF', 'French Southern Territories'
        GA = 'GA', 'Gabon'
        GM = 'GM', 'Gambia'
        GE = 'GE', 'Georgia'
        DE = 'DE', 'Germany'
        GH = 'GH', 'Ghana'
        GI = 'GI', 'Gibraltar'
        GR = 'GR', 'Greece'
        GL = 'GL', 'Greenland'
        GD = 'GD', 'Grenada'
        GP = 'GP', 'Guadeloupe'
        GU = 'GU', 'Guam'
        GT = 'GT', 'Guatemala'
        GG = 'GG', 'Guernsey'
        GN = 'GN', 'Guinea'
        GW = 'GW', 'Guinea-Bissau'
        GY = 'GY', 'Guyana'
        HT = 'HT', 'Haiti'
        HM = 'HM', 'Heard Island and McDonald Islands'
        VA = 'VA', 'Holy See'
        HN = 'HN', 'Honduras'
        HK = 'HK', 'Hong Kong'
        HU = 'HU', 'Hungary'
        IS = 'IS', 'Iceland'
        IN = 'IN', 'India'
        ID = 'ID', 'Indonesia'
        CI = 'CI', "Côte d'Ivoire"
        IR = 'IR', 'Iran (Islamic Republic of)'
        IQ = 'IQ', 'Iraq'
        IE = 'IE', 'Ireland'
        IM = 'IM', 'Isle of Man'
        IL = 'IL', 'Israel'
        IT = 'IT', 'Italy'
        JM = 'JM', 'Jamaica'
        JP = 'JP', 'Japan'
        JE = 'JE', 'Jersey'
        JO = 'JO', 'Jordan'
        KZ = 'KZ', 'Kazakhstan'
        KE = 'KE', 'Kenya'
        KI = 'KI', 'Kiribati'
        KW = 'KW', 'Kuwait'
        KG = 'KG', 'Kyrgyzstan'
        LA = 'LA', "Lao People's Democratic Republic"
        LV = 'LV', 'Latvia'
        LB = 'LB', 'Lebanon'
        LS = 'LS', 'Lesotho'
        LR = 'LR', 'Liberia'
        LY = 'LY', 'Libya'
        LI = 'LI', 'Liechtenstein'
        LT = 'LT', 'Lithuania'
        LU = 'LU', 'Luxembourg'
        MO = 'MO', 'Macao'
        MK = 'MK', 'Macedonia (the former Yugoslav Republic of)'
        MG = 'MG', 'Madagascar'
        MW = 'MW', 'Malawi'
        MY = 'MY', 'Malaysia'
        MV = 'MV', 'Maldives'
        ML = 'ML', 'Mali'
        MT = 'MT', 'Malta'
        MH = 'MH', 'Marshall Islands'
        MQ = 'MQ', 'Martinique'
        MR = 'MR', 'Mauritania'
        MU = 'MU', 'Mauritius'
        YT = 'YT', 'Mayotte'
        MX = 'MX', 'Mexico'
        FM = 'FM', 'Micronesia (Federated States of)'
        MD = 'MD', 'Moldova (Republic of)'
        MC = 'MC', 'Monaco'
        MN = 'MN', 'Mongolia'
        ME = 'ME', 'Montenegro'
        MS = 'MS', 'Montserrat'
        MA = 'MA', 'Morocco'
        MZ = 'MZ', 'Mozambique'
        MM = 'MM', 'Myanmar'
        NA = 'NA', 'Namibia'
        NR = 'NR', 'Nauru'
        NP = 'NP', 'Nepal'
        NL = 'NL', 'Netherlands'
        NC = 'NC', 'New Caledonia'
        NZ = 'NZ', 'New Zealand'
        NI = 'NI', 'Nicaragua'
        NE = 'NE', 'Niger'
        NG = 'NG', 'Nigeria'
        NU = 'NU', 'Niue'
        NF = 'NF', 'Norfolk Island'
        KP = 'KP', "Korea (Democratic People's Republic of)"
        MP = 'MP', 'Northern Mariana Islands'
        NO = 'NO', 'Norway'
        OM = 'OM', 'Oman'
        PK = 'PK', 'Pakistan'
        PW = 'PW', 'Palau'
        PS = 'PS', 'Palestine, State of'
        PA = 'PA', 'Panama'
        PG = 'PG', 'Papua New Guinea'
        PY = 'PY', 'Paraguay'
        PE = 'PE', 'Peru'
        PH = 'PH', 'Philippines'
        PN = 'PN', 'Pitcairn'
        PL = 'PL', 'Poland'
        PT = 'PT', 'Portugal'
        PR = 'PR', 'Puerto Rico'
        QA = 'QA', 'Qatar'
        XK = 'XK', 'Republic of Kosovo'
        RE = 'RE', 'Réunion'
        RO = 'RO', 'Romania'
        RU = 'RU', 'Russian Federation'
        RW = 'RW', 'Rwanda'
        BL = 'BL', 'Saint Barthélemy'
        SH = 'SH', 'Saint Helena, Ascension and Tristan da Cunha'
        KN = 'KN', 'Saint Kitts and Nevis'
        LC = 'LC', 'Saint Lucia'
        MF = 'MF', 'Saint Martin (French part)'
        PM = 'PM', 'Saint Pierre and Miquelon'
        VC = 'VC', 'Saint Vincent and the Grenadines'
        WS = 'WS', 'Samoa'
        SM = 'SM', 'San Marino'
        ST = 'ST', 'Sao Tome and Principe'
        SA = 'SA', 'Saudi Arabia'
        SN = 'SN', 'Senegal'
        RS = 'RS', 'Serbia'
        SC = 'SC', 'Seychelles'
        SL = 'SL', 'Sierra Leone'
        SG = 'SG', 'Singapore'
        SX = 'SX', 'Sint Maarten (Dutch part)'
        SK = 'SK', 'Slovakia'
        SI = 'SI', 'Slovenia'
        SB = 'SB', 'Solomon Islands'
        SO = 'SO', 'Somalia'
        ZA = 'ZA', 'South Africa'
        GS = 'GS', 'South Georgia and the South Sandwich Islands'
        KR = 'KR', 'Korea (Republic of)'
        SS = 'SS', 'South Sudan'
        ES = 'ES', 'Spain'
        LK = 'LK', 'Sri Lanka'
        SD = 'SD', 'Sudan'
        SR = 'SR', 'Suriname'
        SJ = 'SJ', 'Svalbard and Jan Mayen'
        SZ = 'SZ', 'Swaziland'
        SE = 'SE', 'Sweden'
        CH = 'CH', 'Switzerland'
        SY = 'SY', 'Syrian Arab Republic'
        TW = 'TW', 'Taiwan'
        TJ = 'TJ', 'Tajikistan'
        TZ = 'TZ', 'Tanzania, United Republic of'
        TH = 'TH', 'Thailand'
        TL = 'TL', 'Timor-Leste'
        TG = 'TG', 'Togo'
        TK = 'TK', 'Tokelau'
        TO = 'TO', 'Tonga'
        TT = 'TT', 'Trinidad and Tobago'
        TN = 'TN', 'Tunisia'
        TR = 'TR', 'Turkey'
        TM = 'TM', 'Turkmenistan'
        TC = 'TC', 'Turks and Caicos Islands'
        TV = 'TV', 'Tuvalu'
        UG = 'UG', 'Uganda'
        UA = 'UA', 'Ukraine'
        AE = 'AE', 'United Arab Emirates'
        GB = 'GB', 'United Kingdom of Great Britain and Northern Ireland'
        US = 'US', 'United States of America'
        UY = 'UY', 'Uruguay'
        UZ = 'UZ', 'Uzbekistan'
        VU = 'VU', 'Vanuatu'
        VE = 'VE', 'Venezuela (Bolivarian Republic of)'
        VN = 'VN', 'Viet Nam'
        WF = 'WF', 'Wallis and Futuna'
        EH = 'EH', 'Western Sahara'
        YE = 'YE', 'Yemen'
        ZM = 'ZM', 'Zambia'
        ZW = 'ZW', 'Zimbabwe'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country_code = models.CharField(
        choices=CountriesChoises.choices, max_length=2, default=CountriesChoises.IN)
    pincode = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    stripe_customer_id = models.CharField(
        max_length=100, blank=True, null=True)

    objects = BillingProfileManager()

    def __str__(self):
        return self.email

    @property
    def country(self):
        return self.CountriesChoises(self.country_code).label


def billing_profile_created_receiver(sender, instance: BillingProfile, created, *args, **kwargs):
    if created:
        customer = stripe.Customer.create(
            name=instance.name,
            email=instance.email,
            address={
                "line1": instance.address_line_1,
                "line2": instance.address_line_2,
                "city": instance.city,
                "state": instance.state,
                "country": instance.country_code,
                "postal_code": instance.pincode
            })
        instance.stripe_customer_id = customer.stripe_id
        instance.save()
    else:
        customer = stripe.Customer.modify(
            instance.stripe_customer_id,
            name=instance.name,
            email=instance.email,
            address={
                "line1": instance.address_line_1,
                "line2": instance.address_line_2,
                "city": instance.city,
                "state": instance.state,
                "country": instance.country_code,
                "postal_code": instance.pincode
            })


post_save.connect(billing_profile_created_receiver, sender=BillingProfile)
