import httplib, urllib
server="pal.sandbox.dev.bbc.co.uk:9999"
action="/nuxeo/pimms/repository/workspaces/NewsPage"
create="/@views/create"
params = urllib.urlencode({'name': 'name1', 'doctype': 'BBC-Promo', 'dc:title': 'title 1'})
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
conn = httplib.HTTPConnection(server)
conn.request("POST", action, params, headers)
response = conn.getresponse()
print response.status, response.reason
data = response.read()
conn.close()

