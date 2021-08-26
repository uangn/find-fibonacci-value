# Find fibonacci value with recursion
def fibonacciSearch(index):
  assert index >= 0 and int(index) == index, "Index must be positive interger"
      if index in [0,1]:
          return index
      else:
          return fibonacciSearch(index-1) + fibonacciSearch(index-2)
