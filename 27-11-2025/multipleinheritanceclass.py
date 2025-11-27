# example 1
class Programmer:
    def __init__(self, tech_skills, education):
        self.tech_skills = tech_skills
        self.education = education
    def print_bg(self):
        print("Technical Skills: ",self.tech_skills)
        print("Educational Background: ",self.education)

class Statistician:
    def __init__(self, no_of_papers,experience):
        self.no_of_papers = no_of_papers
        self.experience = experience


    def print_statistician(self):
        print("Number of Papers: ",self.no_of_papers)
        print("Number of Experience: ",self.experience)


class DataScientist(Programmer,Statistician):
    def __init__(self, tech_skills,education,no_of_papers, experience,domain):
        Programmer.__init__(self, tech_skills, education)
        Statistician.__init__(self, no_of_papers, experience)
        self.domain = domain

ds=DataScientist(["Python","R"],"Computer Science",4,6,"GENAI")
print(ds.tech_skills)
ds.print_statistician()
ds.print_bg()


#Example2
class Phone:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model

    def phone_details(self):
        print("Phone: ", self.brand)
        print("Model: ", self.model)

class Camera:
    def __init__(self, mega_pixel):
        self.mega_pixel = mega_pixel

    def camera_details(self):
        print(f"MegaPixel:{self.mega_pixel}MP")

class SmartPhone(Phone, Camera):
    def __init__(self, brand,model,mega_pixel,price,battery):
        Phone.__init__(self,brand,model)
        Camera.__init__(self,mega_pixel)
        self.price = price
        self.battery = battery

    def smart_phone_details(self):
        print(f"Price:{self.price}")
        print(f"Battery:{self.battery}hours")

sp1=SmartPhone("Vivo","V23",32,30000,48)
sp1.phone_details()
sp1.smart_phone_details()
sp1.camera_details()

