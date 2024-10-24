class ApplicationState:
    instance = None

    def __init__(self):
        self.isLoggedIn = False

    @staticmethod
    def getAppState():
        if not ApplicationState.instance:  
            ApplicationState.instance = ApplicationState()
        return ApplicationState.instance

appState1 = ApplicationState.getAppState()
print(appState1.isLoggedIn)

appState2 = ApplicationState.getAppState()
appState1.isLoggedIn = True

print(appState1.isLoggedIn)
print(appState2.isLoggedIn)


class SingletonClass:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonClass, cls).__new__(cls)
        return cls._instance
        
    def __init__(self):
        if not hasattr(self, 'isLoggedIn'):
            self.isLoggedIn = False

singleton1 = SingletonClass()
singleton2 = SingletonClass()
singleton1.isLoggedIn = True

print(singleton1 is singleton2)
print(singleton1.isLoggedIn)
print(singleton2.isLoggedIn)