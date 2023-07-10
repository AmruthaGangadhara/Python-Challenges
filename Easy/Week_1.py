/*Question:
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.


sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True */

Solution:

def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False


/* Question:
We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.


parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False */

Solution:

def parrot_trouble(talking, hour):
  if talking and (hour<7 or hour>20):
    return True
  else:
    return False


/*Question:

Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.


makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True */

def makes10(a, b):
  if a==10 or b==10 or (a+b)==10:
    return True
  else:
    return False



