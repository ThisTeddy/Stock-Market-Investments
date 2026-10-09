
import sqlite3

for db_name in ("db.sqlite3", "db_old_backup.sqlite3"):
    conn = sqlite3.connect(db_name)
    print(f"\n--- {db_name}: deposit wallets ---")

    rows = conn.execute("""
        SELECT id, network, active, asset_id
        FROM xcoin_depositwallet
        ORDER BY id
    """).fetchall()

    for row in rows:
        print(row)

    conn.close()