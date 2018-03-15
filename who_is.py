import os

def get_who_is(url):
    command = "whois " + url
    process = os.popen(command)
    results = str(process.read())
    return results

print(get_who_is('reddit.com'))