import reflex as rx
from datetime import datetime, timedelta

"""
def calculate_age(birth_date: datetime):
    today = datetime.now()
    age = today - birth_date

    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day
    if days < 0:
        months -= 1
        days += (birth_date + timedelta(days=32)).day - birth_date.day
    if months < 0:
        years -= 1
        months += 12

    next_birthday = birth_date.replace(year=today.year + (1 if today.month > birth_date.month or (today.month == birth_date.month and today.day >= birth_date.day) else 0))
    days_until_birthday = (next_birthday - today).days
    return years, months, days, age.days, age.total_seconds() // 3600, age.total_seconds() // 60, days_until_birthday


def life_calculator() -> rx.Component:
    birth_date_input = rx.input(type="date", placeholder="Fecha de Nacimiento (dd/mm/yyyy)", id="birthDate")
    
    def show_result():
        birth_date = datetime.strptime(birth_date_input.value, "%Y-%m-%d")
        years, months, days, total_days, total_hours, total_minutes, days_until_birthday = calculate_age(birth_date)
        

        result_text = (
            f"Sua idade: {years} anos, {months} meses, {days} dias\n"
            f"{int(total_days)} dias\n"
            f"{int(total_hours)} horas\n"
            f"{int(total_minutes)} minutos\n"
            f"{days_until_birthday} dias para o seu aniversário"
        )
        return rx.text(result_text)

    return rx.box(
        rx.text("Calculadora de Días de Vida", font_size="24px", font_weight="bold"),
        birth_date_input,
        rx.button("Calcular", on_click=show_result),
        rx.div(id="result")
    )
"""