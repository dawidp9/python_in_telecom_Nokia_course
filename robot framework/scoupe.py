import time
from robot.api.deco import keyword


class SuperMegaTimeClass(object):
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE' #TEST CASE | GLOBAL
    def get_current_time(self, format=None):
        if not format:
            return time.time()
        else:
            return time.strftime(format, time.localtime())

    @keyword('Get how many days passed since ${date:\d+}')
    def get_days_from_date(self, date):
        return 10