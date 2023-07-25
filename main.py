import requests
from pprint import pprint
import os

# remove previous file
if os.path.exists("recipe.txt"):
    os.remove("recipe.txt")
# declare a dict
ThisDict = [
]
colfunc = 0


#                          ***********************
#                          ****** FUNCTIONS ******
#                          ***********************
# declare a function for: search the list of recipe
def RecipeSearch(ingredient):
    AppKey = "d32236e0519bd121151596b8b134e167"
    AppId = "f21a3917"
    url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, AppId, AppKey)
    response = requests.get(url)
    rec = response.json()
    return rec['hits']


# declare a function for: add a new record to dictionary
def AddNewDict(Label, URL, DishType, Cal):
    NewList = {
        'Label': Label,
        'URL': URL,
        'DishType': DishType,
        'Cal': Cal
    }
    ThisDict.append(NewList)


# print the list of recipe and show just LABEL
def PrintList(results):
    for counter in results:
        recipe = counter['recipe']
        # add a new record to dictionary
        AddNewDict(recipe['label'], recipe['url'], recipe['dishType'], recipe['calories'])
        with open("recipe.txt", "a+") as Myfile:
            Myfile.write(recipe['label'] + "\n")
    i = 0
    while i < len(ThisDict):
        print(f"{ThisDict[i]['Label']}")
        i = i + 1


# declare functions for sorting
def get_name(ThisDict):
    return ThisDict.get('Label')


def get_Cal(ThisDict):
    return ThisDict.get('Cal')


# declare functions to sort the list by (Label or calories)
def SortList(SortBy, ThisDict, colfunc):
    i = 0
    while i < len(ThisDict):
        # print(colfunc)
        if colfunc == 1:
            print(f"\033[1m{ThisDict[i][SortBy]}\033[0m {ThisDict[i]['Cal']} calories")
            i = i + 1
        else:
            print(f"\033[1m{ThisDict[i][SortBy]}\033[0m has {ThisDict[i]['Cal']} calories")
            i = i + 1


# declare functions for: Display the recipes for each search result
def DisplayUrl(recipe):
    print("\nYou can find instruction for \033[1m" + recipe + "\033[0m :")
    for x in ThisDict:
        if x['Label'] == recipe:
            print(x['URL'])
    return


# declare functions for:Show menu
def ShowMenu():
    Menu = input("\nChoose your \033[1mNumber\033[0m:"
                 "\n 1)Print Your list with all info "
                 "\n 2)Sort your list by Label/calories "
                 "\n 3)Receive the Recipe "
                 "\n 4)Define ingredient calorie categories from low to high"
                 "\n 5)Exit \n"
                 )
    return Menu


# declare functions for: Choose menu
def ChooseMenu(test):
    if test == "1":
        colfunc = 0
        # Print the list with all info
        SortList("Label", ThisDict, colfunc)
        # Show menu to user and call ChooseMenu func inside ChooseMenu
        test = ShowMenu()
        ChooseMenu(test)
    elif test == "2":
        colfunc = 0
        # sorting by Label/calories
        answer = input("Do you like to sort your list by\033[1m label\033[0m or \033[1mcalories\033[0m:")
        if answer == "label":
            print("\n \033[1m SORTED BY LABEL \033[0m \n")
            ThisDict.sort(key=get_name)
            SortList("Label", ThisDict, colfunc)
        elif answer == "calories":
            print("\n \033[1m SORTED BY CALORIES \033[0m \n")
            ThisDict.sort(key=get_Cal)
            SortList("Label", ThisDict, colfunc)
        # Show menu to user and call ChooseMenu func inside ChooseMenu
        test = ShowMenu()
        ChooseMenu(test)
    elif test == "3":
        # first print the list and then show url
        # print list
        print("\033[1mYOUR LIST IS: \033[0m")
        i = 0
        while i < len(ThisDict):
            print(f"{ThisDict[i]['Label']}")
            i = i + 1
        ReqUrl = input("\n \nChoose your recipe form the list: ")
        # show url
        DisplayUrl(ReqUrl)
        # Show menu to user and call ChooseMenu func inside ChooseMenu
        test = ShowMenu()
        ChooseMenu(test)
    elif test == "4":
        colfunc = 1
        print(colfunc)
        for item in ThisDict:
            if item['Cal'] < 100:
                item['Cal'] = 'is low in'
            elif item['Cal'] < 350:
                item['Cal'] = 'is a mid range of'
            else:
                item['Cal'] = 'is high in'
        SortList("Label", ThisDict, colfunc)
        test = ShowMenu()
        ChooseMenu(test)
    elif test == "5":
        print("Thanks for using our service, see you later :)")
        exit()
    else:
        print("Thanks for using our service, feel free to re-start the program and search for a new ingredient! :)")
        exit()
    # elif test == "4":
    #     print("Thanks and see you later :)")
    #     exit()
    # else:
    #     print("Thanks and see you later :)")
    #     exit()


#                          ***********************
#                          ****** MAIN CODE ******
#                          ***********************
ingredient = input('What ingredient would you like to include in recipe: ')
print(f"\n Your list for \033[1m{ingredient}\033[0m is:\n ")
# search list
results = RecipeSearch(ingredient)
# show labeles and save them in a file
PrintList(results)
# Show menu to user
test = ShowMenu()
# call ChooseMenu to do main program
ChooseMenu(test)


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
