CREATE TABLE "vrach" (
  "id" SERIAL PRIMARY KEY,
  "id_vrach" TEXT NOT NULL,
  "surname" VARCHAR(50) NOT NULL,
  "name" VARCHAR(30) NOT NULL,
  "patroin" VARCHAR(30) NOT NULL
);

CREATE TABLE "raspisanie" (
  "id" SERIAL PRIMARY KEY,
  "id_vrach" INTEGER NOT NULL,
  "den_nedeli" VARCHAR(15) NOT NULL,
  "vremya" TEXT NOT NULL,
  "data" DATE
);

CREATE INDEX "idx_raspisanie__id_vrach" ON "raspisanie" ("id_vrach");

ALTER TABLE "raspisanie" ADD CONSTRAINT "fk_raspisanie__id_vrach" FOREIGN KEY ("id_vrach") REFERENCES "vrach" ("id") ON DELETE CASCADE;

CREATE TABLE "group" (
  "id" SERIAL PRIMARY KEY,
  "id_raspisanie" INTEGER NOT NULL
);

CREATE INDEX "idx_group__id_raspisanie" ON "group" ("id_raspisanie");

ALTER TABLE "group" ADD CONSTRAINT "fk_group__id_raspisanie" FOREIGN KEY ("id_raspisanie") REFERENCES "raspisanie" ("id") ON DELETE CASCADE;

CREATE TABLE "pacient" (
  "id" SERIAL PRIMARY KEY,
  "id_pacient" TEXT NOT NULL,
  "surname" TEXT NOT NULL,
  "name" TEXT NOT NULL,
  "patrion" TEXT NOT NULL,
  "year_bd" DATE,
  "uchastok" TEXT NOT NULL,
  "phone" TEXT NOT NULL,
  "email" VARCHAR(100) NOT NULL,
  "llo" BOOLEAN,
  "group" INTEGER NOT NULL
);

CREATE INDEX "idx_pacient__group" ON "pacient" ("group");

ALTER TABLE "pacient" ADD CONSTRAINT "fk_pacient__group" FOREIGN KEY ("group") REFERENCES "group" ("id") ON DELETE CASCADE