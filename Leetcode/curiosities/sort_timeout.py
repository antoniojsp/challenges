import time
import threading


def delayed_print_based_on_value(arr):
  # present_numbers = set(arr)  # For efficient checking of presence
  # max_val = max(arr) if arr else 0

  def print_with_delay(element, delay):
    time.sleep(delay/100)
    print(element)

  for value in range(len(arr)+1):
    if value in arr:
      delay = value  # Delay proportional to the value
      thread = threading.Thread(target=print_with_delay, args=(value, delay))
      thread.start()

my_array = [1, 1,5, 2, 8, 6]
delayed_print_based_on_value(my_array)