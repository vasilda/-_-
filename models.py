'''
   Файл с моделями БД
   Выполнила: Васильева Д.М.
'''
from typing import Optional
from sqlmodel import *
from datetime import date
from datetime import time
from random import *
# Таблица Должности
class ListPost(SQLModel, table=True):
    CodePost: Optional[int] = Field(default=None, primary_key=True)
    Name: str
# Таблица Сотрудники
class Staff(SQLModel, table=True):
    CodeStaff: Optional[int] = Field(default=None, primary_key=True)
    LName: str
    FName: str
    Patronym: str
    CodePost:  Optional[int] = Field(default=None, foreign_key="listpost.CodePost")
# Таблица Залы
class Halls(SQLModel, table=True):
    CodeHall: Optional[int] = Field(default=None, primary_key=True)
    NameHall: str
    CodeStaff: Optional[int] = Field(default=None, foreign_key="staff.CodeStaff")
# Таблица Контракты
class Contracts(SQLModel, table=True):
    CodeContract: Optional[int] = Field(default=None, primary_key=True)
    Begin: date
    End: date
# Таблица Реставраторы
class Restorers(SQLModel, table=True):
    CodeRestorer: Optional[int] = Field(default=None, primary_key=True)
    LName: str
    FName: str
    Patronym: str
    CodeContract: Optional[int] = Field(default=None, foreign_key="contracts.CodeContract")
# Таблица Экспонаты
class Exhibits(SQLModel, table=True):
    CodeExhibits: Optional[int] = Field(default=None, primary_key=True)
    Name: str
    CodeHall: Optional[int] = Field(default=None, foreign_key="halls.CodeHall")
    Author: str
    Year: str
    Look: str
    Category: str
    DateInspection: date
    CodeRestorer: Optional[int] = Field(default=None, foreign_key="restorers.CodeRestorer")
# Таблица Экскурсии
class Excursions(SQLModel, table=True):
    CodeExcursion: Optional[int] = Field(default=None, primary_key=True)
    Name: str
    Begin: time
    End: time
    DayWeek: str
    Cost: int
    CodeStaff: Optional[int] = Field(default=None, foreign_key="staff.CodeStaff")
    Quantity: int
# Таблица Экскурсанты
class Tourists(SQLModel, table=True):
    Ticket: Optional[int] = Field(default=None, primary_key=True)
    LName: str
    FName: str
    Patronym: str
    AgeGroup: str
    CodeExcursion: Optional[int] = Field(default=None, foreign_key="excursions.CodeExcursion")
# Функция заполнения таблицы Должности
def CreatePost():
    post1 = ListPost(Name = "смотритель")
    post2 = ListPost(Name = "экскурсовод")
    with Session(engine) as session:
        session.add(post1)
        session.add(post2)
        session.commit()
# Функция заполнения таблицы Сотрудники
def CreateStaff():
    staff1  = Staff(LName =    "Носкова", FName =    "Татьяна", Patronym =    "Николаевна", CodePost = 1)
    staff2  = Staff(LName =    "Субетто", FName =    "Дмитрий", Patronym = "Александровчи", CodePost = 1)
    staff3  = Staff(LName =     "Иванов", FName =       "Юрий", Patronym =      "Петрович", CodePost = 1)
    staff4  = Staff(LName =    "Сидоров", FName =    "Николай", Patronym =      "Петрович", CodePost = 1)
    staff5  = Staff(LName =    "Грекова", FName =       "Юлия", Patronym =     "Андреевна", CodePost = 1)
    staff6  = Staff(LName = "Василькова", FName =      "Елена", Patronym =    "Николаевна", CodePost = 2)
    staff7  = Staff(LName =   "Малахова", FName =      "Алина", Patronym =      "Петровна", CodePost = 2)
    staff8  = Staff(LName =    "Маликов", FName =    "Алексей", Patronym =    "Михайлович", CodePost = 2)
    staff9  = Staff(LName =    "Пьянков", FName =   "Григорий", Patronym =    "Михайлович", CodePost = 2)
    staff10 = Staff(LName =   "Синицина", FName = "Александра", Patronym =       "Юрьевна", CodePost = 2)
    staffs  = [staff1, staff2, staff3, staff4,  staff5, 
               staff6, staff7, staff8, staff9, staff10]
    with Session(engine) as session:
        for staff in staffs:
            session.add(staff)
        session.commit()
