# Fyle-Part-1
API usage

1.Autocomplete API Autocomplete API to return possible matches based on the branch name ordered by IFSC code (ascending order) with limit and offset.

Endpoint: /api/branches/autocomplete?q=<>

Example: /api/branches/autocomplete?q=RTGS&limit=3&offset=0

Hosted Url:
https://fyle-part-1.herokuapp.com/api/branches/autocomplete/?q=RTGS&limit=3&offset=0

API Response

{"branches": [{"ifsc": "ABHY0065001", "bank_id": "60", "branch": "RTGS-HO", "address": "ABHYUDAYA BANK BLDG., B.NO.71, NEHRU NAGAR, KURLA (E), MUMBAI-400024", "city": "MUMBAI", "district": "GREATER MUMBAI", "state": "MAHARASHTRA"}, {"ifsc": "ABNA0000001", "bank_id": "110", "branch": "RTGS-HO", "address": "414 EMPIRE COMPLEX, SENAPATI BAPAT MARG LOWER PAREL WEST MUMBAI 400013", "city": "MUMBAI", "district": "GREATER BOMBAY", "state": "MAHARASHTRA"}, {"ifsc": "ADCB0000001", "bank_id": "143", "branch": "RTGS-HO", "address": "75, REHMAT MANZIL, V. N. ROAD, CURCHGATE, MUMBAI - 400020", "city": "MUMBAI", "district": "MUMBAI CITY", "state": "MAHARASHTRA"}]}

2.Search API
Search API to return possible matches across all columns and all rows, ordered by IFSC code (ascending order) with limit and offset.

Endpoint: /api/branches?q=<>

Example: /api/branches?q=Bangalore&limit=4&offset=0

Hosted Url:
https://fyle-part-1.herokuapp.com/api/branches/?q=Bangalore&limit=4&offset=0

API Response

{"branches": [{"ifsc": "ADCB0000002", "bank_id": "143", "branch": "BANGALORE", "address": "CITI CENTRE, 28, CHURCH STREET, OFF M. G. ROAD BANGALORE 560001", "city": "BANGALORE", "district": "BANGALORE URBAN", "state": "KARNATAKA"}, {"ifsc": "ABNA0100318", "bank_id": "110", "branch": "BANGALORE", "address": "PRESTIGE TOWERS', GROUND FLOOR, 99 & 100, RESIDENCY ROAD, BANGALORE 560 025.", "city": "BANGALORE", "district": "BANGALORE URBAN", "state": "KARNATAKA"}, {"ifsc": "ANDB0002073", "bank_id": "15", "branch": "BANGALORE", "address": "BTM 4TH STAGE,929 BY A,4 TH STAGE,BTM LAYOUT,BANGALORE 560076", "city": "BANGALORE", "district": "BANGALORE", "state": "KARNATAKA"}, {"ifsc": "ANDB0002363", "bank_id": "15", "branch": "BANGALORE", "address": "NO 606,SYNDICATE BANK,ANDRAHALLI,MAIN ROAD,HERO HALLI,BANGALORE,560091", "city": "BANGALORE URBAN", "district": "BANGALORE URBAN", "state": "KARNATAKA"}]}
