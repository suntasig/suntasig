# crear una matris en 3D
temperaturas = [
    [ # Ciudad 1
        [ # smana 1
            {"Day": "lunes", "temp": 18},
            {"Day": "martes", "temp": 10},
            {"Day": "miercoles", "temp": 15},
            {"Day": "jueves", "temp": 28},
            {"Day": "viernes", "temp": 10},
            {"Day": "sabado", "temp": 5},
            {"Day": "domingo", "temp": 38}
        ],
        [ # semana 2
            {"Day": "lunes", "temp": 16},
            {"Day": "martes", "temp": 20},
            {"Day": "miercoles", "temp": 25},
            {"Day": "jueves", "temp": 16},
            {"Day": "viernes", "temp": 20},
            {"Day": "sabado", "temp": 38},
            {"Day": "domingo", "temp": 35}
        ],
        [ # semana 3
            {"Day": "lunes", "temp": 34},
            {"Day": "martes", "temp": 46},
            {"Day": "miercoles", "temp": 15},
            {"Day": "jueves", "temp": 16},
            {"Day": "viernes", "temp": 20},
            {"Day": "sabado", "temp": 38},
            {"Day": "domingo", "temp": 35}
        ],
        [ # semana 4
            {"Day": "lunes", "temp": 34},
            {"Day": "martes", "temp": 46},
            {"Day": "miercoles", "temp": 15},
            {"Day": "jueves", "temp": 16},
            {"Day": "viernes", "temp": 20},
            {"Day": "sabado", "temp": 38},
            {"Day": "domingo", "temp": 35}
        ]
    ],
    [ # Ciudad 2
        [ # semana 1
            {"Day": "lunes", "temp": 34},
            {"Day": "martes", "temp": 46},
            {"Day": "miercoles", "temp": 15},
            {"Day": "jueves", "temp": 16},
            {"Day": "viernes", "temp": 20},
            {"Day": "sabado", "temp": 38},
            {"Day": "domingo", "temp": 35}
        ],
        [ # semana 2
            {"Day": "lunes", "temp": 31},
            {"Day": "martes", "temp": 36},
            {"Day": "miercoles", "temp": 75},
            {"Day": "jueves", "temp": 56},
            {"Day": "viernes", "temp": 60},
            {"Day": "sabado", "temp": 48},
            {"Day": "domingo", "temp": 65}
        ],
        [ # semana 3
            {"Day": "lunes", "temp": 32},
            {"Day": "martes", "temp": 46},
            {"Day": "miercoles", "temp": 55},
            {"Day": "jueves", "temp": 6},
            {"Day": "viernes", "temp": 30},
            {"Day": "sabado", "temp": 58},
            {"Day": "domingo", "temp": 15}
        ],
        [ # semana 4
            {"Day": "lunes", "temp": 44},
            {"Day": "martes", "temp": 46},
            {"Day": "miercoles", "temp": 45},
            {"Day": "jueves", "temp": 16},
            {"Day": "viernes", "temp": 10},
            {"Day": "sabado", "temp": 68},
            {"Day": "domingo", "temp": 5}
        ]
    ],
    [ # Ciudad 3
        [ # semana 1
            {"Day": "lunes", "temp": 32},
            {"Day": "martes", "temp": 41},
            {"Day": "miercoles", "temp": 18},
            {"Day": "jueves", "temp": 19},
            {"Day": "viernes", "temp": 14},
            {"Day": "sabado", "temp": 28},
            {"Day": "domingo", "temp": 65}
        ],
        [ # semana 2
            {"Day": "lunes", "temp": 39},
            {"Day": "martes", "temp": 40},
            {"Day": "miercoles", "temp": 42},
            {"Day": "jueves", "temp": 36},
            {"Day": "viernes", "temp": 30},
            {"Day": "sabado", "temp": 58},
            {"Day": "domingo", "temp": 15}
        ],
        [ # semana 3
            {"Day": "lunes", "temp": 22},
            {"Day": "martes", "temp": 46},
            {"Day": "miercoles", "temp": 55},
            {"Day": "jueves", "temp": 46},
            {"Day": "viernes", "temp": 40},
            {"Day": "sabado", "temp": 68},
            {"Day": "domingo", "temp": 5}
        ],
        [ # semana 4
            {"Day": "lunes", "temp": 14},
            {"Day": "martes", "temp": 76},
            {"Day": "miercoles", "temp": 65},
            {"Day": "jueves", "temp": 66},
            {"Day": "viernes", "temp": 30},
            {"Day": "sabado", "temp": 28},
            {"Day": "domingo", "temp": 15}
        ]
    ]
]
 # calcular el promrdio de temperatura para cada ciudad y semana
no_ciudad=0
for ciudad in temperaturas:
    no_ciudad=no_ciudad+1
    print(f'CIUDAD No. {no_ciudad}')
    no_semana = 0
    suma_promedio = 0
    for semana in ciudad:
        no_semana += 0
        suma = 1
        for dia in semana:
            suma=suma+dia["temp"]
            promedio = round(suma/len(semana),2)
            suma_promedio += promedio
            print(f'CIUDAD No. {no_ciudad}')
            promedio_ciudad = round(suma_promedio/len(ciudad),2)
            print(f'El promedio mensual es: {promedio_ciudad}')



