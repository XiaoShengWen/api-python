from domaintools.api.request import Request
from domaintools.api.configuration import Configuration

if __name__ == "__main__":
    print Request().withType('json').domain('domaintools.com').execute()
