"""
Brief description ...
Name: Jihyung Park
Date started: 08/03/2021
GitHub URL: ...
"""

# Constants
FILE_NAME = "places.csv"



def load_places(csv_file, list_of_places):
    try:
        infile = open(csv_file, 'r')
        for line in infile:
            temp_list = line.strip().split(',')
            # convert the second item, which is priority, from str to int
            temp_list[2] = int(temp_list[2])
            list_of_places.append(temp_list)
        infile.close()
        print("{} places loaded from {}".format(len(list_of_places), FILE_NAME))
        print(list_of_places)
    except IOError as error:
        print("I/O error: {}".format(error))


def display_menu():
    print("Menu:")
    print("L - List places")
    print("A - Add new place")
    print("M - Mark a place as visited")
    print("Q - Quit")


def list_places(list_of_places):
    print('choice L')


def add_new_place(list_of_places):
    print('choice A')


def mark_a_place_visited(list_of_places):
    print('choice M')


def save_places(csv_file, list_of_places):
    print('{} places saved to {}'.format(len(list_of_places), csv_file))


def main():
    print("Travel Tracker 1.0 - by student name")
    list_of_places = []
    load_places(FILE_NAME, list_of_places)
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
    save_places(FILE_NAME, list_of_places)
    print("Bye.")


if __name__ == '__main__':
    main()