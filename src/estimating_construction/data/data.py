import sqlite3
import json

from pathlib import Path
from contextlib import contextmanager

@contextmanager
def db_ops(db_name: str):
  conn:sqlite3.Connection = sqlite3.connect(db_name)
  try:
      cur = conn.cursor()
      yield cur
  except Exception as e:
      # do something with exception
      conn.rollback()
      raise e
  else:
      conn.commit()
  finally:
      conn.close()

class SQLiteHandler:
    def __init__(self) -> None:
        self.db = "store.db"
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
        # conn = sqlite3.connect(self.db)
        # cur = conn.cursor()
        with db_ops(self.db) as cur:
            cur.execute("DROP TABLE IF EXISTS gateways;")
            cur.execute("DROP TABLE IF EXISTS estimatetypes;")
            cur.execute("DROP TABLE IF EXISTS partners;")
            cur.execute("DROP TABLE IF EXISTS contracts;")
            cur.execute("DROP TABLE IF EXISTS hubs;")
            cur.execute("DROP TABLE IF EXISTS enquiries;")
            cur.execute("DROP TABLE IF EXISTS questions;")
            cur.execute("DROP TABLE IF EXISTS answers;")
        # conn.commit()
        # conn.close()
    
    def create_all(self) -> None:
        # conn = sqlite3.connect(self.db)
        # cur = conn.cursor()
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
        create_questions = """CREATE TABLE IF NOT EXISTS questions (
                    question_id INTEGER PRIMARY KEY
                    ,question TEXT NOT NULL
                    ,description TEXT NOT NULL
                    ,"order" INTEGER NOT NULL UNIQUE
                    ,multiselect INTEGER NOT NULL DEFAULT 1
                    );"""
        create_answers = """CREATE TABLE IF NOT EXISTS answers (
                    answer_id INTEGER PRIMARY KEY
                    ,answer TEXT NOT NULL
                    ,question_id INTEGER NOT NULL
                    ,"default" INTEGER NOT NULL DEFAULT 0
                    );"""
        with db_ops(self.db) as cur:
            cur.execute(create_gateways)
            cur.execute(create_estimatetypes)
            cur.execute(create_partners)
            cur.execute(create_contracts)
            cur.execute(create_hubs)
            cur.execute(create_enquiries)
            cur.execute(create_questions)
            cur.execute(create_answers)
        # conn.commit()
        # conn.close()
    
    def reset(self) -> None:
        self.drop_all()
        self.create_all()
    
    def background_data(self) -> None:
        # conn = sqlite3.connect(self.db)
        # cur = conn.cursor()
        insert_gateways = "INSERT INTO gateways (gateway) VALUES (?)"
        insert_estimatetypes = """INSERT INTO estimatetypes (type)
                    VALUES
                    ('Target'), ('Gateway'), ('CE Assessment');"""
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
        insert_questions = """INSERT INTO questions 
                    (question, description, "order", multiselect)
                    VALUES
                    ('What is the level of access to the site', 'TBC', 1, 1)
                    ,('Are there any official designations for the site?', 'TBC', 2, 1)
                    ,('What type of site compounds do you have?', 'TBC', 3, 1)
                    ,('Is the project in a remote location with difficult access to resources', 'TBC', 4, 0)
                    ,('How is the project classified?', 'TBC', 5, 0)
                    ,('Is there hazardous waste present on the site?', 'TBC', 6, 0)
                    ,('How would you describe the ground conditions on the site?', 'TBC', 7, 0)
                    ,('What is required for the existing non-Project structures at the site?', 'TBC', 8, 0)
                    ,('What type of species are present/anticipated on the site?', 'TBC', 9, 1)
                    ,('Is the project influenced by any of the following?', 'TBC', 10, 1)
                    ,('Is the project completion milestone constrained due to an external factor?', 'TBC', 11, 0)
                    ,('What ultilies are not available to connect for the construction work?', 'TBC', 12, 1)
                    ;"""
        insert_answers = """INSERT INTO answers 
                    (answer, question_id, "default")
                    VALUES
                    ('Physically constrained access', 1, 0)
                    ,('Unconstrained access', 1, 1)
                    ,('Time-limited access (e.g. certain hours accessible)', 1, 0)
                    ,('Third-party access (e.g. access through land owned by others, access rights needed)', 1, 0)
                    ,('Area of oustanding natural beauty (AONB)', 2, 0)
                    ,('National Park', 2, 0)
                    ,('SSSIS, SACs, SPAs, Ramsar wetlands', 2, 0)
                    ,('Marine Conservation Zones', 2, 0)
                    ,('Conservation Zone', 2, 0)
                    ,('TPO (tree protection orders)', 2, 0)
                    ,('No designation', 2, 1)
                    ,('Standard/main compound', 3, 1)
                    ,('Satellite compound', 3, 0)
                    ,('No compound (welfare only)', 3, 0)
                    ,('Highways', 3, 0)
                    ,('Yes (Significant challenges in accessing materials and labour)', 4, 0)
                    ,('No (Easily accessible with no major logistical issues)', 4, 1)
                    ,('Standard Project (£1m-£50m)', 5, 1)
                    ,('Major Project (£50m+)', 5, 0)
                    ,('Minor Project (below £1m)', 5, 0)
                    ,('Yes', 6, 0)
                    ,('No', 6, 1)
                    ,('No issues', 7, 1)
                    ,('Minor issues', 7, 0)
                    ,('Severe issues', 7, 0)
                    ,('No requirement', 8, 1)
                    ,('Removal (Complete demolition and disposal)', 8, 0)
                    ,('Relocation or diversion (Moving structures to a new location, service or road diversion)', 8, 0)
                    ,('Partial Removal (Selective demolition and disposal)', 8, 0)
                    ,('Protection of existing structures (existing structures in place)', 8, 0)
                    ,('Protected Species (e.g. endangered or threatened species)', 9, 0)
                    ,('Invasive Species (e.g. native species that disrupt the local ecosystem)', 9, 0)
                    ,('Common Species (e.g. native species with no special status)', 9, 1)
                    ,('Migratory Species (e.g. species that move through the area seasonally)', 9, 0)
                    ,('Water', 10, 0)
                    ,('Railway', 10, 0)
                    ,('Highways', 10, 0)
                    ,('Process Plants', 10, 0)
                    ,('Buried pipelines', 10, 0)
                    ,('Electricity routes', 10, 0)
                    ,('No', 10, 1)
                    ,('Critical to complete by completion date', 11, 0)
                    ,('Seasonal deadline used for completion date', 11, 0)
                    ,('Desirable completion used for completion date', 11, 0)
                    ,('Completion date set by programme logic (no constraints)', 11, 1)
                    ,('Water', 12, 0)
                    ,('Foul Water', 12, 0)
                    ,('Power', 12, 0)
                    ,('Data/Telecommunications', 12, 0)
                    ;"""
        with db_ops(self.db) as cur:
            cur.executemany(insert_gateways, self._gateways)
            cur.execute(insert_estimatetypes)
            cur.execute(insert_partners)
            cur.execute(insert_contracts)
            cur.execute(insert_hubs)
            cur.execute(insert_enquiries)
            cur.execute(insert_questions)
            cur.execute(insert_answers)
        # conn.commit()
        # conn.close()
    
    @property
    def enquiries(self) -> list[tuple]:
        # conn = sqlite3.connect(self.db)
        # cur = conn.cursor()
        with db_ops(self.db) as cur:
            query1 = f"{self._enquire}"
            cur.execute(query1)
            output = cur.fetchall()
        # conn.close()
        return output

    def enquiry(self, id: int) -> list:
        # conn = sqlite3.connect(self.db)
        # cur = conn.cursor()
        with db_ops(self.db) as cur:
            query1 = f"{self._enquire} WHERE enquiry_id=?"
            cur.execute(query1, (id,))
            output = cur.fetchone()
        # conn.close()
        return output


