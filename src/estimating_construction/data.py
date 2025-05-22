import sqlite3

class SQLiteHandler:
    def __init__(self) -> None:
        self.db = "links.db"
        self._enquire = """SELECT enq.name, enq.company, enq.email, enq.phone, enq.sop,
                    gw.gateway, enq.description, et.type,
                    pt.partner, ct.contract, hb.hub
                    FROM enquiries AS enq
                    INNER JOIN gateways AS gw ON enq.gateway_id = gw.gateway_id
                    INNER JOIN estimatetypes AS et ON enq.type_id = et.type_id
                    INNER JOIN partners AS pt ON enq.partner_id = pt.partner_id
                    INNER JOIN contracts AS ct ON enq.contract_id = ct.contract_id
                    INNER JOIN hubs AS hb ON enq.hub_id = hb.hub_id"""
        self._gateways = [
            ('0 - Mandate',), 
            ('1 - SOC Development',),
            ('2 - SOC-OBC Appraisal',), 
            ('3 - OBC-FBC Detailed Design',),
            ('4 - Construction',)
            ]
    
    def drop_all(self) -> None:
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS gateways;")
        cur.execute("DROP TABLE IF EXISTS estimatetypes;")
        cur.execute("DROP TABLE IF EXISTS partners;")
        cur.execute("DROP TABLE IF EXISTS contracts;")
        cur.execute("DROP TABLE IF EXISTS hubs;")
        cur.execute("DROP TABLE IF EXISTS enquiries;")
        conn.commit()
        conn.close()
    
    def create_all(self) -> None:
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        create_gateways = """CREATE TABLE IF NOT EXISTS gateways (
                    gateway_id INTEGER PRIMARY KEY,
                    gateway TEXT NOT NULL
                    );"""
        create_estimatetypes = """CREATE TABLE IF NOT EXISTS estimatetypes (
                    type_id INTEGER PRIMARY KEY,
                    type TEXT NOT NULL
                    );"""
        create_partners = """CREATE TABLE IF NOT EXISTS partners (
                    partner_id INTEGER PRIMARY KEY,
                    partner TEXT NOT NULL
                    );"""
        create_contracts = """CREATE TABLE IF NOT EXISTS contracts (
                    contract_id INTEGER PRIMARY KEY,
                    contract TEXT NOT NULL
                    );"""
        create_hubs = """CREATE TABLE IF NOT EXISTS hubs (
                    hub_id INTEGER PRIMARY KEY,
                    hub TEXT NOT NULL
                    );"""
        create_enquiries = """CREATE TABLE IF NOT EXISTS enquiries (
                    enquiry_id INTEGER PRIMARY KEY
                    ,name TEXT NOT NULL
                    ,company TEXT NOT NULL
                    ,email TEXT NOT NULL
                    ,phone TEXT NOT NULL
                    ,sop TEXT NOT NULL
                    ,gateway_id INTEGER NOT NULL
                    ,description TEXT NOT NULL
                    ,type_id INTEGER NOT NULL
                    ,partner_id INTEGER NOT NULL
                    ,contract_id INTEGER NOT NULL
                    ,hub_id INTEGER NOT NULL
                    );"""
        cur.execute(create_gateways)
        cur.execute(create_estimatetypes)
        cur.execute(create_partners)
        cur.execute(create_contracts)
        cur.execute(create_hubs)
        cur.execute(create_enquiries)
        conn.commit()
        conn.close()
    
    def reset(self) -> None:
        self.drop_all()
        self.create_all()
    
    def background_data(self) -> None:
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        insert_gateways = "INSERT INTO gateways (gateway) VALUES (?)"
        insert_estimatetypes = """INSERT INTO estimatetypes (type)
                    VALUES
                    ('Target'), ('Gateway'), ('CE Assement');"""
        insert_partners = """INSERT INTO partners (partner)
                    VALUES
                    ('Lot 1'), ('Lot 2'), ('N/A');"""
        insert_contracts = """INSERT INTO contracts (contract)
                    VALUES
                    ('PSC'), ('ECC');"""
        insert_hubs = """INSERT INTO hubs (hub)
                    VALUES
                    ('North East'), ('North West'),
                    ('South East'), ('South West'),
                    ('Midlands'), ('Eastern');"""
        insert_enquiries = """INSERT INTO enquiries 
                    (name, company, email, phone, sop,
                    gateway_id, description, type_id,
                    partner_id, contract_id, hub_id)
                    VALUES
                    ('Name1', 'JMK', '1@JMK.com', '', 'ENV123', 3, '',
                    2, 1, 1, 5) 
                    ,('Name2', 'Atfam', '2@Atfam.com', '', 'ENV124', 2, '',
                    2, 2, 2, 3)
                    ;"""
        cur.executemany(insert_gateways, self._gateways)
        cur.execute(insert_estimatetypes)
        cur.execute(insert_partners)
        cur.execute(insert_contracts)
        cur.execute(insert_hubs)
        cur.execute(insert_enquiries)
        conn.commit()
        conn.close()
    
    @property
    def enquiries(self) -> list[tuple]:
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        query1 = f"{self._enquire}"
        cur.execute(query1)
        output = cur.fetchall()
        conn.close()
        return output

    def enquiry(self, id: int) -> list:
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        query1 = f"{self._enquire} WHERE enquiry_id=?"
        cur.execute(query1, (1,))
        output = cur.fetchone()
        conn.close()
        return output

# SQLiteHandler().reset()
db = SQLiteHandler()
db.reset()
db.background_data()
print(db.enquiries)
print(db.enquiry(1))

