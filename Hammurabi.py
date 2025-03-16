import random

class Hammurabi:

    def __init__(self):
        self.rand = random.Random()

    def main(self):
        self.playGame()

    def playGame(self):
        self.population = 100
        self.grain = 2800
        self.land = 1000
        self.land_val = 19
        # declare local variables here: grain, population, etc.
        # statements go after the declarations

    # other methods go here
    def askHowManyAcresToBuy(self):
        acresSold = int(input("How many acres will you buy?"))
        return acresSold

    def askHowManyAcresToSell(self):
        acresBought = int(input("How many acres will you sell?"))
        return acresBought

    def askHowMuchGrainToFeedPeople(self):
        feedPeople = int(input("How much grain will you give to your people?"))
        return feedPeople

    def askHowManyAcresToPlant(self):
        acresToPlant = int(input("How many acres will you plant?"))
        return acresToPlant

    def plagueDeaths(self, population):
       if random.randint(0,99) < 16:
        deaths = population / 2
        return deaths

    def starvationDeaths(self, population, bushelsFedToPeople):
        return 0

    def uprising(self, population, howManyPeopleStarved):
       if howManyPeopleStarved > population * (45 / 100):
        return True

    def immigrants(self, population, acresOwned, grainInStorage):
        pass

    def harvest(self, acres, bushelsUsedAsSeed):
        pass

    def grainEatenByRats(self, bushels):
        return 0

    def newCostOfLand(self):
        land_val = random.randint(17,23)
        return land_val

    def summary(self, population, grain, land, land_val):


        print(

        "O great Hammurabi!\n"
        "You are in year 1 of your ten year rule.\n"
        "In the previous year 0 people starved to death.\n"
        "In the previous year 5 people entered the kingdom.\n"
        "The population is now " + str(population) + ".\n"
        "We harvested " + str(grain) + " bushels at " + str(land_val) + " bushels per acre.\n"
        "Rats destroyed 200 bushels, leaving 2800 bushels in storage.\n"
        "The city owns " + str(land) + " acres of land.\n"
        "Land is currently worth " + str(land_val) + " bushels per acre.\n"


        )

    def finalSummary(self):
        pass


if __name__ == "__main__":
    hammurabi = Hammurabi()
    hammurabi.main()
    hammurabi.askHowManyAcresToBuy()
    hammurabi.askHowManyAcresToSell()
    hammurabi.askHowMuchGrainToFeedPeople()
    hammurabi.askHowManyAcresToPlant()
    hammurabi.summary(100,2800,1000,19)