class DRL:
    def __init__(self) -> None:
        self.db = "drl.db"
        self.file_categories = "categories_rev72-20250324.json"
        self.file_assets = "asset-types_rev72-20250324.json"
        self.file_attributes = "attributes_rev72-20250324.json"
        self.file_elements = "elements_rev72-20250324.json"
        self.file_picklists = "picklists_rev72-20250324.json"

    def drop_all(self) -> None:
        with db_ops(self.db) as cur:
            cur.execute("DROP TABLE IF EXISTS categories;")
            cur.execute("DROP TABLE IF EXISTS assets;")
            cur.execute("DROP TABLE IF EXISTS attributes;")
            cur.execute("DROP TABLE IF EXISTS elements;")
            cur.execute("DROP TABLE IF EXISTS picklists;")

    def create_all(self) -> None:
        with db_ops(self.db) as cur:
            create_categories = """CREATE TABLE IF NOT EXISTS categories (
                    category_id INTEGER PRIMARY KEY
                    ,drl_id TEXT NOT NULL
                    ,label TEXT NOT NULL
                    ,description TEXT NOT NULL
                    ,revision TEXT
                    ,date TEXT
                    );"""
            create_assets = """CREATE TABLE IF NOT EXISTS assets (
                    asset_id INTEGER PRIMARY KEY
                    ,drl_id TEXT NOT NULL
                    ,category TEXT NOT NULL
                    ,label TEXT NOT NULL
                    ,description TEXT NOT NULL
                    ,revision TEXT
                    ,date TEXT
                    ,assetcode TEXT
                    ,geometrytype TEXT
                    ,uniclass2015 TEXT
                    );"""
            cur.execute(create_categories)
            cur.execute(create_assets)

    def reset(self) -> None:
        self.drop_all()
        self.create_all()
        self.load_data()

    def load_data(self) -> None:
        self.load_categories()
        self.load_assets()
    
    def load_json(cls, file) -> list[dict]:
        with Path(file).open() as f:
            loaded_ = json.load(f)
        print(loaded_[0])
        return loaded_
    
    def load_categories(self) -> None:
        insert_categories = """INSERT INTO categories 
                    (drl_id, label, description, revision, date)
                    VALUES (?,?,?,?,?);"""
        categories = self.load_json(self.file_categories)
        # with Path(self.file_categories).open() as f:
        #     categories = json.load(f)
        # print(categories[0])
        with db_ops(self.db) as cur:
            to_be_inserted = []
            for item in categories:
                to_be_inserted.append(
                    (
                        item["id"], 
                        item["label"], 
                        item["description"],
                        item["edit"]["id"],
                        item["edit"]["date"],
                    )
                )
            cur.executemany(insert_categories, to_be_inserted)
            # cat = categories[0]
            # cat0 = (cat["id"], cat["label"], cat["description"])
            # cur.execute(insert_categories, cat0)

    def load_assets(self) -> None:
        insert_assets = """INSERT INTO assets 
                    (drl_id, category, label, description, revision, date,
                    assetcode, geometrytype, uniclass2015)
                    VALUES (?,?,?,?,?,?,?,?,?);"""
        assets = self.load_json(self.file_assets)
        # with Path(self.file_assets).open() as f:
        #     assets = json.load(f)
        # print(assets[0])
        with db_ops(self.db) as cur:
            to_be_inserted = []
            for item in assets:
                to_be_inserted.append(
                    (
                        item["id"],
                        item["category"], 
                        item["label"], 
                        item["description"],
                        item["edit"]["id"],
                        item["edit"]["date"],
                        item["assetCode"],
                        item["geometryType"],
                        item["uniclass2015"],
                    )
                )
            cur.executemany(insert_assets, to_be_inserted)

    def load_elements(self) -> None:
        elements = self.load_json(self.file_assets)


if __name__ == "__main":
  # SQLiteHandler().reset()
  db = SQLiteHandler()
  db.reset()
  db.background_data()
  print(db.enquiries)
  print(db.enquiry(1))

  db = DRL()
  db.reset()

