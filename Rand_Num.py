
#18/3/2022: Rand_num()
#=====================

# A function that generates a numpy array of random numbers:
#Parameters: count, start, end, shape_start, shape_end
  # count - the total amount of numbers you want in the array
  # start - the first/initial/least number from the range of numbers you want to randomly select from
  # end - he last/end/most number from the range of numbers you want to randomly select from
  # shape_start (optional) default is zero. The value for the row number for the case of a matrix
  # shape_end (optional) default is zero. The value for the column number for the case of a matrix
 
def rand_num(count, start, end, shape_start=0, shape_end=0):
    if shape_start | shape_end:
        return np.array([[np.random.randint(start,end) for i in np.arange(count)]]).reshape(shape_start,shape_end)
    else:
        return np.array([[np.random.randint(start,end) for i in np.arange(count)]])