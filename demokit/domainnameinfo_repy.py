# -*- coding: utf-8 -*-
### Automatically generated by repyhelper.py ### /Users/tomashasselquist/git/tda596/demokit/domainnameinfo.repy

### THIS FILE WILL BE OVERWRITTEN!
### DO NOT MAKE CHANGES HERE, INSTEAD EDIT THE ORIGINAL SOURCE FILE
###
### If changes to the src aren't propagating here, try manually deleting this file. 
### Deleting this file forces regeneration of a repy translation


from repyportability import *
import repyhelper
mycontext = repyhelper.get_shared_context()
callfunc = 'import'
callargs = []

"""
Author: Justin Cappos

Module: A module that gives info about IP addresses.

Start date: August 7th, 2009

"""

class UnknownHostLocationError(Exception):
  """An exception to indicate we don't know the host's location"""

def domainnameinfo_gethostlocation(hostname):
  """
  <Purpose>
    Given a hostname, returns a string that contains the country the
    hostname is from.

  <Arguments>
    hostname:
      a hostname string that we want information about.   For example:
      'planetlab-2.di.fc.ul.pt'

  <Exceptions>
    UnknownHostLocationError: if we don't know the location of the hostname.
    TypeError if hostname isn't a string.

  <Side Effects>
    None.

  <Returns>
    The string that contains country information
  """
  if type(hostname) != str:
    raise TypeError("domainnameinfo_gethostlocation must be passed a string")

  for domainnameextension in _domainlistmap:
    if hostname.endswith(domainnameextension):
      return _domainlistmap[domainnameextension]

  raise UnknownHostLocationError("The location of hostname '"+hostname+"' cannot be determined.")



