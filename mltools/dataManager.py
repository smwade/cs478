from __future__ import (absolute_import, division, print_function, unicode_literals)
import random
import numpy as np
class DataManager:
    MISSING = float("infinity")

    def __init__(self, arff=None):
        """
        If matrix is provided, all parameters must be provided, and the new matrix will be
        initialized with the specified portion of the provided matrix.
        """
        if arff:
            self.load_arff(arff)
        else:
            pass

    def init_from(self, matrix, row_start, col_start, row_count, col_count):
        """Initialize the matrix with a portion of another matrix"""
        self.data = [matrix.data[row][col_start:col_start+col_count] for row in range(row_start, row_start+row_count)]
        self.attr_names = matrix.attr_names[col_start:col_start+col_count]
        self.str_to_enum = matrix.str_to_enum[col_start:col_start+col_count]    # array of dictionaries
        self.enum_to_str = matrix.enum_to_str[col_start:col_start+col_count]    # array of dictionaries
        return self

    def add_data(self, new_data):
        """Appends a copy of the specified portion of a matrix to this matrix"""
        self.data = np.vstack((self.data, new_data))

    def set_labels(self):
        self.labels = self.data[:,-1]
        self.data = self.data[:,:-1]

    def test_train_split(self, ratio=.8):
        self.shuffle()
        split_point = int(self.num_rows * ratio)
        x_train = self.data[:split_point,:]
        x_test = self.data[split_point:,:]
        y_train = self.labels[:split_point]
        y_test = self.labels[split_point:]
        return x_train, x_test, y_train, y_test

    def set_size(self, rows, cols):
        """Resize this matrix (and set all attributes to be continuous)"""
        self.data = [[0]*cols for row in range(rows)]
        self.attr_names = [""] * cols
        self.str_to_enum = {}
        self.enum_to_str = {}

    def load_arff(self, filename):
        """ Load data from an ARFF file """
        self.data = []
        self.attr_names = []
        self.str_to_enum = []
        self.enum_to_str = []
        reading_data = False

        rows = []           # we read data into array of rows, then convert into array of columns

        f = open(filename)
        for line in f.readlines():
            line = line.rstrip().upper()
            if len(line) > 0 and line[0] != '%':
                if not reading_data:
                    if line.startswith("@RELATION"):
                        self.dataset_name = line[9:].strip()
                    elif line.startswith("@ATTRIBUTE"):
                        attr_def = line[10:].strip()
                        if attr_def[0] == "'":
                            attr_def = attr_def[1:]
                            attr_name = attr_def[:attr_def.index("'")]
                            attr_def = attr_def[attr_def.index("'")+1:].strip()
                        else:
                            attr_name, attr_def = attr_def.split()

                        self.attr_names += [attr_name]

                        str_to_enum = {}
                        enum_to_str = {}
                        if not(attr_def == "REAL" or attr_def == "CONTINUOUS" or attr_def == "INTEGER"):
                            # attribute is discrete
                            assert attr_def[0] == '{' and attr_def[-1] == '}'
                            attr_def = attr_def[1:-1]
                            attr_vals = attr_def.split(",")
                            val_idx = 0
                            for val in attr_vals:
                                val = val.strip()
                                enum_to_str[val_idx] = val
                                str_to_enum[val] = val_idx
                                val_idx += 1

                        self.enum_to_str.append(enum_to_str)
                        self.str_to_enum.append(str_to_enum)

                    elif line.startswith("@DATA"):
                        reading_data = True

                else:
                    # reading data
                    row = []
                    val_idx = 0
                    # print("{}".format(line))
                    vals = line.split(",")
                    for val in vals:
                        val = val.strip()
                        if not val:
                            raise Exception("Missing data element in row with data '{}'".format(line))
                        else:
                            row += [float(self.MISSING if val == "?" else self.str_to_enum[val_idx].get(val, val))]

                        val_idx += 1

                    rows += [row]

        f.close()
        self.data=np.array(rows)
        self.set_labels()


    @property
    def num_rows(self):
        """Get the number of rows in the matrix"""
        return len(self.data)

    @property
    def num_cols(self):
        """Get the number of columns (or attributes) in the matrix"""
        return len(self.attr_names)

    
    def attr_name(self, col):
        """Get the name of the specified attribute"""
        return self.attr_names[col]

    def attr_value(self, attr, val):
        """
        Get the name of the specified value (attr is a column index)
        :param attr: index of the column
        :param val: index of the value in the column attribute list
        :return:
        """
        return self.enum_to_str[attr][val]

    def value_count(self, col):
        """
        Get the number of values associated with the specified attribute (or columnn)
        0=continuous, 2=binary, 3=trinary, etc.
        """
        return len(self.enum_to_str[col]) if len(self.enum_to_str) > 0 else 0

    def shuffle(self):
        """Shuffle the row order. If a buddy Matrix is provided, it will be shuffled in the same order."""
        idx = np.random.permutation(self.num_rows)
        self.data = self.data[idx]
        self.labels = self.labels[idx]

     
    def mean(self):
        return np.mean(self.data, axis=0)

    def column_mean(self, col):
        """Get the mean of the specified column"""
        a = np.ma.masked_equal(self.data[:,col], self.MISSING).compressed()
        return np.mean(a)

    def column_min(self, col):
        """Get the min value in the specified column"""
        a = np.ma.masked_equal(self.data[:,col], self.MISSING).compressed()
        return np.min(a)

    def column_max(self, col):
        """Get the max value in the specified column"""
        a = np.ma.masked_equal(self.data[:,col], self.MISSING).compressed()
        return np.max(a)

    def most_common_value(self, col):
        """Get the most common value in the specified column"""
        a = np.ma.masked_equal(self.data[:,col], self.MISSING).compressed()
        scores = np.unique(np.ravel(a))       # get ALL unique values
        testshape = list(a.shape)
        testshape[axis] = 1
        oldmostfreq = np.zeros(testshape)
        oldcounts = np.zeros(testshape)

        for score in scores:
            template = (a == score)
            counts = np.expand_dims(np.sum(template, axis),axis)
            mostfrequent = np.where(counts > oldcounts, score, oldmostfreq)
            oldcounts = np.maximum(counts, oldcounts)
            oldmostfreq = mostfrequent
        
        return mostfrequent

    def normalize(self):
        """Normalize each column of continuous values"""
        for i in range(self.num_cols):
            if self.value_count(i) == 0:     # is continuous
                min_val = self.column_min(i)
                max_val = self.column_max(i)
                for j in range(self.num_rows):
                    v = self.data[j, i]
                    if v != self.MISSING:
                        self.data[j, i] = (v - min_val)/(max_val - min_val)
                        
    def __str__(self):
        outString = ""
        print("@RELATION {}".format(self.dataset_name))
        for i in range(len(self.attr_names)):
            print("@ATTRIBUTE {}".format(self.attr_names[i]), end="")
            if self.value_count(i) == 0:
                print(" CONTINUOUS")
            else:
                print(" {{{}}}".format(", ".join(self.enum_to_str[i].values())))

        print("@DATA")
        print(self.data)

    def __str__(self):
        outString = ""
        outString += "@RELATION {}".format(self.dataset_name)
        for i in range(len(self.attr_names)):
            outString += "@ATTRIBUTE {}\n".format(self.attr_names[i])
            if self.value_count(i) == 0:
                outString += " CONTINUOUS\n"
            else:
                outString += " {{{}}}\n".format(", ".join(self.enum_to_str[i].values()))

        outString += "@DATA\n"
        outString += str(self.data)
        return outString
