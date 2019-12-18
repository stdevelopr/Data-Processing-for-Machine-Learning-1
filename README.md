# Data-Processing-for-Machine-Learning-1

*Encoding categorical data into number to fit on Machine Learning models...*

**NOTES**:
Often features are not given as continuous values but categorical. For example a person could have features ["male", "female"], ["from Europe", "from US", "from Asia"], ["uses Firefox", "uses Chrome", "uses Safari", "uses Internet Explorer"]. Such features can be efficiently coded as integers, for instance ["male", "from US", "uses Internet Explorer"] could be expressed as [0, 1, 3] while ["female", "from Asia", "uses Chrome"] would be [1, 2, 1].

To work with math models, these text categories should be encoded into numbers.

### Dummy variables:
Integer representation can, however, not be used directly, since the Machine Learning models would interpret the categories as being ordered, which is often not desired.
The use of dummy variables transforms each categorical feature with n_categories possible values into n_categories binary features, with one of them 1, and all others 0.

For example:

Suppose we have two categories, Blue with the value 3 and Red with value 4.

Category|Value
--------|------
Blue  |    3
Red    |   4

After converting into dummy variables it becomes:

Blue |Red |Value
-----|----|----
1    |0   |  3
0    | 1  |4

Reference material:(https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing-categorical-features)

-------------
# Running the code
The file categorical_data.py contains the code to convert categorical variables into numbers.
Just install the requirements and run in python3.
You must have a csv file named Data.csv in the same folder, and a new one will be generated.
Make sure that the file doesn't have null values.

## You can also run using docker:

```docker run -it -v /folder/to/Data-Processing-for-Machine-Learning-1/data:/data data_processing```

where /complete/path/to is the full path of the folder where you cloned this project. You can get it using the pwd command on linux.
