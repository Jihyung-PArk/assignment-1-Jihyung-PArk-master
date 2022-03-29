"""
Brief description : Travel Tracker
Name: Jihyung Park
Date started: 08/03/2021
GitHub URL: https://github.com/Jihyung-PArk/assignment-1-Jihyung-PArk-master.git
"""

# Constants
import csv

file_name = "places.csv"


def load_places(csv_file, list_of_places):
    try:
        infile = open(file_name, 'r')
        for line in infile:
            temp_list = line.strip().split(',')

            # convert the second item, which is priority, from str to int
            temp_list[2] = int(temp_list[2])
            list_of_places.append(temp_list)

            # list sort by visited status and by priority
            list_sort(list_of_places)
        infile.close()
        print("{} places loaded from {}".format(len(list_of_places), csv_file))

        # (check point) below print check list element
        # print(list_of_places)

    except IOError as error:
        print("I/O error: {}".format(error))


def display_menu():
    print("Menu:")
    print("L - List places")
    print("A - Add new place")
    print("M - Mark a place as visited")
    print("Q - Quit")


def list_places(list_of_places):
    num = 0
    un_visit = 0
    visit = 0

    # list sort by visited status and by priority
    list_sort(list_of_places)

    # print list part
    for places in list_of_places:
        num += 1

        print("{0}. {1: <{2}} in {3: <{4}} priority {5}".format(num, places[0],
                                                                find_max_name(list_of_places),
                                                                places[1],
                                                                find_max_country(list_of_places),
                                                                places[2]))

        # add visit and un_visit element
        un_visit += places[3].count("n")
        visit += places[3].count("v")

    # check if un_visit place
    if num == visit:
        print("{0} places. No places left to visit. why not add a new place?".format(num))
    else:
        print("{0} places. You still want to visit {1} places.".format(num, un_visit))


def add_new_place(list_of_places):
    appending_list = []

    # Add name and check error
    method_name(appending_list)

    # add country and check error
    method_country(appending_list)

    # add priority and check error
    method_priority(appending_list)

    # new place is always un_visit
    appending_list.append("n")

    # print new place information
    print(
        "{0} in {1} (priority {2}) added to Travel Tracker".format(appending_list[0],
                                                                   appending_list[1],
                                                                   appending_list[2]))
    # add new place information and sort by visited status and by priority
    list_of_places.append(appending_list)
    list_sort(list_of_places)

def mark_a_place_visited(list_of_places):
    num = 0
    num_check = 0
    visit = 0
    un_visit = 0

    # list sort by visited status and by priority
    list_sort(list_of_places)

    # check visit and un_visit place number
    for list_check in list_of_places:
        num_check += 1
        visit += list_check[3].count("v")
        un_visit += list_check[3].count("n")

    # check no un_visit place
    if num_check == visit:
        print("No unvisited places")
    else:

        # list of places
        for places in list_of_places:
            num += 1
            print("{0}. {1: <{2}} in {3: <{4}} priority {5}".
                  format(num, places[0], find_max_name(list_of_places), places[1],
                         find_max_country(list_of_places), places[2]))
        print("{0} places. You still want to visit {1} places.".format(num, un_visit))

        # check input(mark) error
        mark_place_error_check(list_of_places, num)

def save_places(csv_file, list_of_places):
    # open the file
    infile = open(file_name, "w")
    writer = csv.writer(infile)
    # save new csv file
    writer.writerows(list_of_places)
    infile.close()

    print('{} places saved to {}'.format(len(list_of_places), csv_file))


# function for find max len of name of place
def find_max_name(list_of_places):
    name_list = []
    for i in range(0, len(list_of_places)):
        name_list.append(list_of_places[i][0])
    max_name = sorted(name_list, key=len)
    max_name = max_name[-1]
    return len(max_name)


# function for find max len of name of country
def find_max_country(list_of_places):
    country_list = []
    for i in range(0, len(list_of_places)):
        country_list.append(list_of_places[i][1])
    max_country = sorted(country_list, key=len)
    max_country = max_country[-1]
    return len(max_country)

# function for sort by visited and by priority
def list_sort(list_of_places):
    list_of_places.sort(key=lambda priority: priority[2])
    list_of_places.sort(key=lambda visit: visit[3])

def method_name(appending_list):
    while True:
        name_input = str(input("Name: "))
        # check name_input is blank
        if name_input == "":
            print("Input can not be blank")
        # check name_input is integer
        elif name_input.isnumeric() or name_input[0] == "-":
            print("Input can not be integer")
        else:
            appending_list.append(name_input)
            break


def method_country(appending_list):
    while True:
        country_input = input("Country: ")
        # check county_input is blank
        if country_input == "":
            print("Input can not be blank")
        # check country_input is integer
        elif country_input.isnumeric() or country_input[0] == "-":
            print("Input can not be integer")
        else:
            appending_list.append(country_input)
            break


def method_priority(appending_list):
    while True:
        try:
            priority_input = int(input("Priority: "))

            # check priority_input is negative number
            if int(priority_input) <= 0:
                print("Number must be > 0")
            else:
                appending_list.append(priority_input)
                break

        # check priority_input is not integer
        except ValueError:
            print("Invalid input; enter a valid number")

def mark_place_error_check(list_of_places, num):
    while True:
        try:
            list_change = int(input("Enter the number of a place to mark as visited :"))
            list_change_for_csv = list_change
            list_change_for_csv -= 1

            if int(list_change) <= 0:
                print("Number must be > 0")

            elif int(list_change) > num:
                print("Invalid place number")

            # check mark
            elif list_of_places[int(list_change_for_csv)][3] == "v":
                print("That place is already visited")
                break

            else:
                # change mark
                list_of_places[int(list_change_for_csv)][3] = "v"
                print("{0} in {1} visited".format(list_of_places[list_change_for_csv][0],
                                                  list_of_places[list_change_for_csv][1]))
                break
        except ValueError:
            print("Invalid input; enter a valid number")

def main():
    print("Travel Tracker 1.0 - by Jihyung Park")
    list_of_places = []
    load_places(file_name, list_of_places)

    display_menu()
    choice = input("Enter a choice: ").strip().upper()
    while choice != 'Q':

        if choice == 'L':
            list_places(list_of_places)
        elif choice == 'A':
            add_new_place(list_of_places)
        elif choice == 'M':
            mark_a_place_visited(list_of_places)
        else:
            print("Invalid menu choice")
        display_menu()
        choice = input("Enter a choice: ").strip().upper()
    save_places(file_name, list_of_places)
    print("Have a nice day :)")


if __name__ == '__main__':
    main()
