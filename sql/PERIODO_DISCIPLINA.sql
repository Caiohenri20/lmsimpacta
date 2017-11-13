CREATE TABLE PERIODO_DISCIPLINA (
    periodo_id integer not null,
    disciplina_id integer not null,
    CONSTRAINT pk_periodo PRIMARY KEY (periodo_id, disciplina_id),
    CONSTRAINT fk_periodo_disciplina_periodo
    FOREIGN KEY (periodo_id) REFERENCES PERIODO (id),
    CONSTRAINT fk_periodo_disciplina_disciplina
    FOREIGN KEY (disciplina_id) REFERENCES DISCIPLINA (id)
);