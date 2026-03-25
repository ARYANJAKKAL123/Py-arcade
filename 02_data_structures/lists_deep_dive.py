#1 List with different tpye of Data type

def mixed_list():
    game_data=["Aryan",100,True]
    print(f"Printing the list with different type of content: {game_data}")

#2 Updating a list 

def update_list():
    items = ["Swords","Shield", "Potion"]
    print(f"Original List: {items}")
    items[1] = "Magic Shield"

    print(f"Updated List: {items}")

#3 Insertion in List

def insertion_list():

    items = ["Swords","Shield", "Potion"]
    items.insert(1,"Map")
    print(f"Updated List is: {items}")

#4 Sorting a List

def sort_list():
    items = ["Swords","Shield", "Potion"]
    items.sort(key= str.lower)
    print(f"Sorted List is: {items}")
    
#5 Copying the List

def copy_list():
      items = ["Swords","Shield", "Potion"]
      copy = items[:]
      print(f"The copy List: {copy}")



def main():
    mixed_list()
    update_list()
    insertion_list()
    sort_list()
    copy_list()

if __name__ == "__main__":
    main()