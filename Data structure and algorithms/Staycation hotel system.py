# Name: Ho zhi yang
# Admin no: 202678J
# Tutorial Group: IT2653-03

num_index = 0
record_index = []
dictionary_index = {}

# The menu gets called everytime the user finishes whatever option they selected.


def menu():
    print("Welcome to our hotel!\nHow may we serve you today?")
    print("Menu:")
    print("1. Add Record")
    print("2. Update Record")
    print("3. Remove Record")
    print("4. Display Record")
    print("5. Sort Record")
    print("6. Search Record")
    print("Please enter exit to exit the application ")


def add(index):
    print("Currently adding in customer index {0} information.".format(index))

    package_name = input("Please enter the customer's package name: ")
    name = input("Please enter the Customer's name: ")
    check_in_date = input("Please enter the customer's check in date in the following format (ddmmyyyy): ")
    country = input("Please enter the customer's country of origin: ")
    phone_number = input("Please enter the customer's phone number: ")
    # Add new category here

# validating the user's inputs
    while True:
        if package_name.isalpha():
            if name.isalpha():
                if check_in_date.isdigit():
                    if country.isalpha():
                        if phone_number.isdigit():
                                # Add new validate/store here add the new category under here and validate
                                    # push new information to here ->
                            information = {"package_name": package_name, "name": name, "check_in_date": check_in_date, "country": country, "phone_number": phone_number}
                            dictionary_index[index] = information
                            print("Please check that customer index {0}'s information is correct".format(index))
                            for a in information:
                                print(a, "=", dictionary_index[index][a])
                            break
                                # Add new else for validate
                        else:
                            print("Phone number is not in numbers. Please retry.")
                            phone_number = input("Please enter the customer's phone number: ")

                    else:
                        print("Country is not in alphabets. Please retry.")
                        country = input("Please enter the customer's country of origin: ")

                else:
                    print("check in date is not in numbers. Please retry.")
                    check_in_date = input("Please enter the customer's check in date in the following format (ddmmyyyy): ")

            else:
                print("Name is not in alphabets. Please re-enter the Customer's name")
                name = input("Please enter the Customer's name: ")
        else:
            print("Package name is not in alphabets. Please retry.")
            package_name = input("Please enter the customer's package name: ")


def add_user(num_index):
        index = num_index
        if index not in record_index:
            add(index)
            reset = input("Is the information correct? (Y/N): ")
            reset = reset.upper()

            while True:
                if reset == "Y":
                    record_index.append(index)
                    break

                elif reset == "N":
                    add(index)
                    reset = input("Is the information correct? (Y/N): ")
                    reset = reset.upper()

                else:
                    print("Please enter Y for yes and N for no.")
                    reset = input("Is the information correct? (Y/N): ")
                    reset = reset.upper()

        else:
            print("Index {0} is taken. Please enter a new index.".format(index))


def update(search):
    search_result = "unknown"
    for b in record_index:
        if search == b:
            search_result = "found"
            print("Now updating index {0} customer's records.".format(b))
            package_name = input("Please enter the customer's package name: ")
            name = input("Please enter the Customer's name: ")
            check_in_date = input("Please enter the customer's check in date in the following format (ddmmyyyy): ")
            country = input("Please enter the customer's country of origin: ")
            phone_number = input("Please enter the customer's phone number: ")
            # add new category input

            # validating the user's inputs
            while True:
                if package_name.isalpha():
                    if name.isalpha():
                        if check_in_date.isdigit():
                            if country.isalpha():
                                if phone_number.isdigit():
                                    # Add new validate/store here add the new category under here and validate
                                        # push new information to here ->
                                    information = {"package_name": package_name, "name": name,
                                                   "check_in_date": check_in_date, "country": country,
                                                   "phone_number": phone_number}
                                    dictionary_index[search] = information
                                    print("Please check that customer index {0}'s information is correct".format(search))
                                    for a in information:
                                        print(a, "=", dictionary_index[search][a])
                                    break
                                # Add new else for validate

                                else:
                                    print("Phone number is not in numbers. Please retry.")
                                    phone_number = input("Please enter the customer's phone number: ")

                            else:
                                print("Country is not in alphabets. Please retry.")
                                country = input("Please enter the customer's country of origin: ")

                        else:
                            print("check in date is not in numbers. Please retry.")
                            check_in_date = input(
                                "Please enter the customer's check in date in the following format (ddmmyyyy): ")

                    else:
                        print("Name is not in alphabets. Please re-enter the Customer's name")
                        name = input("Please enter the Customer's name: ")
                else:
                    print("Package name is not in alphabets. Please retry.")
                    package_name = input("Please enter the customer's package name: ")

    if search_result == "unknown":
        print("Error customer index {0} does not exist.\nPlease try again.".format(search))
        try:
            search = int(input("Please enter the index for the customer you want a record of: "))
        except ValueError:
            print("Please try again")
        update(search)


