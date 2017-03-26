import requests


def mc_servstatus(server_address):
    url = "https://mcapi.ca/query/%s/info" % server_address
    r = requests.get(url)
    if r.status_code != 200:
        return "Cannot connect to server"
    data = r.json()
    if data['status']:
        return (data['hostname'], data['port'], "Online", data['players']['online'])
    else:
        return (data['hostname'], data['port'], "Offline", 0)