# Функция заполнения таблицы Залы
def CreateHall():
    hall1 = Halls(NameHall = "Зал Древнего Египта", CodeStaff = 1) #100
    hall2 = Halls(NameHall =           "Белый зал", CodeStaff = 2) #289
    hall3 = Halls(NameHall =     "Военная галерея", CodeStaff = 3) #197
    hall4 = Halls(NameHall =      "Петровский зал", CodeStaff = 4) #194
    hall5 = Halls(NameHall =        "Гербовый зал", CodeStaff = 5) #195
    halls = [hall1, hall2, hall3, hall4, hall5]
    with Session(engine) as session:
        for hall in halls:
            session.add(hall)
        session.commit()
# Функция заполнения таблицы Экспонаты
def CreateExhibits():
    exh1  = Exhibits(Name = "Статуя Аменемхета III", CodeHall = 1, Author = "NULL", Year = "NULL",
                     Look = "неуд.", Category = "скульптура", DateInspection = date(2023,10,13), CodeRestorer = "NULL")
    exh2  = Exhibits(Name = "Стела Хоремхеба", CodeHall = 1, Author = "NULL", Year = "NULL",
                     Look = "уд.", Category = "скульптура", DateInspection = date(2023,8,8), CodeRestorer = "NULL")
    exh3  = Exhibits(Name = "Статуэтка-амулет Исиды", CodeHall = 1, Author = "NULL", Year = "NULL",
                     Look = "уд.", Category = "скульптура", DateInspection = date(2023,7,7), CodeRestorer = "NULL")
    exh4  = Exhibits(Name = "Разорители гнезд", CodeHall = 2, Author = "Гюбер Робер", Year = "1934",
                     Look = "неуд.", Category = "живопись", DateInspection = date(2023,2,12), CodeRestorer = "NULL")
    exh5  = Exhibits(Name = "Обелиск", CodeHall = 2, Author = "Гюбер Робер", Year = "1932",
                     Look = "уд.", Category = "живопись", DateInspection = date(2023,8,22), CodeRestorer = "NULL")
    exh6  = Exhibits(Name = "Деревья", CodeHall = 2, Author = "Гюбер Робер", Year = "1932",
                     Look = "уд.", Category = "живопись", DateInspection = date(2023,8,23), CodeRestorer = "NULL")
    exh7  = Exhibits(Name = "Водопад", CodeHall = 2, Author = "Гюбер Робер", Year = "1919",
                     Look = "неуд.", Category = "живопись", DateInspection = date(2023,4,10), CodeRestorer = "NULL")
    exh8  = Exhibits(Name = "Портрет Александра I", CodeHall = 3, Author = "Франц Крюгер", Year = "NULL",
                     Look = "уд.", Category = "живопись", DateInspection = date(2023,4,20), CodeRestorer = "NULL")
    exh9  = Exhibits(Name = "Портрет Франца I", CodeHall = 3, Author = "Иоганн Петер Краф", Year = "NULL",
                     Look = "уд.", Category = "живопись", DateInspection = date(2022,6,11), CodeRestorer = "NULL")
    exh10 = Exhibits(Name = "Портрет Ф. Вильгельма III", CodeHall = 3, Author = "Франц Крюгер", Year = "NULL",
                     Look = "уд.", Category = "живопись", DateInspection = date(2022,12,12), CodeRestorer = "NULL")
    exh11 = Exhibits(Name = "Петр I с Минервой", CodeHall = 4, Author = "Амигони Якопо", Year = "NULL",
                     Look = "неуд.", Category = "живопись", DateInspection = date(2023,1,12), CodeRestorer = "NULL")
    exh12 = Exhibits(Name = "Церера", CodeHall = 5, Author = "Альберт Торвальдсен", Year = "1920",
                     Look = "уд.", Category = "скульптура", DateInspection = date(2023,3,13), CodeRestorer = "NULL")
    exh13 = Exhibits(Name = "Вид части Гербового зала", CodeHall = 5, Author = "Адольф Игнатьевич Ладюрнер", Year = "1956",
                     Look = "уд.", Category = "живопись", DateInspection = date(2023,9,16), CodeRestorer = "NULL")
    exhs = [exh1, exh2,  exh3,  exh4,  exh5,  exh6, exh7,
             exh8, exh9, exh10, exh11, exh12, exh13]
    with Session(engine) as session:
        for exh in exhs:
            session.add(exh)
        session.commit()
