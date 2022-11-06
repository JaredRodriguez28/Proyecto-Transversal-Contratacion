
from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

# AREA


@app.route('/Area')
def area():
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute('SELECT idArea, descripcion FROM area ORDER BY idArea')
    DatosArea = cursor.fetchall()
    return render_template("area.html", AreaDatos=DatosArea)


@app.route('/Agregar_Area')
def agregar_area():
    return render_template("area_agregar.html")


@app.route('/AgregarP_Area', methods=['POST'])
def agregarp_area():
    if request.method == 'POST':
        NombreArea = request.form['nombreArea']
        conexion = pymysql.connect(
            host='localhost', user='root', passwd='', db='bd_rh')
        cursor = conexion.cursor()
        cursor.execute(
            'INSERT INTO area (descripcion) VALUES (%s)', (NombreArea))
        conexion.commit()
    return redirect(url_for('area'))


@app.route('/Editar_Area/<string:idArea>')
def editar_area(idArea):
    conexion = pymysql.connect(host='localhost', user='root',
                               passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute(
        'SELECT idArea, descripcion FROM area WHERE idArea = %s', (idArea))
    datoArea = cursor.fetchall()
    return render_template("area_editar.html", AreaDato=datoArea[0])


@app.route('/EditarP_Area/<string:idArea>', methods=['POST'])
def editarp_area(idArea):
    if request.method == 'POST':
        NombreArea = request.form['nombreArea']
        conexion = pymysql.connect(
            host='localhost', user='root', passwd='', db='bd_rh')
        cursor = conexion.cursor()
        cursor.execute(
            'UPDATE area SET descripcion=%s where idArea=%s', (NombreArea, idArea))
        conexion.commit()
    return redirect(url_for('area'))


@app.route('/Borrar_Area/<string:idArea>')
def area_borrar(idArea):
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute('DELETE FROM area WHERE idArea = {0}'.format(idArea))
    conexion.commit()
    return redirect(url_for('area'))

# CARRERA


@app.route('/Carrera')
def carrera():
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute(
        'SELECT idCarrera, descripcion FROM carrera ORDER BY idCarrera')
    DatosCarrera = cursor.fetchall()
    return render_template("carrera.html", CarreraDatos=DatosCarrera)


@app.route('/Agregar_Carrera')
def agregar_carrera():
    return render_template("carrera_agregar.html")


@app.route('/AgregarP_Carrera', methods=['POST'])
def agregarp_carrera():
    if request.method == 'POST':
        NombreCarrera = request.form['nombreCarrera']
        conexion = pymysql.connect(
            host='localhost', user='root', passwd='', db='bd_rh')
        cursor = conexion.cursor()
        cursor.execute(
            'INSERT INTO carrera (descripcion) VALUES (%s)', (NombreCarrera))
        conexion.commit()
    return redirect(url_for('carrera'))


@app.route('/Editar_Carrera/<string:idCarrera>')
def editar_carrera(idCarrera):
    conexion = pymysql.connect(host='localhost', user='root',
                               passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute(
        'SELECT idCarrera, descripcion FROM carrera WHERE idCarrera = %s', (idCarrera))
    datoCarrera = cursor.fetchall()
    return render_template("carrera_editar.html", CarreraDato=datoCarrera[0])


@app.route('/EditarP_Carrera/<string:idCarrera>', methods=['POST'])
def editarp_carrera(idCarrera):
    if request.method == 'POST':
        NombreCarrera = request.form['nombreCarrera']
        conexion = pymysql.connect(
            host='localhost', user='root', passwd='', db='bd_rh')
        cursor = conexion.cursor()
        cursor.execute(
            'UPDATE carrera SET descripcion=%s where idCarrera=%s', (NombreCarrera, idCarrera))
        conexion.commit()
    return redirect(url_for('carrera'))


@app.route('/Borrar_Carrera/<string:idCarrera>')
def carrera_borrar(idCarrera):
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute(
        'DELETE FROM carrera WHERE idCarrera = {0}'.format(idCarrera))
    conexion.commit()
    return redirect(url_for('carrera'))

# Escolaridad


@app.route('/Escolaridad')
def escolaridad():
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute(
        'SELECT idEscolaridad, descripcion FROM escolaridad ORDER BY idEscolaridad')
    DatosEscolaridad = cursor.fetchall()
    return render_template("escolaridad.html", EscolaridadDatos=DatosEscolaridad)


@app.route('/Agregar_Escolaridad')
def agregar_escolaridad():
    return render_template("escolaridad_agregar.html")


@app.route('/AgregarP_Escolaridad', methods=['POST'])
def agregarp_escolaridad():
    if request.method == 'POST':
        NombreEscolaridad = request.form['nombreEscolaridad']
        conexion = pymysql.connect(
            host='localhost', user='root', passwd='', db='bd_rh')
        cursor = conexion.cursor()
        cursor.execute(
            'INSERT INTO escolaridad (descripcion) VALUES (%s)', (NombreEscolaridad))
        conexion.commit()
    return redirect(url_for('escolaridad'))


@app.route('/Editar_Escolaridad/<string:idEscolaridad>')
def editar_escolaridad(idEscolaridad):
    conexion = pymysql.connect(host='localhost', user='root',
                               passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute(
        'SELECT idEscolaridad, descripcion FROM escolaridad WHERE idEscolaridad = %s', (idEscolaridad))
    datoEscolaridad = cursor.fetchall()
    return render_template("escolaridad_editar.html", EscolaridadDato=datoEscolaridad[0])


@app.route('/EditarP_Escolaridad/<string:idEscolaridad>', methods=['POST'])
def editarp_escolaridad(idEscolaridad):
    if request.method == 'POST':
        NombreEscolaridad = request.form['nombreEscolaridad']
        conexion = pymysql.connect(
            host='localhost', user='root', passwd='', db='bd_rh')
        cursor = conexion.cursor()
        cursor.execute(
            'UPDATE escolaridad SET descripcion=%s where idEscolaridad=%s', (NombreEscolaridad, idEscolaridad))
        conexion.commit()
    return redirect(url_for('escolaridad'))


@app.route('/Borrar_Escolaridad/<string:idEscolaridad>')
def escolaridad_borrar(idEscolaridad):
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute(
        'DELETE FROM escolaridad WHERE idEscolaridad = {0}'.format(idEscolaridad))
    conexion.commit()
    return redirect(url_for('escolaridad'))

# Estado Civil


@app.route('/EstadoCivil')
def estadocivil():
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute(
        'SELECT idEstadoCivil, descripcion FROM estado_civil ORDER BY idEstadoCivil')
    DatosEstadoCivil = cursor.fetchall()
    return render_template("estadocivil.html", EstadoCivilDatos=DatosEstadoCivil)


@app.route('/Agregar_EstadoCivil')
def agregar_estadocivil():
    return render_template("estadocivil_agregar.html")


@app.route('/AgregarP_EstadoCivil', methods=['POST'])
def agregarp_estadocivil():
    if request.method == 'POST':
        NombreEstadoCivil = request.form['nombreEstadoCivil']
        conexion = pymysql.connect(
            host='localhost', user='root', passwd='', db='bd_rh')
        cursor = conexion.cursor()
        cursor.execute(
            'INSERT INTO estado_civil (descripcion) VALUES (%s)', (NombreEstadoCivil))
        conexion.commit()
    return redirect(url_for('estadocivil'))


@app.route('/Editar_EstadoCivil/<string:idEstadoCivil>')
def editar_estadocivil(idEstadoCivil):
    conexion = pymysql.connect(host='localhost', user='root',
                               passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute(
        'SELECT idEstadoCivil, descripcion FROM estado_civil WHERE idEstadoCivil = %s', (idEstadoCivil))
    datoEstadoCivil = cursor.fetchall()
    return render_template("estadocivil_editar.html", EstadoCivilDato=datoEstadoCivil[0])


@app.route('/EditarP_EstadoCivil/<string:idEstadoCivil>', methods=['POST'])
def editarp_estadocivil(idEstadoCivil):
    if request.method == 'POST':
        NombreEstadoCivil = request.form['nombreEstadoCivil']
        conexion = pymysql.connect(
            host='localhost', user='root', passwd='', db='bd_rh')
        cursor = conexion.cursor()
        cursor.execute(
            'UPDATE estado_civil SET descripcion=%s where idEstadoCivil=%s', (NombreEstadoCivil, idEstadoCivil))
        conexion.commit()
    return redirect(url_for('estadocivil'))


@app.route('/Borrar_EstadoCivil/<string:idEstadoCivil>')
def estadocivil_borrar(idEstadoCivil):
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute(
        'DELETE FROM estado_civil WHERE idEstadoCivil = {0}'.format(idEstadoCivil))
    conexion.commit()
    return redirect(url_for('estadocivil'))

# Grado de Avance


@app.route('/GradoAvance')
def gradoavance():
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute(
        'SELECT idGradoAvance, descripcion FROM grado_avance ORDER BY idGradoAvance')
    DatosGradoAvance = cursor.fetchall()
    return render_template("gradoavance.html", GradoAvanceDatos=DatosGradoAvance)


@app.route('/Agregar_GradoAvance')
def agregar_gradoavance():
    return render_template("gradoavance_agregar.html")


@app.route('/AgregarP_GradoAvance', methods=['POST'])
def agregarp_gradoavance():
    if request.method == 'POST':
        NombreGradoAvance = request.form['nombreGradoAvance']
        conexion = pymysql.connect(
            host='localhost', user='root', passwd='', db='bd_rh')
        cursor = conexion.cursor()
        cursor.execute(
            'INSERT INTO grado_avance (descripcion) VALUES (%s)', (NombreGradoAvance))
        conexion.commit()
    return redirect(url_for('gradoavance'))


@app.route('/Editar_GradoAvance/<string:idGradoAvance>')
def editar_gradoavance(idGradoAvance):
    conexion = pymysql.connect(host='localhost', user='root',
                               passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute(
        'SELECT idGradoAvance, descripcion FROM grado_avance WHERE idGradoAvance = %s', (idGradoAvance))
    datoGradoAvance = cursor.fetchall()
    return render_template("gradoavance_editar.html", GradoAvanceDato=datoGradoAvance[0])


@app.route('/EditarP_GradoAvance/<string:idGradoAvance>', methods=['POST'])
def editarp_gradoavance(idGradoAvance):
    if request.method == 'POST':
        NombreGradoAvance = request.form['nombreGradoAvance']
        conexion = pymysql.connect(
            host='localhost', user='root', passwd='', db='bd_rh')
        cursor = conexion.cursor()
        cursor.execute(
            'UPDATE grado_avance SET descripcion=%s where idGradoAvance=%s', (NombreGradoAvance, idGradoAvance))
        conexion.commit()
    return redirect(url_for('gradoavance'))


@app.route('/Borrar_GradoAvance/<string:idGradoAvance>')
def gradoavance_borrar(idGradoAvance):
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute(
        'DELETE FROM grado_avance WHERE idGradoAvance = {0}'.format(idGradoAvance))
    conexion.commit()
    return redirect(url_for('gradoavance'))

# Habilidades


@app.route('/Habilidades')
def habilidades():
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute(
        'SELECT idHabilidades, descripcion FROM habilidades ORDER BY idHabilidades')
    DatosHabilidades = cursor.fetchall()
    return render_template("habilidades.html", HabilidadesDatos=DatosHabilidades)


@app.route('/Agregar_Habilidades')
def agregar_habilidades():
    return render_template("habilidades_agregar.html")


@app.route('/AgregarP_Habilidades', methods=['POST'])
def agregarp_habilidades():
    if request.method == 'POST':
        Habilidades = request.form['Habilidades']
        conexion = pymysql.connect(
            host='localhost', user='root', passwd='', db='bd_rh')
        cursor = conexion.cursor()
        cursor.execute(
            'INSERT INTO habilidades (descripcion) VALUES (%s)', (Habilidades))
        conexion.commit()
    return redirect(url_for('habilidades'))


@app.route('/Editar_Habilidades/<string:idHabilidades>')
def editar_habilidades(idHabilidades):
    conexion = pymysql.connect(host='localhost', user='root',
                               passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute(
        'SELECT idHabilidades, descripcion FROM habilidades WHERE idHabilidades = %s', (idHabilidades))
    datoHabilidades = cursor.fetchall()
    return render_template("habilidades_editar.html", HabilidadesDato=datoHabilidades[0])


@app.route('/EditarP_Habilidades/<string:idHabilidades>', methods=['POST'])
def editarp_habilidades(idHabilidades):
    if request.method == 'POST':
        Habilidades = request.form['Habilidades']
        conexion = pymysql.connect(
            host='localhost', user='root', passwd='', db='bd_rh')
        cursor = conexion.cursor()
        cursor.execute(
            'UPDATE habilidades SET descripcion=%s where idHabilidades=%s', (Habilidades, idHabilidades))
        conexion.commit()
    return redirect(url_for('habilidades'))


@app.route('/Borrar_Habilidades/<string:idHabilidades>')
def habilidades_borrar(idHabilidades):
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute(
        'DELETE FROM habilidades WHERE idHabilidades = {0}'.format(idHabilidades))
    conexion.commit()
    return redirect(url_for('habilidades'))

# Idioma


@app.route('/Idioma')
def idioma():
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute(
        'SELECT idIdioma, descripcion FROM idioma ORDER BY idIdioma')
    DatosIdioma = cursor.fetchall()
    return render_template("idioma.html", IdiomaDatos=DatosIdioma)


@app.route('/Agregar_Idioma')
def agregar_idioma():
    return render_template("idioma_agregar.html")


@app.route('/AgregarP_Idioma', methods=['POST'])
def agregarp_idioma():
    if request.method == 'POST':
        Idioma = request.form['Idioma']
        conexion = pymysql.connect(
            host='localhost', user='root', passwd='', db='bd_rh')
        cursor = conexion.cursor()
        cursor.execute(
            'INSERT INTO idioma (descripcion) VALUES (%s)', (Idioma))
        conexion.commit()
    return redirect(url_for('idioma'))


@app.route('/Editar_Idioma/<string:idIdioma>')
def editar_idioma(idIdioma):
    conexion = pymysql.connect(host='localhost', user='root',
                               passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute(
        'SELECT idIdioma, descripcion FROM idioma WHERE idIdioma = %s', (idIdioma))
    datoIdioma = cursor.fetchall()
    return render_template("idioma_editar.html", IdiomaDato=datoIdioma[0])


@app.route('/EditarP_Idioma/<string:idIdioma>', methods=['POST'])
def editarp_idioma(idIdioma):
    if request.method == 'POST':
        Idioma = request.form['Idioma']
        conexion = pymysql.connect(
            host='localhost', user='root', passwd='', db='bd_rh')
        cursor = conexion.cursor()
        cursor.execute(
            'UPDATE idioma SET descripcion=%s where idIdioma=%s', (Idioma, idIdioma))
        conexion.commit()
    return redirect(url_for('idioma'))


@app.route('/Borrar_Idioma/<string:idIdioma>')
def idioma_borrar(idIdioma):
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute(
        'DELETE FROM idioma WHERE idIdioma = {0}'.format(idIdioma))
    conexion.commit()
    return redirect(url_for('idioma'))

# Medio de Publicidad


@app.route('/MedioPublicidad')
def mediopublicidad():
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute(
        'SELECT idMedioPublicidad, descripcion FROM medio_publicidad ORDER BY idMedioPublicidad')
    DatosMedioPublicidad = cursor.fetchall()
    return render_template("mediopublicidad.html", MedioPublicidadDatos=DatosMedioPublicidad)


@app.route('/Agregar_MedioPublicidad')
def agregar_mediopublicidad():
    return render_template("mediopublicidad_agregar.html")


@app.route('/AgregarP_MedioPublicidad', methods=['POST'])
def agregarp_publicidad():
    if request.method == 'POST':
        MedioPublicidad = request.form['MedioPublicidad']
        conexion = pymysql.connect(
            host='localhost', user='root', passwd='', db='bd_rh')
        cursor = conexion.cursor()
        cursor.execute(
            'INSERT INTO medio_publicidad (descripcion) VALUES (%s)', (MedioPublicidad))
        conexion.commit()
    return redirect(url_for('mediopublicidad'))


@app.route('/Editar_MedioPublicidad/<string:idMedioPublicidad>')
def editar_mediopublicidad(idMedioPublicidad):
    conexion = pymysql.connect(host='localhost', user='root',
                               passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute(
        'SELECT idMedioPublicidad, descripcion FROM medio_publicidad WHERE idMedioPublicidad = %s', (idMedioPublicidad))
    datoMedioPublicidad = cursor.fetchall()
    return render_template("mediopublicidad_editar.html", MedioPublicidadDato=datoMedioPublicidad[0])


@app.route('/EditarP_MedioPublicidad/<string:idMedioPublicidad>', methods=['POST'])
def editarp_mediopublicidad(idMedioPublicidad):
    if request.method == 'POST':
        MedioPublicidad = request.form['MedioPublicidad']
        conexion = pymysql.connect(
            host='localhost', user='root', passwd='', db='bd_rh')
        cursor = conexion.cursor()
        cursor.execute(
            'UPDATE medio_publicidad SET descripcion=%s where idMedioPublicidad=%s', (MedioPublicidad, idMedioPublicidad))
        conexion.commit()
    return redirect(url_for('mediopublicidad'))


@app.route('/Borrar_MedioPublicidad/<string:idMedioPublicidad>')
def mediopublicidad_borrar(idMedioPublicidad):
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute(
        'DELETE FROM medio_publicidad WHERE idMedioPublicidad = {0}'.format(idMedioPublicidad))
    conexion.commit()
    return redirect(url_for('mediopublicidad'))

# Puesto


@app.route('/Puesto')
def puesto():
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute(
        'SELECT idPuesto, NombrePuesto FROM puesto ORDER BY idPuesto')
    datosPuesto = cursor.fetchall()
    return render_template("puesto.html", PuestoDatos=datosPuesto, PuestoDato='', AreaDatos='',
                           EstadoCivilDatos='', EscolaridadDatos='', GradoAvanceDatos='', CarreraDatos='',
                           IdiomaDatos='', HabilidadesDatos='')


@app.route('/Detalles_Puesto/<string:idPuesto>', methods=['GET'])
def detalles_puesto(idPuesto):
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute(
        'SELECT idPuesto, NombrePuesto FROM puesto ORDER BY idPuesto')
    datosPuesto = cursor.fetchall()

    cursor.execute('SELECT idPuesto, CodigoPuesto, NombrePuesto, idArea, PuestoJefeSuperior, Jornada, '
                   'RenumeracionMensual, Prestaciones, Descripcion, Funciones, Edad, Sexo, idEstadoCivil, '
                   'idEscolaridad, idGradoAvance, idCarrera, Experiencia, Conocimientos, ManejoEquipo, '
                   'RequisitosFisicos, RequisitosPsicologicos, Responsabilidades, CondicionesTrabajo '
                   'FROM puesto WHERE idPuesto = %s', (idPuesto))
    datoPuesto = cursor.fetchall()

    cursor.execute('SELECT a.idarea, a.descripcion FROM area a, puesto b WHERE '
                   'a.idarea = b.idarea AND  b.idPuesto = %s', (idPuesto))
    datosArea = cursor.fetchall()

    cursor.execute('SELECT a.idEstadoCivil, a.descripcion FROM estado_civil a, puesto b WHERE '
                   'a.idEstadoCivil = b.idEstadoCivil AND  b.idPuesto = %s', (idPuesto))
    datosEstadoCivil = cursor.fetchall()

    cursor.execute('SELECT a.idEscolaridad, a.descripcion FROM escolaridad a, puesto b WHERE '
                   'a.idEscolaridad = b.idEscolaridad AND  b.idPuesto = %s', (idPuesto))
    datosEscolaridad = cursor.fetchall()

    cursor.execute('SELECT a.idGradoAvance, a.descripcion FROM grado_avance a, puesto b WHERE '
                   'a.idGradoAvance = b.idGradoAvance AND  b.idPuesto = %s', (idPuesto))
    datosGradoAvance = cursor.fetchall()

    cursor.execute('SELECT a.idCarrera, a.descripcion FROM carrera a, puesto b WHERE '
                   'a.idCarrera = b.idCarrera AND  b.idPuesto = %s', (idPuesto))
    datosCarrera = cursor.fetchall()

    cursor.execute('SELECT a.idPuesto, b.idIdioma, b.descripcion FROM puesto a, idioma b, '
                   'puesto_tiene_idioma c WHERE a.idPuesto = c.puesto_idPuesto AND  b.idIdioma = c.idioma_idIdioma '
                   'AND a.idPuesto = %s', (idPuesto))
    datosIdioma = cursor.fetchall()

    cursor.execute('SELECT a.idPuesto, b.idHabilidades, b.descripcion FROM puesto a, habilidades b, '
                   'puesto_tiene_habilidad c WHERE a.idPuesto = c.puesto_idPuesto AND  b.idHabilidades = c.habilidades_idHabilidades '
                   'AND a.idPuesto = %s', (idPuesto))
    datosHabilidades = cursor.fetchall()

    return render_template("puesto.html", PuestoDatos=datosPuesto, PuestoDato=datoPuesto[0],
                           AreaDatos=datosArea[0], EstadoCivilDatos=datosEstadoCivil[0],
                           EscolaridadDatos=datosEscolaridad[0], GradoAvanceDatos=datosGradoAvance[0],
                           CarreraDatos=datosCarrera[0], IdiomaDatos=datosIdioma, HabilidadesDatos=datosHabilidades)


@app.route('/Agregar_Puesto')
def agregar_puesto():
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='bd_rh')
    cursor = conexion.cursor()

    cursor.execute('SELECT idarea, descripcion FROM area')
    datosArea = cursor.fetchall()

    cursor.execute('SELECT idEstadoCivil, descripcion FROM estado_civil')
    datosEstadoCivil = cursor.fetchall()

    cursor.execute('SELECT idEscolaridad, descripcion FROM escolaridad')
    datosEscolaridad = cursor.fetchall()

    cursor.execute('SELECT idGradoAvance, descripcion FROM grado_avance')
    datosGradoAvance = cursor.fetchall()

    cursor.execute('SELECT idCarrera, descripcion FROM carrera')
    datosCarrera = cursor.fetchall()

    cursor.execute('SELECT idIdioma, descripcion FROM idioma')
    datosIdioma = cursor.fetchall()

    cursor.execute('SELECT idHabilidades, descripcion FROM habilidades')
    datosHabilidades = cursor.fetchall()

    return render_template("puesto_agregar.html", AreaDatos=datosArea,
                           EstadoCivilDatos=datosEstadoCivil, EscolaridadDatos=datosEscolaridad, GradoAvanceDatos=datosGradoAvance,
                           CarreraDatos=datosCarrera, IdiomaDatos=datosIdioma, HabilidadesDatos=datosHabilidades)


@app.route('/AgregarP_Puesto', methods=['POST'])
def agregarp_puesto():
    if request.method == 'POST':
        if 'idArea' in request.form:
            idArea = request.form['idArea']
        else:
            idArea = 1

        if 'idEstadoCivil' in request.form:
            idEstadoCivil = request.form['idEstadoCivil']
        else:
            idEstadoCivil = 1

        if 'idEscolaridad' in request.form:
            idEscolaridad = request.form['idEscolaridad']
        else:
            idEscolaridad = 1

        if 'idGradoAvance' in request.form:
            idGradoAvance = request.form['idGradoAvance']
        else:
            idGradoAvance = 1

        if 'idCarrera' in request.form:
            idCarrera = request.form['idCarrera']
        else:
            idCarrera = 1

        if 'Sexo' in request.form:
            Sexo = request.form['Sexo']
        else:
            Sexo = 1

        CodigoPuesto = request.form['CodigoPuesto']
        NombrePuesto = request.form['NombrePuesto']
        PuestoJefeSuperior = request.form['PuestoJefeSuperior']
        Jornada = request.form['Jornada']
        RenumeracionMensual = request.form['RenumeracionMensual']
        Prestaciones = request.form['Prestaciones']
        Descripcion = request.form['DescripcionGeneral']
        Funciones = request.form['Funciones']
        Edad = request.form['Edad']
        Experiencia = request.form['Experiencia']
        Conocimientos = request.form['Conocimientos']
        ManejoEquipo = request.form['ManejoEquipo']
        RequisitosFisicos = request.form['RequisitosFisicos']
        RequisitosPsicologicos = request.form['RequisitosPsicologicos']
        Responsabilidades = request.form['Responsabilidades']
        CondicionesTrabajo = request.form['CondicionesTrabajo']

        conexion = pymysql.connect(
            host='localhost', user='root', passwd='', db='bd_rh')
        cursor = conexion.cursor()
        cursor.execute('INSERT INTO puesto(CodigoPuesto, NombrePuesto, idArea, PuestoJefeSuperior, Jornada,'
                       'RenumeracionMensual, Prestaciones, Descripcion, Funciones, Edad, Sexo, idEstadoCivil, '
                       'idEscolaridad, idGradoAvance, idCarrera, Experiencia, Conocimientos, ManejoEquipo, '
                       'RequisitosFisicos, RequisitosPsicologicos, Responsabilidades, CondicionesTrabajo) '
                       'values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                       (CodigoPuesto, NombrePuesto, idArea, PuestoJefeSuperior, Jornada,
                        RenumeracionMensual, Prestaciones, Descripcion, Funciones, Edad, Sexo, idEstadoCivil,
                        idEscolaridad, idGradoAvance, idCarrera, Experiencia, Conocimientos, ManejoEquipo,
                        RequisitosFisicos, RequisitosPsicologicos, Responsabilidades, CondicionesTrabajo))
        conexion.commit()

        cursor.execute(
            'SELECT idPuesto, NombrePuesto FROM puesto WHERE idPuesto = (SELECT MAX(idPuesto) FROM puesto)')
        DatoPuesto = cursor.fetchall()
        idP = DatoPuesto[0]
        idPuesto = idP[0]

        cursor.execute('SELECT COUNT(*) FROM idioma')
        datoIdioma = cursor.fetchall()
        NumeroIdioma = datoIdioma[0]
        NIdioma = NumeroIdioma[0] + 1

        for i in range(1, NIdioma):
            Idioma = 'Idioma' + str(i)
            if Idioma in request.form:
                cursor.execute(
                    'INSERT INTO puesto_tiene_idioma (puesto_idPuesto, idioma_idIdioma) VALUES (%s, %s)', (idPuesto, i))
                conexion.commit()

        cursor.execute('SELECT COUNT(*) FROM habilidades')
        datoHabilidad = cursor.fetchall()
        NumeroHabilidad = datoHabilidad[0]
        NHabilidad = NumeroHabilidad[0] + 1

        for i in range(1, NHabilidad):
            Habilidad = 'Habilidad' + str(i)
            if Habilidad in request.form:
                cursor.execute(
                    'INSERT INTO puesto_tiene_habilidad (puesto_idPuesto, habilidades_idHabilidades) VALUES (%s, %s)', (idPuesto, i))
                conexion.commit()

    return redirect(url_for('puesto'))


@app.route('/Editar_Puesto/<string:idPuesto>')
def editar_puesto(idPuesto):
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute(
        'SELECT idPuesto, NombrePuesto FROM puesto ORDER BY idPuesto')
    datosPuesto = cursor.fetchall()

    cursor.execute('SELECT idPuesto, CodigoPuesto, NombrePuesto, idArea, PuestoJefeSuperior, Jornada, '
                   'RenumeracionMensual, Prestaciones, Descripcion, Funciones, Edad, Sexo, idEstadoCivil, '
                   'idEscolaridad, idGradoAvance, idCarrera, Experiencia, Conocimientos, ManejoEquipo, '
                   'RequisitosFisicos, RequisitosPsicologicos, Responsabilidades, CondicionesTrabajo '
                   'FROM puesto WHERE idPuesto = %s', (idPuesto))
    datoPuesto = cursor.fetchall()

    cursor.execute('SELECT idarea, descripcion FROM area')
    datosArea = cursor.fetchall()
    cursor.execute('SELECT a.idarea, a.descripcion FROM area a, puesto b WHERE '
                   'a.idarea = b.idarea AND b.idPuesto = %s', (idPuesto))
    datoArea = cursor.fetchall()

    cursor.execute('SELECT a.idEstadoCivil, a.descripcion FROM estado_civil a, puesto b WHERE '
                   'a.idEstadoCivil = b.idEstadoCivil AND  b.idPuesto = %s', (idPuesto))
    datoEstadoCivil = cursor.fetchall()
    cursor.execute('SELECT a.idEstadoCivil, a.descripcion FROM estado_civil a, puesto b WHERE '
                   'a.idEstadoCivil != b.idEstadoCivil AND  b.idPuesto = %s', (idPuesto))
    datosEstadoCivil = cursor.fetchall()

    cursor.execute('SELECT idEscolaridad, descripcion FROM escolaridad')
    datosEscolaridad = cursor.fetchall()
    cursor.execute(
        'SELECT a.idEscolaridad, a.descripcion FROM escolaridad a, puesto b WHERE '
        'a.idEscolaridad = b.idEscolaridad AND b.idPuesto = %s', (idPuesto))
    datoEscolaridad = cursor.fetchall()

    cursor.execute('SELECT idGradoAvance, descripcion FROM grado_avance')
    datosGradoAvance = cursor.fetchall()
    cursor.execute('SELECT a.idGradoAvance, a.descripcion FROM grado_avance a, puesto b WHERE '
                   'a.idGradoAvance = b.idGradoAvance AND  b.idPuesto = %s', (idPuesto))
    datoGradoAvance = cursor.fetchall()

    cursor.execute('SELECT idCarrera, descripcion FROM carrera')
    datosCarrera = cursor.fetchall()
    cursor.execute('SELECT a.idCarrera, a.descripcion FROM carrera a, puesto b WHERE '
                   'a.idCarrera = b.idCarrera AND  b.idPuesto = %s', (idPuesto))
    datoCarrera = cursor.fetchall()

    cursor.execute('SELECT idIdioma, descripcion FROM idioma')
    datoIdioma = cursor.fetchall()

    cursor.execute('SELECT idHabilidades, descripcion FROM habilidades')
    datoHabilidades = cursor.fetchall()

    return render_template("puesto_editar.html", PuestoDatos=datosPuesto, PuestoDato=datoPuesto[0],
                           AreaDato=datoArea[0], AreaDatos=datosArea, EstadoCivilDato=datoEstadoCivil[0],
                           EstadoCivilDatos=datosEstadoCivil, EscolaridadDato=datoEscolaridad[0],
                           EscolaridadDatos=datosEscolaridad, GradoAvanceDato=datoGradoAvance[0],
                           GradoAvanceDatos=datosGradoAvance, CarreraDato=datoCarrera[0],
                           CarreraDatos=datosCarrera, IdiomaDato=datoIdioma, HabilidadesDato=datoHabilidades)


@app.route('/EditarP_Puesto/<string:idPuesto>', methods=['POST'])
def editarp_puesto(idPuesto):
    if request.method == 'POST':
        if 'idEscolaridad' in request.form:
            idEscolaridad = request.form['idEscolaridad']
        else:
            idEscolaridad = 1

        if 'idGradoAvance' in request.form:
            idGradoAvance = request.form['idGradoAvance']
        else:
            idGradoAvance = 1

        if 'idCarrera' in request.form:
            idCarrera = request.form['idCarrera']
        else:
            idCarrera = 1

        idArea = request.form['idArea']

        CodigoPuesto = request.form['CodigoPuesto']
        NombrePuesto = request.form['NombrePuesto']
        PuestoJefeSuperior = request.form['PuestoJefeSuperior']
        Jornada = request.form['Jornada']
        RenumeracionMensual = request.form['RenumeracionMensual']
        Prestaciones = request.form['Prestaciones']
        Descripcion = request.form['DescripcionGeneral']
        Funciones = request.form['Funciones']
        Edad = request.form['Edad']
        Experiencia = request.form['Experiencia']
        Conocimientos = request.form['Conocimientos']
        ManejoEquipo = request.form['ManejoEquipo']
        RequisitosFisicos = request.form['RequisitosFisicos']
        RequisitosPsicologicos = request.form['RequisitosPsicologicos']
        Responsabilidades = request.form['Responsabilidades']
        CondicionesTrabajo = request.form['CondicionesTrabajo']
        idEstadoCivil = request.form['idEstadoCivil']
        Sexo = request.form['Sexo']

        conexion = pymysql.connect(
            host='localhost', user='root', passwd='', db='bd_rh')
        cursor = conexion.cursor()
        cursor.execute('UPDATE puesto SET CodigoPuesto=%s, NombrePuesto=%s, idArea=%s, PuestoJefeSuperior=%s, Jornada=%s, '
                       'RenumeracionMensual=%s, Prestaciones=%s, Descripcion=%s, Funciones=%s, Edad=%s, Sexo=%s, idEstadoCivil=%s, '
                       'idEscolaridad=%s, idGradoAvance=%s, idCarrera=%s, Experiencia=%s, Conocimientos=%s, ManejoEquipo=%s, '
                       'RequisitosFisicos=%s, RequisitosPsicologicos=%s, Responsabilidades=%s, CondicionesTrabajo=%s '
                       'WHERE idPuesto=%s', (CodigoPuesto, NombrePuesto, idArea, PuestoJefeSuperior, Jornada,
                                             RenumeracionMensual, Prestaciones, Descripcion, Funciones, Edad, Sexo, idEstadoCivil,
                                             idEscolaridad, idGradoAvance, idCarrera, Experiencia, Conocimientos, ManejoEquipo,
                                             RequisitosFisicos, RequisitosPsicologicos, Responsabilidades, CondicionesTrabajo, idPuesto))
        conexion.commit()

        cursor.execute(
            'DELETE FROM puesto_tiene_idioma WHERE puesto_idPuesto=%s', (idPuesto))
        conexion.commit()
        cursor.execute(
            'DELETE FROM puesto_tiene_habilidad WHERE puesto_idPuesto=%s', (idPuesto))
        conexion.commit()

        cursor.execute('SELECT COUNT(*) FROM idioma')
        datoIdioma = cursor.fetchall()
        NumeroIdioma = datoIdioma[0]
        NIdioma = NumeroIdioma[0] + 1

        for i in range(1, NIdioma):
            Idioma = 'Idioma' + str(i)
            if Idioma in request.form:
                cursor.execute(
                    'INSERT INTO puesto_tiene_idioma (puesto_idPuesto, idioma_idIdioma) VALUES (%s, %s)', (idPuesto, i))
                conexion.commit()

        cursor.execute('SELECT COUNT(*) FROM habilidades')
        datoHabilidad = cursor.fetchall()
        NumeroHabilidad = datoHabilidad[0]
        NHabilidad = NumeroHabilidad[0] + 1

        for i in range(1, NHabilidad):
            Habilidad = 'Habilidad' + str(i)
            if Habilidad in request.form:
                cursor.execute(
                    'INSERT INTO puesto_tiene_habilidad (puesto_idPuesto, habilidades_idHabilidades) VALUES (%s, %s)', (idPuesto, i))
                conexion.commit()

        return redirect(url_for('puesto'))


@app.route('/Borrar_Puesto/<string:idPuesto>')
def borrar_puesto(idPuesto):
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='bd_rh')
    cursor = conexion.cursor()

    cursor.execute('DELETE FROM puesto WHERE idPuesto = %s', (idPuesto))
    conexion.commit()

    cursor.execute(
        'DELETE FROM puesto_tiene_idioma WHERE puesto_idPuesto = %s', (idPuesto))
    conexion.commit()

    cursor.execute(
        'DELETE FROM puesto_tiene_habilidad WHERE puesto_idPuesto = %s', (idPuesto))
    conexion.commit()

    return (redirect(url_for('puesto')))


# Requisicion


@app.route('/Agregar_Requisicion')
def agregar_requisicion():
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='bd_rh')
    cursor = conexion.cursor()

    cursor.execute(
        'SELECT idArea, descripcion FROM area')
    datosArea = cursor.fetchall()
    cursor.execute(
        'SELECT * FROM puesto')
    datosPuesto = cursor.fetchall()

    return render_template("requisicion_agregar.html", AreaDatos=datosArea, PuestoDatos=datosPuesto)


@app.route('/AgregarP_Requisicion', methods=['POST'])
def agregarp_requisicion():
    if request.method == 'POST':

        Folio = request.form['Folio']
        idArea = request.form['idArea']
        FechaElaboracion = request.form['FechaElaboracion']
        idPuesto = request.form['idPuesto']
        Solicitante = request.form['Solicitante']
        FechaReclutamiento = request.form['FechaReclutamiento']
        FechaInicioVacante = request.form['FechaInicioVacante']
        TipoVacante = request.form['TipoVacante']

        if 'MotivoOtroInput' in request.form:
            MotivoVacante = request.form['MotivoOtroInput']
        else:
            MotivoVacante = request.form['Motivo']

        conexion = pymysql.connect(
            host='localhost', user='root', passwd='', db='bd_rh')
        cursor = conexion.cursor()
        cursor.execute('INSERT INTO requisicion (folio, idArea, fecha_elaboracion, idPuesto, '
                       'fecha_reclutamiento, fecha_inicio_vacante, tipo_vacante, motivo, nombre_solicitante) '
                       'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', (Folio, idArea, FechaElaboracion, idPuesto,
                                                                       FechaReclutamiento, FechaInicioVacante, TipoVacante, MotivoVacante, Solicitante))
        conexion.commit()

        return redirect(url_for('requisiciones_pendientes'))


@app.route('/Requisiciones_Pendientes')
def requisiciones_pendientes():
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='bd_rh')
    cursor = conexion.cursor()

    cursor.execute(
        'SELECT a.idRequisicion, a.folio, b.NombrePuesto FROM requisicion a, puesto b WHERE '
        'a.idPuesto = b.idPuesto AND a.autorizacion =! %s', ('1'))
    datoRequisicion = cursor.fetchall()

    return render_template("requisiciones_pendientes.html", RequisicionDato=datoRequisicion,
                           RequisicionDatos='', AreaDatos='', PuestoDatos='', EstadoCivilDatos='',
                           EscolaridadDatos='')


@app.route('/Detalles_RequisicionPendientes/<string:idRequisicion>', methods=['GET'])
def detalles_requisicionPendientes(idRequisicion):
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute(
        'SELECT a.idRequisicion, a.folio, b.NombrePuesto FROM requisicion a, puesto b WHERE '
        'a.idPuesto = b.idPuesto AND a.autorizacion =! %s', ('1'))
    datoRequisicion = cursor.fetchall()

    cursor.execute('SELECT a.idarea, a.descripcion FROM area a, requisicion b WHERE '
                   'a.idarea = b.idArea AND b.idRequisicion = %s', (idRequisicion))
    datosArea = cursor.fetchall()

    cursor.execute(
        'SELECT * FROM requisicion WHERE idRequisicion =%s', (idRequisicion))
    datosRequisicion = cursor.fetchall()

    cursor.execute('SELECT a.* FROM puesto a, requisicion b WHERE a.idPuesto = b.idPuesto '
                   'AND b.idRequisicion = %s', (idRequisicion))
    datosPuesto = cursor.fetchall()

    datoPuesto = datosPuesto[0]
    idPuesto = datoPuesto[0]

    cursor.execute('SELECT a.idEstadoCivil, a.descripcion FROM estado_civil a, puesto b WHERE '
                   'a.idEstadoCivil = b.idEstadoCivil AND b.idPuesto = %s', (idPuesto))
    datosEstadoCivil = cursor.fetchall()

    cursor.execute('SELECT a.idEscolaridad, a.descripcion FROM escolaridad a, puesto b WHERE '
                   'a.idEscolaridad = b.idEscolaridad AND b.idPuesto = %s', (idPuesto))
    datosEscolaridad = cursor.fetchall()

    return render_template("requisiciones_pendientes.html", RequisicionDato=datoRequisicion,
                           RequisicionDatos=datosRequisicion[0], AreaDatos=datosArea[0],
                           PuestoDatos=datosPuesto[0], EstadoCivilDatos=datosEstadoCivil[0],
                           EscolaridadDatos=datosEscolaridad[0])


@app.route('/Autorizar_Requisicion/<string:idRequisicion>')
def autorizar_requisicion(idRequisicion):
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute('SELECT a.idRequisicion, a.folio, b.NombrePuesto FROM requisicion a, puesto b '
                   'WHERE a.idPuesto = b.idPuesto AND a.idRequisicion = %s', (idRequisicion))
    datosAutorizar = cursor.fetchall()
    return render_template("autorizar.html", AutorizarDatos=datosAutorizar[0])


@app.route('/AutorizarP_Requisicion/<string:idRequisicion>', methods=['POST'])
def autorizarp_requisicion(idRequisicion):
    if request.method == 'POST':
        NombreRevisado = request.form['Revisado']
        NombreAutorizado = request.form['Autorizado']

        conexion = pymysql.connect(
            host='localhost', user='root', passwd='', db='bd_rh')
        cursor = conexion.cursor()

        cursor.execute('UPDATE requisicion SET nombre_revisa = %s, nombre_autoriza = %s, autorizacion = %s '
                       'WHERE idRequisicion = %s', (NombreRevisado, NombreAutorizado, '1', idRequisicion))
        conexion.commit()
    return redirect(url_for('requisiciones_autorizadas'))


@app.route('/Borrar_Requisicion/<string:idRequisicion>')
def borrar_requisicion(idRequisicion):
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='bd_rh')
    cursor = conexion.cursor()

    cursor.execute(
        'DELETE FROM requisicion WHERE idRequisicion  = %s', (idRequisicion))
    conexion.commit()

    return (redirect(url_for('requisiciones_pendientes')))


@app.route('/Requisiciones_Autorizadas')
def requisiciones_autorizadas():
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='bd_rh')
    cursor = conexion.cursor()

    cursor.execute(
        'SELECT a.idRequisicion, a.folio, b.NombrePuesto FROM requisicion a, puesto b WHERE '
        'a.idPuesto = b.idPuesto AND a.autorizacion =! %s', ('0'))
    datoRequisicion = cursor.fetchall()

    return render_template("requisiciones_autorizadas.html", RequisicionDato=datoRequisicion,
                           RequisicionDatos='', AreaDatos='', PuestoDatos='', EstadoCivilDatos='',
                           EscolaridadDatos='')


@app.route('/Detalles_RequisicionAutorizadas/<string:idRequisicion>', methods=['GET'])
def detalles_requisicionAutorizadas(idRequisicion):
    conexion = pymysql.connect(
        host='localhost', user='root', passwd='', db='bd_rh')
    cursor = conexion.cursor()
    cursor.execute(
        'SELECT a.idRequisicion, a.folio, b.NombrePuesto FROM requisicion a, puesto b WHERE '
        'a.idPuesto = b.idPuesto AND a.autorizacion =! %s', ('0'))
    datoRequisicion = cursor.fetchall()

    cursor.execute('SELECT a.idarea, a.descripcion FROM area a, requisicion b WHERE '
                   'a.idarea = b.idArea AND b.idRequisicion = %s', (idRequisicion))
    datosArea = cursor.fetchall()

    cursor.execute(
        'SELECT * FROM requisicion WHERE idRequisicion =%s', (idRequisicion))
    datosRequisicion = cursor.fetchall()

    cursor.execute('SELECT a.* FROM puesto a, requisicion b WHERE a.idPuesto = b.idPuesto '
                   'AND b.idRequisicion = %s', (idRequisicion))
    datosPuesto = cursor.fetchall()

    datoPuesto = datosPuesto[0]
    idPuesto = datoPuesto[0]

    cursor.execute('SELECT a.idEstadoCivil, a.descripcion FROM estado_civil a, puesto b WHERE '
                   'a.idEstadoCivil = b.idEstadoCivil AND b.idPuesto = %s', (idPuesto))
    datosEstadoCivil = cursor.fetchall()

    cursor.execute('SELECT a.idEscolaridad, a.descripcion FROM escolaridad a, puesto b WHERE '
                   'a.idEscolaridad = b.idEscolaridad AND b.idPuesto = %s', (idPuesto))
    datosEscolaridad = cursor.fetchall()

    return render_template("requisiciones_autorizadas.html", RequisicionDato=datoRequisicion,
                           RequisicionDatos=datosRequisicion[0], AreaDatos=datosArea[0],
                           PuestoDatos=datosPuesto[0], EstadoCivilDatos=datosEstadoCivil[0],
                           EscolaridadDatos=datosEscolaridad[0])


if __name__ == "__main__":
    app.run(debug=True)
