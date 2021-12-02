# Generate TIM Test Data
Scripts to generate IP and hash indicators in XSOAR.

## Prerequisites
Install `python3` and `requests` module.


## Creating Indicators Over API
As your XSOAR deployment grows you may want to load test the onboarding of TIM feeds.
If you are starting with a clean development environment it may be desirable to create
indicators in XSOAR before onboarding the feed to simulate a production environment.

The `create-ip-indicators.py` script can be used to generate IPs from a given `CIDR`.
Modify the script to utilize an `API_KEY` key generated on your instance as well as the `BASE_URL`.

A few random fields are generated with each IP indicator created.
The `body` object can also be modified to add additional custom fields.

The script can then be run with 

```
python3 create-ip-indicators.py
```

or similar.

The `create-hash-indicators.py` script can also be used to create a defined number of random hashes.
Set the variables in the script for `API_KEY` and `BASE_URL` as well as the `COUNT` which defines how many 
random hashes to create.

## Generating Random Indicator Feed
You can generate a file of random hashes and ips using the 

* `create-ip-file.py`
* `create-hash-file.py`

These scripts will output indicators into txt files.
These txt files can then served using 

```
python3 -m http.server
```

This can now be ingested as a custom feed in XSOAR using the `Plain Text Feed` integration.
For large amounts of indicators this is more efficent than making an API call for each indicator
as is the case for the scripts mentioned above (`create-ip-indicators.py` and `create-hash-indicators.py`).
