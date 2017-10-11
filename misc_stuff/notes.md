## Notes to myself about what's going on in the tutorials

## TDD
#### Ideas, concepts, tricks, etc.

* test isolation - no test should depend on or impact any other test
* YAGNI (you ain't gonna need it) - effectively, don't go beyond the stated/created requirements, don't add your own 'fluff' b/c you think it might be needed
* Move from working to working state - tldr: small changes, i.e. for each change adjust testing as needed, then add code to _just_ fix test failures, then move on to the next

## Django
#### Models

In the unit tests `lists/test.py` I added another class to test
storing data entered by the user of the to-do lists app.  That class references another class I created, called Item() to implement a Django model.  The Item class inherits from Djano model class giving it some default methods, and I assume default attributes.  Among those default methods is save(). I also added an attributed called `text`, which is itself an instance of another Django class called TextField.  The test creates instances of Items which are saved to the database (which I believe is sqlite by default).

__Foreign Key__
* field type that points to a PK in another model
* Generally you'd create the other model first but required
* Creates a constraint in the backend DB by default - i.e. forces referential integrity - may not be what you want?
* Enables you to query in "either direction", e.g. show me all articles for reporter=x, etc.
* Here's [Django docs](https://docs.djangoproject.com/en/1.8/topics/db/examples/many_to_one/) on it

#### Questions/things to review

* review django "reverse lookups" (.item_set) << used in tempalates
* django passing entire objects vs. field values (object attributes) - like a List object vs the list ID attribute
* sending data to a template (context) << view views
* django and the "trailing /"
* django models & foreign keys (really need to brush up on FK in a db in general)
* how would I really troubleshoot problems -- i.e. all the troubleshooting in the book is based only on knowing how Django works and taking an educated guess at what is causing the problem, in some cases that seems like enough, but in others the leap to the solution seemed like "magic"

## Selenium
* Tool to automate testing by simulating a browser (actually drives the browser you tell it to)
* Chrome is not supported "out of the box" - must install the ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads)
    * This is a java app (i.e. requires a functioning JRE) - selenium itself is for that matter
    * The ChromeDriver (called driver from here on) must be in your path or you must give the full path when calling it
    * I've put it in my virtual env bin directory - not sure if that's best but, it's on my path by default - as long as I'm in the virtual env of course


