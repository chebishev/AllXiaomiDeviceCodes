# AllXiaomiDeviceCodes

AllXiaomiDeviceCodes is a tool that fetches and parses device data from [mirom.ezbox.idv.tw](https://mirom.ezbox.idv.tw/sitemap.xml), presenting it in two convenient formats:

- 📦 A **console app** that displays a table for quick device code name lookup.
- 🌐 A **web API** that serves device data in JSON format.

Inspired by the awesome work at [XiaomiFirmwareUpdater](https://github.com/XiaomiFirmwareUpdater).

---

## 🔗 Try It Out

- 🖥️ **Console App** (Replit):  
  https://replit.com/@chebishev/AllXiaomiDeviceCodes

- 🔌 **Web API** (Render, may take a few seconds to start):  
  https://allxiaomidevicecodes.onrender.com/docs

---

## ⚙️ Features

- Fetches and parses Xiaomi device codes weekly via GitHub Actions (every Sunday).
- Clean, structured output for both CLI and API use.
- OpenAPI/Swagger documentation available for the API.

---

## 🛠️ GitHub Actions

This project uses a scheduled GitHub Action to automate data updates:

- **Frequency**: Weekly, every Sunday
- **Purpose**: Refresh device data from the source sitemap automatically

---

## 📂 Structure

```plaintext
📁 AllXiaomiDeviceCodes/
├── codenames_as_keys.json #
├── fix_model_names.py #
├── json_data.py #
├── main.py      # FastAPI web app
├── make_jsons_from_xml.py # 
├── print_table_from_json.py #
├── scraper.py   # cli version
└── .github/    # GitHub Actions workflow
