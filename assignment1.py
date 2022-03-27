"""
Brief description ...
Name: Jihyung Park
Date started: 08/03/2021
GitHub URL: ...
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
    unvisit = 0
    visit = 0

    list_sort(list_of_places)

    for list_order in list_of_places:
        num += 1

        print("{0}. {1: <{2}} in {3: <{4}} priority {5}".format(num, list_order[0], find_max_name(list_of_places), list_order[1], find_max_country(list_of_places), list_order[2]))
        unvisit += list_order[3].count("n")
        visit += list_order[3].count("v")

    if num == visit:
        print("{0} places. No places left to visit. why not add a new place?".format(num))
    else:
        print("{0} places. You still want to visit {1} places.".format(num, unvisit))

def add_new_place(list_of_places):

    appending_list = []

    while True:
        name_input = str(input("Name: "))
        if name_input == "":
            print("Input can not be blank")
        else:
            appending_list.append(name_input)
            break

    while True:
        country_input = input("Country: ")
        if country_input == "":
            print("Input can not be blank")
        else:
            appending_list.append(country_input)
            break

    while True:
        try:
            priority_input = int(input("Priority: "))

            if int(priority_input) <= 0:
                print("Number must be > 0")
            else:
                appending_list.append(priority_input)
                break

        except ValueError:
            print("Invalid input; enter a valid number")

    appending_list.append("n")

    print(
        "{0} in {1} (priority {2}) added to Travel Tracker".format(appending_list[0], appending_list[1],
                                                                   appending_list[2]))
    list_of_places.append(appending_list)


def mark_a_place_visited(list_of_places):
    num = 0
    num_check = 0
    visit = 0
    unvisit = 0

    list_sort(list_of_places)

    for list_order in list_of_places:
        num_check += 1
        visit += list_order[3].count("v")
        unvisit += list_order[3].count("n")

    if num_check == visit:
        print("No unvisited places")
    else:

        for list_order in list_of_places:
            num += 1
            print("{0}. {1: <{2}} in {3: <{4}} priority {5}".format(num, list_order[0], find_max_name(list_of_places), list_order[1], find_max_country(list_of_places), list_order[2]))

        print("{0} places. You still want to visit {1} places.".format(num, unvisit))

        while True:
            try:
                list_name_change = int(input("Enter the number of a place to mark as visited :"))
                list_name_change_for_csv = list_name_change
                list_name_change_for_csv -= 1

                if int(list_name_change) <= 0:
                    print("Number must be > 0")

                elif int(list_name_change) > num:
                    print("Invalid palce number")

                elif list_of_places[int(list_name_change_for_csv)][3] == "v":
                    print("That place is already visited")
                    break

                else:
                    list_of_places[int(list_name_change_for_csv)][3] = "v"
                    list_sort(list_of_places)
                    print("{0} in {1} visited".format(list_of_places[list_name_change_for_csv][0],
                                                          list_of_places[list_name_change_for_csv][1]))
                    break
            except ValueError:
                print("Invalid input; enter a valid number")

def save_places(csv_file, list_of_places):

    infile = open(file_name, "w")
    writer = csv.writer(infile)

    writer.writerows(list_of_places)
    infile.close()

    print('{} places saved to {}'.format(len(list_of_places), csv_file))

# find max len of name of place
def find_max_name(list_of_places):
    name_list = []
    for i in range(0, len(list_of_places)):
        name_list.append(list_of_places[i][0])
    max_name = sorted(name_list, key = len)
    max_name = max_name[-1]
    return len(max_name)

# find max len of name of country
def find_max_country(list_of_places):
    country_list = []
    for i in range(0, len(list_of_places)):
        country_list.append(list_of_places[i][1])
    max_country = sorted(country_list, key = len)
    max_country = max_country[-1]
    return len(max_country)

def list_sort(list_of_places):
    list_of_places.sort( key = lambda priority: priority[2])
    list_of_places.sort( key = lambda visit: visit[3])


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
