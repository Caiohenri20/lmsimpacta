CREATE TABLE USUARIO (
    id    integer identity(1,1) not null,
	ra	  integer not null,
	password varchar(255) not null,
    nome  varchar(150) not null,
	email varchar(50) not null,
	celular char(11),
	perfil char(1) not null,
	ativo bit not null default 1,
    CONSTRAINT pk_usuario primary key (id),
    CONSTRAINT un_usuario UNIQUE (ra)
);
