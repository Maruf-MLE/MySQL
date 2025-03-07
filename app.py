import MySQL.connector

try:
    # MySQL-এ কানেক্ট করার চেষ্টা
    db = mysql.connector.connect(
        host="localhost",
        user="root",      # XAMPP-এর ডিফল্ট ইউজার
        password="",      # যদি পাসওয়ার্ড না থাকে, ফাঁকা রাখুন
        database="test_db" # আপনার ডাটাবেসের নাম
    )
    if db.is_connected():
        print("✅ MySQL Connected Successfully!")
    else:
        print("❌ Connection Failed!")
except mysql.connector.Error as e:
    print(f"❌ Error: {e}")
finally:
    if 'db' in locals() and db.is_connected():
        db.close()
