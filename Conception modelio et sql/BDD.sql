DROP TABLE ressources;
DROP TABLE commande;
DROP TABLE portefeuille;
DROP TABLE portefeuille_action;

CREATE DATABASE if not exists BDD_IF;
use BDD_IF;

CREATE TABLE if not exists Ressources(
	nom_action varchar(25) NOT NULL,
	date_action datetime,
	ouverture float(4),
	haut float(4),
	bas float(4),
	dernier float(4),
	volume int(25),

	BNA float(4),
	Dividende float(4),
	Rendement float(4),
	PER float(4),
	Actualité text,

	PRIMARY KEY(date_action)
);

CREATE TABLE if not exists portefeuille (
	rentabilite_total_ptf float(4),
	prix_total_actions_ptf float(4),
	sold_ptf float(4),
	value_total_ptf float(4)
);

CREATE TABLE if not exists portefeuille_action (
	code__ptf_action varchar(25),
	nom__ptf_action	varchar(25),
	cout_ptf_action float(4),
	prix_ptf_action float(4),
	quantitie_ptf_action int(25),
	prix_total_ptf_action float(25),
	rentabilite__ptf_action float(25)
);

CREATE TABLE if not exists commande (
	code_action_cmd varchar(25),
	nom_action_cmd varchar(25),
	opération_cmd varchar(25),
	prix_cmd float(4),
	quantitie_cmd int(25),
	prix_total_cmd float(25),
	date_cmd datetime,
	status_cmd varchar(25),
	PRIMARY KEY(date_cmd)
);