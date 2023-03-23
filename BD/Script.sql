-- MySQL Script generated by MySQL Workbench
-- Thu Jan 26 12:37:03 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema railway
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema railway
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `railway` DEFAULT CHARACTER SET utf8 ;
USE `railway` ;

-- -----------------------------------------------------
-- Table `railway`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `railway`.`Usuario` (
  `codUsuario` INT NOT NULL,
  `Matricula` INT NOT NULL,
  `Email` VARCHAR(100) NOT NULL,
  `Conhecimento` TEXT(500) NOT NULL,
  `Avaliacao` FLOAT NULL,
  `Curso` VARCHAR (45),
  `Nome` VARCHAR(255) NOT NULL,
  `Senha` VARCHAR(75) NOT NULL,
  `Usuario` VARCHAR(100) NOT NULL,
  `RankAvaliacao` float,
  PRIMARY KEY (`codUsuario`),
  UNIQUE INDEX `Usuario_UNIQUE` (`Usuario` ASC) VISIBLE,
  UNIQUE INDEX `Matricula_UNIQUE` (`Matricula` ASC) VISIBLE,
  UNIQUE INDEX `codUsuario_UNIQUE` (`codUsuario` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `railway`.`Demanda`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `railway`.`Demanda` (
  `codDemanda` INT NOT NULL,
  `Descricao` TEXT(500) NOT NULL,
  `Grupo` CHAR(1) NOT NULL,
  `dt_Abertura` DATE NOT NULL,
  `Status` VARCHAR(20) NOT NULL,
  `Solicitante` INT NOT NULL,
  `Ajudante` INT NOT NULL,
  `Avaliacao` float,
  PRIMARY KEY (`codDemanda`, `Solicitante`, `Ajudante`),
  UNIQUE INDEX `codDemanda_UNIQUE` (`codDemanda` ASC) VISIBLE,
  INDEX `fk_Demanda_Usuario_idx` (`Solicitante` ASC) VISIBLE,
  INDEX `fk_Demanda_Usuario1_idx` (`Ajudante` ASC) VISIBLE,
  CONSTRAINT `fk_Demanda_Usuario`
    FOREIGN KEY (`Solicitante`)
    REFERENCES `railway`.`Usuario` (`codUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Demanda_Usuario1`
    FOREIGN KEY (`Ajudante`)
    REFERENCES `railway`.`Usuario` (`codUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `railway`.`Tags`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `railway`.`Tags` (
  `codTag` INT NOT NULL,
  `Nome` TEXT(50) NOT NULL,
  `Recorrencia` INT NOT NULL,
  PRIMARY KEY (`codTag`),
  UNIQUE INDEX `codTags_UNIQUE` (`codTag` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `railway`.`Atrelada`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `railway`.`Atrelada` (
  `codTag` INT NOT NULL,
  `codDemanda` INT NOT NULL,
  PRIMARY KEY (`codTag`, `codDemanda`),
  INDEX `fk_Atrelada_Tags1_idx` (`codTag` ASC) VISIBLE,
  INDEX `fk_Atrelada_Demanda1_idx` (`codDemanda` ASC) VISIBLE,
  UNIQUE INDEX `codTag_UNIQUE` (`codTag` ASC) VISIBLE,
  UNIQUE INDEX `codDemanda_UNIQUE` (`codDemanda` ASC) VISIBLE,
  CONSTRAINT `fk_Atrelada_Tags1`
    FOREIGN KEY (`codTag`)
    REFERENCES `railway`.`Tags` (`codTag`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Atrelada_Demanda1`
    FOREIGN KEY (`codDemanda`)
    REFERENCES `railway`.`Demanda` (`codDemanda`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `railway`.`Forum`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `railway`.`Forum`(
	`idForum` INT NOT NULL,
    PRIMARY KEY (`idForum`),
    UNIQUE INDEX `idForum_UNIQUE` (`idForum` ASC) VISIBLE)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `railway`.`Topicos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `railway`.`Topicos`(
	`idTopicos` INT NOT NULL,
    `idForum` INT NOT NULL,    
    `codUsuario` INT NOT NULL,
    `data_topico` DATE NOT NULL,
    `Texto` TEXT(500),
    PRIMARY KEY (`idTopicos`,`idForum`,`codUsuario`),
    UNIQUE INDEX `idTopicos_UNIQUE` (`idTopicos` ASC) VISIBLE,
    INDEX `fk_Forum_idForum` (`idForum` ASC) VISIBLE,
    INDEX `fk_Topicos_codUsuario` (`codUsuario` ASC) VISIBLE,
    CONSTRAINT `fk_Forum_idForum`
		FOREIGN KEY (`idForum`)
        REFERENCES `railway`.`Forum` (`idForum`)
        ON DELETE NO ACTION 
        ON UPDATE NO ACTION,
	CONSTRAINT `fk_Topicos_codUsuario`
		FOREIGN KEY (`codUsuario`)
        REFERENCES `railway`.`Usuario` (`codUsuario`)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `railway`.`Comentario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `railway`.`Comentario`(
	`idComentario` INT NOT NULL,
    `codUsuario` INT NOT NULL,
    `idTopicos` INT NOT NULL,
    `data_comentario` DATE NOT NULL,
    `mensagem` TEXT(500) NOT NULL,
    PRIMARY KEY (`idComentario`,`codUsuario`,`idTopicos`),
    UNIQUE INDEX `idComentario_UNIQUE` (`idComentario` ASC) VISIBLE,
    INDEX `fk_Comentario_codUsuario` (`codUsuario` ASC) VISIBLE,
	INDEX `fk_Topicos_idTopicos` (`idTopicos` ASC) VISIBLE,
	CONSTRAINT `fk_Comentario_codUsuario`
		FOREIGN KEY (`codUsuario`)
        REFERENCES `railway`.`usuario` (`codUsuario`)
        ON DELETE NO ACTION
		ON UPDATE NO ACTION,
	CONSTRAINT `fk_Topicos_idTopicos`
		FOREIGN KEY (`idTopicos`)
        REFERENCES `railway`.`Topicos` (`idTopicos`)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
)

ENGINE = InnoDB;
SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
