
def get_votes():
    votes = {}
    for id_, vote in votos_congreso.items():
        dYAN = vote.get("YAN", [0, 0, 0])[0] - vote.get("YAN", [0, 0, 0])[2]
        vote["result"] = "Y" if dYAN > 0 else "N" if dYAN < 0 else vote.get("result")
        vote["blocktype"] = "congreso"
        vote["sortable_date"] = sortable_date(vote.get("fecha"))
        vote["tipo_texto"] = get_vote_type_text(vote)

        votes[f"congreso-{id_}"] = vote
    return votes


def get_vote_type_text(vote):
    match vote["tipo"]:
        case "M":
            return "Moción"
        case "E":
            return "Enmienda"
        case "RDL":
            return "Real Decreto Ley"
        case "DL":
            return "Decreto Ley"
        case "PL":
            if "Gobierno" in vote["propone"]:
                return "Proyecto de Ley"
            else:
                return "Proposición de Ley"
        case "PNL":
            if "Gobierno" in vote["propone"]:
                return "Proyecto No de Ley"
            else:
                return "Proposición No de Ley"
        case _:
            return vote["tipo"]


def sortable_date(date):
    if not date:
        date = "00/00/0000"
    broken = date.split("/")
    return f"{broken[2]}/{broken[1]}/{broken[0]}"

# PL = Proyecto de Ley (Gobierno) - únicos que pueden Presupuestos
# PL ? = Proposición de Ley (15 diputados, 25 senadores o 1 grupo)
#      -> ILP = Iniciativa Legislativa Popular (500.000 firmas)
# Si las leyes son orgánicas hace falta mayoría absoluta [!] (si no es orgánica es ordinaria)
    # Las orgánicas son sobre derechos fundamentales, libertades públicas, estatutos, régimen electoral y otras cosas serias
# Decreto-Ley es directa sin PL por motivos de urgencia
# Decreto legislativo es otra cosa
# E = Enmienda = Cambiar algo de una ley
# M = Moción = Pedir a los grupos que se posicionen sobre un tema

# Toma en Consideración = Se decide si hay que legislar sobre eso (Proyecto de Ley se lo salta)
# Enmiendas (totalidad / articulado)


