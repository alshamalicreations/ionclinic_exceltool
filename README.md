# 🚀 TemplateMapper

> **Universal Data Migration Platform**

TemplateMapper is a professional desktop application designed to migrate data between clinic management systems and standardized templates.

Its architecture is built around **importers**, **exporters**, and **mapping engines**, allowing support for multiple source systems and multiple destination templates.

The first supported workflow is:

**DERMA Excel ➜ IonClinic Backup**

---

# ✨ Features

## 📂 Import Engine

- Read Excel workbooks (`.xlsx`)
- Automatic source detection
- Modular importer architecture
- Extensible mapping system

---

## 👤 Patient Migration

- Import patient records
- Preserve patient relationships
- Generate UUIDs
- Data normalization
- Duplicate detection

---

## 📅 Appointment Migration

- Convert treatment history into appointments
- Preserve treatment dates
- Preserve treatment names
- Maintain patient relationships

---

## 💳 Payment Migration

- Import payment history
- Preserve payment methods
- Preserve payment dates
- Calculate balances
- Link payments to patients

---

## 📄 Export Engine

- Generate IonClinic-compatible backup files
- Timestamped exports
- Workbook integrity validation
- Automatic column sizing

---

## ⚙️ Desktop Application

- Modern PySide6 interface
- Background processing
- Live progress tracking
- Migration log
- Responsive UI
- Read-only path selection
- Professional desktop experience

---

# 🧩 Supported Importers

| Source | Status |
|---------|--------|
| DERMA Excel | ✅ Supported |

---

# 📦 Supported Export Templates

| Template | Status |
|----------|--------|
| IonClinic Backup | ✅ Supported |

---

# 🛣️ Roadmap

## Version 1.0

- ✅ DERMA Importer
- ✅ Patient Migration
- ✅ Appointment Migration
- ✅ Payment Migration
- ✅ IonClinic Exporter
- ✅ Background Worker
- ✅ Progress Tracking
- ✅ Desktop GUI

---

## Version 1.1

- ⏳ Migration Summary
- ⏳ ETA Estimation
- ⏳ Remember Previous Paths
- ⏳ Better Validation Reports

---

## Version 1.2

- ⏳ Drag & Drop
- ⏳ Batch Migration
- ⏳ Faster Processing
- ⏳ Multi-threaded Export

---

## Version 2.0

### New Importers

- DentalSoft
- EasyClinic
- CSV Import
- Custom Excel Importers

### New Exporters

- Additional clinic management systems
- Custom template support

---

# 🏗️ Project Architecture

```
TemplateMapper
│
├── assets
├── engine
├── exporters
├── gui
├── importers
├── mappings
├── models
├── services
├── writers
└── tests
```

---

# 🛠️ Technologies

- Python
- PySide6
- OpenPyXL
- Pandas
- RapidFuzz
- Loguru

---

# 📌 Current Status

🚧 **Actively under development**

The first stable release focuses on migrating **DERMA Excel workbooks** into the **IonClinic Backup** format.

The architecture is designed to support additional source systems and export templates in future releases.

---

# 🤝 Contributing

Contributions are welcome.

You can help by:

- Reporting bugs
- Suggesting new features
- Improving documentation
- Adding new importers
- Adding new exporters

---

# 📄 License

Licensed under the **MIT License**.

---

# 👨‍💻 Author

Developed by **Rayyan Alshamali**

---

# ⭐ Support

If you find TemplateMapper useful, consider giving the repository a **⭐ Star**.

It helps support future development and makes the project easier for others to discover.