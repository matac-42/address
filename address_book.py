# coding: utf-8
import datetime


class AddressBook:

    person_list = []

    def add(self, person):
        self.person_list.append(person)

    def show_all(self):
        for person in self.person_list:
            print(person.lastname + " " + person.firstname)

    def search(self, keyword):
        for person in self.person_list:
            if keyword in person.firstname or keyword in person.lastname:
                print(person.lastname + " " + person.firstname)

    def import_data(self, file):
        import csv
        import datetime

        with open(file, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)

            for row in reader:
                p = Person()
                p.lastname = row[0]
                p.firstname = row[1]
                p.maiL_address = row[2]
                p.birthday = datetime.datetime.strptime(row[3], "%Y/%m/%d")
                p.tel = row[4]

                self.person_list.append(p)


class Person:

    firstname= ""
    lastname = ""
    tel = ""
    maiL_address = ""
    birthday = datetime.datetime(2000, 1, 1)


# ab = AddressBook()
#
# p = Person()
# p.firstname = "Y"
# p.lastname = "Mata"
# p.tel = "090-1234-5678"
#
# ab.add(p)
#
# p2 = Person()
# p2.firstname = "Shoki"
# p2.lastname = "Fujiwara"
# p2.tel = "080-8765-4321"
#
# ab.add(p2)
#
# print("Number of people->" + str(len(ab.person_list)))
# ab.show_all()
#
# ab.search("shoki")

ab = AddressBook()
ab.import_data("/Users/e185742/PycharmProjects/address_book/Documents/sample100.csv")

print("Number of people->" + str(len(ab.person_list)))

ab.search("片山")