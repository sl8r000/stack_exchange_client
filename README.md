Stack Exchange Client
=====================

### Python wrapper for the Stack Exchange API

This is a Python wrapper for the read-only portions of the Stack Exchange API. The wrapper is organized to map closely onto the original endpoints. So, for example, the endpoint
```
/questions/{ids}/answers
```
maps onto
```python
client.questions.id([123, 456]).answers.get()
```
(More on ```.get()``` later)

### Getting Started
You can initialize a client object by providing the site name, and your API key and ID:
```python
client = StackExchangeClient(site='stackoverflow', client_id=123, key='50m3 l0n9 h#')
```
Alternatively, you can create a file called config.ini, formatted as follows:
```
[Stack Exchange Info]
site: stackoverflow
client_id: 123
key: 50m3 l0n9 h#
```
Then run auto_setup.py. This approach is useful if you plan on using the client in IPython (since then you don't need to copy/paste the credentials every time you want to use the client): 
```python
In [1]: %run auto_setup.py
Object client ready.

In [2]: client.users.get(pagesize=1)
Out[2]: 
[{u'accept_rate': 83,
  u'account_id': 11683,
  u'age': 37,
  u'badge_counts': {u'bronze': 5204, u'gold': 239, u'silver': 3764},
  u'creation_date': 1222430705,
  u'display_name': u'Jon Skeet',
  u'is_employee': False,
  u'last_access_date': 1385677582,
  u'last_modified_date': 1385643797,
  u'link': u'http://stackoverflow.com/users/22656/jon-skeet',
  u'location': u'Reading, United Kingdom',
  u'profile_image': u'https://www.gravatar.com/avatar/6d8ebb117e8d83d74ea95fbdd0f87e13?s=128&d=identicon&r=PG',
  u'reputation': 626007,
  u'reputation_change_day': 320,
  u'reputation_change_month': 7955,
  u'reputation_change_quarter': 17390,
  u'reputation_change_week': 1405,
  u'reputation_change_year': 107990,
  u'user_id': 22656,
  u'user_type': u'registered',
  u'website_url': u'http://csharpindepth.com'}]
```

### Some Examples
As mentioned above, the client maps closely onto the API's endpoints, so it's easy to use the API documentation to figure out how to make the calls you want. For example, here's what the [documentation](https://api.stackexchange.com/docs) says about answers:
```
/answers                                                Get all answers on the site.
/answers/{ids}                                          Get answers identified by a set of ids.
/answers/{ids}/comments                                 Get comments on the answers identified by a set of ids.
```
And here's how it looks with the client:
```
client.answers.get()                                    Get all answers on the site.
client.answers.ids(<int_or_int_list>).get()             Get answers identified by a set of ids.
client.answers.ids(<int_or_int_list>).comments.get()    Get comments on the answers identified by a set of ids.
```
Or, for some concrete examples:
```python
In [1] client.answers.get()
Out[1] <response omitted>

In [2]: client.answers.get(pagesize=1)
Out[2]: 
[{u'answer_id': 20275803,
  u'creation_date': 1385678711,
  u'is_accepted': False,
  u'last_activity_date': 1385679684,
  u'last_edit_date': 1385679684,
  u'owner': {u'accept_rate': 33,
   u'display_name': u'Sam Walls',
   u'link': u'http://stackoverflow.com/users/2596361/sam-walls',
   u'profile_image': u'https://www.gravatar.com/avatar/9a71b394fd67242a6aea091d6ab546f3?s=128&d=identicon&r=PG',
   u'reputation': 43,
   u'user_id': 2596361,
   u'user_type': u'registered'},
  u'question_id': 20275774,
  u'score': 1}]

In [3]: client.answers.get(sort='creation', order='asc', pagesize=1)
Out[3]: 
[{u'answer_id': 7,
  u'creation_date': 1217542677,
  u'is_accepted': True,
  u'last_activity_date': 1350215416,
  u'last_edit_date': 1350215416,
  u'owner': {u'accept_rate': 41,
   u'display_name': u'Kevin Dente',
   u'link': u'http://stackoverflow.com/users/9/kevin-dente',
   u'profile_image': u'https://www.gravatar.com/avatar/23c1e2063688620b75b248e08c0d5c24?s=128&d=identicon&r=PG',
   u'reputation': 6911,
   u'user_id': 9,
   u'user_type': u'registered'},
  u'question_id': 4,
  u'score': 188}]

In [4]: client.answers.ids(7).get()
Out[4]: 
[{u'answer_id': 7,
  u'creation_date': 1217542677,
  u'is_accepted': True,
  u'last_activity_date': 1350215416,
  u'last_edit_date': 1350215416,
  u'owner': {u'accept_rate': 41,
   u'display_name': u'Kevin Dente',
   u'link': u'http://stackoverflow.com/users/9/kevin-dente',
   u'profile_image': u'https://www.gravatar.com/avatar/23c1e2063688620b75b248e08c0d5c24?s=128&d=identicon&r=PG',
   u'reputation': 6911,
   u'user_id': 9,
   u'user_type': u'registered'},
  u'question_id': 4,
  u'score': 188}]

In [5]: client.answers.ids(7).comments.get()
Out[5]: []
```
Notice that we can pass keyword arguments to ```.get()```. Here, we're using some, such as ```sort```, ```order```, and ```pagesize```, that are explained in the [documentation](https://api.stackexchange.com/docs/answers) for the ```/answers``` endpoint.

### A Word on ```.get()```

All of the chains in the client end with a call to ```.get()```. The role of this call is mainly to let the client know that the chain is ended, e.g. that we're interested in ```/answers/123``` and won't be adding more to the URL to, e.g., get ```answers/123/comments```.

You can also pass keyword arguments into ```.get()```, as we saw in the last section.

Despite the usefulness of ```.get()``` as a terminus, writing ".get()" all the time can be annoying. So for times when you don't have any keyword arguments that you'd like to pass, you can use the alias ".g". For example:

```python
In [9]: client.answers.ids(7).get() == client.answers.ids(7).g
Out[9]: True
```
