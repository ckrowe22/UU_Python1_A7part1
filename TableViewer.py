# COMP1010 Part 1 Provided Code
# Do not change anything in this file.
# These settings let us see more of our data
# Try changing desired_width and max_columns


# DO NOT CHANGE THIS CODE
def view_table(data):
    import pandas as pd

    desired_width = 200
    max_columns = 20
    pd.set_option('display.width', desired_width)
    pd.set_option('display.max_columns', max_columns)

    df = pd.DataFrame(data)

    return df.head()
