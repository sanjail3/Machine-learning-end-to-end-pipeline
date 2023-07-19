class InvalidUrlException(Exception):
    def __init__(self,message:str="Invalid URL"):
        self.message=message
        super().__init__(self.message)

