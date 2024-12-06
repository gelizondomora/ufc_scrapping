import logging
import pandas as pd
# from peleador_scrapper import peleador_scrapper
from historial_peleas_scrapper import historial_peleas_scrapper
from lista_peleas_scrapper import lista_peleas_scrapper
from lista_eventos_scrapper import lista_eventos_scrapper
import time

logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.info("Just logger")

    page = int(float(input(f'\n\n Seleccione pagina del sitio web: 1,2,3,4... \n\n')))
    if page == 1:
        url = 'http://www.ufcstats.com/statistics/events/completed'
    elif page > 1:
        url = f'http://www.ufcstats.com/statistics/events/completed?page={page}'
    else:
        print("Seleccion no es valida")
        exit()
    
    #Obtener lista de eventos y selecionar un evento
    event_list = lista_eventos_scrapper(url)

    #Descargar Masivamente una pagina

    all_in = str(input(f'\n\n Descarga masiva: <y/n> \n\n'))

    if all_in == "n":
        print(event_list.iloc[6,1])
        event_selection = input(f'\n\n Seleccione el numero del evento: \n\n {event_list}')

        event_selection = list(map(int,event_selection.split(',')))

        print(f'\n\n THIS IS THE EVENT SELECTION \n\n {event_selection}')

        for event in event_selection:
            event_url = event_list.iloc[event][2]
            #Obtener lista de peleas y peleadores
            fight_list = lista_peleas_scrapper(event_url)
            print(fight_list)
            
        # event_url = event_list.iloc[event_selection][2]
        # #Obtener lista de peleas y peleadores
        # fight_list = lista_peleas_scrapper(event_url)
        # print(fight_list)

        #Crear dataframe vacio
            historical_df =pd.DataFrame()
            all_fighter_stats =pd.DataFrame()

                #Obtener historico de peleas por peleador
            for i, url in fight_list.iterrows():
                fighter_1_historical, fighter_1_stats = historial_peleas_scrapper(url[3], i)
                fighter_2_historical, fighter_2_stats= historial_peleas_scrapper(url[4], i)

                full_historical_match= pd.concat([fighter_1_historical,fighter_2_historical])
                historical_df = pd.concat([historical_df,full_historical_match])
                
                fighter_stats = pd.concat([fighter_1_stats,fighter_2_stats])
                all_fighter_stats = pd.concat([all_fighter_stats,fighter_stats])
            
                historical_df.to_excel('/Users/gabrielelizondo/Library/CloudStorage/OneDrive-Personal/Apuestas/UFC_Stats/scraping/events/{}.xlsx'.format(event_list.iloc[event][1]))
              

    elif all_in == "y":
        event_index = event_list["INDEX"]
        print(event_index)

        for event_selection in event_index:
            event_url = event_list.iloc[event_selection][2]
            #Obtener lista de peleas y peleadores
            fight_list = lista_peleas_scrapper(event_url)
            print(fight_list)

    #Crear dataframe vacio
            historical_df =pd.DataFrame()
            all_fighter_stats =pd.DataFrame()

            for i, url in fight_list.iterrows():
                fighter_1_historical, fighter_1_stats = historial_peleas_scrapper(url[3], i)
                fighter_2_historical, fighter_2_stats= historial_peleas_scrapper(url[4], i)

                full_historical_match= pd.concat([fighter_1_historical,fighter_2_historical])
                historical_df = pd.concat([historical_df,full_historical_match])
                
                fighter_stats = pd.concat([fighter_1_stats,fighter_2_stats])
                all_fighter_stats = pd.concat([all_fighter_stats,fighter_stats])

                historical_df.to_excel('/Users/gabrielelizondo/Library/CloudStorage/OneDrive-Personal/Apuestas/UFC_Stats/scraping/events/{}.xlsx'.format(event_list.iloc[event_selection][1]))
                

    else:
        print("Seleccion no es valida")
        exit()


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

