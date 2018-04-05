import os

class Olympian:
    __next_ID = -1

    def __init__(self, ID_number, name, sport, num_medals):
        if ID_number == '':
            Olympian.__next_ID += 1
            self.__ID_number = Olympian.__next_ID
        else:
            self.__ID_number = ID_number
            Olympian.__next_ID = int(ID_number)

        self.__name = name
        self.__sport = sport
        self.__num_medals = num_medals


def main():
    print("P4: Olympians Tong Zhou")

    olympians_list = []
    # check if results.txt doesnt exists or if is empty
    # TEST1: remove results.txt from current working directory or results.txt is empty file, will execute else statement and make a new 'results.txt'
    if (not os.path.isfile('results.txt')) or (not os.stat("results.txt").st_size == 0):
        # TEST3: initailize olympian list with 3 olympians and one with no ID
        olympians_list.append(Olympian("1", "Ann", "Skiing", "9"))
        olympians_list.append(Olympian("2", "Ben", "Skating", "10"))
        olympians_list.append(Olympian("", "Leslie", "Running", "4"))

        # print out the olympians list
        print("%10s %10s %10s %10s\n" %
              ("ID Number", "Name", "Sport", "Number of Medals"))
        for olympian in olympians_list:
            print("%10s %10s %10s %10s\n" %
                  (olympian._Olympian__ID_number, olympian._Olympian__name, olympian._Olympian__sport, olympian._Olympian__num_medals))
        # print total medals
        print("%33s %10s\n" % ('', '================='))
        print("%33s %10s\n" % ('', str(compute_medals(olympians_list))))
       # create and write to results.txt if doesnt exist
        file_out = open('results.txt', 'w+')

        for olympian in olympians_list:
            file_out.write(str(olympian._Olympian__ID_number) + ' ' + olympian._Olympian__name +
                           ' ' + olympian._Olympian__sport + ' ' + str(olympian._Olympian__num_medals) + '\n')
        file_out.close()
        print("Olympian list added to results.txt. Exiting program...\n")
        return 0

    else:
        # read in from result.txt
        try:
            file_in = open('results.txt')
            # TEST2: Only put one olympian in results.txt and print to console
            line_list = file_in.readlines()
            for line in line_list:
                line_content = line.strip('\n').split(' ')
                readIn_ID_number = line_content[0]
                readIn_name = line_content[1]
                readIn_sport = line_content[2]
                readIn_num_medal = line_content[3]
                if int(readIn_num_medal) < 0:
                    print("Invalid number of medals. Exiting program...\n")
                    return 0

                olympians_list.append(Olympian(readIn_ID_number, readIn_name,
                                               readIn_sport, readIn_num_medal))
            # print out the olympians list
            print("%10s %10s %10s %10s\n" %
                  ("ID Number", "Name", "Sport", "Number of Medals"))

            for olympian in olympians_list:
                print("%10s %10s %10s %10s\n" % (str(olympian._Olympian__ID_number),
                                                 olympian._Olympian__name, olympian._Olympian__sport, str(olympian._Olympian__num_medals)))
            
            print("%33s %10s\n" % ('', '================='))
            print("%33s %10s\n" % ('', str(compute_medals(olympians_list))))

            file_in.close()

        except IOError as e:
            # TEST4: If read error, will raise exception
            print("Cannot find results.txt")

    return 0

def compute_medals(Olympian_list):
    total_medals=0
    for olympian in Olympian_list:
        total_medals=total_medals + int(olympian._Olympian__num_medals)
    return total_medals


if __name__ == "__main__":
    main()
