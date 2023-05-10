import shodan



# Ingrese su clave de API de Shodan aquí

SHODAN_API_KEY = 'XXXXXXXXXXXXXXXXX'



def search_ip():

    # Solicitamos al usuario que ingrese una dirección IP para buscar

    ip = input('Ingrese una dirección IP para buscar: ')



    try:

        # Creamos una instancia de la clase Shodan con nuestra clave de API

        api = shodan.Shodan(SHODAN_API_KEY)



        # Realizamos la búsqueda en Shodan

        results = api.host(ip)



        # Mostramos los resultados obtenidos

        print('IP: {}'.format(results['ip_str']))

        print('Organización: {}'.format(results.get('org', 'n/a')))

        print('Sistema operativo: {}'.format(results.get('os', 'n/a')))

        print('Puertos abiertos: {}'.format(', '.join(str(port) for port in results['ports'])))

    except shodan.APIError as e:

        print('Error al realizar la búsqueda: {}'.format(e))



def search_url():

    # Solicitamos al usuario que ingrese una URL para buscar

    url = input('Ingrese una URL para buscar: ')



    try:

        # Creamos una instancia de la clase Shodan con nuestra clave de API

        api = shodan.Shodan(SHODAN_API_KEY)



        # Realizamos la búsqueda en Shodan

        results = api.search(url)



        # Mostramos los resultados obtenidos

        print('Resultados de la búsqueda de URL: {}'.format(results['total']))

        for result in results['matches']:

            print('IP: {}'.format(result['ip_str']))

            print('Puerto: {}'.format(result['port']))

            print('Organización: {}'.format(result.get('org', 'n/a')))

            print('Sistema operativo: {}'.format(result.get('os', 'n/a')))

            print('')

    except shodan.APIError as e:

        print('Error al realizar la búsqueda: {}'.format(e))



def main():

    while True:

        print('Ingrese una opción:')

        print('1. Buscar dirección IP')

        print('2. Buscar URL')

        print('0. Salir')



        try:

            option = int(input('>> '))

            if option == 1:

                search_ip()

            elif option == 2:

                search_url()

            elif option == 0:

                break

            else:

                print('Opción inválida, por favor ingrese una opción válida.')

        except ValueError:

            print('Opción inválida, por favor ingrese una opción válida.')



if __name__ == '__main__':

    main()
