import random

class Hammurabi:

    def __init__(self):
        self.rand = random.Random()

    def main(self):
        self.playGame()


    def playGame(self):


            population = 100
            grain = 2800
            acre = 1000
            land_val = 19
            bushels = 2000
            harvest = 0
            starved = 0
            feed = 0
            fed = 0
            immigrants = 0
            total_starved = 0
            bushelsPerAcre = 0
            ratsDestroyed = 0

            acresSold = 0
            sacresBought = 0
            grainFood = 0
            acresToPlant = 0

        # declare local variables here: grain, population, etc.
        # statements go after the declarations
            for i in range(1,11):


                print(
                "=================================\n"
                "O great Hammurabi!\n"
                "You are in year " + str(i) + " of your ten year rule.\n"
                "In the previous year " + str(total_starved) + " people starved to death.\n"
                "In the previous year " + str(immigrants ) + " people entered the kingdom.\n"
                "The population is now " + str(population) + ".\n"
                "We harvested " + str(grain) + " bushels at " + str(land_val) + " bushels per acre.\n"
                "Rats destroyed " + str(ratsDestroyed) + " bushels, leaving 2800 bushels in storage.\n"
                "The city owns " + str(acre) + " acres of land.\n"
                "Land is currently worth " + str(land_val) + " bushels per acre.\n"
                "==================================\n"
                )


                bought_land = Hammurabi.askHowManyAcresToBuy(bushels, land_val)
                if int(bought_land) > 0:
                    bushels = int(bushels) - (int(bought_land) * int(land_val))
                    acre = int(acre) + int(bought_land)

                sell = Hammurabi.askHowManyAcresToSell(land_val, bushels, acre)
                if int(sell) > 0:
                    bushels = int(bushels) + (int(sell) * int(land_val))
                    acre = int(acre) - int(sell)

                feed = Hammurabi.askHowMuchGrainToFeedPeople(bushels)
                feed = bushels - feed

                plant = Hammurabi.askHowManyAcresToPlant(acre, population, bushels)
                bushels = bushels - plant




             #   if i == 10:
             #       return "end of loop"


    #other methods go here
    def askHowManyAcresToBuy(bushels, land_val):
        acresBought = int(input("How many acres will you buy?"))
        while int(acresBought) * int(land_val) > int(bushels):
            print(f"O Hammurabi, I'm not questioning your Wiseness, but we only have " + str(bushels) + "bushels of grain.")
            acresBought = int(input("How many acres will you buy?\n"))
        return acresBought

    def askHowManyAcresToSell(land_val, bushels, acre):
        sell = int(input("How many acres will you sell?"))
        while int(sell) > int(acre):
            print(f"Our kindgom can't face being in debt to these heathen. We only have " + str(acre) + "acres of land.\n")
            sell = int(input("How many acres will you sell?"))
        return sell

    def askHowMuchGrainToFeedPeople(bushels):
        feed = int(input("How much grain will you give to your people?"))
        while feed > bushels:
            print(f"God bless you O Hammurabi for your generous spirit, but we have only " + str(bushels) + "bushels of grain left.")
            feed = int(input("How much grain will you give to your people?"))
        return feed

    def askHowManyAcresToPlant(acre, population, bushels):
        plant = int(input("How many acres will you plant?"))
        while plant > (population * 10):
            print(f"Slavery is so--like--last kingdom, O Hammurabi one. You are more wise than that.\n")
            plant = int(input("How many acres will you plant?\n"))
        while (plant * 2) > bushels:
            print(f"Our farmers crunched the numbers and there's not enough grain to fill that request. \n")
            plant = int(input("How many acres will you plant?\n"))
        while plant > acre:
            print(f"God's Kingdom reaches from the firmanent to the bottom of the seas. Our Kingdom pales in comparison.\n We only have " + str(acre) +"acres of land.")
            plant = int(input("How many acres will you plant?\n"))
        return plant

    def plagueDeaths(population):
        if random.randint(0,99) < 16:
            deaths = population / 2
        return deaths

    def starvationDeaths(population, bushelsFedToPeople):
        if bushelsFedToPeople < 20 * population:
            return 5


    def uprising(population, howManyPeopleStarved):
        if howManyPeopleStarved > population * (45 / 100):
            return True

    def immigrants(population, acresOwned, grainInStorage):
            pass

    def harvest(acres, bushelsUsedAsSeed):
            pass

    def grainEatenByRats(bushels):
            return 0

    def newCostOfLand(self):
        land_val = random.randint(17, 23)
        return land_val



    def finalSummary(self):
        pass



if __name__ == "__main__":
    hammurabi = Hammurabi()
    hammurabi.main()