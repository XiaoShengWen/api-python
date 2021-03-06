# domaintoolsAPI PYTHON Wrapper #

## Presentation ##

The domaintoolsAPI PYTHON Wrapper is a simple connector to access all webservices of [domaintools.com](http://domaintools.com "domaintools.com").

## Getting started ##

1- Clone the project with Git by running:

    $ git clone git://github.com/DomainTools/api-python

2- In domaintools/conf/, rename the **api.ini.default** to **api.ini**

3- Fill **api.ini**  with your domaintools credentials:

    username  = 'your_api_username';
    key       = 'your_api_key';

3-A Create a short PYTHON file to make a simple call to a webservice (**whois** for example):

```python
  from domaintools.api.request import Request

  # Make a call to the webservice whois with a xml return
  # type for the domain name : domaintools.com

  # prepare request
  request  = Request().service("whois").withType("xml").domain("domaintools.com")

  # call request
  response = request.execute()

  # display response
  print response
```

3-B If added you can also override on the fly your configuration :

```python

  from domaintools.api.request       import Request
  from domaintools.api.configuration import Configuration

  # from the default configuration, we change some values
  configuration = Configuration({'username':'username', 'password':'password'});

  # Make a call to the webservice whois with a xml return
  # type for the domain name : domaintools.com

  request  = Request(configuration).service("whois").withType("xml").domain("domaintools.com")
  response = request.execute()

  # Display the response
  print response

```

4- Execute the PYTHON script:

    $ python testDomaintoolsAPI.py

   If everything works fine, you should have a display like this:

```xml
<?xml version="1.0"?>
<whoisapi>
  <response>
    <registrant>DomainTools, LLC</registrant>
    <registration>
      <created>1998-08-02</created>
      <expires>2014-08-01</expires>
      <updated>2010-08-31</updated>
      <registrar>CHEAP-REGISTRAR.COM</registrar>
      <statuses>ok</statuses>
    </registration>
    <name_servers>NS1.P09.DYNECT.NET</name_servers>
    <name_servers>NS2.P09.DYNECT.NET</name_servers>
    <name_servers>NS3.P09.DYNECT.NET</name_servers>
    <name_servers>NS4.P09.DYNECT.NET</name_servers>
    <whois>
      <date>2011-10-17</date>
      <record>Domain name: domaintools.com

      Registrant Contact:
         DomainTools, LLC
         Domain Administrator (memberservices@domaintools.com)
         +1.2068389035
         Fax: +1.2068389056
         2211 5th Avenue
         Suite 201
         Seattle, WA 98121
         US

      Administrative Contact:
         DomainTools, LLC
         Domain Administrator (memberservices@domaintools.com)
         +1.2068389035
         Fax: +1.2068389056
         2211 5th Avenue
         Suite 201
         Seattle, WA 98121
         US

      Technical Contact:
         DomainTools, LLC
         Domain Administrator (memberservices@domaintools.com)
         +1.2068389035
         Fax: +1.2068389056
         2211 5th Avenue
         Suite 201
         Seattle, WA 98121
         US

         Status: Active
         Creation Date: 13-Jul-2002
         Expiration Date: 13-Jul-2016
         Name Server: NS1.P09.DYNECT.NET
         Name Server: NS2.P09.DYNECT.NET
         Name Server: NS3.P09.DYNECT.NET
         Name Server: NS4.P09.DYNECT.NET
      </record>
    </whois>
  </response>
</whoisapi>
```
5- Read the documentation to learn more, and visit [domaintools.com](http://domaintools.com "domaintools.com") to know the list of available services.

## Quick examples ##

In the main directory, you shoud have some examples to quickly test the API :

```
python 1-my-first-call-to-api.py
python 2-different-calls-for-same-result.py

```

## Documentation ##

The domaintoolsAPI PYTHON Wrapper is a fluent API implemented by using method chaining.

After having instanciate your request like this:

```python
request = Request()
```

You can combine methods to specify return type, options, etc.:

```python

print request.service('mark-alert').where({"query":"domaintools"}).withType("xml").execute()
```

### Choose service to call - service ###

```python
request.service("whois")
```
If no **service** is found the default service called will be [Domain Profile](http://www.domaintools.com/api/docs/domain-profile/).
You can find the list of available services on [domaintools.com](http://domaintools.com "domaintools.com").

### Specify options - where ###

```python
request.service("mark-alert").where({"query":"domain tools"})
```

The method **where** allows to specify options of the service. It takes only on parameter, a dictionary of options where the key is the name of the option and value is the value of the option.

The list of options for each service is available on the [domaintoolsAPI documentation](http://domaintools.com/api/docs/ "domaintoolsAPI documentation") .

### Specify return type - withType ###

```python
request.service("whois").withType("json")
```
The method **withType** allows to specify the return type of the response. It takes only one parameter, the **name** of the return type.

The list of return types is available on the [domaintoolsAPI documentation](http://domaintools.com/api/docs/ "domaintoolsAPI documentation").

You can also use **toJson**, **toXml** and **toHtml** as aliases of withType :

```python

  print request.service("whois").domain('domaintools.com').toJson().execute() # json
  print request.service("whois").domain('domaintools.com').toXml().execute()  # xml
  print request.service("whois").domain('domaintools.com').toHtml().execute() # html

```

### If no return type, a Response object is returned ###

By default (If you don't call the method withType) the return type used is  a **Response** object:

```python

  response = request.service("whois").domain('domaintools.com').execute()

```

With this response object, you will be able to access to response properties :

```python

  response = request.service("whois").domain('domaintools.com').execute()

  print response.registrant # Domaintools, LLC

  print response.whois.date # 2011-10-17

```

### Call the service - execute ###

```python

  response = request.service("whois").domain("domaintools.com").execute()

```

To call the service use the method **execute**, and return the response.

The response is a string with the format of the specify return type (JSON or XML for example).


## Tests with minimock ##

Here is the procedure to test this API

1- Install [Minimock](http://pypi.python.org/pypi/MiniMock)

2- Go into the main directory containing **tests.py**

2- Call all tests once (in console) :

```python
python tests.py
```

In **domaintools/tests/** are included all the tests classes. You should have a similar result :

```python


----------------------------------------------------------------------
Ran 17 tests in 0.004s

OK
```

## Changelog ##

See the CHANGELOG.md file for details.

## License ##

Copyright (C) 2011 by domaintools.com, DomaintoolsAPI PYTHON Wrapper is released under the MIT license.
See the LICENSE.md file for details.

