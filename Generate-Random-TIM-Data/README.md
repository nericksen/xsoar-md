# Generate TIM Test Data
Scripts to generate IP and hash indicators in XSOAR.

## Prerequisites
Install `python3` and `requests` module.


# How To
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
