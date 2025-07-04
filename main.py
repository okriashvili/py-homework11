# დაწერეთ პროგრამა, რომელიც მომხმარებელს უსასრულოდ შეეკითხება ჯერ სახელს, შემდეგ გვარს და რაიმე ფაილში ჩაწერს
#    სახელს და გვარს ერთ ხაზზე თავისი ნუმერაციით, ყველა ახალი სახელი და გვარი უნდა იყოს ახალ ხაზზე ჩაწერილი:
#   პროგრამა ჩერდება იმ შემთხევაში, თუ მომხმარებელმა სახელის ადგილას შეიყვანა სიტყვა stop
# def name_list():
#     name_file = open("name_txt", "w+")
#     counter = 0
#     while True:
#         first_name = input("Enter your name: ")
#         if first_name == "stop":
#             break
#
#         last_name = input("Enter your last name: ")
#
#         name_file.write(f"{counter}. {first_name} {last_name}\n")
#         counter += 1
#     return name_file
# print(name_list())

#
# დავალება 2:თანდართულ ფაილში "persons.txt" მოცემულია ადამიანების სია შემდეგი ფორმატით:
#    სახელი და გვარი, ასაკი, ქალაქი
#
#    თქვენი დავალებაა არსებული ფაილიდან წაიკითხოთ ინფორმაცია, შექმნათ ორი ახალი ტექსტური ფაილი (.txt გაფართოებით), ერთ ფაილში
#    ჩაწერეთ ყველა პიროვნება რომლის ასაკი ნაკლებია 50-ზე, ხოლო მეორე ფაილში ჩაწერეთ ყველა პიროვნება, რომლის ასაკი მეტია 50-ზე,
#    ფორმატი დაცული უნდა იყოს ისეთი სახით, როგორიც არის ორიგინალ "persons.txt" ფაილში ანუ თითო პიროვნება თითო ხაზზე!
def reclasification() :
    with open("persons.txt", "r") as persons_file:
        over_fifty = []
        below_fifty = []
        persons_list = persons_file.readlines()
        for i in persons_list:
            j = i.strip().split(",")
            ages = int(j[1])
            if ages >= 50:
                over_fifty.append(j)
            elif ages < 50:
                below_fifty.append(j)

    with open("over.txt", "a") as over_fifty_file:
        for person in over_fifty:
            over_fifty_file.write(f"{person[0]},{person[1]}, {person[2]}\n")

    with open("below.txt", "a") as below_fifty_file:
        for person in below_fifty:
            below_fifty_file.write(f"{person[0]},{person[1]}, {person[2]}\n")
    return persons_file, over_fifty_file, below_fifty_file
print(reclasification())












