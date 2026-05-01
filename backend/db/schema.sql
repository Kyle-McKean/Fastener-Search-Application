-- SQLite database schema for fastener data
CREATE TABLE fasteners (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL,
    material TEXT NOT NULL,
    size TEXT NOT NULL,
    length TEXT NOT NULL,
    name TEXT NOT NULL
);