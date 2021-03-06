# API WebMonitoring

## ROUTES

### /

#### index():

Sample function for checking the availability of server. Returns "Hello, world!" in case of success

### /availableResources/<username>

#### available_resources(username)

Returns all available Resources from DB for a given user

### /availableWebsites/<username>

#### available_websites(username)

Returns all available Websites from DB for a given user

### /resources/metrics/<resource_name>

#### resources_metrics(resource_name)

Returns statistics for minimum, average, maximum and median values recorded for Time, Size and Efficiency metrics.

### /resources/samples/time/<resource_id>/<period>

#### resources_get_samples_time(resource_id, period)

Returns sample values recorded for a resource(Time metrics), for a given period of time (daily, weekly, monthly).

### /websites/samples/time/<resource_id>/<period>

#### websites_get_samples_time(website_id, period)

Returns sample values recorded for a website(Total time metric), for a given period of time (daily, weekly, monthly).

### /resources/samples/size/<resource_id>/<period>

#### resources_get_samples_size(resource_id, period)

Returns sample values recorded for a resource(Size metrics), for a given period of time (daily, weekly, monthly).

### /websites/samples/size/<resource_id>/<period>

#### websites_get_samples_size(website_id, period)

Returns sample values recorded for a website(Size metrics), for a given period of time (daily, weekly, monthly).

### /resources/statistics

#### resources_statistics()

Returns statistics for all ResourceMonitoring Tools recorded all-time, with tailored results for records from the last 24 hours.

### /websites/statistics

#### websites_statistics()

Returns statistics for all WebsiteMonitoring Tools recorded all-time, with tailored results for records from the last 24 hours.

### /addresource

- POST REQUESTS

#### add_resource()

Simple API to add a new resource.

Payload must contain the username of the user, resource name and command:

e.g.

```json
{
  "username": "flask_test_username",
  "resource": "https://cs.pub.ro/",
  "command": "GET"
}
```

### /addwebsite

- POST REQUESTS

#### add_website()

Simple API to add a new website.

Payload must contain the username of the user, website name and the url:

e.g.

```json
{
  "username": "flask_test_username",
  "website_name": "Home - Computer Science Department - UPB",
  "url": "https://cs.pub.ro/"
}
```

### /deleteresource

- POST REQUESTS

#### delete_resource()

Simple API to delete a resource.

Payload must contain the username of the user, resource name and command:

e.g.

```json
{
  "username": "flask_test_username",
  "resource": "https://cs.pub.ro/",
  "command": "GET"
}
```

### /deletewebsite

- POST REQUESTS

#### delete_website()

Simple API to delete a new website.

Payload must contain the username of the user, website name and the url:

e.g.

```json
{
  "username": "flask_test_username",
  "website_name": "Home - Computer Science Department - UPB",
  "url": "https://cs.pub.ro/"
}
```

## Testing functionality

### Add resource

```python
import requests
import json


url = 'http://10.96.0.4:5000/addresource'
data = { "username": "flask_test_username", "resource": "https://www.youtube.com/", "command": "GET" }
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data), headers=headers)
print(r.text)
```

### Delete resource

```python
import requests
import json


url = 'http://10.96.0.4:5000/deleteresource'
data = { "username": "flask_test_username", "resource": "https://www.youtube.com/", "command": "GET" }
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data), headers=headers)
print(r.text)
```
