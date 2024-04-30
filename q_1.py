from datetime import datetime
class Star_Cinema:
    __hall_list = []
    def entry_hall(self,hall) -> None:
        self.__hall_list.append(hall)

class Hall(Star_Cinema):

    def __init__(self,rows,cols,hall_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        super().__init__()
        self.entry_hall(self)

    def entry_show(self,id,movie_name,time):
        tpl = (id,movie_name,time)
        self.__show_list.append(tpl)
        self.__seats[id] = [[0 for _ in range(self.rows)] for _ in range (self.cols)]

    def book_seats(self,id,seat_no):
        if id in self.__seats:
            for st in seat_no:
                if 0<=st[0]<self.rows and 0<=st[1]<self.cols:
                    for key, val in self.__seats.items():
                        if val[st[0]][st[1]] == 0:
                            val[st[0]][st[1]] = 1
                        else:
                            print('Already Booked')
                else:
                    print('Invalid Input')
        else:
            print('Show Not Found')
    
    def view_show_list(self):
        print('-----------------')
        for list in self.__show_list:
            print(f'MOVIE NAME:{list[1]}({list[0]}) SHOW ID:{list[0]} TIME:{list[2]}')
        print('-----------------')

    def view_available_seats(self,id):
        if id not in self.__seats:
            print('Invalid Input')
            print(' ')
        else:
            for st in self.__seats[id]:
                print(st)
        

sony = Hall(7,7,101)
sony.entry_show('101','jawan movie', datetime.today())
sony.entry_show('102','Rajkuram', datetime.today())
sony.entry_show('103','Dabang', datetime.today())

while True:
    print("1. View All Shows Today")
    print("2. View Available Seats")
    print("3. Book Tickets")
    print("4. Exit")
    # print(' ')

    option = int(input('Enter Option: '))
    if option == 1:
        sony.view_show_list()

    if option == 2:
        id = input('Enter Show Id: ')
        sony.view_available_seats(id)

    if option == 3:
        book_seat = []
        id = input('Show Id: ')
        n = int(input('Number of Ticket?: '))
        for _ in range(n):
            row = int(input('Enter Seat Row: '))
            col = int(input('Enter Seat Col: '))
            lst = (row,col)
            book_seat.append(lst)
            sony.book_seats(id,book_seat)
    
    if option == 4:
        break