def update_user():
    while True:
        try:
            search = int(input("Please enter the index for the customer you want a record of: "))
            update(search)
            break
        except UnboundLocalError:
            print("Please try again")

        except ValueError:
            print("Please try again")

    reset = input("Is the information correct? (Y/N): ")
    reset = reset.upper()

    while True:
        if reset == "N":
            update(search)
            reset = input("Is the information correct? (Y/N): ")
            reset = reset.upper()

        elif reset == "Y":
            break

        else:
            print("Please enter Y for yes and N for no.")
            reset = input("Is the information correct? (Y/N): ")
            reset = reset.upper()


def delete_user():
    delete_result = "unknown"
    delete = input("Please enter the index of the customer record to be deleted: ")

    for i in record_index:
        if delete == str(i):
            delete_result = "known"
            del dictionary_index[i]
            record_index.remove(i)
            print("Customer index {0}'s records have been deleted.".format(delete))

    if delete_result == "unknown":
        print("Customer index {0} can't be found. Please enter a valid customer index.".format(delete))


def display_user():
    print("")
    for i in record_index:
        print("This is the record of customer index {0}.".format(i))
        for a in dictionary_index[i]:
            print(a, "=", dictionary_index[i][a])
        print("")


def sortmenu():
    try:
        print("Select a sorting algorithm to perform")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        while True:
            try:
                sort_menu = int(input("Enter a sorting algorithm (1-3): "))
                break
            except ValueError:
                print("Please a number from 1 to 3.")
        while True:
            sortby = input("Please enter what do you want to sort the customer index by: ")
            for i in dictionary_index:
                for b in dictionary_index[i]:
                    if sortby == b:
                        check = "match"
                        break

                    else:
                        check = "no match"

            if check == "match":
                sortOrder = input("Please choose how you would like the sort result to display (A = Ascending order) (D = Descending order): ")
                sortOrder = sortOrder.upper()
                if sortOrder == "A" or "D":
                    if sort_menu == 1:
                        return bubbleSort_optimized(sortby, sortOrder)

                    elif sort_menu == 2:
                        return selectionSort(sortby, sortOrder)

                    elif sort_menu == 3:
                        return insertionSort(sortby, sortOrder)

                    else:
                        print("Invalid function number, try functions (1-3)!")

                else:
                    print("You did not select Ascending order or Descending order please try again")

            else:
                print("Please enter a valid category.")
                print("These are the valid categories to sortby.")
                print("package_name\nname\ncheck_in_date\ncountry\nphone_number")
                print("Please try again.")

    except UnboundLocalError:
        print("Please try again.")


