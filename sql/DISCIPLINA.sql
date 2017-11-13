CREATE TABLE DISCIPLINA (
    id integer identity(1,1) not null primary key,
    nome varchar(240) not null,
    carga_horaria TINYINT not null,
    teoria DECIMAL(3),
    pratica DECIMAL(3),
    competencias TEXT,
    habilidades TEXT,
    conteudo TEXT,
    bibliografia_basica TEXT,
    bibliografia_complementar TEXT,
    CONSTRAINT disciplina_unique UNIQUE (nome)
);