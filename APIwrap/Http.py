import flask

from APIwrap.API import wrapper

app = flask.Flask(__name__)
app.config["DEBUG"] = True


wrap = wrapper()

class HTTP:
    @app.route('/', methods=["GET"])
    def home(self):
       return"Welcome to Our simple API  "

    @app.route('/<country>')
    def getByName(self,country):
            countryInfo = wrap.getName(country)
            if countryInfo is not None:
                return countryInfo
            else:
                 return ("Not Found")

    @app.route('/all')
    def getall(self,country):
            countryInfo = wrap.getall()
            if countryInfo is not None:
                return str(countryInfo)
            else:
                 return ("Not Found")

    @app.route('/<country>/info=<specificInfo>')
    def getSpecificInfobycountry(self,country,specificInfo):

        specificInfo=specificInfo
       # countryInfo = gettingSpecificInfo(country,specificInfo)
        countryInfo = wrap.getSpecific(country, specificInfo)
        if countryInfo is not None:
                return str(countryInfo)
        else:
            return ("Not Found")

    @app.route('/alpha/<code>')
    def getalpha(self,code):


        countryInfo = wrap.getalpha(code)
        if countryInfo is not None:
                return countryInfo
        else:
            return ("Not Found")

    @app.route('/currency/<currency>')
    def getcurrency(self,curr):
        countryInfo = wrap.getcurrency(curr)
        if countryInfo is not None:
                return countryInfo
        else:
            return ("Not Found")

    @app.route('/capital/<capital>')
    def getcapital(self,cap):

        countryInfo = wrap.getcapital(cap)
        if countryInfo is not None:
                return countryInfo
        else:
            return ("Not Found")

    @app.route('/callingcode/<callingcode>')
    def getcallingcode(self,code):

        countryInfo = wrap.getcallingcode(code)
        if countryInfo is not None:
                return countryInfo
        else:
            return ("Not Found")

    @app.route('/region/<region>')
    def getregion(self,reg):

        countryInfo = wrap.getregion(reg)
        if countryInfo is not None:
                return countryInfo
        else:
            return ("Not Found")



    def gettingSpecificInfo(country1,specific1):

        country = country1
        specific=specific1
        countryInfo = wrap.getSpecific(country,specific)
        return countryInfo







if __name__ == '__main__':
    app.run(debug=True)