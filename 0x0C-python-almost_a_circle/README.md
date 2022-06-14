## Python: Almost A Circle

A project that helps us to review different kinds of data and class structures.
This exercies could be interpreted as the base of a Relational Data Model.

Classes will have the following Private instance Attributes:

- "id" (for indexing)
- "width" and "height" (size values)
- "x" and "y" (position values)

Features implemented for the child classes:
- Heritances
- Getter and Setter methods
- Data validation method for Setters
- Area calculation method for Rectangle class
- Display method to build a symbolic representation of the rectangle
- A Protected str method to retrieve data from the rectangle formatted as str

### Models

| File/Models       | Description                                                               | Features  |
| ----------------- | ------------------------------------------------------------------------- | --------- |
| base.py           | A base class/object                                                       |           |
| rectangle.py      | A child class/object which inherits features from "base"                  |           |
| square.py         | A child class/object which inherits features from "base" and "rectangle"  |           |
