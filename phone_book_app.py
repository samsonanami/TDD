class PhoneBook:
    def __init__(self):
        self.contacts = {"Samson Anami":"0722354453", "Maina Charles":"0710345267", "Joel Nganga":"0786564342", "Wysk Brian":"0756465333"}
    def add_contacts(self,name,number):
        self.contacts[name]=number
        return {"Message":"New contact added successfully"}
    def view_contact(self,name):
        if self.contacts.has_key(name):
            print self.contacts[name]
            return {"Message":"Contact view successful"}
        else:
            return {"Message":"Contact not found"}
    def update_contact(self,name,newNumber):
        self.contacts[name]=newNumber
        return {"Message":"Contact updated successfully"}        
    def delete_contact(self,name):
        del self.contacts[name]
        return {"Message":"Contact deleted successfully"}