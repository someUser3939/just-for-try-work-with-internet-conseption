import quistionary


def run_questionnaire():
  print("=== Добро пожаловать в анкету! ===")

  # Создаем словарь для хранения ответов
  user_data = {}

  # Задаем вопросы
  user_data["name"] = input("Как вас зовут? ")
  user_data["age"] = input("Сколько вам лет? ")
  user_data["city"] = input("В каком городе вы живете? ")
  user_data["hobby"] = input("Какое у вас хобби? ")

  print("\n--- Спасибо! Вот ваши ответы: ---")
  print(f"Имя: {user_data['name']}")
  print(f"Возраст: {user_data['age']}")
  print(f"Город: {user_data['city']}")
  print(f"Хобби: {user_data['hobby']}")


# Запуск программы
if __name__ == "__main__":
  run_questionnaire()
