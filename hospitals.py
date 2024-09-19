class Hospital:
    def __init__(self, name, city, url, jobs):
        self.name = name
        self.city = city
        self.url = url
        # self.elementToScrape = elementToScrape
        # FULL LIST VVVV
        # self.keywords = ["data", "redcap", "tableau", "it", "developer", "programmer", "redcap administrator", "data manager", "database analyst", "data integration", "data integration specialist", "research database specialist", "data quality", "programmer analyst", "research it support"]
         # TEST LIST VVVV
        self.keywords = ["nurse", "manager"]
        self.jobs = jobs

UHN = Hospital("University Health Network", "Toronto","https://forms.uhn.ca/UHNCareers", ["test"])


#Check UHN object
# print(UHN.__dict__)