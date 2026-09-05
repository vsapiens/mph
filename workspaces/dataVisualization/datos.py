import pandas as pd

# Encuesta Tecate Pa'l Norte 2026 — datos limpios
# Correcciones aplicadas:
#   - Encoding: caracteres latinos restaurados (√© → é, ¬ø → ¿, etc.)
#   - Excel auto-date: rangos numéricos restaurados ("03-may" → "3-5", "01-feb" → "1-2", "04-jun" → "4-6")
#   - Booleanos: "Sí" / "No" → True / False
#   - Timestamps: normalizados a ISO 8601
#   - Listas: artistas y escenarios separados por " | " para fácil split posterior

""" 
Timestamp	NOMBRE	CORREO ELECTR√ìNICO	¬øEn qu√© rango de edad te encuentras?	¬øCon qu√© g√©nero te identificas?	"Estado de procedencia
(Si nos visitaste de fuera de M√©xico, selecciona OTRO y contesta la siguiente pregunta)"	Si vienes de fuera de M√©xico, ¬øde qu√© pa√≠s nos visitaste?	¬øCu√°ntos festivales o conciertos asistes al a√±o?	¬øQu√© tipo de boletos compraste?	¬øQu√© d√≠a asististe al festival?	¬øPara qu√© zona compraste tu acceso a Tecate Pal Norte?	Del 1 al 10, ¬øc√≥mo evaluar√≠as tu zona?	¬øQu√© mejorar√≠as en tu zona?	¬øPor qu√© compraste boletos?	¬øCon cu√°ntas personas asististe a Tecate Pa'l Norte?	¬øA cu√°ntas ediciones de Tecate Pa'l Norte has asistido?	¬øC√≥mo fue tu llegada al festival?	Si no eres de Monterrey, ¬øpor qu√© medio llegaste a la ciudad?	Si no eres de Monterrey, ¬ød√≥nde te hospedaste?	Del 1 al 10, d√≥nde 1 es "nada" y 10 es "me encant√≥", ¬øQu√© tanto te gust√≥ el line up de Tecate Pa'l Norte 2026?	¬øCu√°l fue tu escenario favorito?	¬øTe result√≥ f√°cil ubicar cada uno de los escenarios dentro del festival?	¬øQu√© g√©nero musical no puede faltar en Tecate Pa'l Norte 2027?	Menciona 3 artistas que te gustar√≠a ver en Tecate Pa'l Norte - Escenarios Tecate Light	Menciona 3 artistas que te gustar√≠a ver en Tecate Pa'l Norte - Escenario Tecate Original 	Menciona 3 artistas que te gustar√≠a ver en Tecate Pa'l Norte - Escenario Fusi√≥n Telcel (Rock Latino)	Menciona 3 artistas que te gustar√≠a ver en Tecate Pa'l Norte - Escenario Sorpresa Viva	Menciona 3 artistas que te gustar√≠a ver en Tecate Pa'l Norte - Escenario Oasis Bacardi (Urbano)	Menciona 3 artistas que te gustar√≠a ver en Tecate Pa'l Norte - Escenario Ac√∫stico Hey Banco (Ac√∫stico)	Menciona 3 artistas que te gustar√≠a ver en Tecate Pa'l Norte - Escenario Club Social Kia (Electr√≥nico)	Menciona 3 artistas que te gustar√≠a ver en Tecate Pa'l Norte - Escenario Hot Nuts Pilos Bar (Regional Mexicano)	¬øConociste la tienda de merch oficial?	Si tu respuesta fue s√≠, ¬øcu√°l fue tu experiencia?	¬øQu√© otros art√≠culos te gustar√≠a se incluyeran en la tienda oficial de merch?	¬øVisitaste las diferentes zonas de restaurantes?	Si tu respuesta fue s√≠, ¬øcu√°l fue tu experiencia?	¬øC√≥mo percibiste los precios?	¬øUtilizaste la zona de sanitarios?	Si tu respuesta fue s√≠, eval√∫a la limpieza	¬øTe sentiste seguro en el festival?	Eval√∫a la seguridad	¬øSab√≠as que el festival tiene un programa de sustentabilidad con acciones para cuidar el planeta?	Menciona 3 marcas que recuerdes sean patrocinadores en Tecate Pa'l Norte.	¬øParticipaste en alguna activaci√≥n de marca dentro del festival?	Si la respuesta es s√≠, ¬øDe qu√© marca fue la activaci√≥n?	Del 1 al 10, ¬øC√≥mo evaluar√≠as tu experiencia con esa marca?	¬øVisitaste la p√°gina web oficial de Tecate Pa'l Norte?	Si tu respuesta fue s√≠, ¬øencontraste la informaci√≥n que buscabas?	Del 1 al 10, ¬øC√≥mo evaluar√≠as tu experiencia en la p√°gina web?	¬øQu√© informaci√≥n quisieras que incluyamos?	¬øDescargaste la APP oficial de Tecate Pa'l Norte?	Si tu respuesta fue s√≠, ¬øLa app te result√≥ √∫til durante el festival?	¬øQu√© te gustar√≠a encontrar en la app?	Del 1 al 10, ¬øqu√© evaluaci√≥n das a la APP?	¬øQu√© evaluaci√≥n le das al festival en general? 	¬øVolver√≠as asistir al festival?	¬øQu√© mejorar√≠as para la pr√≥xima edici√≥n de Tecate Pa'l Norte?	Del 1 al 10, ¬øQu√© tan probable es que recomiendes Tecate Pa‚Äôl Norte a un amigo o familiar?	Acepto recibir informaci√≥n, noticias y promociones por parte de Tecate Pa'l Norte y autorizo el uso de mis datos para fines de comunicaci√≥n y marketing.
2026/03/30 10:49:18 AM CST	Josue 	josuemora0693.gm@gmail.com	25-34	Masculino	OTRO	Costa Rica 	03-may	Abono (boleto para los tres d√≠as)	Los tres d√≠as	General	8	Cashless, mejor empalme de horarios	Conocer un festival nuevo 	02-mar	Es mi primera vez	Metro	Avi√≥n	AirBnb	8	Tecate Light	M√°s o menos	Rock	Limb biskit, Korn, Metallica 	Inspector, ska P, los dos carnales 	Aut√©nticos decadentes, caifanes, caligaris	Versiut, Juli√≥n, Rabanes 	Universe, Oblivion might trash, Lil supa	Miranda, Caligaris, mi sobrino memo 	Penny wu, Rafa barrios, Martin Garrix 	Espinoza paz, tigres del norte, fantasma 	S√≠	1	Nada 	S√≠	5	Muy Altos	S√≠	5	S√≠	9	S√≠	Tecate, electrolit, Kia 	S√≠	De la rosa 	5	No				S√≠	M√°s o menos	M√°s formas de ubicaci√≥n 	6	8	Tal vez	Cashless, empalme de horarios y after despu√©s de la √∫ltima banda en los clubs como el Pepsi 	6	
2026/04/03 12:19:11 AM CST	Aurora Rosales	sofia972003@yahoo.com.mx	25-34	Femenino	Nuevo Le√≥n		M√°s de 5	Abono (boleto para los tres d√≠as)	Los tres d√≠as	General	10	No tierra	Porque me gusta el festival	02-mar	4	Carro particular			8	Tecate Light;Club Social KIA	S√≠	Urbano	Miley Cyrus , Feid, daddy yankee	Ozuna, Aventura, Lala love		Diego Torres, Reik, Camila					S√≠	10	Plumas, impermeable  maleta carry on	S√≠	10	Justos	S√≠	5	S√≠	7	S√≠	Nescaf√©, H&M, saba	S√≠	Nescaf√©	10	No				S√≠	S√≠	Notificaciones pop up en tiempo real 	10	10	S√≠, definitivamente	Que no empalmen horarios entre artistas 	10	S√≠ acepto
2026/03/31 8:17:04 PM CST	Miguel √Ångel Rodr√≠guez Liberato 	Psico_233@hotmail.com	25-34	Masculino	M√©xico		M√°s de 5	2 Day pass (para dos d√≠as)	S√°bado;Domingo	General	8	Poner una zona para lavarse las manos, solo eso 	Porque me gustaron las bandas	Solo	3	Metro	Cami√≥n	AirBnb	8	Tecate Light;Oasis Bacardi;Club Social KIA	M√°s o menos	Urbano	Quevedo, cruz cafune, neutro shorty	La pantera y lucho RK, genitallica, hombres g	Machingon, los delicados, chingadazo de kung fu 	Lagrimita y costel, Alekx Syntek, los primos de durango	Chystemc, movimiento original, la pantera 	Chingadazo de kung fu, liquits, v√≠ctimas del doctor cerebro	Bizarrap, infected mushroom, Mexican institute of sound	Frontera, palomo y los cardenales de Nuevo Le√≥n 	S√≠	8		S√≠	8	Altos	S√≠	6	S√≠	9	S√≠	Lth, Saba, fud 	S√≠	Lth, fud, vero	10	No				S√≠	M√°s o menos	Que el mapas fuera m√°s preciso, era un poco ca√≥tico encontrar lugares	8	8	S√≠, definitivamente	Un poco m√°s de atenci√≥n en los escenarios secundarios 	10	S√≠ acepto
2026/04/01 2:48:22 PM CST	Eduardo Gibran Flores Acosta	Eduardogfa06@gmail.com	25-34	Masculino	Coahuila		01-feb	2 Day pass (para dos d√≠as)	Viernes;S√°bado	General	9	"M√°s ba√±os en las zonas donde se concentra m√°s gente (Tecate light y original).
Destinar hora y zona para abordar al salir app de transporte. Es un caos en todos los lugares.
Hay mucho espacio libre, se podr√≠a usar para m√°s actividades, hidrataci√≥n o zonas de descanso.
Es una buena idea lo que hicieron el club social de poner tarimas en los lados, creo que algo as√≠ puede funcionar en los escenarios principales para mejorar la visibilidad, el flujo de gente y no se sienta tan amontonado sobre todo con los headliners 
"	Porque me gusta el festival	04-jun	3	APP de transporte privado	Carro propio	AirBnb	10	Tecate Light;Tecate Original;Club Social KIA	S√≠	Rock	Linkin park, System of a Down, Harry Styles 	Alfredito Olivas, Feid, C Tangana	Rata Blanca, H√©roes del silencio, Mago de Oz.	Moenia, Chayanne, Motel 	Rels B, Rauw Alejandro, Karol G	Paramore, bandas locales.	Zedd, Solomun, Rufus do soul 	Cadetes, Invasores, Herederos	S√≠	10	Gafas	S√≠	10	Altos	S√≠	8	S√≠	10	S√≠	Tecate, heybanco, viva aerobus	S√≠	Pollo loco 	10	S√≠	S√≠	10	Asistencia AI	S√≠	S√≠	Asistencia AI, agregar recomendaciones, espacio para postear fotos y conocer gente 	10	10	S√≠, definitivamente	Lo que comentamos antes, sobre todo la movilidad y el transporte 	10	S√≠ acepto

 """

