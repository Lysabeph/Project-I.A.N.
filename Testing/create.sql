PRAGMA foreign_keys=ON;

CREATE TABLE Programs (
    ProgramName varchar(31) PRIMARY KEY,
    TimesRun int,
    TotalRunTime int
);

CREATE TABLE ProgramCommands (
    ProgramCMD varchar(63) PRIMARY KEY,
    ProgramName int,
    FOREIGN KEY(ProgramName) REFERENCES Programs(ProgramName)
);

CREATE TABLE ProgramLogs (
    ProgramName varchar(31),
    PID int(6),
    DateTime int,
    OpenClose char(5),
    PRIMARY KEY(ProgramName, PID, DateTime, OpenClose),
    FOREIGN KEY(ProgramName) REFERENCES Programs(ProgramName)
);
