
from app.db.db import engine, SessionLocal, Base
from app.db.models import Category
from app.db.crud import create_category, create_book, get_categories


def init_db():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        existing_categories = get_categories(db)

        if existing_categories:
            print("База данных уже содержит категории.")
            return

        programming = create_category(db, "Программирование")
        fiction = create_category(db, "Художественная литература")

        create_book(
            db,
            "Чистый код",
            "Практическое руководство по написанию чистого кода",
            1500.00,
            "https://example.com/clean-code",
            programming.id
        )

        create_book(
            db,
            "Python. К вершинам мастерства",
            "Книга по углублённому изучению Python",
            1800.00,
            "https://example.com/python",
            programming.id
        )

        create_book(
            db,
            "Совершенный код",
            "Руководство по разработке программного обеспечения",
            2000.00,
            "https://example.com/perfect-code",
            programming.id
        )

        create_book(
            db,
            "Мастер и Маргарита",
            "Роман Михаила Булгакова",
            900.00,
            "https://example.com/master-margarita",
            fiction.id
        )

        create_book(
            db,
            "Преступление и наказание",
            "Роман Фёдора Достоевского",
            850.00,
            "https://example.com/crime-punishment",
            fiction.id
        )

        create_book(
            db,
            "Война и мир",
            "Роман Льва Толстого",
            1200.00,
            "https://example.com/war-and-peace",
            fiction.id
        )

        print("База данных успешно заполнена!")

    finally:
        db.close()


if __name__ == "__main__":
    init_db()
