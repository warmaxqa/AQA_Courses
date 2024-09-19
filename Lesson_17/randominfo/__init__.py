from __future__ import unicode_literals

import csv
import glob
import pytz
import shutil
import sys
from os import access, W_OK
from os.path import abspath, join, dirname, split

sys.path.append("/randominfo/")
from random import randint, choice, sample, randrange
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from math import ceil

__title__ = 'randominfo'
__version__ = '2.0.2'
__author__ = 'Bhutan Gandhi'
__license__ = 'MIT'

full_path = lambda filename: abspath(join(dirname(__file__), filename))


def get_id(length=6, seq_number=None, step=1, prefix=None, postfix=None):
    generated_id = ""
    if seq_number is None:
        for _ in range(length):
            generated_id += str(randint(0, 9))
    else:
        if type(seq_number).__name__ != 'int' or type(step).__name__ != 'int':
            raise TypeError("Sequence number must be an integer.")
        else:
            generated_id = str(seq_number + step)
    if prefix is not None:
        prefix += generated_id
        generated_id = prefix
    if postfix is not None:
        generated_id += postfix
    return generated_id


def get_first_name(gender=None):
    firstNameFile = csv.reader(open(full_path('data.csv'), 'r'))
    filteredData = []
    if gender is None:
        for data in firstNameFile:
            if data[0] != '':
                filteredData.append(data)
    else:
        if gender.lower() == "male":
            for data in firstNameFile:
                if data[0] != '':
                    if data[2] == "male":
                        filteredData.append(data)
        elif gender.lower() == "female":
            for data in firstNameFile:
                if data[0] != '':
                    if data[2] == "female":
                        filteredData.append(data)
        else:
            raise ValueError("Enter gender male or female.")
    return choice(filteredData)[0]


def get_last_name():
    lastNameFile = csv.reader(open(full_path('data.csv'), 'r'))
    filteredData = []
    for data in lastNameFile:
        if data[1] != '':
            filteredData.append(data[1])
    return choice(filteredData)


def get_gender(first_name):
    firstNameFile = csv.reader(open(full_path('data.csv'), 'r'))
    gender = ""
    for data in firstNameFile:
        if data[0] != '' and data[0] == first_name:
            gender = data[2]
            break
    return gender


def get_country(first_name=None):
    countryFile = csv.reader(open(full_path('data.csv'), 'r'))
    country = ""
    if first_name is not None:
        for data in countryFile:
            if data[0] != '' and data[0] == first_name:
                country = data[3]
                break
        if country == "":
            print("Specified user data is not available. Tip: Generate random country.")
    else:
        filteredData = []
        for data in countryFile:
            if data[12] != '':
                filteredData.append(data[12])
        country = choice(filteredData)
    return country


def get_full_name(gender=None):
    return get_first_name(gender) + " " + get_last_name()


def get_otp(length=6, digit=True, alpha=True, lowercase=True, uppercase=True):
    lwrChars = "qwertyuioplkjhgfdsazxcvbnm"
    uprChars = "QWERTYUIOPLKJHGFDSAZXCVBNM"
    digs = "0123456789"
    chars = ""
    otp = ""
    if digit != False or alpha != False:
        if digit:
            chars += digs
        if alpha:
            if lowercase:
                chars += lwrChars
            if uppercase:
                chars += uprChars
        for _ in range(length):
            otp += str(chars[randint(0, len(chars) - 1)])
        return otp
    else:
        raise ValueError("From parameters 'digit' and 'alpha' anyone must be True.")


def get_formatted_datetime(outFormat, strDate, strFormat="%d-%m-%Y %H:%M:%S"):
    return datetime.strptime(strDate, strFormat).strftime(outFormat)


def get_email(person=None):
    domains = ["gmail", "yahoo", "hotmail", "express", "yandex", "nexus", "online", "omega", "institute", "finance",
               "company", "corporation", "community"]
    extentions = ['com', 'in', 'jp', 'us', 'uk', 'org', 'edu', 'au', 'de', 'co', 'me', 'biz', 'dev', 'ngo', 'site',
                  'xyz', 'zero', 'tech']

    if person is None:
        person = Person()

    c = randint(0, 2)
    dmn = '@' + choice(domains)
    ext = choice(extentions)

    if c == 0:
        email = person.first_name + get_formatted_datetime("%Y", person.birthdate, "%d %b, %Y") + dmn + "." + ext
    elif c == 1:
        email = person.last_name + get_formatted_datetime("%d", person.birthdate, "%d %b, %Y") + dmn + "." + ext
    else:
        email = person.first_name + get_formatted_datetime("%y", person.birthdate, "%d %b, %Y") + dmn + "." + ext
    return email


