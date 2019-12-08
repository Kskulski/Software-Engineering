class TimeSetter:
    def convert(self, d):
        y = 1980
        while d > 365:
            if (y % 400 == 0) or \
                    (y % 4 == 0 and y % 100 !=0):
                if d > 365:
                    d -= 366
                    y += 1
            else:
                d -= 365
                y += 1

        return y