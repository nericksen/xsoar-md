# Monitoring Hosted XSOAR via API

You may want to programatically have access to the data provided in the performance and monitoring dashboards.

This is possible to acheive by querying the widgets API in XSOAR.

For example to monitor the average CPU usage it is possible to query the corresponding widget with 


```
curl -X POST 'https://<xsoar>/v2/statistics/widgets/query' -H 'content-type: application/json' -H 'accept: application/json' -H 'Authorization: putYaOwnApiKey' --data-binary '{
 "id": "cpu-current-usage",
 "version": -1,
 "fromVersion": "5.0.0",
 "name": "CPU Current Usage",
 "dataType": "system",
 "widgetType": "number",
 "query": "cpu.usedPercent",
 "isPredefined": true,
 "params": {
  "currencySign": "%",
  "signAlignment": "right",
  "colors": {
   "isEnabled": true,
   "items": {
    "#FF1B15": {
     "value": 80
    },
    "#FAC100": {
     "value": 50
    },
    "#00CD33": {
     "value": -1
    }
   },
   "type": "above"
  }
 },
 "size": 0,
 "description": ""
}' --compressed
```

The query for this widget can be inferred by looking at the widget JSON stored in the demisto/content repo.
This example taken from <https://github.com/demisto/content/blob/e1c26879d309aa84c5aa27c30a0ff3bc4f7905d8/Packs/CommonWidgets/Widgets/widget-CPUUsageAvg.json>

It is also possible to send the audit trail via syslog described [here](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/5-5/cortex-xsoar-admin/logs/send-the-audit-trail-to-an-external-log-service)

The audit trail can also be pulled via Curl once daily as described [here](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-2/cortex-xsoar-admin/logs/audit-trail.html)
