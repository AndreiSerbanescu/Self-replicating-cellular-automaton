
class RuleInitialiser:

    def __init__(self, filename):
        self.file = open(filename, "r")

    def generate_dict(self):

        #FORMAT CNESWC
        self.dict = dict()

        for line in self.file:
            cnesw = line[:5]
            centre = line[0]
            new_centre = line[5]
            nesw = line[1:5]

            new_nesw = nesw

            for i in range(4):
                new_nesw = self.rotate(new_nesw)
                new_key = "".join(centre + new_nesw)
                self.dict.update({new_key : new_centre})

        return self.dict

    def rotate(self, nesw):
        #TODO delete hard-coding
        result = list("    ")

        for i in range(len(nesw)):
            if i + 1 == len(nesw):
                index = 0
            else:
                index = i + 1

            result[index] = nesw[i]

        return "".join(result)

ri = RuleInitialiser("rules.txt")

#print(ri.generate_dict())