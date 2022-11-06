-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema bd_rh
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `bd_rh` ;

-- -----------------------------------------------------
-- Schema bd_rh
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `bd_rh` DEFAULT CHARACTER SET utf8 ;
USE `bd_rh` ;

-- -----------------------------------------------------
-- Table `bd_rh`.`area`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bd_rh`.`area` (
  `idarea` INT(11) NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`idarea`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;

INSERT INTO `bd_rh`.`area` (`idarea`, `descripcion`) VALUES ('1', 'No Aplica');


-- -----------------------------------------------------
-- Table `bd_rh`.`carrera`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bd_rh`.`carrera` (
  `idCarrera` INT(11) NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`idCarrera`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;

INSERT INTO `bd_rh`.`carrera` (`idCarrera`, `descripcion`) VALUES ('1', 'No Requerida');


-- -----------------------------------------------------
-- Table `bd_rh`.`escolaridad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bd_rh`.`escolaridad` (
  `idEscolaridad` INT(11) NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`idEscolaridad`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;

INSERT INTO `bd_rh`.`escolaridad` (`idEscolaridad`, `descripcion`) VALUES ('1', 'No Requerida');


-- -----------------------------------------------------
-- Table `bd_rh`.`estado_civil`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bd_rh`.`estado_civil` (
  `idEstadoCivil` INT(11) NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`idEstadoCivil`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;

INSERT INTO `bd_rh`.`estado_civil` (`idEstadoCivil`, `descripcion`) VALUES ('1', 'No Precisado');

-- -----------------------------------------------------
-- Table `bd_rh`.`grado_avance`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bd_rh`.`grado_avance` (
  `idGradoAvance` INT(11) NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idGradoAvance`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;

INSERT INTO `bd_rh`.`grado_avance` (`idGradoAvance`, `descripcion`) VALUES ('1', 'No Aplica');


-- -----------------------------------------------------
-- Table `bd_rh`.`habilidades`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bd_rh`.`habilidades` (
  `idHabilidades` INT(11) NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(300) NOT NULL,
  PRIMARY KEY (`idHabilidades`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;

INSERT INTO `bd_rh`.`habilidades` (`idHabilidades`, `descripcion`) VALUES ('1', 'No Requeridas');


-- -----------------------------------------------------
-- Table `bd_rh`.`idioma`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bd_rh`.`idioma` (
  `idIdioma` INT(11) NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`idIdioma`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;

INSERT INTO `bd_rh`.`idioma` (`idIdioma`, `descripcion`) VALUES ('1', 'No Requerido');


-- -----------------------------------------------------
-- Table `bd_rh`.`medio_publicidad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bd_rh`.`medio_publicidad` (
  `idMedioPublicidad` INT(11) NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`idMedioPublicidad`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `bd_rh`.`puesto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bd_rh`.`puesto` (
  `idPuesto` INT(11) NOT NULL AUTO_INCREMENT,
  `CodigoPuesto` VARCHAR(20) NOT NULL,
  `NombrePuesto` VARCHAR(60) NOT NULL,
  `idArea` INT(11) NOT NULL,
  `PuestoJefeSuperior` VARCHAR(60) NOT NULL,
  `Jornada` VARCHAR(60) NOT NULL,
  `RenumeracionMensual` INT(11) NOT NULL,
  `Prestaciones` VARCHAR(100) NOT NULL,
  `Descripcion` VARCHAR(200) NOT NULL,
  `Funciones` VARCHAR(200) NOT NULL,
  `Edad` VARCHAR(50) NOT NULL,
  `Sexo` VARCHAR(15) NOT NULL,
  `idEstadoCivil` INT(11) NOT NULL,
  `idEscolaridad` INT(11) NOT NULL,
  `idGradoAvance` INT(11) NOT NULL,
  `idCarrera` INT(11) NOT NULL,
  `Experiencia` VARCHAR(150) NOT NULL,
  `Conocimientos` VARCHAR(150) NOT NULL,
  `ManejoEquipo` VARCHAR(150) NOT NULL,
  `RequisitosFisicos` VARCHAR(100) NOT NULL,
  `RequisitosPsicologicos` VARCHAR(100) NOT NULL,
  `Responsabilidades` VARCHAR(150) NOT NULL,
  `CondicionesTrabajo` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`idPuesto`, `idArea`, `idEstadoCivil`, `idEscolaridad`, `idGradoAvance`, `idCarrera`),
  INDEX `fk_id_idArea_idx` (`idArea` ASC),
  INDEX `fk_id_idEstadoCivil_idx` (`idEstadoCivil` ASC),
  INDEX `fk_id_idEscolaridad_idx` (`idEscolaridad` ASC),
  INDEX `fk_id_idGradoAvance_idx` (`idGradoAvance` ASC),
  INDEX `fk_id_idCarrera_idx` (`idCarrera` ASC),
  CONSTRAINT `fk_id_idArea`
    FOREIGN KEY (`idArea`)
    REFERENCES `bd_rh`.`area` (`idarea`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_id_idCarrera`
    FOREIGN KEY (`idCarrera`)
    REFERENCES `bd_rh`.`carrera` (`idCarrera`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_id_idEscolaridad`
    FOREIGN KEY (`idEscolaridad`)
    REFERENCES `bd_rh`.`escolaridad` (`idEscolaridad`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_id_idEstadoCivil`
    FOREIGN KEY (`idEstadoCivil`)
    REFERENCES `bd_rh`.`estado_civil` (`idEstadoCivil`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_id_idGradoAvance`
    FOREIGN KEY (`idGradoAvance`)
    REFERENCES `bd_rh`.`grado_avance` (`idGradoAvance`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `bd_rh`.`puesto_tiene_habilidad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bd_rh`.`puesto_tiene_habilidad` (
  `puesto_idPuesto` INT(11) NOT NULL,
  `habilidades_idHabilidades` INT(11) NOT NULL,
  PRIMARY KEY (`puesto_idPuesto`, `habilidades_idHabilidades`),
  INDEX `fk_puesto_has_habilidades_habilidades1_idx` (`habilidades_idHabilidades` ASC),
  INDEX `fk_puesto_has_habilidades_puesto_idx` (`puesto_idPuesto` ASC),
  CONSTRAINT `fk_puesto_has_habilidades_habilidades1`
    FOREIGN KEY (`habilidades_idHabilidades`)
    REFERENCES `bd_rh`.`habilidades` (`idHabilidades`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_puesto_has_habilidades_puesto`
    FOREIGN KEY (`puesto_idPuesto`)
    REFERENCES `bd_rh`.`puesto` (`idPuesto`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `bd_rh`.`puesto_tiene_idioma`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bd_rh`.`puesto_tiene_idioma` (
  `puesto_idPuesto` INT(11) NOT NULL,
  `idioma_idIdioma` INT(11) NOT NULL,
  PRIMARY KEY (`puesto_idPuesto`, `idioma_idIdioma`),
  INDEX `fk_puesto_has_idioma_idioma1_idx` (`idioma_idIdioma` ASC),
  CONSTRAINT `fk_puesto_has_idioma_idioma1`
    FOREIGN KEY (`idioma_idIdioma`)
    REFERENCES `bd_rh`.`idioma` (`idIdioma`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_puesto_has_idioma_puesto1`
    FOREIGN KEY (`puesto_idPuesto`)
    REFERENCES `bd_rh`.`puesto` (`idPuesto`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `bd_rh`.`requisicion`
-- -----------------------------------------------------
CREATE TABLE `bd_rh`.`requisicion` (
  `idRequisicion` INT NOT NULL AUTO_INCREMENT,
  `folio` VARCHAR(25) NOT NULL,
  `fecha_elaboracion` DATE NOT NULL,
  `fecha_reclutamiento` DATE NOT NULL,
  `fecha_inicio_vacante` DATE NOT NULL,
  `motivo` VARCHAR(70) NOT NULL,
  `tipo_vacante` VARCHAR(50) NOT NULL,
  `nombre_solicitante` VARCHAR(80) NOT NULL,
  `nombre_revisa` VARCHAR(80) NOT NULL,
  `nombre_autoriza` VARCHAR(80) NOT NULL,
  `autorizacion` TINYINT(1) NOT NULL,
  `idPuesto` INT NOT NULL,
  `idArea` INT NOT NULL,
  PRIMARY KEY (`idRequisicion`, `idPuesto`, `idArea`),
  INDEX `fk_idPuesto_idPuesto_idx` (`idPuesto` ASC),
  INDEX `fk_idArea_idarea_idx` (`idArea` ASC),
  CONSTRAINT `fk_idPuesto_idPuesto`
    FOREIGN KEY (`idPuesto`)
    REFERENCES `bd_rh`.`puesto` (`idPuesto`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_idArea_idarea`
    FOREIGN KEY (`idArea`)
    REFERENCES `bd_rh`.`area` (`idarea`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;
    

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
