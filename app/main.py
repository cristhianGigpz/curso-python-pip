import utils
import read_csv
import charts
"""
data = [{
    'Country': 'Colombia',
    'Population': 500
}, {
    'Country': 'Bolivia',
    'Population': 300
}, {
    'Country': 'Peru',
    'Population': 200
}]
"""


def run():
  data = read_csv.read_csv('./data.csv')

  data = list(filter(lambda item: item['Continent'] == 'South America', data))
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)

  #print(utils.A)
  
  country = input('Type Country => ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0] #aqui resulta se vuelve diccionario
    labels, values = utils.get_population(country)
    #print(labels, values)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)
  
  #print(result)


if __name__ == '__main__':
  run()
