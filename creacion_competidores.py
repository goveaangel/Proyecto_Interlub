import pandas as pd

# === Datos técnicos resumidos de 5 fichas de producto ===
productos = [
    {
        "nombre_producto": "ANDEROL FGCS-2",
        "marca": "ANDEROL",
        "tipo_grasa": "Calcio sulfonato complejo",
        "grado_NLGI": 2,
        "tipo_aceite_base": "White Oil",
        "temp_min_C": -20,
        "temp_max_C": 160,
        "temp_pico_C": 200,
        "punto_goteo_C": 318,
        "viscosidad_40C_mm2s": 95,
        "carga_4ball_N": 4000,
        "lavado_agua_80C_%": 0.3,
        "vida_rodamientos_h": 180,
        "registro_H1": "Sí",
        "aplicaciones": "Industria alimentaria, embotellado, farmacéutica",
        "ventajas": "Alta estabilidad mecánica, resistencia al agua, larga vida útil"
    },
    {
        "nombre_producto": "ELKALUB GLS 163",
        "marca": "ELKALUB",
        "tipo_grasa": "Tixotrópica sintética con PTFE",
        "grado_NLGI": 2,
        "tipo_aceite_base": "Aceite mineral parcialmente sintético",
        "temp_min_C": -20,
        "temp_max_C": 180,
        "punto_goteo_C": 250,
        "viscosidad_40C_mm2s": 100,
        "carga_4ball_N": 2000,
        "lavado_agua_80C_%": 1.0,
        "vida_rodamientos_h": None,
        "registro_H1": "No",
        "aplicaciones": "Rodamientos lentos o rápidos con sellado insuficiente, asientos de pinzas, husillos",
        "ventajas": "Grasa de alta pureza y comportamiento tixotrópico, estable a altas presiones"
    },
    {
        "nombre_producto": "COGELSA ULTRAPLEX MCS 2",
        "marca": "COGELSA",
        "tipo_grasa": "Sulfonato de calcio reforzada",
        "grado_NLGI": 2,
        "tipo_aceite_base": "Aceite base de alta viscosidad",
        "temp_min_C": -20,
        "temp_max_C": 180,
        "punto_goteo_C": 300,
        "viscosidad_40C_mm2s": 460,
        "carga_4ball_N": 620,
        "lavado_agua_80C_%": 11,
        "vida_rodamientos_h": None,
        "registro_H1": "Opcional",
        "aplicaciones": "Engranajes abiertos, reductores, acoplamientos, minería, siderurgia, alimentaria",
        "ventajas": "Excelente capacidad de carga, anticorrosiva y alta estabilidad bajo condiciones severas"
    },
    {
        "nombre_producto": "CHEVRON Starplex EP2",
        "marca": "CHEVRON",
        "tipo_grasa": "Complejo de litio con disulfuro de molibdeno",
        "grado_NLGI": 2,
        "tipo_aceite_base": "Aceite mineral refinado",
        "temp_min_C": -40,
        "temp_max_C": 177,
        "punto_goteo_C": 255,
        "viscosidad_40C_mm2s": 220,
        "carga_4ball_N": 400,
        "lavado_agua_80C_%": 20,
        "vida_rodamientos_h": None,
        "registro_H1": "No",
        "aplicaciones": "Rodamientos automotrices, camiones pesados, maquinaria agrícola y de construcción",
        "ventajas": "Alta estabilidad térmica, excelente protección contra corrosión y desgaste"
    },
    {
        "nombre_producto": "CHEVRON Delo Grease EP 1",
        "marca": "CHEVRON",
        "tipo_grasa": "Complejo de litio",
        "grado_NLGI": 1,
        "tipo_aceite_base": "Aceite mineral refinado",
        "temp_min_C": -40,
        "temp_max_C": 177,
        "punto_goteo_C": 245,
        "viscosidad_40C_mm2s": 226,
        "carga_4ball_N": 315,
        "lavado_agua_80C_%": 10,
        "vida_rodamientos_h": None,
        "registro_H1": "No",
        "aplicaciones": "Vehículos de carretera, autobuses, maquinaria ligera, cojinetes de alta temperatura",
        "ventajas": "Alta resistencia al lavado por agua, buena bombeabilidad a baja temperatura, textura pegajosa"
    }
]

# === Crear DataFrame y exportar ===
df = pd.DataFrame(productos)
df.to_csv("competidores.csv", index=False, encoding="utf-8-sig")

print("Archivo 'competidores.csv' creado exitosamente con 5 productos.")
