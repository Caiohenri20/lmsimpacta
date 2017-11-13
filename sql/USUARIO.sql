CREATE TABLE CURSO (
    id    integer identity(1,1) not null,
    sigla varchar(5) not null,
    nome  varchar(50) not null,
    CONSTRAINT pk_curso primary key (id),
    CONSTRAINT sigla_unique UNIQUE (sigla),
    CONSTRAINT nome_unique UNIQUE (nome)
);