def random_password(length=8, special_chars=True, digits=True):
    spec_chars = ['!', '@', '#', '$', '%', '^', '&', '*']
    alpha = "QWERTYUIOPLKJHGFDSAZXCVBNMmnbvcxzasdfghjklpoiuytrewq"
    spec_char_len = dig_char_len = 0
    chars = ""

    if special_chars:
        spec_char_len = randint(1, ceil(length / 4))
        for _ in range(spec_char_len):
            chars += choice(spec_chars)
    if digits:
        dig_char_len = randint(1, ceil(length / 3))
        for _ in range(dig_char_len):
            chars += str(randint(0, 9))
    for _ in range(length - (dig_char_len + spec_char_len)):
        chars += choice(alpha[randint(0, len(alpha) - 1)])

    paswd = ''.join(sample(chars, len(chars)))
    return paswd


def get_phone_number(country_code=True):
    phone = ""
    if country_code:
        cCodes = [91, 144, 141, 1, 44, 86, 52, 61, 32, 20, 33, 62, 81, 31, 7]
        phone = "+"
        phone += str(choice(cCodes))
        phone += " "
    for i in range(0, 10):
        if i == 0:
            phone += str(randint(6, 9))
        else:
            phone += str(randint(0, 9))
    return phone


def get_alphabetic_profile_img(char, filePath, imgName, charColor=None, bgColor=None):
    chars = "qwertyuioplkjhgfdsazxcvbnmQAZXSWEDCVFRTGBNHYUJMKLIOP0123456789 ,.+=-_()[]{}"
    if all((c in chars) for c in imgName):
        if access(dirname(filePath), W_OK):
            if charColor is not None:
                if not charColor.isalpha():
                    raise ValueError("Character color must be a name of color.")
            if bgColor is not None:
                if not bgColor.isalpha():
                    raise ValueError("Background color must be a name of color.")
            char = char[:1].upper()
            if bgColor is None:
                colors = ['red', 'green', 'royalblue', 'violet', 'pink', 'indigo', 'grey', 'yellowgreen', 'teal']
                bgColor = choice(colors)
            if charColor is None:
                charColor = (40, 40, 40)
            img = Image.new('RGB', (512, 512), color=bgColor)
            d = ImageDraw.Draw(img)
            font = ImageFont.truetype("Candara.ttf", 280)
            d.text((170, 140), char, fill=charColor, font=font)
            filePath = filePath + "\\" + str(imgName) + ".jpg"
            img.save(filePath)
        else:
            raise OSError("Invalid or insufficient privileges for specified file path.")
    else:
        raise OSError(
            "Invalid image name. Image name must contains characher including digits, alphabets, white space, dot, "
            "comma, ( ) [ ] { } _ + - =.")
    return filePath


def get_face_profile_img(filePath, imgName, gender=None):
    dir_name, file_name = split(abspath(__file__))
    chars = "qwertyuioplkjhgfdsazxcvbnmQAZXSWEDCVFRTGBNHYUJMKLIOP0123456789 ,.+=-_()[]{}"
    if all((c in chars) for c in imgName):
        if access(dirname(filePath), W_OK):
            if gender is None:
                orig_file = choice(glob.glob(dir_name + "\\images\\people\\*.jpg"))
            elif gender.lower() == "female":
                orig_file = choice(glob.glob(dir_name + "\\images\\people\\female_*.jpg"))
            elif gender.lower() == "male":
                orig_file = choice(glob.glob(dir_name + "\\images\\people\\male_*.jpg"))
            else:
                return ValueError("Invalid gender. It must be male or female.")
            return shutil.copy(orig_file, filePath + "\\" + str(imgName) + ".jpg")
        else:
            raise OSError("Invalid or insufficient privileges for specified file path.")
    else:
        raise OSError(
            "Invalid image name. Image name must contains characher including digits, alphabets, white space, dot, "
            "comma, ( ) [ ] { } _ + - =.")


startRange = datetime(1970, 1, 1, 0, 0, 0, 0, pytz.UTC)
endRange = datetime.today()


def get_today(_format="%d-%m-%Y %H:%M:%S"):
    return datetime.today().strftime(_format)


# noinspection PyDeprecation
def get_date(tstamp=None, _format="%d %b, %Y"):
    if tstamp is None:
        startTs = startRange.timestamp()
        endTs = datetime.timestamp(endRange)
        tstamp = randrange(int(startTs), int(endTs))
    else:
        if type(tstamp).__name__ != 'int':
            raise ValueError("Timestamp must be an integer.")
    return datetime.utcfromtimestamp(tstamp).strftime(_format)


