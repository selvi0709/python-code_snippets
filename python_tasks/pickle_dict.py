# Ques: To create a pickle file to store your dictionary

import pickle

sample_dict = {1: 'cat', 2: 'dog', 3: 'rat', 4: 'cow', 5: 'pig'}

filename = "pick_dict"

outfile = open(filename, 'wb')

pickle.dump(sample_dict, outfile)
outfile.close()


# Opening pickle file data
infile = open(filename, 'rb')
new_dict = pickle.load(infile)
infile.close()

print(new_dict)
