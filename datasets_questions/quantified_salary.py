import pickle

known_salary = 0
known_emails = 0

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
enron_names = list(enron_data.keys())

for name in enron_names:
  print(enron_data[name]['email_address'])
  print()
  print(enron_data[name]['salary'])
  if enron_data[name]['salary'] != 'NaN':
    known_salary += 1
  if enron_data[name]['email_address'] != 'NaN':
    known_emails += 1

print('known emails ', known_emails, 'known salary ', known_salary)
