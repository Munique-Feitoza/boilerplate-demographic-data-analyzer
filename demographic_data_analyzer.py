import pandas as pd

def calculate_demographic_data(print_data=True):
    # Leitura do arquivo CSV
    df = pd.read_csv("adult.data.csv")

    # 1. Quantidade de cada raça
    race_count = df['race'].value_counts()

    # 2. Idade média dos homens
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Porcentagem com diploma de Bacharel
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Pessoas com ensino superior
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    # 5. % com salário >50K entre pessoas com e sem ensino superior
    higher_education_rich = round(
        (df[higher_education]['salary'] == '>50K').mean() * 100, 1
    )
    lower_education_rich = round(
        (df[lower_education]['salary'] == '>50K').mean() * 100, 1
    )

    # 6. Mínimo de horas trabalhadas por semana
    min_work_hours = df['hours-per-week'].min()

    # 7. % de pessoas que trabalham o mínimo de horas e ganham >50K
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((min_workers['salary'] == '>50K').mean() * 100, 1)

    # 8. País com maior % de pessoas com salário >50K
    country_salary_counts = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack()
    country_salary_over_50k = country_salary_counts['>50K'] * 100
    highest_earning_country = country_salary_over_50k.idxmax()
    highest_earning_country_percentage = round(country_salary_over_50k.max(), 1)

    # 9. Ocupação mais comum entre pessoas >50K na Índia
    top_IN_occupation = df[
        (df['native-country'] == 'India') & (df['salary'] == '>50K')
    ]['occupation'].value_counts().idxmax()

    # Impressão opcional
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    # Retorno dos dados
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
