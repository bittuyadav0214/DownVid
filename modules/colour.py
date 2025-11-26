class color:
    @staticmethod
    def red(text):
        return(f"\033[1;31m{text}\033[0m")

    @staticmethod
    def green(text):
        return(f"\033[1;32m{text}\033[0m")

    @staticmethod
    def yellow(text):
         return(f"\033[1;33m{text}\033[0m")

    @staticmethod
    def blue(text):
         return(f"\033[1;34m{text}\033[0m")

    @staticmethod
    def magenta(text):
         return(f"\033[1;35m{text}\033[0m")   

    @staticmethod
    def cyan(text):
         return(f"\033[1;36m{text}\033[0m")