# Функция заполнения таблицы Контракты
def CreateContract():
    contr1 = Contracts(Begin = date(2019,1,1), End = date(2024,1,1))
    contr2 = Contracts(Begin = date(2020,1,1), End = date(2025,1,1))
    contr3 = Contracts(Begin = date(2021,1,1), End = date(2026,1,1))
    contr4 = Contracts(Begin = date(2022,1,1), End = date(2027,1,1))
    contr5 = Contracts(Begin = date(2023,1,1), End = date(2028,1,1))
    contrs = [contr1, contr2, contr3, contr4, contr5]
    with Session(engine) as session:
        for contr in contrs:
            session.add(contr)
        session.commit()
# Функция заполнения таблицы Реставраторы
def CreateRestorer():
    rest1 = Restorers(LName = "Васнецова", FName =   "Лилия", Patronym =   "Андреевна", CodeContract = 1)
    rest2 = Restorers(LName =   "Архипов", FName =  "Михаил", Patronym = "Анатольевич", CodeContract = 2)
    rest3 = Restorers(LName =    "Иванов", FName = "Алексей", Patronym =  "Викторович", CodeContract = 3)
    rest4 = Restorers(LName =    "Жукова", FName =  "Таисия", Patronym =   "Никитична", CodeContract = 4)
    rest5 = Restorers(LName = "Васильева", FName =   "Дарья", Patronym =  "Михайловна", CodeContract = 5)
    rests = [rest1, rest2, rest3, rest4, rest5]
    with Session(engine) as session:
        for rest in rests:
            session.add(rest)
        session.commit()
# Функция заполнения таблицы Экскурсии
def CreateExcursion():
    # Расписание экскурсий на понедельник
    ex1  = Excursions(Name = "Большое путешествие по Эрмитажу", Begin = time(11,30), End = time(13,30),
                      DayWeek = "пн", Cost = 5900, CodeStaff = 6, Quantity = 20)
    ex2  = Excursions(Name = "С умом по Эрмитажу", Begin = time(12,30), End = time(14,30),
                      DayWeek = "пн", Cost = 5330, CodeStaff = 7, Quantity = 15)
    ex3  = Excursions(Name = "Эрмитаж. Знакомство", Begin = time(13,0), End = time(15,0),
                      DayWeek = "пн", Cost = 2964, CodeStaff = 8, Quantity = 15)
    ex4  = Excursions(Name = "Экскурсия в мир искусства", Begin = time(13,30), End = time(15,30),
                      DayWeek = "пн", Cost = 3600, CodeStaff = 9, Quantity = 15)
    ex5  = Excursions(Name = "Большое путешествие по Эрмитажу", Begin = time(14,0), End = time(16,0),
                      DayWeek = "пн", Cost = 3600, CodeStaff = 10, Quantity = 15)
    # Расписание экскурсий на вторник
    ex6  = Excursions(Name = "Экскурсия в мир искусства", Begin = time(11,30), End = time(13,30),
                      DayWeek = "вт", Cost = 3600, CodeStaff = 6, Quantity = 20)
    ex7  = Excursions(Name = "Эрмитаж не для галочки", Begin = time(12,0), End = time(14,0),
                      DayWeek = "вт", Cost = 3900, CodeStaff = 7, Quantity = 15)
    ex8  = Excursions(Name = "Тайны шедевров Эрмитажа", Begin = time(12,30), End = time(14,30),
                      DayWeek = "вт", Cost = 5300, CodeStaff = 8, Quantity = 15)
    ex9  = Excursions(Name = "Залы Эрмитажа", Begin = time(13,0), End = time(15,0),
                      DayWeek = "вт", Cost = 2500, CodeStaff = 9, Quantity = 15)
    ex10 = Excursions(Name = "Эрмитаж и тайны семьи Романовых", Begin = time(13,30), End = time(15,30),
                      DayWeek = "вт", Cost = 5250, CodeStaff = 10, Quantity = 15)
    # Расписание экскурсий на среду
    ex11 = Excursions(Name = "Эрмитаж. Знакомство", Begin = time(11,30), End = time(13,30),
                      DayWeek = "ср", Cost = 2964, CodeStaff = 6, Quantity = 20)
    ex12 = Excursions(Name = "Эрмитаж и тайны семьи Романовых", Begin = time(12,0), End = time(14,0),
                      DayWeek = "ср", Cost = 5250, CodeStaff = 7, Quantity = 15)
    ex13 = Excursions(Name = "Тайны шедевров Эрмитажа", Begin = time(12,30), End = time(14,30),
                      DayWeek = "ср", Cost = 5300, CodeStaff = 8, Quantity = 15)
    ex14 = Excursions(Name = "Большое путешествие по Эрмитажу", Begin = time(13,0), End = time(15,0),
                      DayWeek = "ср", Cost = 5900, CodeStaff = 9, Quantity = 15)
    ex15 = Excursions(Name = "Эрмитаж и тайны семьи Романовых", Begin = time(13,30), End = time(15,30),
                      DayWeek = "ср", Cost = 5250, CodeStaff = 10, Quantity = 15)
    rests = [ex1,  ex2,  ex3,  ex4,  ex5,  ex6,  ex7, ex8,
             ex9, ex10, ex11, ex12, ex13, ex14, ex15]
    with Session(engine) as session:
        for rest in rests:
            session.add(rest)
        session.commit()
