## 📘 **alx\_travel\_app\_0x00**

### ✅ **Objective**

This project demonstrates **Database Modeling** and **Data Seeding** in Django.
You will:

* Define models for listings, bookings, and reviews.
* Create serializers for API representation.
* Implement a management command to seed the database with sample data.

---

### 📂 **Project Structure**

```
alx_travel_app_0x00/
├── alx_travel_app/
│   ├── listings/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   └── management/
│   │       └── commands/
│   │           └── seed.py
│   ├── ...
├── README.md
```

---

### 🚀 **Instructions**

#### 1️⃣ Duplicate the Project

Duplicate the existing `alx_travel_app` to `alx_travel_app_0x00`.

---

#### 2️⃣ Create Models

* Define **Listing**, **Booking**, and **Review** models in `listings/models.py`.
* Include all required fields, relationships, and constraints as specified:

  * **Listing (Property)**: `title`, `description`, `location`, `price_per_night`.
  * **Booking**: references `User` and `Property` with `check_in` and `check_out` dates.
  * **Review**: references `User` and `Property` with `rating` and `comment`.

---

#### 3️⃣ Set Up Serializers

* In `listings/serializers.py`, create:

  * `ListingSerializer` for the `Property` model.
  * `BookingSerializer` for the `Booking` model.

---

#### 4️⃣ Implement Seeder

* Create `listings/management/commands/seed.py`.
* Implement a management command named `seed` to populate the database with sample listing data.

---

#### 5️⃣ Run Seed Command

Run the management command to test seeding:

```bash
python manage.py seed
```

Verify that the database contains the sample listings.

---

### 🗂️ **Repo**

* **GitHub repository:** `alx_travel_app_0x00`
* **Key files:**

  * `listings/models.py`
  * `listings/serializers.py`
  * `listings/management/commands/seed.py`
  * `README.md`

---



