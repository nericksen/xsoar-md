# XSIAM Data Archiving

**Goal**: to pull case details from Cortex XSOAR or XSIAM via API and store in another location. 

The examples below are curl commands for pulling incident and alert data from XSIAM.  The same API calls can be applied to XSOAR 8 instances (except those which are specific to XSIAM data types)

Note, for raw data you can use data forwarding solution. These curls are for alert, incident, files, etc.

Create a standard API key for use in curl commands below as described in our docs: https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-API-Reference.



## Get an Individual Incident
```
curl -X POST https://{TENANT_ID_HERE}.xdr.us.paloaltonetworks.com/public_api/v1/incidents/get_incidents -H "x-xdr-auth-id: {AUTH_ID_HERE}" -H "Authorization: {API_KEY_HERE}" -H "Content-Type:application/json" -d '{"request_data": {"filters": [{"field": "incident_id", "value": "{INCIDENT_ID_HERE}", "operator": "eq"}]}}'
```


## Get Incident Extra Data (Alerts)

```
curl -X POST https://{TENANT_ID_HERE}.xdr.us.paloaltonetworks.com/public_api/v1/incidents/get_incident_extra_data -H "x-xdr-auth-id: {AUTH_ID_HERE}" -H "Authorization: {API_KEY_HERE}" -H "Content-Type:application/json" -d '{"request_data": {"incident_id": "{INCIDENT_ID_HERE}"}}'
```


## Get the Entries on the Alert

```
curl -X POST https://{TENANT_ID_HERE}.xdr.us.paloaltonetworks.com/xsoar/investigation/{ALERT_ID_HERE} -H "x-xdr-auth-id: {AUTH_ID_HERE}" -H "Authorization: {API_KEY_HERE}" -H "Content-Type:application/json" -d '{"request_data": {}}'
```

## Get the Context Data for Alert
```
curl -X POST https://{TENANT_ID_HERE}.xdr.us.paloaltonetworks.com/xsoar/investigation/{ALERT_ID_HERE}/context -H "x-xdr-auth-id: {AUTH_ID_HERE}" -H "Authorization: {API_KEY_HERE}" -H "Content-Type:application/json" -d '{"query": "${.}"}'

```


## Download the Files Contents from Alert
NOTE: need to put the content bytes into an actual file on disk in the code.
```
curl -X GET https://{TENANT_ID_HERE}.xdr.us.paloaltonetworks.com/xsoar/entry/download/{FILE_ENTRY_ID_HERE}%40{ALERT_ID_HERE} -H "x-xdr-auth-id: {AUTH_ID_HERE}" -H "Authorization: {API_KEY_HERE}" -H "Content-Type:application/json" 
```


## Get Risky Users Cards
```
https://{{url}}/public_api/v1/get_risky_users
```


These HTTP requests can be crafted into a script external to XSOAR/XSIAM which polls this information and runs as a service to backup the data as required.
Exact incident types can be filtered when requesting the data as well as their status (ie archive only closed incidents) and additional filters can be added.
You may also use Post-Processing scripts attached to incident types in XSOAR to auto submit these pieces of data to external data stores using XSOAR integrations.


## DISCLAIMER: There are many options for exporting data but it is worth considering the operational overhead to maintain a backup system of record that has a high level of integrity with checks in place to ensure the data is actually there when needed. As such it is highly recommended to use the retention extension capabilities within the SaaS service to maintain data longer term and use these calls only as one off exceptions to the rule. These API calls also may be undocumented and unsupported and change from time to time as a result. Consult with your Account managers and Customer Support teams for guidance.



