## Notes to myself about what's going on in the tutorials

#### Models

In the unit tests `lists/test.py` I added another class to test
storing data entered by the user of the to-do lists app.  That class references another class I created, called Item() to implement a Django model.  The Item class inherits from Djano model class giving it some default methods, and I assume default attributes.  Among those default methods is save(). I also added an attributed called `text`, which is itself an instance of another Django class called TextField.  The test creates instances of Items which are saved to the database (which I believe is sqlite by default).