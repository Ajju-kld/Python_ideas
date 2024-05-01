import os

def create_folder(full_Sequence_of_names):
    
    names=full_Sequence_of_names.split(",") # to split the names by comma
    for name in names:
        try:
            # Create the directory
            os.mkdir(name)
            print("Directory", name, "created")
        except FileExistsError:
            print("Directory", name, "exists")


if __name__ == "__main__":
    full_Sequence_of_names = "Adarsh,Namiya,Harirag,Pooja,Soorya,Ashik,Juvairya,Justin,Aditya,Kailas,Jasil,Rafeeq,Arafahath,Ninu,Rafahath,Saadi,Adarsh CK,Ashker,Swetha,Thushara,Arjun TV,Ronald,Nithin,Srijith,Mithun C V,Abhinand,Anshaj Krishnan,Ashwin Krishna"
    create_folder(full_Sequence_of_names)
    
