class Open():
    instance=None
    def __init__(self,_from):
        self._from=_from

    def __new__(cls,*arg,**kwargs):
        if cls.instance is None: 
            cls.instance=super().__new__(cls)

        return cls.instance  