_domainlistmap = {
 '.ac': 'Ascension Island', 
 '.ad': 'Andorra', 
 '.ae': 'United Arab Emirates', 
 '.af': 'Afghanistan', 
 '.ag': 'Antigua and Barbuda', 
 '.ai': 'Anguilla', 
 '.al': 'Albania', 
 '.am': 'Armenia', 
 '.an': 'Netherlands Antilles', 
 '.ao': 'Angola', 
 '.aq': 'Antarctica', 
 '.ar': 'Argentina', 
 '.as': 'American Samoa', 
 '.at': 'Austria', 
 '.au': 'Australia', 
 '.aw': 'Aruba', 
 '.ax': 'Aland Islands',  # The 'A' is a special character we don't support
 '.az': 'Azerbaijan', 
 '.ba': 'Bosnia and Herzegovina', 
 '.bb': 'Barbados', 
 '.bd': 'Bangladesh', 
 '.be': 'Belgium', 
 '.bf': 'Burkina Faso', 
 '.bg': 'Bulgaria', 
 '.bh': 'Bahrain', 
 '.bi': 'Burundi', 
 '.bj': 'Benin', 
 '.bm': 'Bermuda', 
 '.bn': 'Brunei Darussalam', 
 '.bo': 'Bolivia', 
 '.br': 'Brazil', 
 '.bs': 'Bahamas', 
 '.bt': 'Bhutan', 
 '.bv': 'Bouvet Island', 
 '.bw': 'Botswana', 
 '.by': 'Belarus', 
 '.bz': 'Belize', 
 '.ca': 'Canada', 
 '.cc': 'Cocos (Keeling) Islands', 
 '.cd': 'Congo, Democratic republic of the (former Zaire)', 
 '.cf': 'Central African Republic', 
 '.cg': 'Congo, Republic of', 
 '.ch': 'Switzerland', 
 '.ci': "Cote d'Ivoire",   # The 'o' is a special character we don't support
 '.ck': 'Cook Islands', 
 '.cl': 'Chile', 
 '.cm': 'Cameroon', 
 '.cn': 'China', 
 '.co': 'Colombia', 
 '.cr': 'Costa Rica', 
 '.cs': 'Czechoslovakia (former - non-existing)', 
 '.cu': 'Cuba', 
 '.cv': 'Cape Verde', 
 '.cx': 'Christmas Island', 
 '.cy': 'Cyprus', 
 '.cz': 'Czech Republic', 
 '.de': 'Germany', 
 '.dj': 'Djibouti', 
 '.dk': 'Denmark', 
 '.dm': 'Dominica', 
 '.do': 'Dominican Republic', 
 '.dz': 'Algeria', 
 '.ec': 'Ecuador', 
 '.ee': 'Estonia', 
 '.eg': 'Egypt', 
 '.eh': 'Western Sahara', 
 '.er': 'Eritrea', 
 '.es': 'Spain', 
 '.et': 'Ethiopia', 
 '.eu': 'European Union', 
 '.fi': 'Finland', 
 '.fj': 'Fiji', 
 '.fk': 'Falkland Islands', 
 '.fm': 'Micronesia', 
 '.fo': 'Faroe Islands', 
 '.fr': 'France', 
 '.ga': 'Gabon', 
 '.gb': 'United Kingdom', 
 '.gd': 'Grenada', 
 '.ge': 'Georgia', 
 '.gf': 'French Guiana', 
 '.gg': 'Guernsey', 
 '.gh': 'Ghana', 
 '.gi': 'Gibraltar', 
 '.gl': 'Greenland', 
 '.gm': 'Gambia', 
 '.gn': 'Guinea', 
 '.gp': 'Guadeloupe', 
 '.gq': 'Equatorial Guinea', 
 '.gr': 'Greece', 
 '.gs': 'South Georgia and the South Sandwich Islands', 
 '.gt': 'Guatemala', 
 '.gu': 'Guam', 
 '.gw': 'Guinea-Bissau', 
 '.gy': 'Guyana', 
 '.hk': 'Hong Kong', 
 '.hm': 'Heard and McDonald Islands', 
 '.hn': 'Honduras', 
 '.hr': 'Croatia', 
 '.ht': 'Haiti', 
 '.hu': 'Hungary', 
 '.id': 'Indonesia', 
 '.ie': 'Ireland', 
 '.il': 'Israel', 
 '.im': 'Isle of Man', 
 '.in': 'India', 
 '.io': 'British Indian Ocean Territory', 
 '.iq': 'Iraq', 
 '.ir': 'Iran', 
 '.is': 'Iceland', 
 '.it': 'Italia', 
 '.je': 'Jersey', 
 '.jm': 'Jamaica', 
 '.jo': 'Jordan', 
 '.jp': 'Japan', 
 '.ke': 'Kenya', 
 '.kg': 'Kyrgyzstan', 
 '.kh': 'Cambodia', 
 '.ki': 'Kiribati', 
 '.km': 'Comoros', 
 '.kn': 'Saint Kitts and Nevis', 
 '.kp': 'Korea, Democratic Peoples Republic of', 
 '.kr': 'Korea, Republic of', 
 '.kw': 'Kuwait', 
 '.ky': 'Cayman Islands', 
 '.kz': 'Kazakhstan', 
 '.la': "Lao People's Democratic Republic", 
 '.lb': 'Lebanon', 
 '.lc': 'Saint Lucia', 
 '.li': 'Liechtenstein', 
 '.lk': 'Sri Lanka', 
 '.lr': 'Liberia', 
 '.ls': 'Lesotho', 
 '.lt': 'Lithuania', 
 '.lu': 'Luxembourg', 
 '.lv': 'Latvia', 
 '.ly': 'Libyan Arab Jamahiriya', 
 '.ma': 'Morocco', 
 '.mc': 'Monaco', 
 '.md': 'Moldova', 
 '.me': 'Montenegro', 
 '.mg': 'Madagascar', 
 '.mh': 'Marshall Islands', 
 '.mk': 'Macedonia', 
 '.ml': 'Mali', 
 '.mm': 'Myanmar', 
 '.mn': 'Mongolia', 
 '.mo': 'Macau', 
 '.mp': 'Northern Mariana Islands', 
 '.mq': 'Martinique', 
 '.mr': 'Mauritania', 
 '.ms': 'Montserrat', 
 '.mt': 'Malta', 
 '.mu': 'Mauritius', 
 '.mv': 'Maldives', 
 '.mw': 'Malawi', 
 '.mx': 'Mexico', 
 '.my': 'Malaysia', 
 '.mz': 'Mozambique', 
 '.na': 'Namibia', 
 '.nc': 'New Caledonia', 
 '.ne': 'Niger', 
 '.nf': 'Norfolk Island', 
 '.ng': 'Nigeria', 
 '.ni': 'Nicaragua', 
 '.nl': 'The Netherlands', 
 '.no': 'Norway', 
 '.np': 'Nepal', 
 '.nr': 'Nauru', 
 '.nu': 'Niue', 
 '.nz': 'New Zealand', 
 '.om': 'Oman', 
 '.pa': 'Panama', 
 '.pe': 'Peru', 
 '.pf': 'French Polynesia', 
 '.pg': 'Papua New Guinea', 
 '.ph': 'Philippines', 
 '.pk': 'Pakistan', 
 '.pl': 'Poland', 
 '.pm': 'St. Pierre and Miquelon', 
 '.pn': 'Pitcairn', 
 '.pr': 'Puerto Rico', 
 '.ps': 'Palestine', 
 '.pt': 'Portugal', 
 '.pw': 'Palau', 
 '.py': 'Paraguay', 
 '.qa': 'Qatar', 
 '.re': 'Reunion', 
 '.ro': 'Romania', 
 '.rs': 'Serbia', 
 '.ru': 'Russia', 
 '.rw': 'Rwanda', 
 '.sa': 'Saudi Arabia', 
 '.sb': 'Solomon Islands', 
 '.sc': 'Seychelles', 
 '.sd': 'Sudan', 
 '.se': 'Sweden', 
 '.sg': 'Singapore', 
 '.sh': 'St. Helena', 
 '.si': 'Slovenia', 
 '.sj': 'Svalbard and Jan Mayen Islands', 
 '.sk': 'Slovakia', 
 '.sl': 'Sierra Leone', 
 '.sm': 'San Marino', 
 '.sn': 'Senegal', 
 '.so': 'Somalia', 
 '.sr': 'Surinam', 
 '.st': 'Sao Tome and Principe', 
 '.su': 'USSR (former)', 
 '.sv': 'El Salvador', 
 '.sy': 'Syrian Arab Republic', 
 '.sz': 'Swaziland', 
 '.tc': 'The Turks and Caicos Islands', 
 '.td': 'Chad', 
 '.tf': 'French Southern Territories', 
 '.tg': 'Togo', 
 '.th': 'Thailand', 
 '.tj': 'Tajikistan', 
 '.tk': 'Tokelau', 
 '.tl': 'Timor-Leste', 
 '.tm': 'Turkmenistan', 
 '.tn': 'Tunisia', 
 '.to': 'Tonga', 
 '.tp': 'East Timor', 
 '.tr': 'Turkey', 
 '.tt': 'Trinidad and Tobago', 
 '.tv': 'Tuvalu', 
 '.tw': 'Taiwan', 
 '.tz': 'Tanzania', 
 '.ua': 'Ukraine', 
 '.ug': 'Uganda', 
 '.uk': 'United Kingdom', 
 '.um': 'United States Minor Outlying Islands', 
 '.us': 'United States', 
 '.uy': 'Uruguay', 
 '.uz': 'Uzbekistan', 
 '.va': 'Holy See (Vatican City State)', 
 '.vc': 'Saint Vincent and the Grenadines', 
 '.ve': 'Venezuela', 
 '.vg': 'Virgin Islands British', 
 '.vi': 'Virgin Islands U.S', 
 '.vn': 'Vietnam', 
 '.vu': 'Vanuatu', 
 '.wf': 'Wallis and Futuna Islands', 
 '.ws': 'Samoa', 
 '.ye': 'Yemen', 
 '.yt': 'Mayotte', 
 '.yu': 'Yugoslavia', 
 '.za': 'South Africa', 
 '.zm': 'Zambia', 
 '.zr': 'Zaire (non-existent, see Congo)', 
 '.zw': 'Zimbabwe'}

### Automatically generated by repyhelper.py ### /Users/tomashasselquist/git/tda596/demokit/domainnameinfo.repy