votos_congreso = {
    1: {"name": "Que las empresas y fondos buitre no puedan comprar casas",
        "desc": "Y que las empresas que especulan con ellas paguen más impuestos que las familias que las usan para vivir.",
        "ámbitos": ["Vivienda"],
        "propone": ["Sumar"],
        "ref": "162/000498",
        "tipo": "PNL",
        "fecha": "20/05/2026",
        "url": "https://www.congreso.es/es/busqueda-de-iniciativas?p_p_id=iniciativas&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_iniciativas_mode=mostrarDetalle&_iniciativas_legislatura=XV&_iniciativas_id=162/000498",
        "result": "N",
        "YAN": [169, 8, 170],
        "votos": {
            "Podemos": "Y",
            "Sumar": "Y",
            "ERC": "Y",
            "PSOE": "Y",
            "Junts": "A",
            "PP": "N",
            "VOX": "N",
        }},
    2: {
        "name": "Mandar apoyo urgente a Ceuta",
        "desc": "Ayudas para autónomos y empresas, para la ciudad, para ONGs y para gestionar la atención humanitaria.",
        "ámbitos": ["Inmigración"],
        "propone": ["Gobierno"],
        "ref": "130/000053",
        "tipo": "DL",
        "fecha": "16/09/2026",
        "result": "Y",
        "YAN": [304, 7, 33],
        "votos": {
            "Podemos": "Y",
            "Sumar": "Y",
            "ERC": "Y",
            "PSOE": "Y",
            "Junts": "A",
            "PP": "Y",
            "VOX": "N",
        },
    },
    3: {
        "name": "Que podamos saber de qué maneras presionan las empresas a los políticos",
        "desc": "Regular y hacer transparente la manera en la que grupos de interés y empresas presionan para cambiar las leyes.",
        "ámbitos": [""],
        "propone": ["Gobierno"],
        "ref": "130/000052",
        "tipo": "RDL",
        "fecha": "27/08/2026",
        "urls": {"congreso": "https://www.congreso.es/es/busqueda-de-iniciativas?p_p_id=iniciativas&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_iniciativas_mode=mostrarDetalle&_iniciativas_legislatura=XV&_iniciativas_id=130%2F000052"},
        "result": "N",
        "YAN": [155, 12, 179],
        "votos": {
                "Podemos": "A",
                "Sumar": "Y",
                "ERC": "Y",
                "PSOE": "Y",
                "Junts": "N",
                "PP": "N",
                "VOX": "N",
            },
    },
    4: {
        "name": "Que no se pueda echar de su casa a las familias vulnerables",
        "desc": "Y que el gobierno pague al propietario para compensar por el alquiler. También lleva ayudas para DANAs e incendios.",
        "ámbitos": [""],
        "propone": ["Gobierno"],
        "ref": "130/000030",
        "tipo": "RDL",
        "fecha": "26/12/2025",
        "urls": {},
        "result": "N",
        "YAN": [171, 0, 178],
        "votos": {
                "Podemos": "Y",
                "Sumar": "Y",
                "ERC": "Y",
                "PSOE": "Y",
                "Junts": "N",
                "PP": "N",
                "VOX": "N",
            },
    },
    5: {
        "name": "Prohibir las terapias de conversión",
        "desc": "Que sean un delito las terapias que intentan cambiar, esconder o eliminar la orientación sexual o la identidad de género.",
        "ámbitos": [""],
        "propone": ["Sumar", "BNG"],
        "ref": "122/000167",
        "tipo": "PL",
        "fecha": "18/02/2025",
        "urls": {},
        "result": "Y",
        "YAN": [178, 138, 32],
        "votos": {
                "Podemos": "Y",
                "Sumar": "Y",
                "ERC": "Y",
                #"BNG": "Y",
                "PSOE": "Y",
                "Junts": "Y",
                "PP": "A",
                "VOX": "N",
            },
    },
    6: {
        "name": "Que las personas con menos dinero paguen menos por los medicamentos",
        "desc": "",
        "ámbitos": ["Salud"],
        "propone": ["Gobierno"],
        "ref": "130/000042",
        "tipo": "RDL",
        "fecha": "14/05/2026",
        "urls": {"congreso": "https://www.congreso.es/es/busqueda-de-iniciativas?p_p_id=iniciativas&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_iniciativas_mode=mostrarDetalle&_iniciativas_legislatura=XV&_iniciativas_id=130%2F000042"},
        "result": "Y",
        "YAN": [164, 149, 33],
        "votos": {
                "Podemos": "Y",
                "Sumar": "Y",
                "ERC": "A",
                "PSOE": "Y",
                "Junts": "A",
                "PP": "A",
                "VOX": "N",
            },
    },
    7: {
        "name": "Que las empresas no puedan aprovechar las emergencias para abusar con los precios",
        "desc": "Que cuando haya emergencias, el precio máximo de las cosas no pueda superar el máximo del último mes.",
        "ámbitos": [""],
        "propone": ["Gobierno"],
        "ref": "130/000035",
        "tipo": "RDL",
        "fecha": "12/02/2026",
        "urls": {"congreso": "https://www.congreso.es/es/busqueda-de-iniciativas?p_p_id=iniciativas&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_iniciativas_mode=mostrarDetalle&_iniciativas_legislatura=XV&_iniciativas_id=130%2F000035"},
        "result": "N",
        "YAN": [172, 1, 177],
        "votos": {
                "Podemos": "Y",
                "Sumar": "Y",
                "ERC": "Y",
                "PSOE": "Y",
                "Junts": "N",
                "PP": "N",
                "VOX": "N",
            },
    },
    8: {
        "name": "Que las empresas más grandes paguen almenos un 15% de impuestos",
        "desc": "Que multinacionales y grandes empresas no se escaqueen y paguen un 15% como mínimo (acorde con Europa).",
        "ámbitos": ["Impuestos"],
        "propone": ["Gobierno"],
        "ref": "121/000023",
        "tipo": "PL",
        "fecha": "06/06/2024",
        "urls": {"congreso": "https://www.congreso.es/es/busqueda-de-iniciativas?p_p_id=iniciativas&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_iniciativas_mode=mostrarDetalle&_iniciativas_legislatura=XV&_iniciativas_id=121%2F000023"},
        "result": "Y",
        "YAN": [178, 0, 171],
        "votos": {
                "Podemos": "Y",
                "Sumar": "Y",
                "ERC": "Y",
                "PSOE": "Y",
                "Junts": "Y",
                "PP": "N",
                "VOX": "N",
            },
    },
    9: {
        "name": "Poder repartir a los menores migrantes para acogerlos sin que se sature nada",
        "desc": "Que si en algún momento hay muchos en la misma ciudad o comunidad, se puedan repartir para aliviar la carga.",
        "ámbitos": ["Migración"],
        "propone": ["Gobierno"],
        "ref": "130/000016",
        "tipo": "RDL",
        "fecha": "21/03/2025",
        "urls": {"congreso": "https://www.congreso.es/es/busqueda-de-iniciativas?p_p_id=iniciativas&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_iniciativas_mode=mostrarDetalle&_iniciativas_legislatura=XV&_iniciativas_id=130%2F000016"},
        "YAN": [179, 1, 170],
        "votos": {
                "Podemos": "Y",
                "Sumar": "Y",
                "ERC": "Y",
                "PSOE": "Y",
                "Junts": "Y",
                "PP": "N",
                "VOX": "N",
            },
    },
    10: {
        "name": "Impedir que existan asociaciones franquistas",
        "desc": "Desmantelar las asociaciones que justifiquen o ensalcen la dictadura y/o que humillen a sus víctimas.",
        "ámbitos": ["Memoria"],
        "propone": ["PSOE"],
        "ref": "122/000126",
        "tipo": "PL",
        "fecha": "06/09/2024",
        "urls": {"congreso": "", "ECM": "", "QHLD": ""},
        "YAN": [178, 137, 33],
        "votos": {
                "Podemos": "Y",
                "Sumar": "Y",
                "ERC": "Y",
                "PSOE": "Y",
                "Junts": "Y",
                "PP": "A",
                "VOX": "N",
            },
    },
    11: {
        "name": "Verano Joven 2025",
        "desc": "Descuentos y otras medidas para promover el transporte público entre los jóvenes durante el verano.",
        "ámbitos": ["Transporte"],
        "propone": ["Gobierno"],
        "ref": "130/000019",
        "tipo": "RDL",
        "fecha": "16/06/2025",
        "urls": {"congreso": "", "ECM": "", "QHLD": ""},
        "YAN": [177, 136, 33],
        "votos": {
                "Podemos": "Y",
                "Sumar": "Y",
                "ERC": "Y",
                "PSOE": "Y",
                "Junts": "Y",
                "PP": "A",
                "VOX": "N",
            },
    },
    12: {
        "name": "Limitar el margen de beneficio de las distribuidoras de alimentos",
        "desc": "Que haya un máximo en el beneficio que pueden sacar vendiendo productos (almenos los básicos o esenciales).",
        "ámbitos": ["Alimentación"],
        "propone": ["Podemos"],
        "ref": "173/000187 p4",
        "tipo": "M",
        "fecha": "10/09/2026",
        "urls": {"congreso": "", "ECM": "", "QHLD": ""},
        "YAN": [19, 24, 304],
        "votos": {
                "Podemos": "Y",
                "Sumar": "A",
                "ERC": "Y",
                "PSOE": "N",
                "Junts": "N",
                "PP": "N",
                "VOX": "N",
            },
    },
    13: {
        "name": "Bajar los alquileres un 40% por ley",
        "desc": "Reducirlos un 40% respecto al precio que tienen actualmente para combatir el encarecimiento del precio de la vida.",
        "ámbitos": ["Vivienda"],
        "propone": ["Podemos"],
        "ref": "173/000187 p1",
        "tipo": "M",
        "fecha": "10/09/2026",
        "urls": {"congreso": "https://www.congreso.es/es/mociones-consecuencia-de-interpelacion-urgente?p_p_id=iniciativas&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_iniciativas_mode=mostrarDetalle&_iniciativas_legislatura=XV&_iniciativas_id=173/000187",
                 "ECM": "", "QHLD": "", "BOE": "https://www.congreso.es/public_oficiales/L15/CONG/BOCG/D/BOCG-15-D-590.PDF#page=31"},
        "YAN": [19, 144, 183],
        "votos": {
                "Podemos": "Y",
                "Sumar": "A",
                "ERC": "Y",
                "PSOE": "A",
                "Junts": "N",
                "PP": "N",
                "VOX": "N",
            },
    },
    14: {
        "name": "Obligar a los grandes propietarios a poner sus viviendas en alquiler social",
        "desc": "Expropiarles el uso de 650.000 viviendas (que sigan siendo suyas pero las tengan que usar para alquiler social).",
        "ámbitos": ["Vivienda"],
        "propone": ["Podemos"],
        "ref": "173/000187 p3",
        "tipo": "M",
        "fecha": "10/09/2026",
        "urls": {"congreso": "https://www.congreso.es/es/mociones-consecuencia-de-interpelacion-urgente?p_p_id=iniciativas&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_iniciativas_mode=mostrarDetalle&_iniciativas_legislatura=XV&_iniciativas_id=173/000187",
                 "ECM": "", "QHLD": "", "BOE": "https://www.congreso.es/public_oficiales/L15/CONG/BOCG/D/BOCG-15-D-590.PDF#page=31"},
        "YAN": [19, 144, 183],
        "votos": {
                "Podemos": "Y",
                "Sumar": "A",
                "ERC": "Y",
                "PSOE": "A",
                "Junts": "N",
                "PP": "N",
                "VOX": "N",
            },
    },
    15: {
        "name": "Coger el dinero que estaba planeado para el rearme militar y gastarlo en educación",
        "desc": "Que los 10.500 Millones previstos para la primera fase del rearme se usen para servicios públicos y políticas sociales.",
        "ámbitos": ["Educación"],
        "propone": ["Podemos"],
        "ref": "173/000103",
        "tipo": "M",
        "fecha": "29/05/2025",
        "urls": {"congreso": "https://www.congreso.es/es/busqueda-de-iniciativas?p_p_id=iniciativas&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_iniciativas_mode=mostrarDetalle&_iniciativas_legislatura=XV&_iniciativas_id=173/000103",
                 "ECM": "", "QHLD": ""},
        "YAN": [45, 7, 296],
        "votos": {
                "Podemos": "Y",
                "Sumar": "Y",
                "ERC": "Y",
                "PSOE": "N",
                "Junts": "A",
                "PP": "N",
                "VOX": "N",
            },
    },
    16: {
        "name": "Hacer públicos los documentos sobre el intento de golpe de estado del 23F",
        "desc": "Porque en un audio filtrado el rey Juan Carlos da a entender que él y un condenado saben más cosas de las que dijeron.",
        "ámbitos": [""],
        "propone": ["Podemos"],
        "ref": "173/000060",
        "tipo": "M",
        "fecha": "14/11/2024",
        "urls": {"congreso": "https://www.congreso.es/es/busqueda-de-iniciativas?p_p_id=iniciativas&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_iniciativas_mode=mostrarDetalle&_iniciativas_legislatura=XV&_iniciativas_id=173/000060",
                 "ECM": "", "QHLD": ""},
        "YAN": [57, 1, 291],
        "votos": {
                "Podemos": "Y",
                "Sumar": "Y",
                "ERC": "Y",
                "PSOE": "N",
                "Junts": "Y",
                "PP": "N",
                "VOX": "N",
            },
    },
    17: {
        "name": "Que los autónomos que cobran menos del salario mínimo paguen menos cuota",
        "desc": "Bajar la cuota de autónomo para los trabajadores autónomos que tienen ingresos por debajo del SMI.",
        "ámbitos": ["Trabajo"],
        "propone": ["ERC"],
        "ref": "173/000147 p3",
        "tipo": "M",
        "fecha": "12/12/2025",
        "urls": {"congreso": "https://www.congreso.es/es/busqueda-de-iniciativas?p_p_id=iniciativas&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_iniciativas_mode=mostrarDetalle&_iniciativas_legislatura=XV&_iniciativas_id=173/000147",
                 "ECM": "", "QHLD": ""},
        "YAN": [57, 136, 153],
        "votos": {
                "Podemos": "Y",
                "Sumar": "Y",
                "ERC": "Y",
                "PSOE": "N",
                "Junts": "Y",
                "PP": "A",
                "VOX": "N",
            },
    },
    18: {
        "name": "Perseguir más a las empresas que usan falsos autónomos",
        "desc": "Sancionar a las empresas que tienen trabajadores cotizando como si en realidad fueran autónomos.",
        "ámbitos": ["Trabajo"],
        "propone": ["ERC"],
        "ref": "173/000147 p9",
        "tipo": "M",
        "fecha": "12/12/2025",
        "urls": {"congreso": "https://www.congreso.es/es/busqueda-de-iniciativas?p_p_id=iniciativas&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_iniciativas_mode=mostrarDetalle&_iniciativas_legislatura=XV&_iniciativas_id=173/000147",
                 "ECM": "", "QHLD": ""},
        "YAN": [178, 166, 0],
        "votos": {
                "Podemos": "Y",
                "Sumar": "Y",
                "ERC": "Y",
                "PSOE": "Y",
                "Junts": "Y",
                "PP": "A",
                "VOX": "A",
            },
    },
    19: {
        "name": "Que los trabajadores pobres paguen menos y las empresas ricas paguen más",
        "desc": "Bajar el IRPF para trabajadores que cobren menos de 25.000€ y subir el IS para empresas que ganan más de 4M€.",
        "ámbitos": ["Impuestos"],
        "propone": ["ERC"],
        "ref": "173/000147 p12",
        "tipo": "M",
        "fecha": "12/12/2025",
        "urls": {"congreso": "https://www.congreso.es/es/busqueda-de-iniciativas?p_p_id=iniciativas&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_iniciativas_mode=mostrarDetalle&_iniciativas_legislatura=XV&_iniciativas_id=173/000147",
                 "ECM": "", "QHLD": ""},
        "YAN": [44, 13, 289],
        "votos": {
                "Podemos": "Y",
                "Sumar": "Y",
                "ERC": "Y",
                "PSOE": "N",
                "Junts": "A",
                "PP": "N",
                "VOX": "N",
            },
    },
}

voto_congreso_sample = {
    # desde aquí
    1: {
        "name": "",
        "desc": "",
        "ámbitos": [""],
        "propone": [""],
        "ref": "",
        "tipo": "",
        "fecha": "",
        "urls": {"congreso": "", "ECM": "", "QHLD": ""},
        "YAN": [0, 0, 0],
        "votos": {
                "Podemos": "",
                "Sumar": "",
                "ERC": "",
                "PSOE": "",
                "Junts": "",
                "PP": "",
                "VOX": "",
            },
    },
    # hasta aquí
}