# Sorts a sequence in ascending order using the
# optimized bubble sort algorithm
def bubbleSort_optimized(sortby, sortOrder):
    num_index_list = []
    type = ""
    list = []
    new_dictionary_index = {}
    for i in dictionary_index:
        for a in dictionary_index[i]:
            if a == sortby:
                if dictionary_index[i][a].isalpha():
                    sort = dictionary_index[i][a] + " from index " + str(i)
                    list.append(sort)
                    type = "string"
                else:
                    sort = dictionary_index[i][a]
                    num_index_list.append(i)
                    sort = int(sort)
                    list.append(sort)
                    type = "number"

    n = len(list)
    # Perform n-1 bubble operations on the sequence
    for i in range(n - 1, 0, -1):
        # Set boolean variable to check occurrence of swapping
        # in inner loop
        noSwap = True
        # Bubble the largest item to the end
        for j in range(i):
            if sortOrder == "A":
                if list[j] > list[j + 1]:
                    # Swap the j and j+1 items
                    tmp = list[j]
                    list[j] = list[j + 1]
                    list[j + 1] = tmp
                    # Set boolean variable value if swapping occurred
                    noSwap = False
            elif sortOrder == "D":
                if list[j] < list[j + 1]:
                    # Swap the j and j+1 items
                    tmp = list[j]
                    list[j] = list[j + 1]
                    list[j + 1] = tmp
                    # Set boolean variable value if swapping occurred
                    noSwap = False
        # Exit the loop if no swapping occurred
        # in the previous pass
        if noSwap:
            break
    if type == "string":
        for index in list:
            # using List comprehension + isdigit() +split()
            # getting numbers from string
            res = [int(i) for i in index.split() if i.isdigit()]
            for i in range(0, 1):
                res = int(res[i])
            new_dictionary_index[res] = dictionary_index[res]

    elif type == "number":
        for index in list:
            index = str(index)
            for num in num_index_list:
                if index == dictionary_index[num][sortby]:
                    num = int(num)
                    new_dictionary_index[num] = dictionary_index[num]

    print("")
    for p in new_dictionary_index:
        print("This is the record of customer index {0}.".format(p))
        for a in new_dictionary_index[p]:
            print(a, "=", new_dictionary_index[p][a])
        print("")

    return new_dictionary_index


def selectionSort(sortby, sortOrder):
    num_index_list = []
    type = ""
    list = []
    new_dictionary_index = {}
    for i in dictionary_index:  # For Every Element In Dict
        for a in dictionary_index[i]:  # For Every Element in Nested Dict
            if a == sortby:
                if dictionary_index[i][a].isalpha():
                    sort = dictionary_index[i][a] + " from index " + str(i)
                    list.append(sort)
                    type = "string"
                else:
                    sort = dictionary_index[i][a]
                    num_index_list.append(i)
                    sort = int(sort)
                    list.append(sort)
                    type = "number"

    n = len(list)

    for i in range(n - 1):
        # Assume the ith element is the smallest.
        currNdx = i
        # Determine if any other element contains a smaller value.
        for j in range(i + 1, n):
            if sortOrder == "A":
                if list[j] < list[currNdx]:  # find smaller
                    currNdx = j
            elif sortOrder == "D":
                if list[j] > list[currNdx]:  # find bigger
                    currNdx = j

        # Swap the ith value and currNdx value only if the
        # smallest value is not already in its proper position.
        if currNdx != i:
            tmp = list[i]
            list[i] = list[currNdx]
            list[currNdx] = tmp

    if type == "string":
        for index in list:
            # using List comprehension + isdigit() +split()
            # getting numbers from string
            res = [int(i) for i in index.split() if i.isdigit()]
            for i in range(0, 1):
                res = int(res[i])
            new_dictionary_index[res] = dictionary_index[res]

    elif type == "number":
        for index in list:
            index = str(index)
            for num in num_index_list:
                if index == dictionary_index[num][sortby]:
                    num = int(num)
                    new_dictionary_index[num] = dictionary_index[num]

    print("")
    for p in new_dictionary_index:
        print("This is the record of customer index {0}.".format(p))
        for a in new_dictionary_index[p]:
            print(a, "=", new_dictionary_index[p][a])
        print("")

    return new_dictionary_index


