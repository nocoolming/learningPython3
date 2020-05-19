class Show(object):
    def __init__(self, message):
        self._message = message
    
    @property
    def message(self):
        return self._message
    
    @property
    def message(self, message):
        self._message = message


    def show(self):
        print('message: %s' % self._message)

def main():
    show = Show('Hello, python')
    show.show()

if __name__ == '__main__':
    main()