# Функция заполнения таблицы Экскурсанты
def CreateTourist():
    group  = ['дошкольник', 'школьник', 'студент', 'взрослый', 'пенсионер']
    tour1  = Tourists(LName =    "Гусева", FName = "Анастасия", Patronym =    "Сергеевна", AgeGroup = choice(group), CodeExcursion =  1)
    tour2  = Tourists(LName = "Чекалова", FName =     "Ольга", Patronym = "Ростиславовна", AgeGroup = choice(group), CodeExcursion =  1)
    tour3  = Tourists(LName =   "Гдалин", FName =   "Дмитрий", Patronym =    "Викторович", AgeGroup = choice(group), CodeExcursion =  3)
    tour4  = Tourists(LName =  "Соломин", FName =    "Андрей", Patronym =     "Сергеевич", AgeGroup = choice(group), CodeExcursion = 13)
    tour5  = Tourists(LName = "Соломина", FName =  "Виктория", Patronym =    "Михайловна", AgeGroup = choice(group), CodeExcursion = 12)
    tour6  = Tourists(LName =    "Белов", FName =      "Илья", Patronym =         "Ильич", AgeGroup = choice(group), CodeExcursion = 14)
    tour7  = Tourists(LName = "Кравцова", FName =   "Валерия", Patronym =     "Никитична", AgeGroup = choice(group), CodeExcursion = 14)
    tour8  = Tourists(LName =   "Нечаев", FName =   "Дмитрий", Patronym =         "Ильич", AgeGroup = choice(group), CodeExcursion = 14)
    tour9  = Tourists(LName =  "Нечаева", FName =      "Алла", Patronym =     "Борисовна", AgeGroup = choice(group), CodeExcursion = 14)
    tour10 = Tourists(LName =   "Елкина", FName =   "Евгения", Patronym =       "Ильична", AgeGroup = choice(group), CodeExcursion =  5)
    tours = [tour1, tour2, tour3, tour4, tour5,
             tour6, tour7, tour8, tour9, tour10]
    with Session(engine) as session:
        for tour in tours:
            session.add(tour)
        session.commit()
engine = create_engine("sqlite:///database.db")
# Создание БД
if __name__ == "__main__":
    SQLModel.metadata.create_all(engine)
    CreatePost();      CreateStaff();    
    CreateHall();      CreateExhibits(); 
    CreateContract();  CreateRestorer()
    CreateExcursion(); CreateTourist()