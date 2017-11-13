CREATE TABLE PERIODO (
    id integer not null primary key,
    grade_curricular_id integer not null,
    numero tinyint not null,
    CONSTRAINT periodo_unique UNIQUE (grade_curricular_id, numero),
    CONSTRAINT fk_periodo_grade_curricular
    FOREIGN KEY (grade_curricular_id)
    REFERENCES GRADE_CURRICULAR (id)
);