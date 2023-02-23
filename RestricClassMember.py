class JustCounter:
    __secretCount = 0

    def count(self):
        JustCounter.__secretCount += 1
        print(JustCounter.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter.__secretCount) # this will return error as it is restricted within the class itself
# print(counter._JustCounter__secretCount)

"""
class JustCounter:
    secretCount = 0

    def count(self):
        JustCounter.secretCount += 1
        print(JustCounter.secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter.secretCount) # this will return error as it is restricted within the class itself
"""
