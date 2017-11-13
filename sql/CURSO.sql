CREATE TABLE CURSO (
    id    integer not null primary key,
    sigla varchar(5) not null,
    nome  varchar(50) not null,
    CONSTRAINT sigla_unique UNIQUE (sigla),
    CONSTRAINT nome_unique UNIQUE (nome)
);