def get_birthdate(startAge=None, endAge=None, _format="%d %b, %Y"):
    start_range = datetime.today()
    end_range = datetime(1970, 1, 1, 0, 0, 0, 0, pytz.UTC)
    if startAge is not None:
        if type(startAge).__name__ != 'int':
            raise ValueError("Starting age value must be integer.")
    if endAge is not None:
        if type(endAge).__name__ != 'int':
            raise ValueError("Ending age value must be integer.")
    if startAge is not None and endAge is not None:  # If both are given in arg
        if startAge >= endAge:
            raise ValueError("Starting age must be less than ending age.")
        else:
            start_range = datetime(datetime.now().year - startAge, 12, 31, 23, 59, 59, 0, pytz.UTC)
            end_range = datetime(datetime.now().year - endAge, 1, 1, 0, 0, 0, 0, pytz.UTC)
    elif startAge is not None or endAge is not None:  # If anyone is given in arg
        ageYear = startAge if startAge is not None else endAge
        start_range = datetime(datetime.now().year - ageYear, 12, 31, 23, 59, 59, 0, pytz.UTC)
        end_range = datetime(datetime.now().year - ageYear, 1, 1, 0, 0, 0, 0, pytz.UTC)
    else:
        pass
    startTs = start_range.timestamp()
    endTs = end_range.timestamp()
    return datetime.fromtimestamp(randrange(int(endTs), int(startTs))).strftime(_format)


def get_address():
    full_addr = []
    addrParam = ['street', 'landmark', 'area', 'city', 'state', 'country', 'pincode']

    with open(full_path('data.csv'), 'r') as file:
        addrFile = csv.reader(file)

        for i in range(5, 12):
            allAddrs = []
            for addr in addrFile:
                try:
                    if addr[i] != '':
                        allAddrs.append(addr[i])
                except IndexError:
                    print("Индекс {i} выходит за пределы в строке: {addr}")
                    continue

            if allAddrs:
                full_addr.append(choice(allAddrs))
            else:
                full_addr.append("N/A")

    full_addr = dict(zip(addrParam, full_addr))
    return full_addr


def get_hobbies():
    hobbiesFile = csv.reader(open(full_path('data.csv'), 'r'))
    allHobbies = []
    for data in hobbiesFile:
        if data[4] != '':
            allHobbies.append(data[4])
    hobbies = []
    for _ in range(1, randint(2, 6)):
        hobbies.append(choice(allHobbies))
    return hobbies


class Person:
    def __init__(self, gender=None):
        firstName = get_first_name(gender)
        self.first_name = firstName
        self.last_name = get_last_name()
        self.full_name = self.first_name + " " + self.last_name
        self.birthdate = get_birthdate()
        self.phone = get_phone_number()
        self.email = get_email(self)
        self.gender = get_gender(firstName)
        self.country = get_country(firstName)
        self.password = random_password()
        self.hobbies = get_hobbies()
        self.address = get_address()
        self.customAttr = {}

    def set_attr(self, attr_name, value=None):
        if attr_name.isalnum():
            if attr_name[0].isalpha():
                self.customAttr[attr_name] = value
                print("Attribute '" + str(attr_name) + "' added.")
            else:
                raise ValueError("First character of attribute must be an alphabet.")
        else:
            raise ValueError("Attribute name only contains alphabets and digits.")

    def get_attr(self, attr_name):
        if attr_name.isalnum():
            if attr_name[0].isalpha():
                if attr_name in self.customAttr.keys():
                    return self.customAttr[attr_name]
                else:
                    raise AttributeError("Specified attribute is not exists.")
            else:
                raise ValueError("First character of attribute must be an alphabet.")
        else:
            raise ValueError("Attribute name only contains alphabets and digits.")

    def get_details(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "full_name": self.full_name,
            "birthdate": self.birthdate,
            "gender": self.gender,
            "email": self.email,
            "phone": self.phone,
            "password": self.password,
            "country": self.country,
            "hobbies": self.hobbies,
            "address": self.address,
            "other_attr": self.customAttr
        }


'''
REFERENCE:
https://www.first-names-meanings.com/country-indian-names.html
https://www.familyeducation.com/baby-names/browse-origin/surname/indian
https://thispersondoesnotexist.com/
https://en.wikipedia.org/wiki/List_of_hobbies
'''