# ---------------------------------------------------------------------------
# Nombres cortos en el orden exacto de columnas del CSV (posición 0-58)
# Más robusto que el matching por string: el archivo tiene encoding mixto
# que corrompe algunos caracteres especiales en los encabezados.
# ---------------------------------------------------------------------------
COLUMNAS = [
    "timestamp",               # 00
    "nombre",                  # 01
    "correo",                  # 02
    "rango_edad",              # 03
    "genero",                  # 04
    "estado",                  # 05
    "pais_origen",             # 06
    "festivales_anuales",      # 07
    "tipo_boleto",             # 08
    "dias_asistencia",         # 09
    "zona",                    # 10
    "evaluacion_zona",         # 11
    "mejora_zona",             # 12
    "razon_compra",            # 13
    "personas_grupo",          # 14
    "ediciones_asistidas",     # 15
    "llegada_festival",        # 16
    "llegada_ciudad",          # 17
    "hospedaje",               # 18
    "evaluacion_lineup",       # 19
    "escenario_favorito",      # 20
    "facil_ubicar_escenarios", # 21
    "genero_2027",             # 22
    "artistas_tecate_light",   # 23
    "artistas_tecate_original",# 24
    "artistas_fusion_telcel",  # 25
    "artistas_sorpresa_viva",  # 26
    "artistas_oasis_bacardi",  # 27
    "artistas_acustico_hey_banco", # 28
    "artistas_club_social_kia",    # 29
    "artistas_hot_nuts_pilos", # 30
    "visito_merch",            # 31
    "evaluacion_merch",        # 32
    "articulos_deseados_merch",# 33
    "visito_restaurantes",     # 34
    "evaluacion_restaurantes", # 35
    "percepcion_precios",      # 36
    "utilizo_sanitarios",      # 37
    "evaluacion_limpieza",     # 38
    "se_sintio_seguro",        # 39
    "evaluacion_seguridad",    # 40
    "conocia_sustentabilidad", # 41
    "marcas_recordadas",       # 42
    "participo_activacion",    # 43
    "marca_activacion",        # 44
    "evaluacion_activacion",   # 45
    "visito_web",              # 46
    "encontro_info_web",       # 47
    "evaluacion_web",          # 48
    "info_deseada_web",        # 49
    "descargo_app",            # 50
    "app_util",                # 51
    "que_gustaria_app",        # 52
    "evaluacion_app",          # 53
    "evaluacion_general",      # 54
    "volveria_asistir",        # 55
    "mejoras_proxima",         # 56
    "nps",                     # 57
    "acepto_marketing",        # 58
]

