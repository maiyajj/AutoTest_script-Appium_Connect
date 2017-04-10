# encoding:utf-8


class a(object):
    def __init__(self):
        print "sdafasdfasdf"
        self.b()

    def b(self):
        print "hhg"
        self.flag = 1

    def c(self):
        print "bb"
        return self.flag, "jj"


def write_report(case):
    CASE = case
    report = u"[CASE_TITLE=%s, RESULT=%s]" % \
             (CASE[1], CASE[0])
    return report


report = open(r"Report.log", "w")
report.write("sdafdf")
report.write("sdafdf")
report.close()

# with open(r"Report.log", "a") as report:
#     report.write(write_report(a().c()))
# a().c()
