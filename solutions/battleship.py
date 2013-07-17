import random

class Ship:

    def __init__(self):
        self.name =''
        self.size = 0
        self.id = 0

    def set_ship(self,info): 
        self.id = info[0]
        self.name = 'submarine'if info[1] == 3 else 'patrol'
        self.name = self.name + ' ' + str(self.id)
        self.size = info[1]

    def get_id(self):
        return self.id

    def get_health(self):
        return self.size

    def hit_ship(self):
        self.size -= 1


class BattleShipGame:

    def __init__(self,size=5,num=3):
        self.size = size
        self.ship_num = num
        self.grids = []
        self.counter = 1
        self.ships = []

    # set position of each ship
    def set_up_game(self):
        self.grids = [0] * self.size ** 2

        for i in range(self.ship_num):
            info = self.set_location()
            if not info:
                break 
            ship = Ship()
            ship.set_ship(info)
            self.ships.append(ship)

    def set_location(self):
        success = False
        attempt = 0
        gridsize = len(self.grids)
        # vertical if odd, otherwise horizontal 
        incr = self.size if self.counter%2 == 1 else 1

        ship_id = self.counter
        # size 2 / 3
        ship_size = random.randint(0,1) + 2

        while not success and attempt < 200:
            attempt += 1
            ps = random.randint(0,gridsize-1)

            if self.grids[ps]:
                continue

            success = True
            temp = ship_size - 1
            loc = ps + incr
            while success and temp:
                temp -= 1
                if loc >= gridsize or self.grids[loc]:
                    success = False
                elif loc > 0 and loc % self.size == 0:
                    success = False
                loc = loc + incr

        if success:
            for i in range(ship_size):
                self.grids[ps+i*incr]= ship_id

            self.counter += 1
            return (ship_id, ship_size)

        return 

    # playing 
    def playing(self):
        guess_times = 0
        print "There are %d ships, try to sink them!" % len(self.ships)
        while self.ships:
            guess_times += 1
            self.get_input()

        print "Totally, You guessed %d times to sunk all ships." % guess_times

    # get user input 
    def get_input(self):
        try:
            s = raw_input("You guess:")
            ps = s.split(',')
            X = int(ps[0])
            Y = int(ps[1])

            if X < 0 or Y < 0 or X >= self.size or Y >= self.size:
                raise Exception()

            self.check_input(X,Y)
        except:
            print "Input format: X,Y (X, Y are in [0, %d])" % (self.size - 1)

    # check user input
    def check_input(self, X, Y):
        index = X * self.size + Y

        v = self.grids[index]
        if v:
            self.grids[index]=0
            ship = self.sunk(v)
            if ship:
                self.ships.remove(ship)
                print "You sunk ship: "+ship.name
            else:
                print 'hit'
        else:
            print 'miss'

    # check if ship sink or not.
    def sunk(self, v):
        for ship in self.ships:
            if ship.get_id() == v:
                ship.hit_ship()
                if ship.get_health() == 0:
                    return ship
        return False

    # used for testing
    def print_grids(self):
        temp = 0
        for i in range(self.size **2):
            temp += 1
            if temp == self.size:
                print self.grids[i]
                temp = 0
            else:
                print self.grids[i],

    def print_ships(self):
        for ship in self.ships:
            print "name:%s, size:%s" % (ship.name, ship.size)


def main():
    game = BattleShipGame()
    game.set_up_game()
    game.playing()

    # test 
    # test set position function, output the grids
    #game.print_grids()
    #game.print_ships()

if __name__=="__main__":
    main()

