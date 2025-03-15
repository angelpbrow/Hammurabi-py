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

        pass

    def askHowManyAcresToSell(self):
        pass

    def askHowMuchGrainToFeedPeople(self):
        pass

    def askHowManyAcresToPlant(self):
        pass

    def plagueDeaths(self, population):
        pass

    def starvationDeaths(self, population, bushelsFedToPeople):
        pass

    def uprising(self, population, howManyPeopleStarved):
        pass

    def immigrants(self, population, acresOwned, grainInStorage):
        pass

    def harvest(self, acres, bushelsUsedAsSeed):
        pass

    def grainEatenByRats(self, bushels):
        pass

    def newCostOfLand(self):
        pass

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
    hammurabi.summary(100,2800,1000,19)
