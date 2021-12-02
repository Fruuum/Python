from time import sleep


class TrafficLight:
    __color = "none"

    def running(self):
        all_time = int(input("введите длительность работы светофора: "))
        while True:
            if all_time <= 0:
                print("\r{}\033[0m".format(""), end="")
                print("TrafficLight switch off")
                break
            elif all_time >= 0:
                print(("\r\033[31m\033[41m{}\033[0m".format(self.__color)), end="")
                sleep(7)
                all_time -= 7
            elif all_time >= 0:
                print(("\r\033[33m\033[43m{}\033[0m".format(self.__color)), end="")
                sleep(2)
                all_time -= 2
            elif all_time >= 0:
                print(("\r\033[32m\033[42m{}\033[0m".format(self.__color)), end="")
                sleep(7)
                all_time -= 7


run_fct = TrafficLight()
run_fct.running()
