import argparse
from openpyxl import load_workbook
from validate_email import validate_email
from tqdm import tqdm
from multiprocessing import Pool


def parse_args():
    parser = argparse.ArgumentParser(description='Парсим почтовые адреса')
    parser.add_argument('--file', type=str, required=True, help='file with data')
    args = parser.parse_args()
    return args


def read(text):
    emails = []
    wb = load_workbook(filename = text+'.xlsx')
    ws = wb.active
    for row in ws.values:
       for value in row:
         emails.append(value)
    return emails


whitelist_domains = [
    'yandex.ru',
    'gmail.com',
	'mail.ru',
    'icloud.com'
]


def do_check(email):
    valid_regex = validate_email(email_address=email, check_regex=True, check_mx=False)

    if not valid_regex:
        return False

    domain = email[email.find('@') + 1:]
    valid_mx = (domain in whitelist_domains) or validate_email(email_address=email, check_regex=False, check_mx=True, dns_timeout=10)

    return valid_mx


def check(emails):
    correct = []
    incorrect = []

    with Pool(100) as p:
        res = list(tqdm(p.imap(do_check, emails), total=len(emails)))

    for email, valid in zip(emails, res):
        if valid:
            correct.append(email)
        else:
            incorrect.append(email)

    return correct, incorrect


def write(data, filename):
    with open(filename, 'w') as f:
        f.write('\n'.join(data))


def main():
    args = parse_args()
    print('Read file...')
    emails = read(args.file)
    print('Check email...')
    correct, incorrect = check(emails)
    print('Save data...')
    write(correct, 'Correct.txt')
    write(incorrect, 'Incorrect.txt')
    print('Done!')


if __name__ == '__main__':
    main()
