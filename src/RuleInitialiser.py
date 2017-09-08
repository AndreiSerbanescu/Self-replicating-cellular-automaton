
class RuleInitialiser:

    def __init__(self, filename):
        self.file = open(filename, "r")

    def generate_dict(self):

        #FORMAT CNESWC
        self.dict = dict()
        for line in self.file:
            old_centre = line[0]
            nesw = line[1:5]
            cnesw = line[:5]
            new_centre = line[5]

            self.dict.update({(old_centre + nesw) : new_centre})


            for i in range(3):
                new_cnesw = old_centre + self.rotate(i + 1, nesw)
                self.dict.update({new_cnesw : new_centre})



        return self.dict

    #PRE - times >= 1 and <= 3 and nesw has 4 characters
    def rotate(self, times, nesw):
        new_nesw = list("    ")

        for i in range(len(nesw)):
            new_nesw[(i + times) % len(new_nesw)] = nesw[i]

        return "".join(new_nesw)


ri = RuleInitialiser("rules.txt")

print(ri.generate_dict())