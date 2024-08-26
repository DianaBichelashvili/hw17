აღწერეთ ორი კლასი შემდეგი მონაცემების მიხედვით:

Person:
name
deposit (default value = 1000, მიუთითებს ამჟამად რამდენი აქვს დეპოზიტზე)
loan (default value = 0, მიუთითებს ამჟამად რამდენი აქვს სესხი აღებული)


House:
ID – ბინის საკატასტრო კოდი
price – ბინის ფასი
owner – სახლის მეპატრონე (Person ტიპის ობიექტი)
status – ახალი ბინის დამატებისას სტატუსი არის ყოველთვის “გასაყიდი”



გაითვალისწინეთ owner-ის მნიშვნელობა არის Person კლასის ობიექტი

Person კლასში დაამატეთ __str__ მეთოდი რომელიც დააბრუნებს პიროვნების სრულ ინფორმაციას


შექმენით ორი Person კლასის ობიექტი(მაგალითად ერთი მეპატრონე, მეორე მყიდველი). ასევე შექმენით House კლასის ობიექტი რომლის owner იქნება ერთ-ერთი Person ობიექტი

House კლასში დაამატეთ ბინის გაყიდვის მეთოდი, რომლის დროსაც პარამეტრებად გადაეცემა მყიდველი, თუ მეტი პარამეტრი არ გადაეცემა, ამ დროს უნდა შესრულდეს ბინის გაყიდვის ოპერაცია(გამყიდველის deposit უნდა გაიზარდოს ბინის ღირებულებით, უნდა შეიცვალოს owner და status უნდა გახდეს “გაყიდული”, დაბეჭდეთ შესაბამისი ტექსტი). თუ ამ მეთოდის გამოძახების დროს მყიდველის გარდა პარამეტრად გადაეცა კიდევ ერთი რიცხვი, მაშინ შესრულდეს ბინის სესხით გაყიდვის ოპერაცია, სადაც პარამეტრად გადაცემული რიცხვი მიუთითებს მყიდველის მიერ აღებული სესხის რაოდენობას, მეთოდმა კი უნდა შეასრულოს შემდეგი ოპერაციები: გამყიდველის deposit უნდა გაიზარდოს ბინის ღირებულებით, owner უნდა შეიცვალოს, status გახდეს “გაყიდული სესხით”, მყიდველის სესხი (loan) უნდა გაიზარდოს შესაბამისი რაოდენობით და დაიბეჭდოს გაყიდვის შესაბამისი შეტყობინება.

კლასის გარეთ მოახდინეთ აღწერილი ფუნქციების გამოძახება


class Person:

deposit_amount=1000
loan_amount=0

def __init__(self,deposit_amount, loan_amount):
    self.deposit_amount = deposit_amount
    self.loan_amount = loan_amount


class House:

 def __init__(self, cadastral, price, owner, status):
    self.cadastral=cadastral
    self.price=price
    self.owner=owner
    self.status=status


def __str__(self):
        return f"Person(name={self.name}, deposit={self.deposit}, loan={self.loan})"


def on_sale (self):
   print(f"House Status:{self.status}")
   print(f"House Price:{self.price}")


owner=Person()

def sell(self, buyer, loan=None):
         if loan is None:
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = "house is sold"
            print(f"house{self.cadastral} sold {buyer.name}")

         else:
            loan_amount = self.price - loan
            if self.owner.deposit < loan_amount:
                print(f"house sold with loan {loan_amount}")
      

            

seller = Person(name="John")
buyer = Person(name="Jane")


