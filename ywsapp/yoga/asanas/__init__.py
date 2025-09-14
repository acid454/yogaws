#
# Scan for global asanas on import
#  Use __init__ here to initialize Asanas class in package, use
#   AsanasType - is metaclass, that allows us to redefine __getattr__
#   for class (not for class's object).
#  Other words - metaclass allows us redefine __getattr__ for class
#  https://stackoverflow.com/questions/3155436/getattr-for-static-class-variables
#

from resmanager import ResourcesManager


class AsanasType(type):
    def __getattr__(cls, key):
        # Use non-empty fromlist, to import only last module
        #  (https://stackoverflow.com/questions/9806963/how-to-use-the-import-function-to-import-a-name-from-a-submodule)
        return __import__("asanas.%s"%(key), fromlist=[None])

class Asanas(metaclass=AsanasType):
    ASANAS_IMPORTS = {}

    @staticmethod
    def get_class(name : str):
        for f in ResourcesManager().list_asanas_files():
            #print(f"Asanas __init__, processing {f}")
            if f not in Asanas.ASANAS_IMPORTS.keys():
                Asanas.ASANAS_IMPORTS[f] = __import__("asanas.%s"%(f[:-3]), fromlist=[None])
            
            result = getattr(Asanas.ASANAS_IMPORTS[f], name, None)
            if result is not None:
                return result
