
glob = {
    "Mark" : "Facebook/Full-stack",
    "John" : "Netflix/Frontend",
    "Anne" : "Google/Frontend",
    "David" : "Google/Backend",
    "Elon" : "Oracle/Backend",
    "Michael" : "Oracle/Full-stack"
}

d = []

class Team:

    def __init__(self, name, project, status):
        self._name = name
        self._project = project
        self._status = status

    
    @property
    def name(self):
        return self._name
    
    @property
    def project(self):
        return self._project

    @property
    def status(self):
        return self._status

    @name.setter
    def name(self, name):
        self._name = name

    @project.setter
    def project(self, project):
        self._project = project 
    
    @status.setter
    def status(self, status):
        self._status = status

    def __eq__(self, other):
        return self.project == other.project



def main():

    for k,v in glob.items():
        s = v.split("/")
        new_developer = Team(k, s[0],s[1])

        if (new_developer):
            d.append(new_developer)
            print("--Developer created successfully--")
            print(f"{new_developer.name} a {new_developer.project}-en dolgozik {new_developer.status} szerepkörben.\n")
        else:
            print("--Developer failed to create--")
      

    for x in range(0, len(d)-1):
        if d[x] == d[x+1]:
            print(f"{d[x].name} és {d[x+1].name} ugyanazon a projekten dolgoznak!")


if __name__ == "__main__":
    main()