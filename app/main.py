
from app.db.db import SessionLocal
from app.db.models import Category


def main():
    db = SessionLocal()

    try:
        categories = db.query(Category).all()

        print("\n========== КАТАЛОГ КНИГ ==========\n")

        for category in categories:
            print(f"\nКатегория: {category.title}")
            print("-" * 50)

            for book in category.books:
                print(f"Название: {book.title}")
                print(f"Описание: {book.description}")
                print(f"Цена: {book.price} руб.")
                print(f"Ссылка: {book.url}")
                print()

        print("========== КОНЕЦ КАТАЛОГА ==========")

    finally:
        db.close()


if __name__ == "__main__":
    main()
