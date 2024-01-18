year = [
    1962,
    1963,
    1964,
    1965,
    1966,
    1967,
    1968,
    1969,
    1970,
    1971,
    1972,
    1973,
    1974,
    1975,
    1976,
    1977,
    1978,
    1979,
    1980,
    1981,
    1982,
    1983,
    1984,
    1985,
    1986,
    1987,
    1988,
    1989,
    1990,
    1991,
    1992,
    1993,
    1994,
    1995,
    1996,
    1997,
    1998,
    1999,
    2000,
    2001,
    2002,
    2003,
    2004,
    2005,
    2006,
    2007,
    2008,
    2009,
    2010,
    2011,
    2012,
    2013,
    2014,
    2015,
    2016,
    2017,
    2018,
    2019,
    2020,
    2021,
    2022,
    2023,
    2024,
    ]

countries = {
    "Afghanistan":4,
    "Albania":8,
    "Antarctica":10,
    "Algeria":12,
    "American Samoa":16,
    "Andorra":20,
    "Angola":24,
    "Antigua and Barbuda":28,
    "Azerbaijan":31,
    "Argentina":32,
    "Australia":36,
    "Austria":40,
    "Bahamas":44,
    "Bahrain":48,
    "Bangladesh":50,
    "Armenia":51,
    "Barbados":52,
    "Belgium":56,
    "Bermuda":60,
    "Bhutan":64,
    "Bolivia (Plurinational State of)":68,
    "Bosnia and Herzegovina":70,
    "Botswana":72,
    "Bouvet Island":74,
    "Brazil":76,
    "Belize":84,
    "British Indian Ocean Territory":86,
    "Solomon Islands":90,
    "British Virgin Islands":92,
    "Brunei Darussalam":96,
    "Bulgaria":100,
    "Myanmar":104,
    "Burundi":108,
    "Belarus":112,
    "Cambodia":116,
    "Cameroon":120,
    "Canada":124,
    "Cabo Verde":132,
    "Cayman Islands":136,
    "Central African Republic":140,
    "Sri Lanka":144,
    "Chad":148,
    "Chile":152,
    "China":156,
    "Christmas Island":162,
    "Cocos (Keeling) Islands":166,
    "Colombia":170,
    "Comoros":174,
    "Mayotte":175,
    "Congo":178,
    "Democratic Republic of the Congo":180,
    "Cook Islands":184,
    "Costa Rica":188,
    "Croatia":191,
    "Cuba":192,
    "Cyprus":196,
    "Czechia":203,
    "Benin":204,
    "Denmark":208,
    "Dominica":212,
    "Dominican Republic":214,
    "Ecuador":218,
    "El Salvador":222,
    "Equatorial Guinea":226,
    "Ethiopia":231,
    "Eritrea":232,
    "Estonia":233,
    "Faroe Islands":234,
    "Falkland Islands (Malvinas)":238,
    "South Georgia and the South Sandwich Islands":239,
    "Fiji":242,
    "Finland":246,
    "Åland Islands":248,
    "France":250,
    "French Guiana":254,
    "French Polynesia":258,
    "French Southern Territories":260,
    "Djibouti":262,
    "Gabon":266,
    "Georgia":268,
    "Gambia":270,
    "State of Palestine":275,
    "Germany":276,
    "Ghana":288,
    "Gibraltar":292,
    "Kiribati":296,
    "Greece":300,
    "Greenland":304,
    "Grenada":308,
    "Guadeloupe":312,
    "Guam":316,
    "Guatemala":320,
    "Guinea":324,
    "Guyana":328,
    "Haiti":332,
    "Heard Island and McDonald Islands":334,
    "Holy See":336,
    "Honduras":340,
    "China, Hong Kong Special Administrative Region":344,
    "Hungary":348,
    "Iceland":352,
    "India":356,
    "Indonesia":360,
    "Iran (Islamic Republic of)":364,
    "Iraq":368,
    "Ireland":372,
    "Israel":376,
    "Italy":380,
    "Côte d’Ivoire":384,
    "Jamaica":388,
    "Japan":392,
    "Kazakhstan":398,
    "Jordan":400,
    "Kenya":404,
    "Democratic People's Republic of Korea":408,
    "Republic of Korea":410,
    "Kuwait":414,
    "Kyrgyzstan":417,
    "Lao People's Democratic Republic":418,
    "Lebanon":422,
    "Lesotho":426,
    "Latvia":428,
    "Liberia":430,
    "Libya":434,
    "Liechtenstein":438,
    "Lithuania":440,
    "Luxembourg":442,
    "China, Macao Special Administrative Region":446,
    "Madagascar":450,
    "Malawi":454,
    "Malaysia":458,
    "Maldives":462,
    "Mali":466,
    "Malta":470,
    "Martinique":474,
    "Mauritania":478,
    "Mauritius":480,
    "Mexico":484,
    "Monaco":492,
    "Mongolia":496,
    "Republic of Moldova":498,
    "Montenegro":499,
    "Montserrat":500,
    "Morocco":504,
    "Mozambique":508,
    "Oman":512,
    "Namibia":516,
    "Nauru":520,
    "Nepal":524,
    "Netherlands (Kingdom of the)":528,
    "Curaçao":531,
    "Aruba":533,
    "Sint Maarten (Dutch part)":534,
    "Bonaire, Sint Eustatius and Saba":535,
    "New Caledonia":540,
    "Vanuatu":548,
    "New Zealand":554,
    "Nicaragua":558,
    "Niger":562,
    "Nigeria":566,
    "Niue":570,
    "Norfolk Island":574,
    "Norway":578,
    "Northern Mariana Islands":580,
    "United States Minor Outlying Islands":581,
    "Micronesia (Federated States of)":583,
    "Marshall Islands":584,
    "Palau":585,
    "Pakistan":586,
    "Panama":591,
    "Papua New Guinea":598,
    "Paraguay":600,
    "Peru":604,
    "Philippines":608,
    "Pitcairn":612,
    "Poland":616,
    "Portugal":620,
    "Guinea-Bissau":624,
    "Timor-Leste":626,
    "Puerto Rico":630,
    "Qatar":634,
    "Réunion":638,
    "Romania":642,
    "Russian Federation":643,
    "Rwanda":646,
    "Saint Barthélemy":652,
    "Saint Helena":654,
    "Saint Kitts and Nevis":659,
    "Anguilla":660,
    "Saint Lucia":662,
    "Saint Martin (French Part)":663,
    "Saint Pierre and Miquelon":666,
    "Saint Vincent and the Grenadines":670,
    "San Marino":674,
    "Sao Tome and Principe":678,
    "Saudi Arabia":682,
    "Senegal":686,
    "Serbia":688,
    "Seychelles":690,
    "Sierra Leone":694,
    "Singapore":702,
    "Slovakia":703,
    "Viet Nam":704,
    "Slovenia":705,
    "Somalia":706,
    "South Africa":710,
    "Zimbabwe":716,
    "Spain":724,
    "South Sudan":728,
    "Sudan":729,
    "Western Sahara":732,
    "Suriname":740,
    "Svalbard and Jan Mayen Islands":744,
    "Eswatini":748,
    "Sweden":752,
    "Switzerland":756,
    "Syrian Arab Republic":760,
    "Tajikistan":762,
    "Thailand":764,
    "Togo":768,
    "Tokelau":772,
    "Tonga":776,
    "Trinidad and Tobago":780,
    "United Arab Emirates":784,
    "Tunisia":788,
    "Türkiye":792,
    "Turkmenistan":795,
    "Turks and Caicos Islands":796,
    "Tuvalu":798,
    "Uganda":800,
    "Ukraine":804,
    "North Macedonia":807,
    "Egypt":818,
    "United Kingdom of Great Britain and Northern Ireland":826,
    "Guernsey":831,
    "Jersey":832,
    "Isle of Man":833,
    "United Republic of Tanzania":834,
    "United States of America":840,
    "United States Virgin Islands":850,
    "Burkina Faso":854,
    "Uruguay":858,
    "Uzbekistan":860,
    "Venezuela (Bolivarian Republic of)":862,
    "Wallis and Futuna Islands":876,
    "Samoa":882,
    "Yemen":887,
    "Zambia":894,
    }