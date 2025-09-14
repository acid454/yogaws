#
# Scan for global sets on import
# See __init__.py comments in asanas for details
#


from resmanager import ResourcesManager

class Sets():
    SETS_IMPORTS = {}

    @staticmethod
    def get_class(name : str, default):
        for f in ResourcesManager().list_sets_files():
            #print(f"Sets __init__, processing {f}")
            if f not in Sets.SETS_IMPORTS.keys():
                Sets.SETS_IMPORTS[f] = __import__("sets.%s"%(f[:-3]), fromlist=[None])
            
            result = getattr(Sets.SETS_IMPORTS[f], name, None)
            if result is not None:
                return result
        return default



