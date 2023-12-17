'''
   Файл с запросами к БД
   Выполнила: Васильева Д.М.
'''
from typing import Optional
from sqlmodel import *
from models import *
# Вывод информации о принадлежности экспонатов к залам
def ExhInHall():
    with Session(engine) as session:
        statement = select(Halls)
        result = session.exec(statement)
        print("Экспонаты в залах:")
        for st in result:
            print("-> {}".format(st.NameHall))
            statement2 = select(Exhibits).where(Exhibits.CodeHall == st.CodeHall)
            result2 = session.exec(statement2)
            for st2 in result2:
                print("   {} ({})".format(st2.Name, st2.Author))
# Вывод стоимости билетов для туристов разных возрастных групп
def CostOfTicket():
    with Session(engine) as session:
        # Скидки:
        # 25% для студентов и школьников
        # 50% для дошкольников
        # 75% для пенсионеров
        statement = select(Excursions)
        result = session.exec(statement)
        print("Экскурсии:")
        for st in result:
            print("-> {}\n   Цена: {}".format(st.Name, st.Cost))
            statement2 = select(Tourists).where(Tourists.CodeExcursion == st.CodeExcursion)
            result2 = session.exec(statement2)
            for st2 in result2:
                FullName = "   {} {} {} ({})".format(st2.LName, st2.FName, st2.Patronym, st2.AgeGroup)
                if (st2.AgeGroup == "студент" or st2.AgeGroup == "школьник"):
                    NewCost = st.Cost * (1 - 0.25)
                elif (st2.AgeGroup == "дошкольник"):
                    NewCost = st.Cost * 0.5
                elif (st2.AgeGroup == "пенсионер"):
                    NewCost = st.Cost * (1 - 0.75)
                else:
                    NewCost = st.Cost
                print(FullName + ' ' + str(NewCost))
# Вывод фактического количества участников экскурсии
def CountTourist():
    with Session(engine) as session:
        statement = select(Excursions)
        result = session.exec(statement)
        print("Экскурсии:")
        for st in result:
            print("-> {} ({})\n   Максимальное кол-во туристов: {}".format(st.Name, st.DayWeek, st.Quantity))
            statement2 = select(Tourists).where(Tourists.CodeExcursion == st.CodeExcursion)
            result2 = session.exec(statement2)
            print("   Фактическое кол-во: " + str((len(result2.all()))))
# Вывод информации об экспонатах с неудовлетворительным внешним видом
def BadLook():
    with Session(engine) as session:
        statement = select(Halls)
        result = session.exec(statement)
        print("Экспонаты в залах:")
        for st in result:
            print("-> {}".format(st.NameHall))
            statement2 = select(Exhibits).where(and_(Exhibits.CodeHall == st.CodeHall, Exhibits.Look == "неуд."))
            result2 = session.exec(statement2)
            for st2 in result2:
                print("   {} ({}) -> {}".format(st2.Name, st2.Author, st2.Look))
# Вывод информации о расписании экскурсовода
def Schedule(id):
    with Session(engine) as session:
        statement = select(Staff).where(Staff.CodeStaff == id)
        result = session.exec(statement)
        print("Расписание:")
        for st in result:
            print("-> ФИО: {} {} {}".format(st.LName, st.FName, st.Patronym))
            statement2 = select(Excursions).where(Excursions.CodeStaff == id)
            result2 = session.exec(statement2)
            for st2 in result2:
                print("  {} ({} - {}, {})".format(st2.Name, st2.Begin, st2.End, st2.DayWeek))            
# Запуск программы
if __name__ == "__main__":
    ExhInHall()
    CostOfTicket()
    CountTourist()
    BadLook()
    Schedule(6)