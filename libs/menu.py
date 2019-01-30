"""
This Module it is used to create well formatted and flexible text menus.
"""
import os
import sys


class Menu:
    """
    Class Menu it is the only class and it is used to create the simple text menus, it is modifiable through some
    arguments and could also handle the loop for the selection returning a tuple with the selected item

    Methods

    change_cols: Used to change the reserved columns for each field on the menu

    add_item: Used to add items to the menu

    print_page: Used to print an specific page of the menu

    __clear: Used to clear the terminal window, it depends on OS to issue clear or cls it should be work on windows and linux

    __previous_page: Used to navigate to a previous menu page

    __next_page: Used to navigate to the nex menu page

    loop: used to get the user input through a loop
    """

    def __init__(self):
        """
        Initialization Function

        Arguments

        menu_title: It is used to change the Title of the Menu, it is always shown at the beginning of the menu

        menu_subtitle: It is used for the Subtitle of the Menu, optional and it is only shown below the Title if has a value

        len_page: It is the argument to control the length of each page of the menu

        curr_page: It is used to know which page is rendering

        prompt: It is used to change the Prompt of the menu
        """
        self.menu_title = 'MENU TITLE'
        self.menu_subtitle = ''
        self.len_page = 5
        #Private Variable created to fill the menu has a structure:
        #{page_number(int):[(item_number(int), item_name(str), item_description(str)), (1, 'Item 1', 'Description 1')]}
        self.__items = {}
        self.curr_page = 1
        #Number of columns reserved for item numbers
        self.__num_col = 2
        #Number of columns reserved for the item names
        self.__item_col = 20
        #Number of columns reserved for the item description
        self.__desc_col = 40
        self.prompt = 'Enter your selection: '
        #Counter for menu items
        self.__count_items = 1

    def change_cols(self, num, item, desc):
        """
        This method is used to change the reserved columns for watch field in the menu

        Parameters

        num: Columns used for the number field in the menu

        item: Columns used for the item field in the menu

        desc: Columns used for the description field in the menu
        """
        self.__num_col = num
        self.__item_col = item
        self.__desc_col = desc

    #This function fill the __items dictionary to organize everything in pages and items for pages
    def add_item(self, item, desc):
        """
        Method used to add items to the Menu

        Parameters

        item: Item name

        desc: Description of the item
        """
        if len(self.__items) == 0:
            #Adding first element in the first page
            self.__items[1] = [(str(self.__count_items), item, desc)]
        else:
            last_page = self.__items.keys()[-1]
            if len(self.__items[last_page]) < self.len_page:
                #Adding elements on the last page
                self.__items[last_page].append((str(self.__count_items), item, desc))
            else:
                #Creating a new page and adding the element if the length of the page was passed
                self.__items[last_page + 1] = [(str(self.__count_items), item, desc)]

        self.__count_items += 1

    def print_page(self, page):
        """
        It prints in a pre-established format the page of the menu

        Arguments

        page: Page number to print

        Navigation Keys

        n: next page
        p: previous page
        q: quit

        Notes

        The format establishes the print of the Title first, the subtitle second it it exists, the items to fill one page
        and regulated by the len_page parameter, at the end prints the instructions to navigate also with the indication
        on which page you are, there are lines that delimits the diferent fields, if a menu has more pages the top and
        bottom boundaries could change from "solid" lines to "arrows" to indicate that there are more items on previous
        or following pages.
        """
        last_page = self.__items.keys()[-1]
        total_col = self.__num_col + self.__item_col + self.__desc_col + 2
        print('+' + total_col * '-' + '+')
        #Print Title
        print('|' + self.menu_title[:total_col] + (total_col - len(self.menu_title)) * ' ' + '|')
        #Print Subtitle if Exists
        if self.menu_subtitle:
            print('+' + total_col * '-' + '+')
            print('|' + self.menu_subtitle[:total_col] + (total_col - len(self.menu_subtitle)) * ' ' + '|')
            #Change the boundary if there are previous pages to arrows
            if (page - 1) in self.__items.keys():
                print('^' + total_col * '^' + '^')
            else:
                print('+' + total_col * '-' + '+')
        else:
            #Change the boundary if there are previous pages to arrows
            if (page - 1) in self.__items.keys():
                print('^' + total_col * '^' + '^')
            else:
                print('+' + total_col * '-' + '+')
        #Print the page of the menu
        if self.__items:
            j = 1
            for i in self.__items[page]:
                menu_line = '|' + i[0][:self.__num_col] + (self.__num_col - len(i[0])) * ' ' + '|'
                menu_line = menu_line + ' ' + i[1][:self.__item_col - 1] + (self.__item_col - len(i[1]) - 1) * ' ' + '|'
                menu_line = menu_line + ' ' + i[2][:self.__desc_col - 1] + (self.__desc_col - len(i[2]) - 1) * ' ' + '|'
                print(menu_line)
                j += 1
            #Change the boundary if there are following pages to arrows
            if (page + 1) in self.__items.keys():
                print('v' + total_col * 'v' + 'v')
            else:
                print('+' + total_col * '-' + '+')
        #Print Navigation Instructions at the left and current page and total number of pages at the right
        if ((page + 1) in self.__items.keys()) and ((page - 1) in self.__items.keys()):
            print('n: next p: previous q: quit' + ' ' * (total_col - 27 - 14 + 2) + '#page %02d of %02d' % (
                self.curr_page, last_page))
        elif ((page + 1) in self.__items.keys()) and not ((page - 1) in self.__items.keys()):
            print('n: next q: quit' + ' ' * (total_col - 15 - 14 + 2) + '#page %02d of %02d' % (
                self.curr_page, last_page))
        elif not ((page + 1) in self.__items.keys()) and ((page - 1) in self.__items.keys()):
            print('p: previous q: quit' + ' ' * (total_col - 19 - 14 + 2) + '#page %02d of %02d' % (
                self.curr_page, last_page))
        else:
            print('q: quit' + ' ' * (total_col - 7 - 14 + 2) + '#page %02d of %02d' % (self.curr_page, last_page))

    def __clear(self):
        """
        Method to Clear the terminal window, it should work on linux and windows
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def __previous_page(self):
        """
        Method to navigate to the previous page.
        """
        #It decrements the current page in one of it is not the first
        if self.curr_page != 1:
            self.curr_page -= 1

    def __next_page(self):
        """
        Method to navigate to the next page.
        """
        #It increment the current page if it is not the last one
        last_page = self.__items.keys()[-1]
        if self.curr_page != last_page:
            self.curr_page += 1

    def loop(self):
        """
        Method to enter in a loop for the user input

        Returns

        Returns a tuple with the format (item_number, item_name, item_description) of the selected option
        """
        #Error initialization
        error = False
        #Clear terminal, print the first page and wait for input user
        self.__clear()
        self.print_page(self.curr_page)
        resp = input(self.prompt)

        #Private list with the item numbers available on the current page
        item_numbers = []
        for i in self.__items[self.curr_page]:
            item_numbers.append(i[0])

        #Navigation decisions
        if resp == 'p':
            self.__previous_page()
        elif resp == 'n':
            self.__next_page()
        elif resp == 'q':
            sys.exit(0)
        else:
            error = True

        #Loop for the rest of the ser inputs
        while not (resp in item_numbers):
            self.__clear()
            self.print_page(self.curr_page)
            #Print the error if exists
            if error:
                print('##Error## Please select a number from the menu')
            resp = input(self.prompt)
            #Navigation Decisions
            if resp == 'p':
                self.__previous_page()
                error = False
            elif resp == 'n':
                self.__next_page()
                error = False
            elif resp == 'q':
                sys.exit(0)
            else:
                error = True
            item_numbers = []
            for i in self.__items[self.curr_page]:
                item_numbers.append(i[0])

        #Return tuple with selection
        return (self.__items[self.curr_page][int(resp) - (self.len_page * (self.curr_page - 1)) - 1][0],
                self.__items[self.curr_page][int(resp) - (self.len_page * (self.curr_page - 1)) - 1][1],
                self.__items[self.curr_page][int(resp) - (self.len_page * (self.curr_page - 1)) - 1][2])
