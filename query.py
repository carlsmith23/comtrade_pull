from comtradecut import Download

query = {
    "api_key": "fb6483764ea64e49a2d1f9364c33ea82",
    "type_code": "C",
    "freq_code": "A",
    "flow_direction": "M",
    "cl_code": "HS",
    "starting_year": 2000,
    "ending_year": 2021,
    "reporter_country": "156",
    "partner_country": None,
    "second_partner_country": None,
}
dl = Download(query)
dl.get()
