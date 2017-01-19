# Data Manager
# Sean Wade

import numpy as np

class DataManager():
    """
    Members:
      data : 
      labels :
      train_data :
      train_labels :
      test_data :
      test_labels : 
    """

    def __init__(self, input_file, test_file=None):
        """
        Args:
          input_file : (.arff)
          test_file : (.arff) If two separate for test and train.
        """
        if test_file is None:
            self.train_data = self.load_arff(input_file)


    def load_arff(input_file):
        in_file = open(input_file, 'r')
        attribute_list = []
        read_data = False
        for line in in_file.read().splitlines():
            if not read_data:
                line = line.split()
                if line == [] or line[0] == '%':
                    pass
                elif line[0] == '@RELATION':
                    relation = line[1]
                elif line[0] == '@ATTRIBUTE':
                    attribute_list.append(line[1])
                    ' '.join(line[2:])
                elif line[0] == '@DATA':
                    read_data = True
                    data = [attribute_list]
            else:
                if line[0] != '%':
                    line = line.rsplit(',')
                    data.append(line) 
        return np.array(data)

    def test_train_split(self, data, ratio=.8):
        pass

    def shuffle(self):
        pass

    def next_batch(self):
        pass
        

if __name__ == '__main__':
    load_arff('iris.arff')
