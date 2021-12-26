import pickle
my_list = [1, 2, 3]
pickle_file = open('my_list.pkl', 'wb')
pickle.dump(my_list, pickle_file)
pickle.dump(my_list, pickle_file)
pickle_file.close()

pickle_file = open('my_list.pkl', 'wb')
pickle.dump(my_list, pickle_file)
pickle_file.close()

pickle_file = open('my_list.pkl', 'rb')
my_list2 = pickle.load(pickle_file)
my_list3 = pickle.load(pickle_file)
pickle_file.close()
print(my_list3)


