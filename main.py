import pywhatkit
import sys


phoneNumbers = sys.argv[1]
countryCode = sys.argv[2]
message = sys.argv[3]


with open(phoneNumbers, 'r', encoding='utf-8') as phoneNumbers:
    for line in phoneNumbers:
        number = countryCode+line.strip()
        pywhatkit.sendwhatmsg_instantly(number, message, 7, True, 2)