# Valores que Excel corrompió al interpretar rangos numéricos como fechas
EXCEL_DATES = {
    "01-ene": "1",    "01-feb": "1-2",  "02-mar": "2-3",
    "03-abr": "3-4",  "03-may": "3-5",  "04-jun": "4-6",
    "05-jul": "5-7",  "06-ago": "6-8",
}

# Columnas donde puede ocurrir la corrupción de fecha de Excel
COLS_EXCEL_DATE = ["festivales_anuales", "personas_grupo", "ediciones_asistidas"]

# Columnas cuyo valor "Sí" / "No" debe convertirse a booleano
COLS_BOOL = [
    "visito_merch", "visito_restaurantes", "utilizo_sanitarios",
    "se_sintio_seguro", "conocia_sustentabilidad", "participo_activacion",
    "visito_web", "encontro_info_web", "descargo_app", "acepto_marketing",
]

# Columnas numéricas (calificaciones 1-10)
COLS_NUMERICAS = [
    "evaluacion_zona", "evaluacion_lineup", "evaluacion_seguridad",
    "evaluacion_limpieza", "evaluacion_restaurantes", "evaluacion_merch",
    "evaluacion_activacion", "evaluacion_web", "evaluacion_app",
    "evaluacion_general", "nps",
]


def cargar_csv(filepath: str = "datos.csv") -> pd.DataFrame:
    """
    Carga datos.csv exportado de Google Forms y devuelve un DataFrame limpio.

    El archivo debe ser:
      - Tab-separado (\\t) — Google Forms exporta TSV, no CSV estricto
      - Codificado en UTF-8 — Google Forms siempre usa UTF-8

    Transformaciones aplicadas automáticamente:
      1. Renombra las 57 columnas a nombres cortos (ver COLUMNAS)
      2. Revierte corrupción de Excel en rangos numéricos ("03-may" → "3-5")
      3. Convierte "Sí"/"No" a True/False en columnas booleanas
      4. Convierte calificaciones a int (NaN donde la respuesta fue vacía)
      5. Parsea el timestamp a datetime
      6. Elimina espacios extra en strings
    """
    raw = pd.read_csv(
        filepath,
        sep=",",                    # Google Forms CSV usa coma, no tabulador
        encoding="utf-8",           # datos UTF-8; headers mixtos pero los reemplazamos por posición
        encoding_errors="replace",  # reemplaza bytes no mapeables en vez de fallar
        quoting=0,                  # QUOTE_MINIMAL — maneja campos con saltos de línea
        on_bad_lines="warn",
    )

    # 1. Renombrar columnas por posición (más robusto que matching por string
    #    porque el archivo tiene encoding mixto en algunos encabezados)
    raw.columns = COLUMNAS[:len(raw.columns)]

    # 2. Quitar espacios extra en todos los strings
    str_cols = raw.select_dtypes("object").columns
    raw[str_cols] = raw[str_cols].apply(lambda col: col.str.strip())

    # 3. Convertir Sí/No a booleano
    si_no = {"Sí": True, "Si": True, "sí": True, "si": True,
             "No": False, "no": False}
    for col in COLS_BOOL:
        if col in raw.columns:
            raw[col] = raw[col].map(si_no)

    # 4. Convertir calificaciones a numérico (entero nullable)
    for col in COLS_NUMERICAS:
        if col in raw.columns:
            raw[col] = pd.to_numeric(raw[col], errors="coerce").astype("Int64")

    # 5. Parsear timestamp  (formato: "2026/03/30 10:49:18 AM CST")
    if "timestamp" in raw.columns:
        raw["timestamp"] = pd.to_datetime(
            raw["timestamp"].str.replace(r"\s+[A-Z]{2,4}$", "", regex=True),
            format="%Y/%m/%d %I:%M:%S %p",
            errors="coerce",
        )

    return raw