# Sorts a sequence in ascending order using the insertion sort
# algorithm
def insertionSort(sortby, sortOrder):
    num_index_list = []
    type = ""
    list = []
    new_dictionary_index = {}
    for i in dictionary_index:  # For Every Element In Dict
        for a in dictionary_index[i]:  # For Every Element in Nested Dict
            if a == sortby:
                if dictionary_index[i][a].isalpha():
                    sort = dictionary_index[i][a] + " from index " + str(i)
                    list.append(sort)
                    type = "string"
                else:
                    sort = dictionary_index[i][a]
                    num_index_list.append(i)
                    sort = int(sort)
                    list.append(sort)
                    type = "number"

    n = len(list)

    # Starts with the first item as the only sorted entry.
    for i in range(1, n):
        # Save the value to be positioned
        value = list[i]
    # Find the position where value fits in the
    # ordered part of the list.
        pos = i
        if sortOrder == "A":
            while pos > 0 and value < list[pos - 1]:
                # Shift the items to the right during the search
                list[pos] = list[pos - 1]
                pos -= 1
                # Put the saved value into the open slot.
            list[pos] = value

        elif sortOrder == "D":
            while pos > 0 and value > list[pos - 1]:
                # Shift the items to the left during the search
                list[pos] = list[pos - 1]
                pos -= 1
            # Put the saved value into the open slot.
            list[pos] = value

    if type == "string":
        for index in list:
            # using List comprehension + isdigit() +split()
            # getting numbers from string
            res = [int(i) for i in index.split() if i.isdigit()]
            for i in range(0, 1):
                res = int(res[i])
            new_dictionary_index[res] = dictionary_index[res]

    elif type == "number":
        for index in list:
            index = str(index)
            for num in num_index_list:
                if index == dictionary_index[num][sortby]:
                    num = int(num)
                    new_dictionary_index[num] = dictionary_index[num]
    print("")
    for p in new_dictionary_index:
        print("This is the record of customer index {0}.".format(p))
        for a in new_dictionary_index[p]:
            print(a, "=", new_dictionary_index[p][a])
        print("")

    return new_dictionary_index


def searchmenu():
    print("1. linear Search")
    print("2. Binary Search")
    try:
        search_menu = int(input("Enter a search algorithm (1-2): "))

    except ValueError:
        print("Please enter number 1 to 2.")

    new_dictionary_index = {}
    new_values = []

    if search_menu == 1:
        try:
            category = input("Please enter what you want to search: ")
            target = input("Please enter what you want to search in {0}: ".format(category))
            match = linearsearch(category, target)
            if len(match) != 0:
                print("\nThese customer index records match the search requirements of {0} from {1}".format(target, category))
                for i in match:
                    print("customer index {0} information: ".format(i))
                    for a in dictionary_index[i]:
                        print(a, "=", dictionary_index[i][a])
                    print("")
            else:
                print("There are no customer index records that matches your requirements.")

        except KeyError:
            print("Error {0} is not found.\nPlease try again".format(category))
            pass

    elif search_menu == 2:
        try:
            category = input("Please enter what you want to search : ")
            target = input("Please enter what you want to search in {0} : ".format(category))
            match = binarysearch(category, target)
            if len(match) != 0:
                print("\nThese customer index records match the search requirements of {0} from {1}".format(target, category))
                for i in match:
                    print("customer index {0} information: ".format(i))
                    for a in dictionary_index[i]:
                        print(a, "=", dictionary_index[i][a])
                    print("")
            else:
                print("There are no customer index records that matches your requirements.")

        except KeyError:
            print("Error {0} is not found.\nPlease try again".format(category))
    else:
        print("Invalid function number, try functions (1-2)!")

def linearsearch(category, target):
    # target is like all the index with name that matches the target
    match = []
    for i in record_index:
        if dictionary_index[i][category] == target:
            match.append(i)

        elif dictionary_index[i][category] != target:
            continue

    return match


def binarysearch(category, target):
    match = []
    value_list = []
    index_list = []
    for i in record_index:
        value_list.append(dictionary_index[i][category])
        index_list.append(i)

    low = 0
    high = len(value_list)

    while low <= high:
        mid = (high + low) // 2
        if value_list[mid] == target:
            for index in index_list:
                for value in value_list:
                    if value == target:
                        match.append(index)
                        break
            return match

        elif target < value_list[mid]:
            high = mid - 1

        elif target > value_list[mid]:
            low = mid + 1
    return match


while True:
    menu()
    instruction = input("Option: ")
    instruction = instruction.upper()

    if instruction == "1":
        if len(record_index) < 19:
            num_index += 1
            add_user(num_index)
        elif len(record_index) > 19:
            print("There is more then 20 customers currently.")

    elif instruction == "2":
        update_user()

    elif instruction == "3":
        delete_user()

    elif instruction == "4":
        display_user()

    elif instruction == "5":
        new_record_index = []
        dictionary_index = sortmenu()
        for i in dictionary_index:
            new_record_index.append(i)

        record_index = new_record_index

    elif instruction == "6":
        searchmenu()

    elif instruction == "EXIT":
        if instruction == "EXIT":
            print("You have exited the program.\nPlease have a great day!")
            break

        else:
            print("error occurred.")
            break

    else:
        print("Invalid option please try again.")
