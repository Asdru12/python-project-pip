import utils
import random
import read_csv
import charts

data = [    
        {   
            'Country': 'Colombia',
            'Population': 900
        },
        {
            'Country': 'Brazil',
            'Population': 600
        },
        {   
            'Country': 'Argentina',
            'Population': 800
        }
    ]

def run():
    data = read_csv.read_csv('data.csv')
    continent = input('Type Continet => ')
    result = utils.population_by_porcentages(data, continent)

    countries = list(map(lambda x: x['Country/Territory'], data))
    porcentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(countries,porcentages)

    country = input('Type Country =>')
    print(country)

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        print(country)
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'], labels, values)

if __name__ == '__main__':
    run()