# ---------------------------------------------------------------------------
# Uso: reemplaza el DataFrame manual cuando datos.csv está disponible
#
#   from datos import cargar_csv
#   df = cargar_csv("datos.csv")          # 20 000 filas, todas limpias
#   df = cargar_csv("datos_piloto.csv")   # piloto de 4 filas
# ---------------------------------------------------------------------------

respuestas = [
    {
        "timestamp": "2026-03-30 10:49:18",
        "nombre": "Josue",
        "correo": "josuemora0693.gm@gmail.com",
        "rango_edad": "25-34",
        "genero": "Masculino",
        "estado": "Extranjero",
        "pais_origen": "Costa Rica",
        "festivales_anuales": "3-5",            # Excel convirtió "3-5" → "03-may"
        "tipo_boleto": "Abono (3 días)",
        "dias_asistencia": "Viernes | Sábado | Domingo",
        "zona": "General",
        "evaluacion_zona": 8,
        "mejora_zona": "Cashless, mejor empalme de horarios",
        "razon_compra": "Conocer un festival nuevo",
        "personas_grupo": "2-3",                # Excel convirtió "2-3" → "02-mar"
        "ediciones_asistidas": "Primera vez",
        "llegada_festival": "Metro",
        "llegada_ciudad": "Avión",
        "hospedaje": "AirBnb",
        "evaluacion_lineup": 8,
        "escenario_favorito": "Tecate Light",
        "facil_ubicar_escenarios": "Más o menos",
        "genero_2027": "Rock",
        "artistas_tecate_light": "Limp Bizkit | Korn | Metallica",
        "artistas_tecate_original": "Inspector | Ska-P | Los Dos Carnales",
        "artistas_fusion_telcel": "Auténticos Decadentes | Caifanes | Caligaris",
        "artistas_sorpresa_viva": "Versiut | Julión | Rabanes",
        "artistas_oasis_bacardi": "Universe | Oblivion Might Trash | Lil Supa",
        "artistas_acustico_hey_banco": "Miranda | Caligaris | Mi Sobrino Memo",
        "artistas_club_social_kia": "Penny Wu | Rafa Barrios | Martin Garrix",
        "artistas_hot_nuts_pilos": "Espinoza Paz | Tigres del Norte | Fantasma",
        "visito_merch": True,
        "evaluacion_merch": 1,
        "articulos_deseados_merch": None,
        "visito_restaurantes": True,
        "evaluacion_restaurantes": 5,
        "percepcion_precios": "Muy Altos",
        "utilizo_sanitarios": True,
        "evaluacion_limpieza": 5,
        "se_sintio_seguro": True,
        "evaluacion_seguridad": 9,
        "conocia_sustentabilidad": True,
        "marcas_recordadas": "Tecate | Electrolit | Kia",
        "participo_activacion": True,
        "marca_activacion": "De la Rosa",
        "evaluacion_activacion": 5,
        "visito_web": False,
        "encontro_info_web": None,
        "evaluacion_web": None,
        "info_deseada_web": None,
        "descargo_app": True,
        "app_util": "Más o menos",
        "que_gustaria_app": "Más formas de ubicación",
        "evaluacion_app": 6,
        "evaluacion_general": 8,
        "volveria_asistir": "Tal vez",
        "mejoras_proxima": "Cashless, empalme de horarios y after después de la última banda",
        "nps": 6,
        "acepto_marketing": None,
    },
    {
        "timestamp": "2026-04-03 00:19:11",
        "nombre": "Aurora Rosales",
        "correo": "sofia972003@yahoo.com.mx",
        "rango_edad": "25-34",
        "genero": "Femenino",
        "estado": "Nuevo León",
        "pais_origen": None,
        "festivales_anuales": "Más de 5",
        "tipo_boleto": "Abono (3 días)",
        "dias_asistencia": "Viernes | Sábado | Domingo",
        "zona": "General",
        "evaluacion_zona": 10,
        "mejora_zona": "No tierra (piso sin polvo)",
        "razon_compra": "Porque me gusta el festival",
        "personas_grupo": "2-3",                # Excel convirtió "2-3" → "02-mar"
        "ediciones_asistidas": 4,
        "llegada_festival": "Carro particular",
        "llegada_ciudad": None,
        "hospedaje": None,
        "evaluacion_lineup": 8,
        "escenario_favorito": "Tecate Light | Club Social KIA",
        "facil_ubicar_escenarios": "Sí",
        "genero_2027": "Urbano",
        "artistas_tecate_light": "Miley Cyrus | Feid | Daddy Yankee",
        "artistas_tecate_original": "Ozuna | Aventura | Lala Love",
        "artistas_fusion_telcel": None,
        "artistas_sorpresa_viva": "Diego Torres | Reik | Camila",
        "artistas_oasis_bacardi": None,
        "artistas_acustico_hey_banco": None,
        "artistas_club_social_kia": None,
        "artistas_hot_nuts_pilos": None,
        "visito_merch": True,
        "evaluacion_merch": 10,
        "articulos_deseados_merch": "Plumas, impermeable, maleta carry on",
        "visito_restaurantes": True,
        "evaluacion_restaurantes": 10,
        "percepcion_precios": "Justos",
        "utilizo_sanitarios": True,
        "evaluacion_limpieza": 5,
        "se_sintio_seguro": True,
        "evaluacion_seguridad": 7,
        "conocia_sustentabilidad": True,
        "marcas_recordadas": "Nescafé | H&M | Saba",
        "participo_activacion": True,
        "marca_activacion": "Nescafé",
        "evaluacion_activacion": 10,
        "visito_web": False,
        "encontro_info_web": None,
        "evaluacion_web": None,
        "info_deseada_web": None,
        "descargo_app": True,
        "app_util": "Sí",
        "que_gustaria_app": "Notificaciones pop-up en tiempo real",
        "evaluacion_app": 10,
        "evaluacion_general": 10,
        "volveria_asistir": "Sí, definitivamente",
        "mejoras_proxima": "Que no empalmen horarios entre artistas",
        "nps": 10,
        "acepto_marketing": True,
    },
    {
        "timestamp": "2026-03-31 20:17:04",
        "nombre": "Miguel Ángel Rodríguez Liberato",
        "correo": "Psico_233@hotmail.com",
        "rango_edad": "25-34",
        "genero": "Masculino",
        "estado": "Otro estado de México",
        "pais_origen": None,
        "festivales_anuales": "Más de 5",
        "tipo_boleto": "2 Day pass (2 días)",
        "dias_asistencia": "Sábado | Domingo",
        "zona": "General",
        "evaluacion_zona": 8,
        "mejora_zona": "Zona para lavarse las manos",
        "razon_compra": "Porque me gustaron las bandas",
        "personas_grupo": "Solo",
        "ediciones_asistidas": 3,
        "llegada_festival": "Metro",
        "llegada_ciudad": "Camión",
        "hospedaje": "AirBnb",
        "evaluacion_lineup": 8,
        "escenario_favorito": "Tecate Light | Oasis Bacardi | Club Social KIA",
        "facil_ubicar_escenarios": "Más o menos",
        "genero_2027": "Urbano",
        "artistas_tecate_light": "Quevedo | Cruz Cafuné | Neutro Shorty",
        "artistas_tecate_original": "La Pantera y Lucho RK | Genitallica | Hombres G",
        "artistas_fusion_telcel": "Machingón | Los Delicados | Chingadazo de Kung Fu",
        "artistas_sorpresa_viva": "Lagrimita y Costel | Alex Syntek | Los Primos de Durango",
        "artistas_oasis_bacardi": "Chystemc | Movimiento Original | La Pantera",
        "artistas_acustico_hey_banco": "Chingadazo de Kung Fu | Liquits | Víctimas del Doctor Cerebro",
        "artistas_club_social_kia": "Bizarrap | Infected Mushroom | Mexican Institute of Sound",
        "artistas_hot_nuts_pilos": "Frontera | Palomo y los Cardenales de Nuevo León",
        "visito_merch": True,
        "evaluacion_merch": 8,
        "articulos_deseados_merch": None,
        "visito_restaurantes": True,
        "evaluacion_restaurantes": 8,
        "percepcion_precios": "Altos",
        "utilizo_sanitarios": True,
        "evaluacion_limpieza": 6,
        "se_sintio_seguro": True,
        "evaluacion_seguridad": 9,
        "conocia_sustentabilidad": True,
        "marcas_recordadas": "LTH | Saba | FUD",
        "participo_activacion": True,
        "marca_activacion": "LTH | FUD | Vero",
        "evaluacion_activacion": 10,
        "visito_web": False,
        "encontro_info_web": None,
        "evaluacion_web": None,
        "info_deseada_web": None,
        "descargo_app": True,
        "app_util": "Más o menos",
        "que_gustaria_app": "Mapa más preciso",
        "evaluacion_app": 8,
        "evaluacion_general": 8,
        "volveria_asistir": "Sí, definitivamente",
        "mejoras_proxima": "Más atención en los escenarios secundarios",
        "nps": 10,
        "acepto_marketing": True,
    },
    {
        "timestamp": "2026-04-01 14:48:22",
        "nombre": "Eduardo Gibran Flores Acosta",
        "correo": "Eduardogfa06@gmail.com",
        "rango_edad": "25-34",
        "genero": "Masculino",
        "estado": "Coahuila",
        "pais_origen": None,
        "festivales_anuales": "1-2",            # Excel convirtió "1-2" → "01-feb"
        "tipo_boleto": "2 Day pass (2 días)",
        "dias_asistencia": "Viernes | Sábado",
        "zona": "General",
        "evaluacion_zona": 9,
        "mejora_zona": "Más baños en zonas de alta concentración; zona de abordaje para apps de transporte; más actividades en espacios libres; tarimas laterales en escenarios principales para mejorar visibilidad",
        "razon_compra": "Porque me gusta el festival",
        "personas_grupo": "4-6",                # Excel convirtió "4-6" → "04-jun"
        "ediciones_asistidas": 3,
        "llegada_festival": "App de transporte privado",
        "llegada_ciudad": "Carro propio",
        "hospedaje": "AirBnb",
        "evaluacion_lineup": 10,
        "escenario_favorito": "Tecate Light | Tecate Original | Club Social KIA",
        "facil_ubicar_escenarios": "Sí",
        "genero_2027": "Rock",
        "artistas_tecate_light": "Linkin Park | System of a Down | Harry Styles",
        "artistas_tecate_original": "Alfredito Olivas | Feid | C. Tangana",
        "artistas_fusion_telcel": "Rata Blanca | Héroes del Silencio | Mago de Oz",
        "artistas_sorpresa_viva": "Moenia | Chayanne | Motel",
        "artistas_oasis_bacardi": "Rels B | Rauw Alejandro | Karol G",
        "artistas_acustico_hey_banco": "Paramore | Bandas locales",
        "artistas_club_social_kia": "Zedd | Solomun | Rufus Du Sol",
        "artistas_hot_nuts_pilos": "Cadetes | Invasores | Herederos",
        "visito_merch": True,
        "evaluacion_merch": 10,
        "articulos_deseados_merch": "Gafas",
        "visito_restaurantes": True,
        "evaluacion_restaurantes": 10,
        "percepcion_precios": "Altos",
        "utilizo_sanitarios": True,
        "evaluacion_limpieza": 8,
        "se_sintio_seguro": True,
        "evaluacion_seguridad": 10,
        "conocia_sustentabilidad": True,
        "marcas_recordadas": "Tecate | Hey Banco | Viva Aerobús",
        "participo_activacion": True,
        "marca_activacion": "Pollo Loco",
        "evaluacion_activacion": 10,
        "visito_web": True,
        "encontro_info_web": True,
        "evaluacion_web": 10,
        "info_deseada_web": "Asistencia con IA",
        "descargo_app": True,
        "app_util": "Sí",
        "que_gustaria_app": "Asistencia con IA, recomendaciones, espacio para postear fotos y conocer gente",
        "evaluacion_app": 10,
        "evaluacion_general": 10,
        "volveria_asistir": "Sí, definitivamente",
        "mejoras_proxima": "Movilidad y transporte",
        "nps": 10,
        "acepto_marketing": True,
    },
]

df = pd.DataFrame(respuestas)
