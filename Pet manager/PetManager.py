import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

class PetInfoAPP(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Pet Info App')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.pet_input = QLineEdit(self)
        self.pet_input.setPlaceholderText('Enter petname name')
        layout.addWidget(self.pet_input)
        self.pet_input.returnPressed.connect(self.fetch_info)

        self.get_Info = QPushButton('Get Info', self)
        self.get_Info.clicked.connect(self.fetch_info)
        layout.addWidget(self.get_Info)

        self.result_label = QLabel('', self)
        self.result_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.result_label)

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText('Pet Name')
        layout.addWidget(self.name_input)

        self.age_input = QLineEdit(self)
        self.age_input.setPlaceholderText('Age')
        layout.addWidget(self.age_input)

        self.owner_input = QLineEdit(self)
        self.owner_input.setPlaceholderText('Owner')
        layout.addWidget(self.owner_input)

        self.animal_type_input = QLineEdit(self)
        self.animal_type_input.setPlaceholderText('Animal Type')
        layout.addWidget(self.animal_type_input)

        self.insert_pet_btn = QPushButton('Insert Pet', self)
        self.insert_pet_btn.clicked.connect(self.insert_pet)
        layout.addWidget(self.insert_pet_btn)


        self.setLayout(layout)
    def fetch_info(self):
        petname = self.pet_input.text()
        if petname:
            connection = sqlite3.connect('animalinfo.db')
            cursor = connection.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute("""SELECT pets.Name, pets.Owner, animals.species,
                                pets.Age, animals.Lifespan, animals.Food 
                                FROM pets join animals ON pets.AnimalID = animals.id 
                                WHERE pets.Name=?""", (petname,))
            data = cursor.fetchone()
            if data:
                name, owner, species, age, lifespan, food = data
                self.result_label.setText(f'Name: {name}\n Owner: {owner}\nSpecies: {species}\nAge: {age}\nLifespan: {lifespan} years\nFood: {food}')
            else:
                self.result_label.setText('Pet not found!')
            connection.close()
        else:
            self.result_label.setText('Please enter a pet name!')
    def insert_pet(self):
        name = self.name_input.text()
        age = self.age_input.text()
        owner = self.owner_input.text()
        animal_type = self.animal_type_input.text()
        if not (name and age and owner and animal_type):
            self.result_label.setText('Please fill in all fields!')
            return
        
        try:
            connection = sqlite3.connect('animalinfo.db')
            cursor = connection.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute("SELECT id FROM animals WHERE species=?", (animal_type,))
            result = cursor.fetchone()
            if not result:
                cursor.execute("INSERT OR IGNORE INTO animals (species, Food, Type, Lifespan) VALUES (?, '', '', 0)", (animal_type,))
                connection.commit()
                cursor.execute("SELECT id FROM animals WHERE species=?", (animal_type,))
                result = cursor.fetchone()
            animal_id = result[0]
            cursor.execute(
                """INSERT OR IGNORE INTO pets (Name, Age, Owner, AnimalID)
                VALUES (?, ?, ?, ?)""",
                (name, int(age), owner, int(animal_id)))

            connection.commit()
            connection.close()

            self.result_label.setText(f'Inserted pet {name}!')
        except ValueError:
            self.result_label.setText('Age and Animal ID must be numbers!')
        self.name_input.clear()
        self.age_input.clear()
        self.owner_input.clear()
        self.animal_type_input.clear()


connection = sqlite3.connect('animalinfo.db')
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")
command= "CREATE TABLE IF NOT EXISTS animals (id INTEGER PRIMARY KEY, species TEXT UNIQUE, Food TEXT, Type TEXT, Lifespan INTEGER)"
cursor.execute(command)
command1 = " CREATE TABLE IF NOT EXISTS pets (id INTEGER PRIMARY KEY, Name TEXT UNIQUE, Age INTEGER, Owner TEXT, AnimalID INTEGER, FOREIGN KEY (AnimalID) REFERENCES animals(id))"
cursor.execute(command1)


# cursor.execute("INSERT OR IGNORE INTO animals (species, Food, Type, Lifespan) VALUES ('Dog', 'Carnivore', 'Mammal', 12)")
# cursor.execute ("INSERT OR IGNORE INTO animals (species, Food, Type, Lifespan) VALUES ('Cat', 'Carnivore', 'Mammal', 15)")
# cursor.execute ("INSERT OR IGNORE INTO animals (species, Food, Type, Lifespan) VALUES ('Parrot', 'Herbivore', 'Bird', 15)")
# cursor.execute ("INSERT OR IGNORE INTO pets (Name, Age, Owner, AnimalID) VALUES ('Buddy', 3, 'Alice', 1)")
# cursor.execute ("INSERT OR IGNORE INTO pets (Name, Age, Owner, AnimalID) VALUES ('Whiskers', 2, 'Bob', 2)")
# cursor.execute ("INSERT OR IGNORE INTO pets (Name, Age, Owner, AnimalID) VALUES ('Polly', 4, 'Charlie', 3)")

# cursor.execute("SELECT pets.Name, animals.species, pets.Age, animals.Lifespan FROM pets join animals ON pets.AnimalID = animals.id")
# results = cursor.fetchall()
# print(results)

connection.commit()
connection.close()
if __name__ == '__main__':
    app = QApplication([])
    ex = PetInfoAPP()
    ex.show()
    sys.exit(app.exec_())



