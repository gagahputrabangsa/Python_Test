def students_subscribed_to_either(english_students, french_students):
  """Calculates the number of students subscribed to either English or French newspaper.

  Args:
    english_students: A set of student roll numbers subscribed to English newspaper.
    french_students: A set of student roll numbers subscribed to French newspaper.

  Returns:
    The number of students subscribed to either English or French newspaper but not both.
  """

  # Find students subscribed to both newspapers
  both_newspapers = english_students.intersection(french_students)

  # Calculate students subscribed to either English or French but not both
  students_either = len(english_students) + len(french_students) - 2 * len(both_newspapers)

  return students_either

if __name__ == '__main__':
  n_english = int(input())
  english_students = set(map(int, input().split()))
  n_french = int(input())
  french_students = set(map(int, input().split()))

  result = students_subscribed_to_either(english_students, french_students)
  print(result)