CREATE TABLE MATRICULA (
    aluno_id  integer not null,
    turma_id integer not null,
    CONSTRAINT pk_matricula primary key (aluno_id, turma_id),
    CONSTRAINT fk_matricula_aluno
    FOREIGN KEY (aluno_id)
    REFERENCES ALUNO (usuario_id),
    CONSTRAINT fk_matricula_turma
    FOREIGN KEY (turma_id)
    REFERENCES TURMA (id)
);